# pip install opencv-python 
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import base64
import time
import cv2

captures = []
captures_lock = threading.Lock()

def capture_webcam_frames(num_frames=5, delay=1):
    """
    Capture frames from the default webcam in BGRA format.
    
    Args:
        num_frames (int): Number of frames to capture.
        delay (float): Delay in seconds between captures.
    """
    cap = cv2.VideoCapture(0)
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            break
        frame_bgra = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        with captures_lock:
            captures.append(frame_bgra)
        time.sleep(delay)
    cap.release()

class WebcamHandler(BaseHTTPRequestHandler):
    """
    HTTP handler that serves captured webcam images as base64-encoded PNGs in HTML.
    """

    def do_GET(self):
        """
        Respond with an HTML page embedding all captured frames as images.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = "<html><body>"
        with captures_lock:
            for img in captures:
                ret, buf = cv2.imencode('.png', img)
                if not ret:
                    continue
                img_b64 = base64.b64encode(buf).decode('utf-8')
                html += f'<img src="data:image/png;base64,{img_b64}"><br><br>'
        html += "</body></html>"

        self.wfile.write(html.encode('utf-8'))


if __name__ == '__main__':
    """
    Starts the webcam capture thread and HTTP server on localhost:8080.
    Access http://localhost:8080 to view captured images.
    Press Ctrl-C to stop.
    """
    capture_thread = threading.Thread(target=capture_webcam_frames)
    capture_thread.start()

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, WebcamHandler)
    print('Server started at http://localhost:8080 - press Ctrl-C to stop.')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()