# Plan de trabajo: penta-discovery (Discovery)

Este documento contiene la arquitectura, distribución y hoja de ruta detallada para el desarrollo del prototipo en Python, como parte del proyecto final de Code in Place (Stanford University).

## 1. Arquitectura de archivos (MVC)

El proyecto se estructurará en cuatro archivos principales para garantizar la separación de responsabilidades:

* main.py: punto de entrada de la aplicación. Inicializa el MODELO (modelo.py), la VISTA (vista.py) y el CONTROLADOR (controlador.py), y arranca el loop principal de la interfaz gráfica.
* modelo.py: contiene la lógica de datos, llamadas a APIs externas (letras/música) y el algoritmo de recomendaciones. (en principio reutilizable a futuro como API en Penta).
* vista.py: contiene la interfaz gráfica nativa con tkinter y Canvas. Dibuja los componentes y expone los elementos de la interfaz.
* controlador.py: el puente. Escucha los eventos de la vista (clicks, búsquedas), le pide datos al modelo y actualiza la vista con la nueva información.

---

## 2. Especificación del layout (UI Canvas)

La ventana de la aplicación tendrá un tamaño base (ej. 800x600 píxeles) y se dividirá visualmente mediante áreas (Canvas o frames de tkinter) respetando la siguiente distribución:

+---------------------------------------------------------+
|                    [ Barra de busqueda ]                |
+---------------------------+-----------------------------+
|                           |   [ Info de la Cancion ]    |
|                           |   - Titulo / Artista        |
|    [ Letras de la         |   - Album                   |
|       Cancion ]           +-----------------------------+
|                           |   [ Lista de Sugerencias ]  |
|                           |   - Cancion Recomendada 1   |
|                           |   - Cancion Recomendada 2   |
|                           |   - Cancion Recomendada 3   |
+---------------------------+-----------------------------+
|                  [ Barra de reproduccion ]              |
+---------------------------------------------------------+

---

## 3. Hoja de ruta: paso a paso (iterativa)

### Fase 1: El esqueleto estatico
* Objetivo: crear los archivos base del proyecto y levantar la interfaz vacía con sus bloques delimitados.
* Directiva: en vista.py, definir las dimensiones de la ventana y pintar rectángulos de diferentes colores de fondo para cada sección (ej. gris para letras, negro para reproducción, amarillo para info, etc.) usando el sistema de grillas (grid) o empaquetado (pack) de tkinter.

### Fase 2: El flujo de datos "Mock" (falsos)
* Objetivo: validar que la arquitectura MVC funciona y se comunica correctamente antes de meter código complejo de internet.
* Directiva: 
    * en modelo.py, crear un método que devuelva un diccionario con datos estáticos (Título: "Song A", Letra: "Letra de la cancion...", Sugerencias: ["Song B", "Song C"]).
    * en controlador.py, hacer que al presionar el botón "Buscar" de la vista, se invoque este método e inyecte los textos correspondientes en el Canvas.

### Fase 3: Conexión con el mundo real (APIs & algoritmo)
* Objetivo: reemplazar los datos falsos por datos reales, dinámicos y funcionales.
* Directiva:
    * implementar en el modelo el uso de librerías como urllib o requests para consultar una API de música (como el endpoint público de búsqueda de Deezer) y una API de letras.
    * crear una función de recomendación en Python puro que tome el género o artista de la canción actual y filtre una lista local (o de la API) para devolver canciones similares.

### Fase 4: Reproducción y pulido visual
* Objetivo: hacer que el prototipo suene y se vea completamente integrado.
* Directiva:
    * integrar un módulo de audio (como pygame.mixer o similar) en el modelo para reproducir el stream de audio (preview de 30 segundos) obtenido de la API.
    * sincronizar una barra de progreso visual en el Canvas que avance segundo a segundo utilizando el método .after() nativo de tkinter.