# Generador de Sonidos y Visualizador mediante Series de Fourier

Aplicación interactiva desarrollada en Python para la visualización de formas de onda (Senoidal, Cuadrada, Diente de sierra y Triangular) utilizando Series de Fourier, con gráficos dinámicos y síntesis de audio en tiempo real.

## 🛠️ Requisitos e Instalación

Para que este programa funcione correctamente, grafique las señales y pueda reproducir los tonos audibles, es **indispensable** contar con Python y las siguientes librerías externas:

* **`numpy`**: Utilizada para el procesamiento de señales y cálculos matemáticos de las series.
* **`matplotlib`**: Encargada de renderizar y actualizar la interfaz gráfica de la onda en tiempo real.
* **`sounddevice`**: Necesaria para la síntesis, gestión del búfer y reproducción del audio.

### ¿Cómo instalar las dependencias?

Copia o descarga el codigo y abrelo en tu compilador
ejecuta el siguiente comando en tu terminal para instalar todas las librerías necesarias de forma automática:

```bash
pip install numpy matplotlib sounddevice
