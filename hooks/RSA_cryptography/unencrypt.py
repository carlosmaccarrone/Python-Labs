from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib, base64

def encrypt_element(element, public_key):
    # PKCS1_OAEP is an asymmetric encryption based on RSA with OAEP padding.
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)

    # Compress the data
    element = zlib.compress(element)

    # The chunk size is determined as the length of the private key in bytes
    # minus 42 bytes (when using PKCS1_OAEP). Data will be encrypted in chunks.
    # 512 - 42 = 470
    chunk_size = 470
    offset = 0
    done = False
    encrypted = bytearray()

    while not done:
        chunk = element[offset : offset + chunk_size]

        # If chunk is smaller than chunk_size, pad with zeros.
        # This indicates the end of the data, so we finish the loop.
        if len(chunk) % chunk_size != 0:
            done = True
            chunk += bytes(chunk_size - len(chunk))

        # Append the encrypted chunk to the overall encrypted data
        encrypted += cipher_rsa.encrypt(chunk)

        # Move offset forward by chunk_size
        offset += chunk_size

    # Base64 encode the encrypted data before returning
    return base64.b64encode(encrypted)

# Load public key for encryption
with open("example/publicPass.pem", "rb") as file:
    public_key = file.read()

# Load the file to encrypt, for example a photo
with open("example/cover.jpg", "rb") as file:
    element_to_encrypt = file.read()

encrypted_element = encrypt_element(element_to_encrypt, public_key)

# Write the encrypted file
with open("example/encryptedElement.jpg", "wb") as file:
    file.write(encrypted_element)

    