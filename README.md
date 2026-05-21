# ED1 - Proyecto: Calculadora y Ordenador de Fracciones (MVC)

Este proyecto es una aplicación de escritorio interactiva desarrollada en **Python** utilizando **Tkinter** para la interfaz gráfica de usuario (GUI). Su objetivo principal es resolver operaciones con números racionales y gestionar colecciones de fracciones, sirviendo como un proyecto práctico para la materia de Estructuras de Datos I (ED1).

El diseño de software se ha realizado siguiendo rigurosamente el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**, asegurando un código modular, mantenible y con una clara separación de responsabilidades.

---

## 🚀 Características Clave

La aplicación se divide en dos secciones principales mediante un sistema de pestañas:

1. **Calculadora de Fracciones:**
   * Permite realizar operaciones aritméticas estándar: suma (`+`), resta (`-`), multiplicación (`*`) y división (`/`).
   * Convierte automáticamente las entradas de texto (como `1/2` o enteros como `3`) a objetos racionales.
   * Cuenta con **simplificación automática** a su forma irreducible utilizando el Máximo Común Divisor (MCD).

2. **Comparador y Ordenador de Listas:**
   * Permite ingresar una lista de fracciones separadas por comas (ej. `1/2, 3/4, 1/4`).
   * Ordena los elementos de forma **Ascendente** o **Descendente** basándose en la lógica interna de comparación.
   * Muestra de forma inteligente una pista de comparación entre las dos primeras fracciones de la lista (`=`, `<`, `>`).

3. **Robustez Matemático-Lógica:**
   * Validación integrada para evitar denominadores en cero mediante excepciones personalizadas (`FractionError`).
   * Normalización automática de signos (ej. `1/-2` se transforma y procesa correctamente como `-1/2`).

---

## 📁 Estructura del Código

El repositorio respeta la distribución modular clásica de una arquitectura de capas:

* 📂 **`models/` (Modelo):** Contiene `fraction_model.py`. Define la lógica de negocio a través de las clases `Rational` y `FractionModel`, administrando el estado, el parseo de texto y las operaciones matemáticas puras.
* 📂 **`views/` (Vista):** Contiene `main_view.py`. Construye la ventana principal (`MainView`), configura los estilos visuales avanzados de los elementos (`ttk`) y expone los métodos para actualizar la pantalla y los mensajes de error.
* 📂 **`controllers/` (Controlador):** Contiene `fraction_controller.py`. Une ambas capas mediante la clase `FractionController`, capturando las acciones del usuario en la vista, llamando a los cálculos del modelo y enviando las respuestas de vuelta a la pantalla.
* 📄 **`app.py`:** El punto de inicio de la aplicación. Instancia el modelo, la vista, conecta el controlador e inicia el ciclo de vida del programa mediante `view.mainloop()`.

---

## 🛠️ Instalación y Ejecución

Al estar construido sobre la biblioteca estándar de Python, el proyecto **no requiere la instalación de dependencias externas** con `pip`.

### Instrucciones de ejecución:

1. **Clona este repositorio en tu computadora:**
   ```bash
   git clone [https://github.com/edwinelioflores699-pixel/ED1-PROYECTO-1.-calculadora-de-fracciones-.git](https://github.com/edwinelioflores699-pixel/ED1-PROYECTO-1.-calculadora-de-fracciones-.git)
