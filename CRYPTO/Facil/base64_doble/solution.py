#!/usr/bin/env python3

import base64

# Encoded data (run challenge.py to get this)
encoded = "Q1RGe2Jhc2U2NF9mbGFnfQ=="  # This is the double-encoded version

print(f"Encoded: {encoded}")

# Decode once
decoded1 = base64.b64decode(encoded).decode()
print(f"After 1st decode: {decoded1}")

# Decode again
decoded2 = base64.b64decode(decoded1).decode()
print(f"After 2nd decode: {decoded2}")
