# Kutumia Windows GPU kuunda suluhisho la Prompt flow na Phi-3.5-Instruct ONNX 

Hati ifuatayo ni mfano wa jinsi ya kutumia PromptFlow na ONNX (Open Neural Network Exchange) kwa ajili ya kuunda programu za AI zinazotegemea modeli za Phi-3.

PromptFlow ni seti ya zana za maendeleo iliyoundwa kurahisisha mzunguko mzima wa maendeleo ya programu za AI zinazotegemea LLM (Large Language Model), kuanzia mawazo na utengenezaji wa prototaipu hadi majaribio na tathmini.

Kwa kuunganisha PromptFlow na ONNX, watengenezaji wanaweza:

- **Kuboresha Utendaji wa Modeli:** Tumia ONNX kwa ufanisi wa maelekezo ya modeli na utekelezaji.
- **Kurahisisha Maendeleo:** Tumia PromptFlow kusimamia mtiririko wa kazi na kuendesha kazi zinazojirudia.
- **Kuboresha Ushirikiano:** Rahisisha ushirikiano kati ya wanachama wa timu kwa kutoa mazingira ya maendeleo yaliyounganishwa.

**Prompt flow** ni seti ya zana za maendeleo iliyoundwa kurahisisha mzunguko mzima wa maendeleo ya programu za AI zinazotegemea LLM, kuanzia mawazo, utengenezaji wa prototaipu, majaribio, tathmini hadi utekelezaji wa uzalishaji na ufuatiliaji. Inafanya uhandisi wa maelekezo kuwa rahisi zaidi na inakuwezesha kujenga programu za LLM zenye ubora wa uzalishaji.

Prompt flow inaweza kuunganishwa na OpenAI, Azure OpenAI Service, na modeli zinazoweza kubadilishwa (Huggingface, LLM/SLM za ndani). Tunatarajia kutekeleza modeli ya Phi-3.5 iliyokokotolewa (quantized) ya ONNX kwenye programu za ndani. Prompt flow inaweza kutusaidia kupanga biashara yetu vyema na kukamilisha suluhisho za ndani zinazotegemea Phi-3.5. Katika mfano huu, tutaunganisha Maktaba ya ONNX Runtime GenAI kukamilisha suluhisho la Prompt flow linalotegemea Windows GPU.

## **Usakinishaji**

### **ONNX Runtime GenAI kwa Windows GPU**

Soma mwongozo huu wa kusakinisha ONNX Runtime GenAI kwa Windows GPU [bonyeza hapa](./ORTWindowGPUGuideline.md)

### **Sanidi Prompt flow kwenye VSCode**

1. Sakinisha Kiendelezi cha Prompt flow cha VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.sw.png)

2. Baada ya kusakinisha Kiendelezi cha Prompt flow cha VS Code, bofya kiendelezi hicho, na uchague **Installation dependencies** kisha fuata mwongozo huu kusakinisha Prompt flow SDK kwenye mazingira yako

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.sw.png)

3. Pakua [Msimbo wa Mfano](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) na tumia VS Code kufungua mfano huu

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.sw.png)

4. Fungua **flow.dag.yaml** kuchagua mazingira yako ya Python

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.sw.png)

   Fungua **chat_phi3_ort.py** kubadilisha eneo la modeli yako ya Phi-3.5-instruct ONNX

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.sw.png)

5. Endesha Prompt flow yako kwa majaribio

Fungua **flow.dag.yaml** kisha bofya mhariri wa kuona (visual editor)

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.sw.png)

Baada ya kubofya hapo, endesha ili kujaribu

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.sw.png)

1. Unaweza kuendesha kundi (batch) kwenye terminal ili kuona matokeo zaidi

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Unaweza kuangalia matokeo kwenye kivinjari chako chaguo-msingi

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.sw.png)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za mtafsiri wa kibinadamu mtaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.