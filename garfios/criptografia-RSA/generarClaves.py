#!/usr/bin/python
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA

#Generar un par de claves Pública/Privada usando 4096 bits de longitud de clave (512 bytes)
claveNueva = RSA.generate(4096, e=65537)

clavePrivada = claveNueva.exportKey("PEM")
clavePublica = claveNueva.publickey().exportKey("PEM")

print(clavePrivada)
archivo = open("ejemplo/clavePrivada.pem", "wb")
archivo.write(clavePrivada)
archivo.close()

print(clavePublica)
archivo = open("ejemplo/clavePublica.pem", "wb")
archivo.write(clavePublica)
archivo.close()
