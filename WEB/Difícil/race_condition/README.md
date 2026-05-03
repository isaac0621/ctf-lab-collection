# Race Condition (WEB - Difícil)

## Descripción
La aplicación tiene una vulnerabilidad de race condition. El balance se verifica pero antes de restar hay un delay. Múltiples requests concurrentes pueden explotar esto.

## Instrucciones
1. Inicia el servidor: `python app.py`
2. Inicia múltiples requests simultáneos al endpoint `/buy`
3. Explota la race condition para llevar el balance a 0 o negativo
4. Obtén la flag en `/flag`

## Solución
Ejecuta el exploit:
```bash
python exploit.py
```

Esto enviará múltiples requests concurrentes que aprovecharán la ventana de tiempo entre la verificación y la resta.

## Flag
```
CTF{race_cond_won}
```

## Conceptos
- Race conditions
- Concurrency issues
- Vulnerabilidades de timing
- TOCTOU (Time-of-check-time-of-use)
- Sincronización de threads
