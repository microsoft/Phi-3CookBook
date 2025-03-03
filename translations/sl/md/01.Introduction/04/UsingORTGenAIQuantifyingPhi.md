# **Kvadratizacija družine Phi z uporabo generativnih AI razširitev za onnxruntime**

## **Kaj so generativne AI razširitve za onnxruntime**

Te razširitve vam omogočajo izvajanje generativnega AI z ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Zagotavljajo generativno AI zanko za ONNX modele, vključno z inferenco z ONNX Runtime, obdelavo logitov, iskanjem in vzorčenjem ter upravljanjem KV predpomnilnika. Razvijalci lahko pokličejo visokonivojsko metodo generate() ali pa znotraj zanke izvajajo vsako iteracijo modela, generirajo en token naenkrat in po želji posodabljajo parametre generiranja. Podprti so greedy/beam search ter TopP, TopK vzorčenje za generiranje sekvenc tokenov, prav tako pa tudi vgrajena obdelava logitov, kot so kazni za ponavljanje. Prav tako lahko enostavno dodate lastno ocenjevanje.

Na ravni aplikacij lahko generativne AI razširitve za onnxruntime uporabite za gradnjo aplikacij z uporabo C++/C#/Python. Na ravni modelov jih lahko uporabite za združevanje modelov s finim prilagajanjem in za povezano delo na kvantitativni implementaciji.


## **Kvadratizacija Phi-3.5 z generativnimi AI razširitvami za onnxruntime**

### **Podprti modeli**

Generativne AI razširitve za onnxruntime podpirajo pretvorbo v kvantizirane različice za Microsoft Phi, Google Gemma, Mistral in Meta LLaMA.


### **Graditelj modelov v generativnih AI razširitvah za onnxruntime**

Graditelj modelov močno pospeši ustvarjanje optimiziranih in kvantiziranih ONNX modelov, ki delujejo z ONNX Runtime generate() API.

S pomočjo Graditelja modelov lahko model kvadratizirate na INT4, INT8, FP16, FP32 in združite različne metode pospeševanja strojne opreme, kot so CPU, CUDA, DirectML, Mobile itd.

Za uporabo Graditelja modelov morate namestiti

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po namestitvi lahko zaženete skript Graditelja modelov iz terminala za izvedbo pretvorbe formata modela in kvadratizacije.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Razumevanje ustreznih parametrov

1. **model_name** To je model na Hugging Face, kot so microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itd. Lahko je tudi pot, kjer shranjujete model.

2. **path_to_output_folder** Pot za shranjevanje kvadratiziranih pretvorb.

3. **execution_provider** Podpora za različne metode pospeševanja strojne opreme, kot so cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Model prenesemo iz Hugging Face in ga lokalno predpomnimo.




***Opomba:***


## **Kako uporabljati Graditelja modelov za kvadratizacijo Phi-3.5**

Graditelj modelov zdaj podpira kvadratizacijo ONNX modelov za Phi-3.5 Instruct in Phi-3.5-Vision.

### **Phi-3.5-Instruct**


**CPU pospešena pretvorba v kvadratiziran INT 4**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA pospešena pretvorba v kvadratiziran INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Nastavite okolje v terminalu

```bash

mkdir models

cd models 

```

2. Prenesite microsoft/Phi-3.5-vision-instruct v mapo models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Prenesite te datoteke v svojo mapo Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. Prenesite to datoteko v mapo models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pojdite v terminal

    Pretvorite podporo ONNX z FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **Opomba:**

1. Graditelj modelov trenutno podpira pretvorbo Phi-3.5-Instruct in Phi-3.5-Vision, ne pa Phi-3.5-MoE.

2. Za uporabo kvadratiziranega modela ONNX ga lahko uporabite prek Generativnih AI razširitev za onnxruntime SDK.

3. Potrebno je razmisliti o bolj odgovornem AI, zato je po pretvorbi modela v kvadratizacijo priporočljivo izvesti učinkovitejše testiranje rezultatov.

4. S kvadratizacijo CPU INT4 modela ga lahko implementiramo na Edge Device, kar ponuja boljše aplikacijske scenarije, zato smo zaključili Phi-3.5-Instruct okoli INT 4.


## **Viri**

1. Več o generativnih AI razširitvah za onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GitHub repozitorij za generativne AI razširitve za onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Zavrnitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.