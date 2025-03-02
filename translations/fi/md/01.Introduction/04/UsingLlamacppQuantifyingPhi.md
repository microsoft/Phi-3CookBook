# **Phi-perheen kvantisointi käyttäen llama.cpp:ta**

## **Mikä on llama.cpp**

llama.cpp on avoimen lähdekoodin ohjelmistokirjasto, joka on pääasiassa kirjoitettu C++:lla ja suorittaa päättelyä erilaisilla suurilla kielimalleilla (LLM), kuten Llama. Sen päätavoite on tarjota huipputason suorituskykyä LLM-päättelyssä laajalla laitevalikoimalla ja minimaalisella asennuksella. Lisäksi kirjastolle on saatavilla Python-sidoksia, jotka tarjoavat korkean tason API:n tekstin täydentämiseen ja OpenAI-yhteensopivan verkkopalvelimen.

llama.cpp:n päätavoite on mahdollistaa LLM-päättely minimaalisella asennuksella ja huipputason suorituskyvyllä monenlaisilla laitteilla - paikallisesti ja pilvessä.

- Yksinkertainen C/C++-toteutus ilman riippuvuuksia
- Apple Silicon on ensiluokkainen kohde - optimoitu ARM NEON-, Accelerate- ja Metal-kehysten avulla
- AVX-, AVX2- ja AVX512-tuki x86-arkkitehtuureille
- 1,5-bittinen, 2-bittinen, 3-bittinen, 4-bittinen, 5-bittinen, 6-bittinen ja 8-bittinen kokonaislukukvantisointi nopeampaan päättelyyn ja pienempään muistinkäyttöön
- Mukautetut CUDA-ytimet LLM:ien suorittamiseen NVIDIA:n GPU:illa (tuki AMD:n GPU:ille HIP:n kautta)
- Vulkan- ja SYCL-taustajärjestelmien tuki
- CPU+GPU-hybridi-päättely nopeuttamaan osittain malleja, jotka ovat suurempia kuin kokonais-VRAM-kapasiteetti

## **Phi-3.5:n kvantisointi llama.cpp:lla**

Phi-3.5-Instruct-malli voidaan kvantisoida käyttämällä llama.cpp:ta, mutta Phi-3.5-Vision ja Phi-3.5-MoE eivät ole vielä tuettuja. llama.cpp:n muuntama formaatti on gguf, joka on myös laajimmin käytetty kvantisointiformaatti.

Hugging Facessa on suuri määrä kvantisoituja GGUF-formaatin malleja. AI Foundry, Ollama ja LlamaEdge käyttävät llama.cpp:ta, joten GGUF-malleja käytetään myös usein.

### **Mikä on GGUF**

GGUF on binääriformaatti, joka on optimoitu mallien nopeaan lataamiseen ja tallentamiseen, tehden siitä erittäin tehokkaan päättelytarkoituksiin. GGUF on suunniteltu käytettäväksi GGML:n ja muiden suorittimien kanssa. GGUF:n kehitti @ggerganov, joka on myös llama.cpp:n, suositun C/C++-LLM-päättelykehysten, kehittäjä. Alun perin esimerkiksi PyTorchilla kehitetyt mallit voidaan muuntaa GGUF-formaattiin käytettäväksi näiden moottorien kanssa.

### **ONNX vs GGUF**

ONNX on perinteinen koneoppimisen/syvän oppimisen formaatti, jota tuetaan hyvin eri AI-kehyksissä ja jolla on hyviä käyttötilanteita reunalaitteissa. GGUF puolestaan perustuu llama.cpp:hen ja voidaan sanoa olevan GenAI-aikakauden tuote. Molemmilla on samankaltaisia käyttötarkoituksia. Jos haluat paremman suorituskyvyn sulautetussa laitteistossa ja sovelluskerroksessa, ONNX voi olla valintasi. Jos käytät llama.cpp:n johdannaiskehystä ja -teknologiaa, GGUF voi olla parempi.

### **Phi-3.5-Instructin kvantisointi llama.cpp:lla**

**1. Ympäristön konfigurointi**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisointi**

Phi-3.5-Instructin muuntaminen FP16 GGUF:ksi käyttäen llama.cpp:ta


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5:n kvantisointi INT4:ksi


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testaus**

Asenna llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Huom*** 

Jos käytät Apple Siliconia, asenna llama-cpp-python näin


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testaus 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurssit**

1. Lisätietoja llama.cpp:sta [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Lisätietoja GGUF:sta [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluita käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.