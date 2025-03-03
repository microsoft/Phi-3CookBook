# Rekebisha Phi3 kwa kutumia Olive

Katika mfano huu utatumia Olive kufanya:

1. Kuboresha adapta ya LoRA ili kuainisha misemo kuwa Sad, Joy, Fear, Surprise.
2. Kuunganisha uzito wa adapta kwenye modeli ya msingi.
3. Kuboresha na Kubana modeli kuwa `int4`.

Pia tutakuonyesha jinsi ya kutumia modeli iliyorekebishwa kwa kutumia API ya ONNX Runtime (ORT) Generate.

> **⚠️ Kwa Rekebishaji, utahitaji kuwa na GPU inayofaa - kwa mfano, A10, V100, A100.**

## 💾 Sakinisha

Tengeneza mazingira mapya ya Python (kwa mfano, kwa kutumia `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Kisha, sakinisha Olive na utegemezi kwa mchakato wa rekebishaji:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Rekebisha Phi3 kwa kutumia Olive
[Faili ya usanidi ya Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ina *mchakato wa kazi* na *hatua* zifuatazo:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Kwa kiwango cha juu, mchakato huu wa kazi utafanya:

1. Rekebisha Phi3 (kwa hatua 150, unaweza kubadilisha) kwa kutumia data ya [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Unganisha uzito wa adapta ya LoRA kwenye modeli ya msingi. Hii itakupa modeli moja katika umbizo la ONNX.
3. Model Builder itaboresha modeli kwa ONNX runtime *na* kubana modeli kuwa `int4`.

Ili kutekeleza mchakato wa kazi, endesha:

```bash
olive run --config phrase-classification.json
```

Baada ya Olive kukamilisha, modeli yako ya Phi3 iliyorekebishwa na kuboreshwa `int4` itapatikana hapa: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Jumuisha Phi3 iliyorekebishwa kwenye programu yako 

Ili kuendesha programu:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Majibu yanapaswa kuwa uainishaji wa neno moja wa msemo (Sad/Joy/Fear/Surprise).

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kimitambo zinazotumia AI. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au dosari. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.