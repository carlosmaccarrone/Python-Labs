#!/usr/bin/python
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib, base64

def funcionParaDesencriptar(elemento, clavePrivada):
    # PKCS_OAEP es un cifrado asimétrico basado en RSA y padding OAEP.
    claveRSA = RSA.importKey(clavePrivada)
    claveRSA = PKCS1_OAEP.new(claveRSA)

    # base64 decodifica el archivo
    elemento = base64.b64decode(elemento)

    # El tamaño del fragmento es la longitud de la clave privada utilizada en bytes
    # Los datos se descifrarán por porciones.
    fragmento = 512
    offset = 0
    descifrado = ""

    # El loop se ejecuta hasta que haya procesado toda la longitud del elemento
    while offset < len(elemento):

        porcion = elemento[offset: offset + fragmento]

        # Agregue la porcion descifrada al archivo descifrado general
        descifrado += claveRSA.decrypt(porcion)

        # Añadir al offset un fragmento para obtener longitud de elemento
        offset += fragmento

    # zlib descomprime los datows descifrados para terminar
    return zlib.decompress(descifrado)

# Traer clave privada para desencriptar
descriptor = open("ejemplo/clavePrivada.pem", "rb")
clavePrivada = descriptor.read()
descriptor.close()

# Archivo que se quiere desencriptar
descriptor = open("ejemplo/elementoEncriptado.jpg", "rb")
elementoEncriptado = descriptor.read()
descriptor.close()

# Escribir el archivo desencriptado
descriptor = open("ejemplo/elementoDesencriptado.jpg", "wb")
descriptor.write(funcionParaDesencriptar(elementoEncriptado, clavePrivada))
descriptor.close()