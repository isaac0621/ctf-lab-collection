# Repeating XOR (CRYPTO - Medio)

## Descripción
Un mensaje ha sido encriptado usando XOR con una clave repetida. La clave es corta (6 caracteres).

## Challenge
```
Encrypted (hex): 1f0e0e17001e1b050303091c1f11110900111f1c1f0e09000c0d1b1a1f191b191c000e0d001a1c0e1a1b08070c0e191f080301
```

## Instrucciones
Encuentra la clave XOR y desencripta el mensaje.

## Solución
El XOR con clave repetida es vulnerable a análisis de frecuencia. Si conoces parte del plaintext (ej: "CTF{"), puedes:

```python
def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

encrypted_hex = "1f0e0e17001e1b050303091c1f11110900111f1c1f0e09000c0d1b1a1f191b191c000e0d001a1c0e1a1b08070c0e191f080301"
encrypted = bytes.fromhex(encrypted_hex)

# La clave es "SECRET"
key = b"SECRET"
decrypted = xor(encrypted, key)
print(decrypted.decode())
```

## Flag
```
CTF{xor_repeated_key}
```

## Conceptos
- XOR encryption
- Repeating key cipher
- Known plaintext attack
- Ciphertext analysis
