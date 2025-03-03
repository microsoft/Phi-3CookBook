# **Inferenca Phi-3 na iOS-u**

Phi-3-mini je nova serija modelov podjetja Microsoft, ki omogoča uvajanje velikih jezikovnih modelov (LLM) na robnih napravah in napravah IoT. Phi-3-mini je na voljo za iOS, Android in uvajanje na robne naprave, kar omogoča uporabo generativne umetne inteligence v okolju BYOD. Naslednji primer prikazuje, kako uvajati Phi-3-mini na iOS-u.

## **1. Priprava**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ali novejši)
- **d.** Namestite Python 3.10+ (priporočeno je Conda)
- **e.** Namestite Python knjižnico: `python-flatbuffers`
- **f.** Namestite CMake

### Semantic Kernel in Inferenca

Semantic Kernel je aplikacijski okvir, ki omogoča ustvarjanje aplikacij, združljivih z Azure OpenAI Service, OpenAI modeli in celo lokalnimi modeli. Dostop do lokalnih storitev prek Semantic Kernel omogoča enostavno integracijo z vašim lokalno gostovanim Phi-3-mini modelnim strežnikom.

### Klicanje kvantiziranih modelov z Ollama ali LlamaEdge

Veliko uporabnikov raje uporablja kvantizirane modele za lokalno izvajanje. [Ollama](https://ollama.com) in [LlamaEdge](https://llamaedge.com) omogočata klicanje različnih kvantiziranih modelov:

#### **Ollama**

Lahko zaženete `ollama run phi3` neposredno ali pa ga konfigurirate brez povezave. Ustvarite Modelfile s potjo do vaše datoteke `gguf`. Primer kode za zagon kvantiziranega modela Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Če želite uporabiti `gguf` tako v oblaku kot na robnih napravah hkrati, je LlamaEdge odlična izbira.

## **2. Kompilacija ONNX Runtime za iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Obvestilo**

- **a.** Pred kompilacijo preverite, da je Xcode pravilno konfiguriran in nastavljen kot aktivni razvijalski imenik v terminalu:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime je treba skompilirati za različne platforme. Za iOS lahko kompilirate za `arm64` or `x86_64`.

- **c.** Priporočljivo je uporabiti najnovejši iOS SDK za kompilacijo. Vendar pa lahko uporabite tudi starejšo različico, če potrebujete združljivost s prejšnjimi SDK-ji.

## **3. Kompilacija generativne umetne inteligence z ONNX Runtime za iOS**

> **Opomba:** Ker je generativna umetna inteligenca z ONNX Runtime še v predogledu, bodite pozorni na morebitne spremembe.

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

## **4. Ustvarjanje aplikacije v Xcode**

Izbral sem Objective-C kot način razvoja aplikacije, saj je pri uporabi generativne umetne inteligence z ONNX Runtime C++ API Objective-C bolje združljiv. Seveda lahko ustrezne klice izvedete tudi prek Swift bridginga.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.sl.png)

## **5. Kopiranje ONNX kvantiziranega INT4 modela v projekt aplikacije**

Uvoziti moramo INT4 kvantiziran model v ONNX formatu, ki ga je treba najprej prenesti.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.sl.png)

Po prenosu ga morate dodati v imenik Resources projekta v Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.sl.png)

## **6. Dodajanje C++ API-ja v ViewControllers**

> **Obvestilo:**

- **a.** Dodajte ustrezne C++ glavične datoteke v projekt.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.sl.png)

- **b.** Vključite `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.sl.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm`, da omogočite podporo za Objective-C++.

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

## **7. Zagon aplikacije**

Ko je nastavitev zaključena, lahko zaženete aplikacijo in si ogledate rezultate inferenčnega modela Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.sl.jpg)

Za več vzorčnih kod in podrobna navodila obiščite [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo strojnih storitev za prevajanje z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.