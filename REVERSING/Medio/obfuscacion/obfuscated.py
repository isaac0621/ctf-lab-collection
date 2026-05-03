#!/usr/bin/env python3

# Obfuscation Challenge

def check(x):
    # Obfuscated check
    a = (x ^ 0x55) + 3
    if a == 0x42:  # 'B'
        return True
    return False

# Find x such that (x ^ 0x55) + 3 == 0x42
# (x ^ 0x55) == 0x3f
# x == 0x3f ^ 0x55
x = 0x3f ^ 0x55
print(f"Solution: {x} (0x{x:02x})")
print(f"Character: {chr(x)}")
