"""
file_hex_encode_decode.py

This module provides functions to encode a binary file into a hexadecimal string,
save it to a text file, and decode the hexadecimal string back into the original binary file.

Use case:
- Useful for storing or transmitting binary data in text format.
- Basic example of encoding and decoding binary files using hex representation.
"""

def encode_file_to_hex(input_file_path: str, output_text_path: str) -> None:
    """
    Reads a binary file, encodes its content to a hexadecimal string,
    and writes the hex string to a text file.

    Args:
        input_file_path (str): Path to the input binary file.
        output_text_path (str): Path where the hex string text file will be saved.
    """
    with open(input_file_path, "rb") as file:
        file_data = file.read().hex()
    with open(output_text_path, "w") as file:
        file.write(file_data)

def decode_hex_to_file(input_text_path: str, output_file_path: str) -> None:
    """
    Reads a hexadecimal string from a text file, decodes it back into binary,
    and writes the binary data to an output file.

    Args:
        input_text_path (str): Path to the input text file containing hex string.
        output_file_path (str): Path where the decoded binary file will be saved.
    """
    with open(input_text_path, "r") as file:
        file_data = bytes.fromhex(file.read())
    with open(output_file_path, "wb") as file:
        file.write(file_data)

if __name__ == "__main__":
    # Example usage
    encode_file_to_hex("bookshelf.jpg", "photo_data.txt")
    decode_hex_to_file("photo_data.txt", "biblioteca.jpg")
