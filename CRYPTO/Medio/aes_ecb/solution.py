#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# AES ECB Decryption
key = b"YELLOW_SUBMARINE"

# This is the ciphertext from the challenge
ciphertext_hex = "9c2e9c2e5f2e8c5f9c2e9c2e5f2e8c5f3d4c5d6e7f8g9h0i1j2k3l4m5n6o7p8"

# In a real scenario, you'd need to find the key
# ECB is vulnerable because identical plaintext blocks produce identical ciphertext blocks

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = bytes.fromhex(ciphertext_hex)

try:
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(f"Decrypted: {plaintext.decode()}")
except:
    print("Decryption failed - might need the key")
