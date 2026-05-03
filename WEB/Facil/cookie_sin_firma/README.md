# Cookie sin Firma (WEB - Fácil)

## Descripción
La aplicación verifica si eres admin solo mirando una cookie sin validarla. Es una vulnerabilidad de autenticación débil.

## Instrucciones
1. Inicia el servidor: `node app.js`
2. Accede a `http://localhost:3000/admin` normalmente (recibirás "nope")
3. Modifica la cookie para hacerte pasar por admin

## Solución
Usando curl:
```bash
curl -H "Cookie: role=admin" http://localhost:3000/admin
```

O en el navegador:
- Abre la consola (F12)
- Ve a Application → Cookies
- Añade una cookie con nombre `role` y valor `admin`
- Recarga la página
- Accede a `/admin`

## Flag
```
CTF{cookie_pwned}
```

## Conceptos
- Inseguridad en manejo de cookies
- Falta de autenticación real
- Validación del lado del cliente
- Escalación de privilegios
