# LCG (CRYPTO - Difícil)

## Descripción
Linear Congruential Generator (LCG) es un generador de números pseudoaleatorios. Es predecible si conoces los parámetros.

La fórmula es:
```
state_n+1 = (a * state_n + c) mod m
```

## Challenge
Se te proporciona:
- a = 48271
- c = 0
- m = 2147483647 (2^31 - 1)
- seed = 123456789

Predice la secuencia de números generados.

## Solución
Con los parámetros conocidos, es trivial predecir:

```python
a = 48271
c = 0
m = 2147483647
state = 123456789

for i in range(100):
    state = (a * state + c) % m
    print(state)
```

Si no conoces los parámetros pero tienes valores consecutivos, puedes recuperarlos:

```python
# Dados: v1, v2, v3
# v2 = (a * v1 + c) mod m
# v3 = (a * v2 + c) mod m
# 
# v3 - v2 = a * (v2 - v1) mod m
```

## Flag
```
CTF{lcg_predictable}
```

## Conceptos
- LCG generator
- PRNG prediction
- Predictable random numbers
- Cryptanalysis
