# Base64 Doble (CRYPTO - Fácil)

## Descripción
El flag ha sido codificado en base64 dos veces. Debes descodificarlo dos veces para obtener el original.

## Challenge
```
Q1RGe2Jhc2U2NF9mbGFnfQ==
```

## Instrucciones
Descodifica el texto en base64 dos veces.

## Solución
```python
import base64

encoded = "Q1RGe2Jhc2U2NF9mbGFnfQ=="

# Descodificar primera vez
decoded1 = base64.b64decode(encoded)
print(decoded1)  # b'CTF{base64_flag}'

# Descodificar segunda vez
decoded2 = base64.b64decode(decoded1).decode()
print(decoded2)  # CTF{base64_flag}
```

O usando herramientas en línea:
1. Descodifica en https://www.base64decode.org/
2. Descodifica el resultado nuevamente
3. Obtendrás el flag

## Flag
```
CTF{base64_flag}
```

## Conceptos
- Base64 encoding/decoding
- Layered encoding
- Obfuscación de datos
