Esta demo muestra cómo utilizar un modelo preentrenado para generar código Python basado en una imagen y un mensaje de texto.

[Código de Ejemplo](../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aquí tienes una explicación paso a paso:

1. **Importaciones y Configuración**:
   - Se importan las bibliotecas y módulos necesarios, incluyendo `requests`, `PIL` para el procesamiento de imágenes, y `transformers` para manejar el modelo y el procesamiento.

2. **Cargando y Mostrando la Imagen**:
   - Se abre un archivo de imagen (`demo.png`) utilizando la biblioteca `PIL` y se muestra.

3. **Definiendo el Prompt**:
   - Se crea un mensaje que incluye la imagen y una solicitud para generar código Python para procesar la imagen y guardarla utilizando `plt` (matplotlib).

4. **Cargando el Procesador**:
   - Se carga el `AutoProcessor` desde un modelo preentrenado especificado por el directorio `out_dir`. Este procesador manejará las entradas de texto e imagen.

5. **Creando el Prompt**:
   - Se utiliza el método `apply_chat_template` para formatear el mensaje en un prompt adecuado para el modelo.

6. **Procesando las Entradas**:
   - El prompt y la imagen se procesan en tensores que el modelo puede entender.

7. **Configurando Argumentos de Generación**:
   - Se definen los argumentos para el proceso de generación del modelo, incluyendo el número máximo de nuevos tokens a generar y si se debe muestrear la salida.

8. **Generando el Código**:
   - El modelo genera el código Python basado en las entradas y los argumentos de generación. Se utiliza el `TextStreamer` para manejar la salida, omitiendo el prompt y los tokens especiales.

9. **Salida**:
   - Se imprime el código generado, que debería incluir código Python para procesar la imagen y guardarla según lo especificado en el prompt.

Esta demo ilustra cómo aprovechar un modelo preentrenado utilizando OpenVino para generar código dinámicamente basado en la entrada del usuario y las imágenes.

