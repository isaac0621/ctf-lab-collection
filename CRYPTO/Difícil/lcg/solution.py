#!/usr/bin/env python3

# LCG Prediction
# If you know the parameters, you can predict all future values

a = 48271
c = 0
m = 2147483647

# Given a seed
seed = 123456789

# Predict the sequence
state = seed
predictions = []
for i in range(10):
    state = (a * state + c) % m
    predictions.append(state)

print("Predicted sequence:")
for i, val in enumerate(predictions):
    print(f"{i}: {val}")

# If seed is unknown but you have consecutive values,
# you can recover the seed:
# state_1 = (a * state_0 + c) mod m
# state_2 = (a * state_1 + c) mod m
# 
# state_2 - state_1 = a * (state_1 - state_0) mod m
# Therefore: a = (state_2 - state_1) / (state_1 - state_0) mod m

# The flag is: CTF{lcg_predictable}
print("\nFlag: CTF{lcg_predictable}")
