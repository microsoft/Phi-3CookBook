# **Pokyny pre OnnxRuntime GenAI Windows GPU**

Tento návod poskytuje kroky na nastavenie a používanie ONNX Runtime (ORT) s GPU na Windows. Je navrhnutý tak, aby vám pomohol využiť akceleráciu GPU pre vaše modely, čím zlepšíte výkon a efektivitu.

Dokument obsahuje pokyny na:

- Nastavenie prostredia: Inštrukcie na inštaláciu potrebných závislostí ako CUDA, cuDNN a ONNX Runtime.
- Konfiguráciu: Ako nakonfigurovať prostredie a ONNX Runtime na efektívne využitie GPU zdrojov.
- Tipy na optimalizáciu: Rady, ako doladiť nastavenia GPU pre optimálny výkon.

### **1. Python 3.10.x /3.11.8**

   ***Poznámka*** Odporúčame použiť [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) ako vaše Python prostredie.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Pripomienka*** Ak ste už nainštalovali akúkoľvek ONNX knižnicu pre Python, odinštalujte ju.

### **2. Inštalácia CMake pomocou winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Inštalácia Visual Studio 2022 - Desktop Development with C++**

   ***Poznámka*** Ak nechcete kompilovať, môžete tento krok preskočiť.

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.sk.png)

### **4. Inštalácia NVIDIA ovládača**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Pripomienka*** Použite predvolené nastavenia počas inštalačného procesu.

### **5. Nastavenie NVIDIA prostredia**

Skopírujte súbory z NVIDIA CUDNN 9.4 lib, bin, include do NVIDIA CUDA 12.4 lib, bin, include.

- skopírujte súbory z *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* do *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- skopírujte súbory z *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* do *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- skopírujte súbory z *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* do *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Stiahnutie Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Spustenie InferencePhi35Instruct.ipynb**

   Otvorte [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) a spustite ho.

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.sk.png)

### **8. Kompilácia ORT GenAI GPU**

   ***Poznámka*** 
   
   1. Najprv odinštalujte všetko, čo súvisí s onnx, onnxruntime a onnxruntime-genai.

   ```bash

   pip list 
   
   ```

   Potom odinštalujte všetky ONNX Runtime knižnice, napr.:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Skontrolujte podporu rozšírení Visual Studio.

   Skontrolujte priečinok C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras, či obsahuje priečinok C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration. 
   
   Ak ho nenájdete, skontrolujte iné priečinky ovládačov CUDA toolkit a skopírujte priečinok visual_studio_integration a jeho obsah do C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration.

   - Ak nechcete kompilovať, môžete tento krok preskočiť.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Stiahnite [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Rozbaľte onnxruntime-win-x64-gpu-1.19.2.zip a premenujte ho na **ort**, skopírujte priečinok ort do onnxruntime-genai.

   - Použite Windows Terminal, otvorte Developer Command Prompt pre VS 2022 a prejdite do priečinka onnxruntime-genai.

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.sk.png)

   - Kompilujte s vaším Python prostredím.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.