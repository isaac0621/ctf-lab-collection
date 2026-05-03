#!/usr/bin/env python3

import base64

# Base64 Double Encoding Challenge
flag = b"CTF{base64_flag}"

enc1 = base64.b64encode(flag)
enc2 = base64.b64encode(enc1)

print(f"Encoded: {enc2.decode()}")
print(f"Save this to solve the challenge!")
