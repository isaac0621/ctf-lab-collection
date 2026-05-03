# Multilayer Steganography (STEGO - Medio)

## Descripción
Los datos están ocultos en múltiples capas: primero codificados en base64, luego escondidos en LSB.

## Instrucciones
1. Extrae el LSB de la imagen
2. Decodifica el resultado usando base64
3. Lee el mensaje

## Solución
```python
from PIL import Image
import base64

def extract_multilayer(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    # Paso 1: Extraer LSBs
    bits = []
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            bits.append(r & 1)
    
    # Paso 2: Convertir a string
    encoded = ""
    for i in range(0, len(bits) - 7, 8):
        byte_bits = bits[i:i+8]
        byte_str = ''.join(str(b) for b in byte_bits)
        try:
            encoded += chr(int(byte_str, 2))
        except:
            break
    
    # Paso 3: Decodificar base64
    message = base64.b64decode(encoded).decode()
    return message

message = extract_multilayer('image.png')
print(message)
```

## Flag
```
CTF{multilayer_stego}
```

## Conceptos
- Layered steganography
- Base64 encoding
- LSB extraction
- Multi-step decoding
