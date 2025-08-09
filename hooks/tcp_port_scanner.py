import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from scapy.all import sr1, IP, TCP
from typing import List

TARGET_IP = '172.217.30.142'  # Example: google.com IP
MAX_THREADS = 5  # Max concurrent threads
open_ports: List[int] = []
RULE = 1  # Controls verbosity and scan behavior

# Lock for thread-safe operations on open_ports
open_ports_lock = threading.Lock()

def scan_port(host: str, port: int) -> None:
    """
    Scan a single TCP port on the given host using a TCP SYN scan.
    """
    if RULE <= 0:
        return

    if RULE > 0:
        print(f"[++] Scanning port {port}")

    # Send TCP SYN packet
    response = sr1(IP(dst=host)/TCP(dport=port, flags='S'), verbose=False, timeout=0.2)

    # TCP flag 18 means SYN-ACK (flags = SYN(2) + ACK(16))
    if response and response.haslayer(TCP):
        if response[TCP].flags == 18:
            with open_ports_lock:
                open_ports.append(port)
            if RULE > 1:
                print(f"Port {port} is open.")

def main():
    """
    Main function to scan TCP ports from 1 to 89 on TARGET_IP concurrently.

    RULE variable controls the scanning behavior:
    - RULE < 1: No scanning performed.
    - RULE = 1: Ports are scanned silently, results shown after completion.
    - RULE > 1: Ports are scanned and open ports are reported immediately.

    Requires root privileges to send raw packets.

    Uses ThreadPoolExecutor for concurrency and thread-safe list for storing open ports.
    """
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(scan_port, TARGET_IP, port) for port in range(1, 90)]

        # Wait for all scans to complete
        for _ in as_completed(futures):
            pass

    print("[*] Open TCP ports:")
    for port in open_ports:
        print(f"  - {port}/TCP")

if __name__ == '__main__':
    main()

    