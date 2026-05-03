# Retos CTF Prácticos - Repositorio Colaborativo

![CTF](https://img.shields.io/badge/CTF-Capture%20The%20Flag-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Un repositorio colaborativo de retos de Capture The Flag (CTF) para estudiantes de ciberseguridad colegial. Aprende seguridad ofensiva resolviendointeriores y ayuda a tus compañeros.

## 📋 Estructura

```
Retos-CTF-Prácticos/
├── WEB/
│   ├── Facil/
│   │   ├── hidden_endpoint/
│   │   └── cookie_sin_firma/
│   ├── Medio/
│   │   ├── sqli_union/
│   │   └── xss_reflejado/
│   └── Difícil/
│       ├── deserializacion_insegura/
│       └── race_condition/
├── CRYPTO/
│   ├── Facil/
│   │   ├── caesar/
│   │   └── base64_doble/
│   ├── Medio/
│   │   ├── repeating_xor/
│   │   └── aes_ecb/
│   └── Difícil/
│       ├── rsa_sin_padding/
│       └── lcg/
├── PWN/
│   ├── Facil/
│   │   ├── bof/
│   │   └── ret2win/
│   ├── Medio/
│   │   ├── ret2libc/
│   │   └── got_overwrite/
│   └── Difícil/
│       ├── rop/
│       └── fastbins/
├── REVERSING/
│   ├── Facil/
│   ├── Medio/
│   │   └── obfuscacion/
│   └── Difícil/
│       └── vm/
├── FORENSICS/
│   ├── Facil/
│   ├── Medio/
│   │   └── volatility/
│   └── Difícil/
│       └── pcap_fragmentado/
├── STEGO/
│   ├── Facil/
│   │   └── lsb/
│   ├── Medio/
│   │   └── multilayer/
│   └── Difícil/
│       └── ruido_adaptativo/
├── OSINT/
│   ├── Facil/
│   │   └── buscar_username/
│   ├── Medio/
│   │   └── correlacion_redes/
│   └── Difícil/
│       └── identidad_falsa/
└── README.md
```

## 🎯 Categorías

### 🌐 WEB (6 retos)
Vulnerabilidades web como SQLi, XSS, inseguridad en cookies, race conditions.

### 🔐 CRYPTO (6 retos)
Criptografía: Caesar, Base64, XOR, AES, RSA, LCG.

### ⚙️ PWN (5 retos)
Binary exploitation: Buffer overflow, ret2win, ret2libc, ROP, heap.

### 🔍 REVERSING (3 retos)
Ingeniería inversa: Análisis de binarios, desobfuscación, VM.

### 🕵️ FORENSICS (3 retos)
Análisis forense: Metadatos, memoria, tráfico de red.

### 🎨 STEGO (3 retos)
Esteganografía: LSB, multilayer, ruido adaptativo.

### 🌍 OSINT (3 retos)
Inteligencia de fuentes abiertas: búsqueda, correlación, identidad.

## 🚀 Cómo usar

### 1. Clonar el repositorio
```bash
git clone https://github.com/isaac0621/ctf-lab-collection.git
cd Retos-CTF-Prácticos
```

### 2. Resolver un reto
```bash
cd WEB/Facil/hidden_endpoint
cat README.md  # Lee las instrucciones
# Resuelve el reto
python3 checker.py "tu_flag_aqui"  # Verifica tu respuesta
```

### 3. Enviar una solución
```bash
# Crea una rama con tu nombre
git checkout -b mi-solucion

# Añade tu solución en solution.txt o solution.md
echo "CTF{flag}" > WEB/Facil/hidden_endpoint/solution.txt

# Commit y push
git add .
git commit -m "Solución WEB/Facil/hidden_endpoint"
git push origin mi-solucion

# Abre un Pull Request en GitHub
```

## 📝 Estructura de cada reto

Cada reto contiene:

- **README.md** - Descripción, instrucciones y concepto de seguridad
- **challenge.py/app.js** - El reto vulnerable
- **checker.py** - Script para verificar tu flag
- **solution.py/solution.md** - Solución (solo para referencia)
- **exploit.py** - Exploit automático (cuando aplica)

## 🏆 Sistema de Flags

Las flags tienen este formato:
```
CTF{descripcion_corta}
```

Ejemplo:
```
CTF{hidden_js123}
CTF{xss_reflected}
CTF{buffer_overflow}
```

## 📚 Recursos recomendados

### Herramientas
- **Web**: Burp Suite, OWASP ZAP, curl
- **Crypto**: Wireshark, CyberChef, OpenSSL
- **PWN**: GDB, Radare2, pwntools
- **Reverse**: Ghidra, IDA, objdump
- **Forensics**: Volatility, Wireshark, exiftool
- **Stego**: Stegsolve, SilentEye, Binwalk
- **OSINT**: Shodan, Google Dorks, Maltego

### Documentación
- [HackTricks](https://book.hacktricks.xyz/) - Técnicas de hacking
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Payloads
- [PortSwigger Academy](https://portswigger.net/web-security) - Web security
- [Pwn College](https://pwn.college/) - Binary exploitation
- [TryHackMe](https://tryhackme.com/) - Plataforma de aprendizaje

## 🤝 Contribuir

1. Resuelve un reto
2. Sube tu solución en una rama
3. Abre un PR con:
   - Tu solución en `solution.md`
   - Explicación de la técnica
   - Links a recursos útiles

## 📊 Progreso

Mantén un registro de los retos que has completado:

- [ ] WEB/Facil/hidden_endpoint
- [ ] WEB/Facil/cookie_sin_firma
- [ ] WEB/Medio/sqli_union
- [ ] WEB/Medio/xss_reflejado
- [ ] WEB/Difícil/deserializacion_insegura
- [ ] WEB/Difícil/race_condition
- [ ] CRYPTO/Facil/caesar
- [ ] CRYPTO/Facil/base64_doble
- [ ] CRYPTO/Medio/repeating_xor
- [ ] CRYPTO/Medio/aes_ecb
- [ ] CRYPTO/Difícil/rsa_sin_padding
- [ ] CRYPTO/Difícil/lcg
- [ ] PWN/Facil/bof
- [ ] PWN/Facil/ret2win
- [ ] PWN/Medio/ret2libc
- [ ] PWN/Medio/got_overwrite
- [ ] PWN/Difícil/rop
- [ ] PWN/Difícil/fastbins
- [ ] REVERSING/Facil (string comparison)
- [ ] REVERSING/Medio/obfuscacion
- [ ] REVERSING/Difícil/vm
- [ ] FORENSICS/Facil (EXIF)
- [ ] FORENSICS/Medio/volatility
- [ ] FORENSICS/Difícil/pcap_fragmentado
- [ ] STEGO/Facil/lsb
- [ ] STEGO/Medio/multilayer
- [ ] STEGO/Difícil/ruido_adaptativo
- [ ] OSINT/Facil/buscar_username
- [ ] OSINT/Medio/correlacion_redes
- [ ] OSINT/Difícil/identidad_falsa

## ⚠️ Disclaimer

Este repositorio es para **educación y aprendizaje** en un ambiente de CTF colegial. 
**No uses estas técnicas** en sistemas sin autorización explícita.

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE)

## 👥 Autores

- Josué - Creador y mantenedor

## 💬 Contacto

- Issues: [GitHub Issues](https://github.com/tu-usuario/Retos-CTF-Prácticos/issues)
- Discussions: [GitHub Discussions](https://github.com/tu-usuario/Retos-CTF-Prácticos/discussions)

---

¡Buena suerte resolviendo los retos! 🎯

