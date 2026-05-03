# Reversing Fácil

## Descripción
Un programa binario simple que valida una contraseña. Debes encontrar la contraseña correcta.

## Archivo
`check` - Binario compilado

## Compilación
```bash
gcc -o check check.c
```

## Instrucciones
1. Abre el binario en un disassembler (IDA, Ghidra, objdump)
2. Busca la comparación de strings
3. Encuentra la contraseña

## Solución
```bash
# Usar strings para extraer strings de texto
strings check | grep -i password

# O usar objdump
objdump -d check
```

## Flag
```
CTF{reversing_easy}
```

## Conceptos
- Binary analysis
- Disassembly
- String extraction
- Static analysis
