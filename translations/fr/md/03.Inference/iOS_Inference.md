# **Inference Phi-3 sur iOS**

Phi-3-mini est une nouvelle série de modèles de Microsoft qui permet le déploiement de modèles de langage de grande taille (LLM) sur des appareils périphériques et des dispositifs IoT. Phi-3-mini est disponible pour les déploiements sur iOS, Android et appareils Edge, permettant ainsi le déploiement de l'IA générative dans des environnements BYOD. L'exemple suivant montre comment déployer Phi-3-mini sur iOS.

## **1. Préparation**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ou supérieur)
- **d.** Installer Python 3.10+ (Conda est recommandé)
- **e.** Installer la bibliothèque Python : `python-flatbuffers`
- **f.** Installer CMake

### Semantic Kernel et Inference

Semantic Kernel est un framework d'application qui vous permet de créer des applications compatibles avec Azure OpenAI Service, les modèles OpenAI, et même les modèles locaux. Accéder aux services locaux via Semantic Kernel permet une intégration facile avec votre serveur de modèle Phi-3-mini auto-hébergé.

### Appeler des modèles quantifiés avec Ollama ou LlamaEdge

De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour exécuter des modèles localement. [Ollama](https://ollama.com) et [LlamaEdge](https://llamaedge.com) permettent aux utilisateurs d'appeler différents modèles quantifiés :

#### **Ollama**

Vous pouvez exécuter `ollama run phi3` directement ou le configurer hors ligne. Créez un Modelfile avec le chemin vers votre fichier `gguf`. Exemple de code pour exécuter le modèle quantifié Phi-3-mini :

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Si vous souhaitez utiliser `gguf` à la fois sur des appareils cloud et edge simultanément, LlamaEdge est une excellente option.

## **2. Compiler ONNX Runtime pour iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Remarque**

- **a.** Avant de compiler, assurez-vous que Xcode est correctement configuré et définissez-le comme répertoire développeur actif dans le terminal :

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime doit être compilé pour différentes plateformes. Pour iOS, vous pouvez compiler pour `arm64` or `x86_64`.

- **c.** Il est recommandé d'utiliser le dernier SDK iOS pour la compilation. Cependant, vous pouvez également utiliser une version plus ancienne si vous avez besoin de compatibilité avec des SDK précédents.

## **3. Compiler l'IA générative avec ONNX Runtime pour iOS**

> **Note :** Étant donné que l'IA générative avec ONNX Runtime est en aperçu, veuillez être conscient des changements potentiels.

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

## **4. Créer une application App dans Xcode**

J'ai choisi Objective-C comme méthode de développement de l'application, car en utilisant l'IA générative avec l'API C++ d'ONNX Runtime, Objective-C est mieux compatible. Bien sûr, vous pouvez également effectuer des appels connexes via le pont Swift.

![xcode](../../../../translated_images/xcode.2817f1d089dc7d09ba6a41361db7052567d63f714062e2e4325b0e0895ccb4c4.fr.png)

## **5. Copier le modèle quantifié INT4 ONNX dans le projet d'application App**

Nous devons importer le modèle de quantification INT4 au format ONNX, qu'il faut d'abord télécharger

![hf](../../../../translated_images/hf.dd843c3e95f3b462a3d5f06dbbb17c1f1a33b87688c1cda4d990084ef71a4eed.fr.png)

Après le téléchargement, vous devez l'ajouter au répertoire Resources du projet dans Xcode.

![model](../../../../translated_images/model.2b8e95a590e70374b2294b16f8ae18c9110239a550e64dc034d6bc16d37e0106.fr.png)

## **6. Ajouter l'API C++ dans les ViewControllers**

> **Remarque :**

- **a.** Ajouter les fichiers d'en-tête C++ correspondants au projet.

  ![Header File](../../../../translated_images/head.7eeb79e1de8f375590e7a5c54fcc8278d265fee3135ebce9c8e241e08d823f7c.fr.png)

- **b.** Inclure `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../translated_images/lib.9388329df08543518d094d14c8ca0c8e6f0ce264ee68630a8c5c3d783355b6d1.fr.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` pour activer la prise en charge d'Objective-C++.

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

## **7. Exécuter l'application**

Une fois la configuration terminée, vous pouvez exécuter l'application pour voir les résultats de l'inférence du modèle Phi-3-mini.

![Running Result](../../../../translated_images/result.a2debbd16a6697a8cbd23dadff703358ea87eee7d68f0643b83707a578ca73e8.fr.jpg)

Pour plus d'exemples de code et d'instructions détaillées, visitez le [référentiel Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.