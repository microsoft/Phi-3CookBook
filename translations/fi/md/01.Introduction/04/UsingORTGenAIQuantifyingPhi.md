# **Phi-perheen kvantisointi Generative AI -laajennusten avulla onnxruntimelle**

## **Mitä ovat Generative AI -laajennukset onnxruntimelle**

Nämä laajennukset auttavat sinua käyttämään generatiivista tekoälyä ONNX Runtimen kanssa ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Ne tarjoavat generatiivisen tekoälyn silmukan ONNX-malleille, mukaan lukien päättely ONNX Runtimella, logiikkien käsittely, haku ja näytteenotto sekä KV-välimuistin hallinta. Kehittäjät voivat kutsua korkean tason generate()-metodia tai suorittaa mallin jokaisen iteraation silmukassa, luoden yhden tokenin kerrallaan ja tarvittaessa päivittää generointiparametreja silmukan sisällä. Laajennukset tukevat ahnetta/keilaushakua sekä TopP- ja TopK-näytteenottoa token-sekvenssien luomiseksi ja sisältävät sisäänrakennetun logiikkien käsittelyn, kuten toistopenaltiot. Voit myös helposti lisätä mukautettuja pisteytyksiä.

Sovellustasolla voit käyttää Generative AI -laajennuksia onnxruntimelle rakentaaksesi sovelluksia C++-, C#- tai Python-kielillä. Mallitasolla voit käyttää niitä yhdistääksesi hienosäädettyjä malleja ja tehdäksesi niihin liittyvää kvantitatiivista käyttöönottoa.

## **Phi-3.5:n kvantisointi Generative AI -laajennusten avulla onnxruntimelle**

### **Tuetut mallit**

Generative AI -laajennukset onnxruntimelle tukevat Microsoft Phi-, Google Gemma-, Mistral- ja Meta LLaMA-mallien kvantisointimuunnoksia.

### **Model Builder Generative AI -laajennuksissa onnxruntimelle**

Model Builder nopeuttaa huomattavasti optimoitujen ja kvantisoitujen ONNX-mallien luomista, jotka toimivat ONNX Runtimen generate()-API:n kanssa.

Model Builderin avulla voit kvantisoida mallin INT4-, INT8-, FP16- ja FP32-muotoihin sekä yhdistää erilaisia laitteistokiihdytystapoja, kuten CPU, CUDA, DirectML, Mobile jne.

Käyttääksesi Model Builderia sinun täytyy asentaa

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Asennuksen jälkeen voit suorittaa Model Builder -skriptin terminaalista mallin muoto- ja kvantisointimuunnoksia varten.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Ymmärrä tärkeät parametrit:

1. **model_name** Tämä on Hugging Face -malli, kuten microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct jne. Se voi myös olla polku, johon olet tallentanut mallin.

2. **path_to_output_folder** Kvantisoidun muunnoksen tallennuspolku.

3. **execution_provider** Eri laitteistokiihdytystuki, kuten CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Malli ladataan Hugging Facesta ja välimuistitetaan paikallisesti.

***Huomaa:***

## **Kuinka käyttää Model Builderia Phi-3.5:n kvantisointiin**

Model Builder tukee nyt Phi-3.5 Instruct- ja Phi-3.5-Vision-mallien ONNX-kvantisointia.

### **Phi-3.5-Instruct**

**CPU-kiihdytetty INT4-kvantisointi**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA-kiihdytetty INT4-kvantisointi**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Aseta ympäristö terminaalissa

```bash

mkdir models

cd models 

```

2. Lataa microsoft/Phi-3.5-vision-instruct models-kansioon  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Lataa seuraavat tiedostot Phi-3.5-vision-instruct-kansioosi:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Lataa tämä tiedosto models-kansioon:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Avaa terminaali.

   Muunna ONNX-tuki FP32:lla.

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Huomaa:**

1. Model Builder tukee tällä hetkellä Phi-3.5-Instruct- ja Phi-3.5-Vision-mallien muunnoksia, mutta ei Phi-3.5-MoE-mallia.

2. Käyttääksesi ONNX:n kvantisoitua mallia voit käyttää sitä Generative AI -laajennusten onnxruntime-SDK:n kautta.

3. Meidän täytyy huomioida vastuullinen tekoäly, joten mallin kvantisointimuunnoksen jälkeen on suositeltavaa suorittaa tehokkaampia tulostestejä.

4. Kvantisoimalla CPU INT4 -malli voimme ottaa sen käyttöön Edge-laitteilla, joissa sillä on parempia sovellusskenaarioita. Siksi olemme viimeistelleet Phi-3.5-Instruct-mallin INT4-muodossa.

## **Resurssit**

1. Lue lisää Generative AI -laajennuksista onnxruntimelle: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI -laajennusten onnxruntime GitHub-repositorio: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeää tietoa varten suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkintavirheistä.