# Caesar Cipher (CRYPTO - Fácil)

## Descripción
Una contraseña ha sido encriptada con el famoso cifrado Caesar (desplazamiento de 3 posiciones).

## Challenge
```
Encrypted: iodj
```

## Instrucciones
Desencripta el texto desplazando cada letra hacia atrás en el alfabeto.

## Solución
El Caesar Cipher con desplazamiento de 3 significa que cada letra está corrida 3 posiciones hacia adelante:
- a → d
- b → e
- c → f
- ...
- x → a
- y → b
- z → c

Para desencriptar, desplazamos hacia atrás 3 posiciones:
- i → f
- o → l
- d → a
- j → g

Resultado: "flag"

```python
def dec(s, shift=3):
    return ''.join(chr((ord(c)-97-shift)%26+97) for c in s)

print(dec("iodj"))  # flag
```

## Flag
```
CTF{caesar_iodj}
```

## Conceptos
- Cifrado Caesar
- Análisis de frecuencia
- Criptografía clásica
- Ataques por fuerza bruta
