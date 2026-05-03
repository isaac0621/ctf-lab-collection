# LSB Steganography (STEGO - Fácil)

## Descripción
El Least Significant Bit (LSB) steganography esconde datos en el bit menos significativo de los píxeles. Es imperceptible al ojo humano pero fácil de extraer.

## Instrucciones
1. Abre la imagen
2. Extrae los LSBs de cada píxel
3. Convierte los bits a caracteres
4. Lee el mensaje oculto

## Solución
```python
from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    bits = []
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            bits.append(r & 1)  # Extract LSB from red channel
    
    message = ""
    for i in range(0, len(bits) - 7, 8):
        byte_bits = bits[i:i+8]
        byte_str = ''.join(str(b) for b in byte_bits)
        message += chr(int(byte_str, 2))
    
    return message

message = extract_lsb('image.png')
print(message)
```

## Flag
```
CTF{lsb_extracted}
```

## Conceptos
- Steganography
- LSB encoding/decoding
- Image data hiding
- Information hiding
