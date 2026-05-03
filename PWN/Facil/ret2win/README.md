# ret2win (PWN - Fácil)

## Descripción
Hay una función `win()` que nunca se llama. Debes explotar un buffer overflow para redirigir la ejecución hacia esa función.

## Archivo
`ret2win.c` - Programa con función win()

## Compilación
```bash
gcc -fno-stack-protector -o ret2win ret2win.c
```

## Instrucciones
1. Abre el binario en un debugger (gdb)
2. Encuentra la dirección de `win()`
3. Calcula el offset del buffer overflow
4. Crea un payload que sobrescriba RIP con la dirección de win()

## Solución
```bash
# Encontrar dirección de win()
objdump -d ret2win | grep win

# Con gdb
gdb ./ret2win
(gdb) p &win
(gdb) p &buf
```

Luego crear el exploit en Python.

## Flag
```
CTF{ret2win_shell}
```

## Conceptos
- ret2win attack
- Function pointer hijacking
- Stack frame inspection
- Address space layout
