#!/usr/bin/env python3

# RSA Textbook Attack
# If e=3 (small exponent) and message is small, c = m^3 mod n
# We can recover m by taking the cube root

def integer_nth_root(x, n):
    """Compute the integer nth root of x"""
    if x == 0:
        return 0
    r = 1
    while True:
        r_new = ((n - 1) * r + x // (r ** (n - 1))) // n
        if r_new >= r:
            return r
        r = r_new

# Example with small e
e = 3
n = 61924882325330225440671220297852126909
c = 25326840684541486255820097635905833893

# Try cube root
m = integer_nth_root(c, e)
print(f"Recovered message: {m}")

# Try to convert to string
try:
    message = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
    print(f"Message: {message}")
except:
    print("Could not decode")
