# Carlos Esteban Maccarrone -cem- 2018 
import cv2, time, threading, base64
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def webcam():
	for i in range(5):
		rc, imagen = cap.read()
		color = cv2.cvtColor(imagen, cv2.COLOR_BGR2BGRA)
		capturas.append(color)
		time.sleep(1)
	cap.release()

class vehiculo(BaseHTTPRequestHandler):
    def do_GET(self):
		for foto in capturas:
			self.send_response(200)
			self.end_headers()
			rec, arrayIMG = cv2.imencode('.png', foto)
			foto = base64.b64encode(bytearray(arrayIMG))
			self.wfile.write('<img src="data:image/png;base64,'+foto+'"><br><br>')
			self.wfile.write('\r\n')

if __name__ == '__main__':
	cap = cv2.VideoCapture(0)
	global capturas
	capturas = []
	threads = list()
	t = threading.Thread(target=webcam)
	threads.append(t)
	t.start()

	urlSite = 'localhost' or '127.0.0.1'

	try:
		server = HTTPServer((urlSite, 8080), vehiculo)
		print 'Starting server, use <Ctrl-C> to stop'
		server.serve_forever()
	except KeyboardInterrupt:
		server.socket.close()

		
# Este programa crea un servidor en localhost:8080 o 127.0.0.1:8080
# y muestra cinco fotos capturadas al momento de correr	
