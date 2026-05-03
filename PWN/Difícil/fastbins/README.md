# Fastbins Attack (PWN - Difícil)

## Descripción
Los fastbins son listas enlazadas de chunks pequeños en el heap. Un double free permite insertar un chunk arbitrario en la lista, causando asignaciones controladas.

## Archivo
`fastbins.c` - Programa con vulnerabilidad de double free

## Compilación
```bash
gcc -o fastbins fastbins.c
```

## Instrucciones
1. Causa un double free
2. Manipula la lista de fastbins
3. Fuerza una asignación en una dirección arbitraria
4. Sobrescribe datos críticos

## Solución
```python
# Básicamente:
# 1. malloc(32) -> p1
# 2. malloc(32) -> p2  
# 3. free(p1) -> p1 en fastbin[0]
# 4. free(p1) -> double free! ahora p1 está dos veces en la lista
# 5. malloc(32) -> retorna p1
# 6. Sobrescribe p1 con datos maliciosos
# 7. malloc(32) -> retorna p1 de nuevo con datos sobrescritos
```

## Flag
```
CTF{fastbin_attack}
```

## Conceptos
- Heap exploitation
- Double free vulnerability
- Fastbin structure
- Heap feng shui
