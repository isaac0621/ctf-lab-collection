# Hidden Endpoint (WEB - Fácil)

## Descripción
La aplicación tiene un endpoint oculto en JavaScript que revela la flag. El objetivo es encontrarlo.

## Instrucciones
1. Inicia el servidor: `node app.js`
2. Abre `http://localhost:3000` en el navegador
3. Busca el endpoint en el código JavaScript
4. Accede a `/api/flag_hidden_92a`

## Solución
- Abre las herramientas de desarrollador (F12)
- Ve a la pestaña "Network" o "Sources"
- Busca en `public/script.js` el endpoint `/api/flag_hidden_92a`
- Accede directamente a `http://localhost:3000/api/flag_hidden_92a`
- La flag aparece en la respuesta

## Flag
```
CTF{hidden_js123}
```

## Conceptos
- Reconocimiento de aplicaciones web
- Análisis de código JavaScript
- Enumeración de endpoints API
