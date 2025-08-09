from Crypto.PublicKey import RSA

# Generate a new 4096-bit public/private key pair (512 bytes)
new_key = RSA.generate(4096, e=65537)

private_key = new_key.export_key()
public_key = new_key.publickey().export_key()

print(private_key)
with open("example/privatePass.pem", "wb") as file:
    file.write(private_key)

print(public_key)
with open("example/publicPass.pem", "wb") as file:
    file.write(public_key)

# pip install pycryptodome
# Certificates can be saved with extensions .cer, .crt, .pem and read similarly


