# Obfuscación (REVERSING - Medio)

## Descripción
El código ha sido ofuscado con operaciones bitwise. Debes descifrarlo.

## Challenge
```python
def check(x):
    a = (x ^ 0x55) + 3
    if a == 0x42:
        return True
    return False
```

¿Qué valor de x hace que check(x) retorne True?

## Instrucciones
Resuelve la ecuación:
```
(x ^ 0x55) + 3 == 0x42
```

## Solución
Trabajando hacia atrás:
```
(x ^ 0x55) + 3 == 0x42
(x ^ 0x55) == 0x42 - 3
(x ^ 0x55) == 0x3f
x == 0x3f ^ 0x55
x == 0x6a  (106 en decimal, 'j' en ASCII)
```

Verificación:
```python
x = 0x6a
a = (x ^ 0x55) + 3
print(a == 0x42)  # True
```

## Flag
```
CTF{obfuscation_solved}
```

## Conceptos
- Bitwise operations
- XOR cipher
- Code obfuscation
- Deobfuscation techniques
