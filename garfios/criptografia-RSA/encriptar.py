#!/usr/bin/python
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib, base64

def funcionDeEncriptamiento(elemento, clavePublica):
    # PKCS_OAEP es un cifrado asimétrico basado en RSA y padding OAEP.
    claveRSA = RSA.importKey(clavePublica)
    claveRSA = PKCS1_OAEP.new(claveRSA)

    # Comprimir los datos
    elemento = zlib.compress(elemento)

    # Se determina el tamaño del fragmento como longitud de la clave privada utilizada 
    # en bytes menos 42 bytes (cuando se usa PKCS1_OAEP). Los datos se encriptaran en
    # porciones.
    # 512 - 42 = 470
    fragmento = 470
    offset = 0
    fin_loop = False
    cifrado =  bytearray()

    while not fin_loop:

        porcion = elemento[offset:offset + fragmento]

        #Si la porción de datos es menor que el fragmento, entonces 
        #se agrega padding con "". Esto indica que llegamos al final del archivo.
        #Así que terminamos el bucle aquí.
        if len(porcion) % fragmento != 0:
            fin_loop = True
            porcion += bytes(fragmento - len(porcion))

        # Agregue la porcion cifrada al archivo cifrado general
        cifrado += claveRSA.encrypt(porcion)

        # Añadir al offset un fragmento para obtener longitud de elemento
        offset += fragmento

    # base64 codifica el archivo cifrado para terminar
    return base64.b64encode(cifrado)

# Traer clave publica para encriptar
descriptor = open("ejemplo/clavePublica.pem", "rb")
clavePublica = descriptor.read()
descriptor.close()

# Archivo que se quiere encriptar, por ejemplo una foto
descriptor = open("ejemplo/cover.jpg", "rb")
elementoAEncriptar = descriptor.read()
descriptor.close()

elementoEncriptado = funcionDeEncriptamiento(elementoAEncriptar, clavePublica)

# Escribir el archivo encriptado
descriptor = open("ejemplo/elementoEncriptado.jpg", "wb")
descriptor.write(elementoEncriptado)
descriptor.close()
