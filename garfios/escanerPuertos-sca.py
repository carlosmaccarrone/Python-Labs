## -*- coding: utf-8 -*-
# Correr con sudo
# Carlos Esteban Maccarrone -cem- 2018
import threading

from scapy.all import sr1, IP, TCP

ESCANEARIP = '172.217.30.142'
valorRelease = 5 # Máxima cantidad de threads en zona crítica
puertosAbiertos = []
REGLA = 1

def estudiarPuerto(host, puerto, semaforo):
	if REGLA > 0:
		print "[++] Analizando puerto %s " % puerto

		# transmision control protocol handshaking
		# 1)envío sync, 2)responde sync-ack, 3)envío ack

		respuesta = sr1(IP(dst=host)/TCP(dport=puerto),\
		 	verbose=False, timeout=0.2)
		# URG	ACK		PSH		RST		SYN		FIN
		# 32	16		8		4		2		1
		# 18 = ACK & SYNC

		if respuesta is not None and TCP in respuesta:
			if respuesta[TCP].flags == 18:
				puertosAbiertos.append(puerto)
				if REGLA > 1:
					print "Puerto %s abierto." % puerto

		# Semaforo verde, se puede lanzar otro thread
		semaforo.release()

def main():
	sem = threading.BoundedSemaphore(value=valorRelease)
	threads = []

	# Se analizara entre los puertos 1 y 90
	for p in range(1, 90):
		t = threading.Thread(target=estudiarPuerto,\
		 	args=(ESCANEARIP, p, sem, ))
		threads.append(t)

		# Semaforo en rojo, se debe poner en verde
		# 							para lanzar otro thread
		sem.acquire()
		t.start()

	# investigar resultados
	print "[*] Puertos abiertos:"
	for p in puertosAbiertos:
		print "		- %s/TCP" % p
	print

if __name__ == '__main__':
	main()

# La variable REGLA puede ser:
# <1 no se escanean puertos
# =1 se escanean puertos y no se muestran hasta terminar
# >1 se escanean puertos y se muestran al instante
