# ROP (PWN - Difícil)

## Descripción
Return-Oriented Programming (ROP) es una técnica para ejecutar código reutilizando pequeños fragmentos de código existente ("gadgets") terminados con `ret`.

## Archivo
`rop.c` - Programa vulnerable

## Compilación
```bash
gcc -fno-stack-protector -o rop rop.c
```

## Instrucciones
1. Encuentra gadgets útiles en el binario
2. Encadena gadgets para construir una cadena ROP
3. Ejecuta un comando deseado

## Solución
Usar herramientas como:
- `ropper` - Para encontrar gadgets
- `pwn` (Python library) - Para construir chains
- `ROPgadget` - Búsqueda de gadgets

```bash
ropper --file rop -s "pop rdi"
```

## Flag
```
CTF{rop_gadgets}
```

## Conceptos
- ROP (Return-Oriented Programming)
- Gadget chaining
- DEP/NX bypass
- Control flow hijacking
