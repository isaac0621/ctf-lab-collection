#!/usr/bin/env python3

import base64
from PIL import Image

# Multilayer Steganography: Base64 + LSB

# Crear una imagen con mensaje oculto en LSB
def hide_message_multilayer(image_path, message):
    # Primero: encriptar con base64
    encoded = base64.b64encode(message.encode()).decode()
    print(f"Base64 encoded: {encoded}")
    
    # Segundo: ocultar en LSB
    img = Image.open(image_path)
    pixels = img.load()
    
    message_bits = ''.join(format(ord(c), '08b') for c in encoded)
    
    bit_index = 0
    for i in range(img.width):
        for j in range(img.height):
            if bit_index < len(message_bits):
                r, g, b = pixels[i, j]
                bit = int(message_bits[bit_index])
                r = (r & 0xFE) | bit
                pixels[i, j] = (r, g, b)
                bit_index += 1
    
    img.save('multilayer.png')

# Usar:
# hide_message_multilayer('source.png', 'CTF{multilayer}')
