# Protocolo Estándar para Retos CTF

## Flag Format

Todas las flags siguen este formato:
```
CTF{descripcion_corta}
```

Ejemplos válidos:
```
CTF{hidden_js_flag}
CTF{xss_reflected}
CTF{buffer_overflow_exploit}
CTF{rsa_cracked}
```

## Checker Script Template

Todos los retos incluyen un `checker.py` con este formato:

```python
import sys

FLAG = "CTF{mi_flag}"

if len(sys.argv) != 2:
    print("Usage: python3 checker.py <flag>")
    sys.exit(1)

result = "OK" if sys.argv[1] == FLAG else "FAIL"
print(result)
```

### Uso
```bash
python3 checker.py "CTF{mi_flag}"
```

## README Template

Cada reto incluye un `README.md` con:

```markdown
# Nombre del Reto (Categoría - Dificultad)

## Descripción
Breve descripción del reto

## Challenge/Instrucciones
Cómo empezar

## Solución
Pasos o código para resolver

## Flag
```CTF{flag_aqui}```

## Conceptos
- Concepto 1
- Concepto 2
```

## Estructura de Directorios

```
NombreReto/
├── README.md           # Descripción y guía
├── checker.py          # Verificador de flag
├── challenge.py        # El reto (puede ser .js, .c, etc)
├── solution.py         # Solución completa
└── exploit.py          # Exploit automático (opcional)
```

## Enviar Soluciones

Para compartir tu solución:

1. Crea una rama: `git checkout -b solucion-categoria-nombre`
2. Añade un archivo `solution.md` con:
   - Tu nombre/nick
   - Pasos de solución
   - Explicación de conceptos
   - Links a recursos útiles

Ejemplo:
```markdown
# Solución: WEB/Facil/hidden_endpoint

## Resuelto por: TuNombre

## Pasos
1. Abrí las developer tools (F12)
2. Busqué en la pestaña Network
3. Encontré el endpoint en script.js

## Explicación
La aplicación tenía un endpoint oculto en JavaScript...

## Recursos
- [OWASP - Hidden endpoints](https://...)
- [Recon web](https://...)
```

3. Haz un commit: `git commit -m "Add solution for WEB/Facil/hidden_endpoint"`
4. Push: `git push origin solucion-categoria-nombre`
5. Abre un Pull Request

## Niveles de Dificultad

### Fácil ⭐
- Conceptos básicos
- Herramientas simples
- Pocos pasos
- Tiempo: < 30 minutos

### Medio ⭐⭐
- Conceptos avanzados
- Múltiples pasos
- Herramientas especializadas
- Tiempo: 30 min - 2 horas

### Difícil ⭐⭐⭐
- Conceptos complejos
- Requiere investigación
- Múltiples técnicas
- Tiempo: 2+ horas

## Mejores Prácticas

1. **Documenta tu proceso**
   - Qué intentaste
   - Qué funcionó
   - Qué aprendiste

2. **Sé claro en explicaciones**
   - Usa código formateado
   - Explica cada paso
   - Proporciona referencias

3. **Ayuda a otros**
   - Comenta en PRs
   - Sugiere mejoras
   - Comparte recursos

4. **Respeta la dificultad**
   - No publiques spoilers sin advertencia
   - Usa tags `[SPOILER]`
   - Deja espacio para que otros resuelvan

## Reportar Issues

Si encuentras un problema:
1. Verifica que no esté reportado
2. Sé específico en la descripción
3. Incluye versiones de herramientas
4. Proporciona logs si es necesario

## Evolución del Repositorio

- v1.0: Retos básicos (fácil)
- v1.1: Retos intermedios (medio)
- v1.2: Retos avanzados (difícil)
- v2.0: Nuevas categorías
- Futuro: Plataforma interactiva

---

¡Feliz hacking! 🎯
