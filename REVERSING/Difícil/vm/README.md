# VM Interpreter (REVERSING - Difícil)

## Descripción
Se te proporciona un intérprete de una máquina virtual simple. Debes entender el bytecode y ejecutarlo.

## Archivo
`vm.py` - Intérprete simple

## Instrucciones
1. Aprende el formato de bytecode
2. Crea bytecode que produzca un resultado específico
3. Ejecuta e interpreta los resultados

## Opcodes
- 0x01: LOAD A (cargar valor en registro A)
- 0x02: LOAD B (cargar valor en registro B)
- 0x03: ADD (sumar A + B)
- 0x04: CMP (comparar A con valor)
- 0xFF: END (terminar)

## Solución
```python
bytecode = [
    0x01, 0x0A,  # LOAD A 10
    0x02, 0x05,  # LOAD B 5
    0x03,        # ADD (A = 15)
    0x04, 0x0F,  # CMP 15 (compara A con 0x0F)
    0xFF         # END
]
```

## Flag
```
CTF{vm_interpreter}
```

## Conceptos
- Virtual machine
- Bytecode interpretation
- Custom instruction set
- Assembly language
