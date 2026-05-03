# AES ECB (CRYPTO - Medio)

## Descripción
AES en modo ECB es inseguro porque bloques de plaintext idénticos generan ciphertexts idénticos. Este reto muestra esta vulnerabilidad.

## Challenge
Tienes un ciphertext encriptado con AES-ECB. La clave es "YELLOW_SUBMARINE" (16 bytes).

## Instrucciones
1. Desencripta el ciphertext usando la clave proporcionada
2. Extrae el flag del plaintext

## Solución
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b"YELLOW_SUBMARINE"
ciphertext = bytes.fromhex("...")  # El ciphertext

cipher = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(plaintext.decode())
```

## Flag
```
CTF{aes_ecb_vulnerable}
```

## Conceptos
- AES encryption
- ECB mode weakness
- Block cipher modes
- Pattern recognition in ECB
