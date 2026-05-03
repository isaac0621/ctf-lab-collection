#!/usr/bin/env python3

# Caesar Cipher Challenge
secret = "flag"

def enc(s):
    return ''.join(chr((ord(c)-97+3)%26+97) for c in s)

encrypted = enc(secret)
print(f"Encrypted: {encrypted}")
print(f"Flag: CTF{{caesar_{encrypted}}}
")
