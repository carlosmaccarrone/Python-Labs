#!/usr/bin/python
# -*- coding: utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib, base64

def decrypt_element(encrypted_element, private_key):
    # PKCS1_OAEP is an asymmetric encryption based on RSA with OAEP padding.
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)

    # Decode the base64 encoded data
    encrypted_element = base64.b64decode(encrypted_element)

    # The chunk size corresponds to the length of the private key in bytes
    # Data will be decrypted in chunks.
    chunk_size = 512
    offset = 0
    decrypted = bytearray()

    # Loop until the whole encrypted_element is processed
    while offset < len(encrypted_element):
        chunk = encrypted_element[offset : offset + chunk_size]

        # Append the decrypted chunk to the overall decrypted data
        decrypted += cipher_rsa.decrypt(chunk)

        # Move the offset forward by chunk_size
        offset += chunk_size

    # Finally, decompress the decrypted data with zlib
    return zlib.decompress(decrypted)


# Load private key for decryption
with open("example/privatePass.pem", "rb") as file:
    private_key = file.read()

# Load the file to be decrypted
with open("example/encryptedElement.jpg", "rb") as file:
    encrypted_element = file.read()

# Write the decrypted file
with open("example/unencryptedElement.jpg", "wb") as file:
    file.write(decrypt_element(encrypted_element, private_key))
