# EXIF y Strings Challenge

## Reto Fácil - Forensics

### Instrucciones
1. Se te proporciona una imagen y un archivo
2. Extrae información usando herramientas forenses básicas
3. Encuentra el flag

### Herramientas útiles
- `exiftool` - Extrae metadatos EXIF
- `strings` - Extrae strings legibles del archivo
- `file` - Identifica tipo de archivo
- `hexdump` - Muestra contenido en hexadecimal

### Ejemplo
```bash
# Extraer EXIF
exiftool image.jpg

# Ver strings
strings image.jpg

# Ver tipo de archivo
file image.jpg
```

### Flag
```
CTF{forensics_exif}
```

### Conceptos
- EXIF metadata
- File analysis
- String extraction
- Steganography basics
