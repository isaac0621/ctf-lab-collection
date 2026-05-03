#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

# RSA without padding - Textbook RSA
# This is vulnerable because m^e mod n can be decrypted without knowing d
# if the message is small

# Generate RSA key
key = RSA.generate(2048)
n = key.n
e = key.e
d = key.d

# Message to encrypt
m = int.from_bytes(b"CTF{rsa_no_padding}", 'big')

# Encrypt
c = pow(m, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")
print(f"message = {m}")

# Vulnerability: if message is small, cube root might recover it
# Or use Wiener's attack if d is small
