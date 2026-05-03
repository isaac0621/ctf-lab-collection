#!/usr/bin/env python3

from PIL import Image

# Extraer mensaje LSB
def extract_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    bits = []
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            bits.append(r & 1)  # Extract LSB
    
    # Convertir bits a mensaje
    message = ""
    for i in range(0, len(bits) - 7, 8):
        byte = ''.join(str(b) for b in bits[i:i+8])
        message += chr(int(byte, 2))
    
    return message

# Uso
# message = extract_lsb('lsb_image.png')
# print(message)
