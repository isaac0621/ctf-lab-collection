# 🚀 Cómo Publicar en GitHub

## Paso 1: Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Click en **New repository** (botón verde)
3. Llena los datos:
   - **Repository name**: `Retos-CTF-Prácticos`
   - **Description**: `Un repositorio colaborativo de retos CTF para estudiantes de ciberseguridad colegial.`
   - **Public** (marca esta opción para que sea visible)
   - Marca "Add a README file" (opcional, ya tienes uno)
4. Click **Create repository**

---

## Paso 2: Inicializar Git Localmente

```bash
cd c:\Users\______Aquí su usuario de la compu\ctf-lab-collection

# Inicializar git
git init

# Configurar usuario (una sola vez)
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Agregar todos los archivos
git add .

# Crear commit inicial
git commit -m "Initial commit: CTF repository with 29 challenges"
```

---

## Paso 3: Conectar con GitHub

```bash
# Reemplaza URL_DEL_REPO con la URL que GitHub te proporciona
# Formato: https://github.com/tu-usuario/Retos-CTF-Prácticos.git

git remote add origin https://github.com/TU_USUARIO/Retos-CTF-Prácticos.git

# Si usas SSH (requiere configuración previa):
# git remote add origin git@github.com:TU_USUARIO/Retos-CTF-Prácticos.git
```

---

## Paso 4: Subir los cambios

```bash
# Renombrar rama a 'main' (estándar moderno)
git branch -M main

# Subir los cambios
git push -u origin main
```

---

## ✅ Verificar que funcionó

1. Ve a https://github.com/tu-usuario/Retos-CTF-Prácticos
2. Deberías ver:
   - Todos los archivos y carpetas
   - El README.md en la página principal
   - Los retos organizados por categoría

---

## 🔒 Configuración Adicional (Recomendada)

### Agregar colaboradores
1. Ve a **Settings** → **Collaborators**
2. Click **Add people**
3. Ingresa el username de GitHub de tus compañeros

### Activar Discussions
1. Ve a **Settings**
2. Baja a **Features**
3. Marca **Discussions**

### Crear Plantilla de PR
Crea archivo `.github/pull_request_template.md`:
```markdown
## Descripción
- [ ] Solución de reto
- [ ] Mejora de documentación
- [ ] Nuevo reto

## Reto
[Nombre del reto]

## Cambios
- 

## Checklist
- [ ] Testeo completado
- [ ] Documentación actualizada
```

---

## 💻 Comandos Útiles Posteriores

```bash
# Ver estado
git status

# Ver cambios
git diff

# Actualizar desde GitHub
git pull origin main

# Crear rama para nueva solución
git checkout -b solucion/web/hidden_endpoint

# Cambiar de rama
git checkout main

# Ver historial
git log --oneline

# Ver ramas
git branch -a
```

---

## 📊 Flujo típico después del setup

```
1. Compañero clona el repo
   → git clone https://github.com/tu-usuario/Retos-CTF-Prácticos.git

2. Resuelve un reto
   → Crea archivo solution.md

3. Hace commit
   → git commit -m "Solution: WEB/Facil/hidden_endpoint"

4. Sube cambios
   → git push origin mi-rama

5. Abre PR en GitHub
   → Describe su solución

6. Otros comentan y revisan
   → Feedback en los comentarios

7. Se aprueba y merge
   → El código se integra
```

---

## 🎯 Primera Persona que Clona

Tus compañeros harán esto:

```bash
# 1. Clonar
git clone https://github.com/tu-usuario/Retos-CTF-Prácticos.git
cd Retos-CTF-Prácticos

# 2. Ver retos disponibles
ls -la

# 3. Elegir un reto
cd WEB/Facil/hidden_endpoint

# 4. Leer instrucciones
cat README.md

# 5. Resolver
# ... trabajar en el reto ...

# 6. Probar
python3 checker.py "CTF{flag}"

# 7. Subir solución (opcional)
git checkout -b mi-solucion
echo "# Mi solución" > solution.md
git add .
git commit -m "Solved WEB/Facil/hidden_endpoint"
git push origin mi-solucion
# Abrir PR en GitHub
```

---

## ⚠️ Si algo sale mal

### Error: "fatal: not a git repository"
```bash
git init
```

### Error: "failed to push"
```bash
# Asegurar que tienes la rama correcta
git branch -M main
git push -u origin main
```

### Error: "authentication failed"
```bash
# Usa token de GitHub en lugar de contraseña
# O configura SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
```

---

## 📚 Recursos Útiles

- [GitHub Docs - Getting started](https://docs.github.com/en/get-started)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Desktop (GUI alternativa)](https://desktop.github.com/)

---

## 🎉 ¡Listo!

Una vez que hayas completado estos pasos:
- Tu repositorio estará en GitHub
- Tus compañeros podrán clonarlo
- Podrán contribuir con soluciones
- Será un espacio colaborativo de aprendizaje

---

**¡Éxito con tu repositorio CTF! 🎯**

Para ayuda adicional, abre un issue en GitHub o contacta a tu profesor/mentor.
