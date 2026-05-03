#!/usr/bin/env python3

# Repeating XOR Challenge

def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

message = b"The flag is hidden here CTF{xor_repeated_key}"
key = b"SECRET"

encrypted = xor(message, key)
print(f"Encrypted (hex): {encrypted.hex()}")
print(f"Key length: {len(key)}")
print(f"Message length: {len(message)}")
