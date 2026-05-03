# Memory Forensics - Volatility (FORENSICS - Medio)

## Descripción
Se te proporciona un dump de memoria del sistema. Debes analizarlo usando Volatility.

## Instrucciones
1. Instala Volatility: `pip install volatility3`
2. Analiza el memory dump
3. Busca el flag

## Comandos útiles
```bash
volatility -f memory.dmp windows.pslist
volatility -f memory.dmp windows.netscan
volatility -f memory.dmp windows.dumpfiles
```

## Flag
```
CTF{volatility_mem}
```

## Conceptos
- Memory forensics
- Process analysis
- Network forensics
- File recovery
