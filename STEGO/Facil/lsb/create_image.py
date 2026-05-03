#!/usr/bin/env python3

from PIL import Image
import numpy as np

# LSB Steganography Challenge

# Create a simple image with LSB data hidden
img = Image.new('RGB', (100, 100), color=(255, 0, 0))
pixels = img.load()

# Hide message "flag" in LSBs
message = "flag"
message_bits = ''.join(format(ord(c), '08b') for c in message)

bit_index = 0
for i in range(100):
    for j in range(100):
        if bit_index < len(message_bits):
            r, g, b = pixels[i, j]
            bit = int(message_bits[bit_index])
            r = (r & 0xFE) | bit  # Replace LSB of red channel
            pixels[i, j] = (r, g, b)
            bit_index += 1

img.save('lsb_image.png')
print("Image created with LSB hidden message")
