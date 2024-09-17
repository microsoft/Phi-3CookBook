Esta demostración muestra cómo usar un modelo preentrenado para generar código Python basado en una imagen y una indicación de texto.

[Código de Ejemplo](../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aquí tienes una explicación paso a paso:

1. **Importaciones y Configuración**:
   - Se importan las bibliotecas y módulos necesarios, incluyendo `requests`, `PIL` para el procesamiento de imágenes, y `transformers` para manejar el modelo y el procesamiento.

2. **Cargar y Mostrar la Imagen**:
   - Se abre un archivo de imagen (`demo.png`) usando la biblioteca `PIL` y se muestra.

3. **Definir la Indicación**:
   - Se crea un mensaje que incluye la imagen y una solicitud para generar código Python que procese la imagen y la guarde usando `plt` (matplotlib).

4. **Cargar el Procesador**:
   - Se carga el `AutoProcessor` desde un modelo preentrenado especificado por el directorio `out_dir`. Este procesador manejará las entradas de texto e imagen.

5. **Crear la Indicación**:
   - Se utiliza el método `apply_chat_template` para formatear el mensaje en una indicación adecuada para el modelo.

6. **Procesar las Entradas**:
   - La indicación y la imagen se procesan en tensores que el modelo puede entender.

7. **Establecer Argumentos de Generación**:
   - Se definen argumentos para el proceso de generación del modelo, incluyendo el número máximo de nuevos tokens a generar y si se debe muestrear la salida.

8. **Generar el Código**:
   - El modelo genera el código Python basado en las entradas y los argumentos de generación. Se utiliza el `TextStreamer` para manejar la salida, omitiendo la indicación y los tokens especiales.

9. **Salida**:
   - Se imprime el código generado, que debería incluir código Python para procesar la imagen y guardarla según lo especificado en la indicación.

Esta demostración ilustra cómo aprovechar un modelo preentrenado usando OpenVino para generar código dinámicamente basado en la entrada del usuario e imágenes.

Aviso legal: La traducción fue realizada a partir de su original por un modelo de inteligencia artificial y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.