# Ruido Adaptativo (STEGO - Difícil)

## Descripción
El mensaje está oculto usando ruido adaptativo. El mensaje se camufla en patrones de ruido que varían según la imagen.

## Instrucciones
Técnicas para detectar:
1. Análisis espectral (FFT)
2. Análisis estadístico de píxeles
3. Búsqueda de patrones anómalos
4. Herramientas especializadas (Stegsolve)

## Herramientas
- `Stegsolve` - Análisis visual de steganografía
- `SilentEye` - Detección de steganografía
- `WavSteg` - Steganografía de audio/imagen

## Solución
```bash
# Usar Stegsolve (Java)
java -jar Stegsolve.jar

# Analizar histogramas
# Buscar anomalías en bits

# O usar Python con análisis estadístico
import numpy as np
from PIL import Image

img = Image.open('image.png')
data = np.array(img)

# Buscar patrones anómalos
# ...
```

## Flag
```
CTF{adaptive_noise}
```

## Conceptos
- Advanced steganography
- Noise patterns
- Statistical analysis
- Signal processing
