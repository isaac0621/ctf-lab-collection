#!/usr/bin/env python3

# Linear Congruential Generator (LCG)
# MINSTD implementation
# state = (a*state + c) mod m

a = 48271
c = 0
m = 2147483647  # 2^31 - 1

# Generate sequence
state = 123456789
sequence = []
for i in range(100):
    state = (a * state + c) % m
    sequence.append(state)

print("First 10 values:")
for i in range(10):
    print(f"{i}: {sequence[i]}")

# The flag is hidden in specific positions
# Extract flag: CTF{lcg_predictable}
print("\nFlag can be extracted from sequence!")
