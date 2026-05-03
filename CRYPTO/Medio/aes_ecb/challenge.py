#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# AES ECB Challenge
key = b"YELLOW_SUBMARINE"  # 16 bytes
plaintext = b"The flag is: CTF{aes_ecb_vulnerable}!!!!!!!!!!"

# Pad plaintext to multiple of 16
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(f"Key (hex): {key.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Block size: {AES.block_size}")

# Save to file
with open('encrypted.txt', 'w') as f:
    f.write(ciphertext.hex())
