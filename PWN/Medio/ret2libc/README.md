# ret2libc (PWN - Medio)

## Descripción
El binario tiene DEP (Data Execution Prevention) habilitado, por lo que no puedes ejecutar shellcode en la pila. En su lugar, debes reutilizar funciones de libc (ret2libc o ROP gadgets) para ejecutar comandos.

## Archivo
`ret2libc.c` - Programa vulnerable

## Compilación
```bash
gcc -fno-stack-protector -z execstack -o ret2libc ret2libc.c
```

## Instrucciones
1. Filtra una dirección de libc
2. Usa gadgets ROP para preparar argumentos
3. Llama a `system()` o `execve()`

## Solución
```python
from pwn import *

p = process('./ret2libc')

# Leak libc address
...

# Construir ROP chain para system("/bin/sh")
# pop rdi; ret;
# address_of_"/bin/sh"
# address_of_system
```

## Flag
```
CTF{ret2libc_exploited}
```

## Conceptos
- ret2libc attack
- DEP/NX bypass
- Libc leaking
- ROP gadgets
