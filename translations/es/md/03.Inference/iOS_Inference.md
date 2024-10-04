# **Inferencia Phi-3 en iOS**

Phi-3-mini es una nueva serie de modelos de Microsoft que permite el despliegue de Modelos de Lenguaje Grande (LLMs) en dispositivos edge y dispositivos IoT. Phi-3-mini está disponible para despliegues en iOS, Android y dispositivos Edge, permitiendo que la IA generativa se despliegue en entornos BYOD. El siguiente ejemplo demuestra cómo desplegar Phi-3-mini en iOS.

## **1. Preparación**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 o superior)
- **d.** Instalar Python 3.10+ (se recomienda Conda)
- **e.** Instalar la biblioteca de Python: `python-flatbuffers`
- **f.** Instalar CMake

### Kernel Semántico e Inferencia

Kernel Semántico es un marco de aplicaciones que te permite crear aplicaciones compatibles con Azure OpenAI Service, modelos de OpenAI e incluso modelos locales. Acceder a servicios locales a través del Kernel Semántico permite una fácil integración con tu servidor de modelos Phi-3-mini autoalojado.

### Llamando a Modelos Cuantizados con Ollama o LlamaEdge

Muchos usuarios prefieren usar modelos cuantizados para ejecutar modelos localmente. [Ollama](https://ollama.com) y [LlamaEdge](https://llamaedge.com) permiten a los usuarios llamar a diferentes modelos cuantizados:

#### **Ollama**

Puedes ejecutar `ollama run phi3` directamente o configurarlo offline. Crea un archivo de modelo con la ruta a tu archivo `gguf`. Código de ejemplo para ejecutar el modelo cuantizado Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Si deseas usar `gguf` tanto en la nube como en dispositivos edge simultáneamente, LlamaEdge es una gran opción.

## **2. Compilando ONNX Runtime para iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Aviso**

- **a.** Antes de compilar, asegúrate de que Xcode esté configurado correctamente y configúralo como el directorio de desarrollador activo en la terminal:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime necesita ser compilado para diferentes plataformas. Para iOS, puedes compilar para `arm64` or `x86_64`.

- **c.** Se recomienda usar el último SDK de iOS para la compilación. Sin embargo, también puedes usar una versión anterior si necesitas compatibilidad con SDKs previos.

## **3. Compilando IA Generativa con ONNX Runtime para iOS**

> **Nota:** Dado que la IA Generativa con ONNX Runtime está en vista previa, ten en cuenta los posibles cambios.

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. Crear una aplicación en Xcode**

Elegí Objective-C como el método de desarrollo de la App, porque usando IA Generativa con la API de C++ de ONNX Runtime, Objective-C es mejor compatible. Por supuesto, también puedes completar las llamadas relacionadas a través de Swift bridging.

![xcode](../../../../translated_images/xcode.2817f1d089dc7d09ba6a41361db7052567d63f714062e2e4325b0e0895ccb4c4.es.png)

## **5. Copiar el modelo INT4 cuantizado de ONNX al proyecto de la aplicación**

Necesitamos importar el modelo de cuantización INT4 en formato ONNX, el cual debe descargarse primero.

![hf](../../../../translated_images/hf.dd843c3e95f3b462a3d5f06dbbb17c1f1a33b87688c1cda4d990084ef71a4eed.es.png)

Después de descargarlo, necesitas agregarlo al directorio de Recursos del proyecto en Xcode.

![model](../../../../translated_images/model.2b8e95a590e70374b2294b16f8ae18c9110239a550e64dc034d6bc16d37e0106.es.png)

## **6. Agregar la API de C++ en ViewControllers**

> **Aviso:**

- **a.** Agrega los archivos de cabecera C++ correspondientes al proyecto.

  ![Header File](../../../../translated_images/head.7eeb79e1de8f375590e7a5c54fcc8278d265fee3135ebce9c8e241e08d823f7c.es.png)

- **b.** Incluye `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../translated_images/lib.9388329df08543518d094d14c8ca0c8e6f0ce264ee68630a8c5c3d783355b6d1.es.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` para habilitar el soporte de Objective-C++.

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. Ejecutando la Aplicación**

Una vez que la configuración esté completa, puedes ejecutar la aplicación para ver los resultados de la inferencia del modelo Phi-3-mini.

![Running Result](../../../../translated_images/result.a2debbd16a6697a8cbd23dadff703358ea87eee7d68f0643b83707a578ca73e8.es.jpg)

Para más código de ejemplo e instrucciones detalladas, visita el [repositorio de Ejemplos de Phi-3 Mini](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

        **Descargo de responsabilidad**:
        Este documento ha sido traducido utilizando servicios de traducción automatizada por IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.