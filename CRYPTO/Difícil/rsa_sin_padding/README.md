# RSA sin Padding (CRYPTO - Difícil)

## Descripción
RSA sin padding (textbook RSA) es inseguro. Si el exponente es pequeño (ej: 3), el ciphertext puede ser desencriptado sin conocer la clave privada.

## Challenge
Se te proporciona:
- n (modulus)
- e (exponente público - generalmente 3 o 65537)
- c (ciphertext)

Recupera el mensaje.

## Solución
Si e=3, intenta tomar la raíz cúbica del ciphertext:

```python
def integer_nth_root(x, n):
    if x == 0:
        return 0
    r = 1
    while True:
        r_new = ((n - 1) * r + x // (r ** (n - 1))) // n
        if r_new >= r:
            return r
        r = r_new

m = integer_nth_root(c, e)
message = m.to_bytes((m.bit_length() + 7) // 8, 'big')
print(message.decode())
```

## Flag
```
CTF{rsa_no_padding}
```

## Conceptos
- RSA cryptosystem
- Textbook RSA attacks
- Small exponent attacks
- CRT factorization
