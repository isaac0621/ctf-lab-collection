# CTF Colaborativo - Guía Rápida

## 🎯 Para participantes

### Empezar
```bash
# Clonar
git clone https://github.com/isaac0621/ctf-lab-collection.git

# Elegir un reto
cd WEB/Facil/hidden_endpoint

# Leer instrucciones
cat README.md
```

### Resolver
1. Lee `README.md`
2. Usa `challenge.py` o `app.js`
3. Resuelve el reto
4. Verifica con `checker.py`

```bash
python3 checker.py "CTF{tu_flag}"
```

### Compartir solución
```bash
git checkout -b mi-solucion
echo "# Mi solución" > solution.md
git add .
git commit -m "Solución del reto"
git push origin mi-solucion
# Abre PR en GitHub
```

## 📊 Estado del Repositorio

```
✅ WEB:       6/6 retos completados
✅ CRYPTO:    6/6 retos completados
✅ PWN:       5/5 retos completados
✅ REVERSING: 3/3 retos completados
✅ FORENSICS: 3/3 retos completados
✅ STEGO:     3/3 retos completados
✅ OSINT:     3/3 retos completados

TOTAL: 29/29 retos listos para resolver
```

## 🎓 Contenido Educativo

Cada reto enseña:
- Vulnerabilidades reales
- Técnicas de explotación
- Herramientas profesionales
- Mejores prácticas de seguridad

## 💡 Tips

- Empieza por retos fáciles
- Lee la documentación completamente
- Experimenta y prueba ideas
- Busca recursos en internet
- Pide ayuda en issues
- Comparte lo que aprendes

## 🔗 Recursos

- [Protocolo y estructura](PROTOCOLO.md)
- [README principal](README.md)
- [GitHub Issues](https://github.com/tu-usuario/Retos-CTF-Prácticos/issues)

---

¿Preguntas? ¡Abre un issue! 📝
