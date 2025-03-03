# Ajuste fin al lui Phi3 folosind Olive

În acest exemplu vei folosi Olive pentru a:

1. Ajusta fin un adaptor LoRA pentru a clasifica frazele în Sad, Joy, Fear, Surprise.
1. Îmbina greutățile adaptorului în modelul de bază.
1. Optimiza și cuantifica modelul în `int4`.

De asemenea, îți vom arăta cum să faci inferențe cu modelul ajustat fin folosind API-ul Generate din ONNX Runtime (ORT).

> **⚠️ Pentru ajustarea fină, vei avea nevoie de un GPU adecvat - de exemplu, un A10, V100, A100.**

## 💾 Instalare

Creează un nou mediu virtual Python (de exemplu, folosind `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Apoi, instalează Olive și dependențele necesare pentru un flux de lucru de ajustare fină:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustează fin Phi3 folosind Olive

[Fișierul de configurare Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) conține un *flux de lucru* cu următoarele *etape*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

La un nivel general, acest flux de lucru va:

1. Ajusta fin Phi3 (pentru 150 de pași, pe care îi poți modifica) folosind datele din [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Îmbina greutățile adaptorului LoRA în modelul de bază. Acest lucru îți va oferi un singur artefact de model în format ONNX.
1. Model Builder va optimiza modelul pentru runtime-ul ONNX *și* va cuantifica modelul în `int4`.

Pentru a executa fluxul de lucru, rulează:

```bash
olive run --config phrase-classification.json
```

Când Olive a finalizat, modelul tău Phi3 ajustat fin și optimizat în `int4` va fi disponibil în: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrează Phi3 ajustat fin în aplicația ta

Pentru a rula aplicația:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Acest răspuns ar trebui să fie o clasificare într-un singur cuvânt a frazei (Sad/Joy/Fear/Surprise).

**Declinări de responsabilitate**:  
Acest document a fost tradus utilizând servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.