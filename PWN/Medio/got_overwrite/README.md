# GOT Overwrite (PWN - Medio)

## Descripción
La tabla GOT (Global Offset Table) contiene direcciones de funciones de libc. Si puedes sobrescribir una entrada GOT, puedes redirigir las llamadas de función.

## Archivo
`got_overwrite.c` - Programa vulnerable

## Compilación
```bash
gcc -o got_overwrite got_overwrite.c -z relro=partial
```

## Instrucciones
1. Encuentra la dirección GOT de `puts()` o `printf()`
2. Sobrescribe la entrada GOT con la dirección de `print_flag()`
3. Cuando la función sea llamada, se ejecutará tu función

## Solución
```bash
# Encontrar GOT
objdump -R got_overwrite | grep puts
gdb ./got_overwrite
(gdb) p puts
(gdb) p &print_flag
```

## Flag
```
CTF{got_overwrite}
```

## Conceptos
- GOT table structure
- Relocation entries
- Function pointer hijacking
- Partial RELRO bypass
