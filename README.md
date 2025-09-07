# 🎮 Grammar Adventure

🎓 Juego educativo interactivo desarrollado con Python y Pygame para aprender gramática inglesa de manera divertida 🎯📚, featuring 4 capítulos temáticos (Simple Past, Comparatives, Present Perfect, Future) 📖⚡ con sistema de puntuación progresivo 🏆, velocidad adaptativa 🚀 y feedback inmediato 🎵. Interfaz pixel art retro 🎨 con mecánicas de typing game 💨 optimizada para el aprendizaje interactivo y la mejora de habilidades lingüísticas 🌟.

<div align="center">

![Grammar Adventure Logo](Grammar%20Adventure/Material/Logo.jpg)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)
[![Game](https://img.shields.io/badge/Game-Educational-purple.svg)](#)

[🎯 Características](#-características) • [🚀 Instalación](#-instalación) • [🎮 Cómo Jugar](#-cómo-jugar) • [📚 Temas](#-temas-disponibles) • [🛠️ Desarrollo](#️-desarrollo)

</div>

---

## 📋 Descripción

**Grammar Adventure** es un juego educativo desarrollado en Python con Pygame que te ayuda a mejorar tus habilidades en gramática inglesa de manera divertida e interactiva. El juego presenta diferentes niveles temáticos donde debes completar oraciones con la palabra correcta antes de que desaparezcan de la pantalla.

### 🎯 Características

- 🎨 **Interfaz gráfica atractiva** con estilo pixel art
- 🎵 **Efectos de sonido inmersivos** para cada acción
- 📈 **Sistema de puntuación progresivo** con dificultad incremental
- ❤️ **Sistema de vidas** con 3 oportunidades por partida
- 🎪 **4 capítulos temáticos** diferentes de gramática inglesa
- ⚡ **Velocidad adaptativa** que aumenta con tu progreso
- 🏆 **Feedback inmediato** con sonidos de éxito y error

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/grammar-adventure.git
   cd grammar-adventure
   ```

2. **Instala las dependencias**
   ```bash
   pip install pygame
   ```

3. **Ejecuta el juego**
   ```bash
   python "Grammar Adventure.py"
   ```

### 📦 Estructura del proyecto

```
Grammar Adventure/
├── Grammar Adventure.py          # Archivo principal del juego
├── Font/                        # Fuentes personalizadas
│   ├── Pixelletters-RLm3.ttf
│   └── Pixellettersfull-BnJ5.ttf
├── Material/                    # Recursos del juego
│   ├── *.png                   # Imágenes y sprites
│   ├── *.jpg                   # Fondos y gráficos
│   └── *.wav                   # Efectos de sonido
└── README.md                   # Este archivo
```

## 🎮 Cómo Jugar

### 🎯 Objetivo
Completa las oraciones escribiendo la palabra correcta antes de que la frase salga de la pantalla.

### 🕹️ Controles
- **Teclado**: Escribe la palabra faltante
- **Backspace**: Borra caracteres
- **ESC**: Salir del juego

### 📋 Reglas del juego

1. 📝 **Aparecerá una frase con una palabra faltante** (marcada con "_")
2. ⌨️ **Escribe la palabra correcta** para ganar puntos
3. 📈 **A medida que aumenta tu puntuación**, aparecerán más frases simultáneamente
4. ⚡ **La velocidad aumenta** progresivamente con tu puntaje
5. 🚫 **No se permiten contracciones** (usa la forma completa)
6. ❤️ **Pierdes una vida** por cada frase que no completes
7. 💀 **El juego termina** cuando te quedas sin vidas

## 📚 Temas Disponibles

<details>
<summary><strong>🕐 Simple Past (Pasado Simple)</strong></summary>

- **Enfoque**: Verbos regulares e irregulares en pasado
- **Ejemplos**: 
  - "She _ the tree (climb)" → "climbed"
  - "Mary _ off the tree (fall)" → "fell"
- **Dificultad**: ⭐⭐☆☆☆
</details>

<details>
<summary><strong>📊 Comparatives and Superlatives (Comparativos y Superlativos)</strong></summary>

- **Enfoque**: Formas comparativas y superlativas de adjetivos
- **Ejemplos**: 
  - "La Paz is _ _ Santa Cruz (cold)" → "colder than"
  - "Mt. Everest is _ _ mountain in the world (tall)" → "the tallest"
- **Dificultad**: ⭐⭐⭐☆☆
</details>

<details>
<summary><strong>✅ Present Perfect (Presente Perfecto)</strong></summary>

- **Enfoque**: Estructura have/has + participio pasado
- **Ejemplos**: 
  - "She _ _ to the movies (go)" → "has gone"
  - "I _ _ living in Bolivia this year (be)" → "have been"
- **Dificultad**: ⭐⭐⭐⭐☆
</details>

<details>
<summary><strong>🔮 Future with will / going to (Futuro)</strong></summary>

- **Enfoque**: Expresiones de futuro con "will" y "going to"
- **Ejemplos**: 
  - "I _ _ _ to Bolivia next year (won't/go)" → "will not go"
  - "She is _ _ _ a new business (go/start)" → "going to start"
- **Dificultad**: ⭐⭐⭐⭐⭐
</details>

## 🎨 Capturas de Pantalla

<div align="center">

### 🏠 Menú Principal
*Interfaz de inicio con animación del logo*

### 📖 Pantalla de Reglas
*Explicación visual de las mecánicas del juego*

### 🎯 Gameplay
*Acción en tiempo real con múltiples frases*

### 📊 Selección de Capítulos
*Elige tu tema de gramática favorito*

</div>

## 🛠️ Desarrollo

### 🔧 Tecnologías utilizadas

- **Python 3.8+**: Lenguaje de programación principal
- **Pygame 2.0+**: Framework para desarrollo de juegos 2D
- **Pixel Art**: Estilo gráfico retro

### 🏗️ Arquitectura del código

```python
# Estructura principal
├── Inicialización (pygame, mixer, display)
├── Configuración de recursos (sonidos, imágenes, fuentes)
├── Sistema de temas y frases
├── Funciones principales:
│   ├── ventana_principal()      # Menú de inicio
│   ├── mostrar_reglas()         # Pantalla de instrucciones
│   ├── menu_niveles()           # Selección de capítulos
│   ├── bucle_juego()            # Loop principal del juego
│   ├── nueva_frase()            # Generador de contenido
│   └── game_over()              # Pantalla final
```

### 🎮 Mecánicas del juego

- **Sistema de puntuación**: +1 punto por respuesta correcta
- **Sistema de vidas**: 3 vidas iniciales, -1 por frase perdida
- **Velocidad dinámica**: `velocidad = 0.4 + (puntuacion/50)`
- **Frases simultáneas**: `cantidad = (puntuacion // 8) + 1`
- **Colores aleatorios**: Cada frase tiene un color único

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el juego:

1. 🍴 Fork el proyecto
2. 🌱 Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔄 Abre un Pull Request

### 💡 Ideas para contribuir

- [ ] Agregar más temas de gramática
- [ ] Implementar sistema de puntuación máxima
- [ ] Añadir modo multijugador
- [ ] Crear sistema de logros
- [ ] Mejorar efectos visuales
- [ ] Traducir a otros idiomas

## 📝 License

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [Tu GitHub](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- 🎨 Recursos gráficos en estilo pixel art
- 🎵 Efectos de sonido para una experiencia inmersiva
- 📚 Contenido educativo de gramática inglesa
- 🎮 Comunidad de Pygame por el framework

---

<div align="center">

**¿Te gustó el proyecto? ¡Dale una ⭐ estrella!**

[🐛 Reportar Bug](https://github.com/tu-usuario/grammar-adventure/issues) • [💡 Solicitar Feature](https://github.com/tu-usuario/grammar-adventure/issues) • [💬 Discusiones](https://github.com/tu-usuario/grammar-adventure/discussions)

**¡Aprende gramática inglesa jugando! 🎓🎮**

</div>
