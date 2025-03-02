# Fine-tune Phi3 folosind Olive

În acest exemplu vei folosi Olive pentru a:

1. Ajusta un adaptor LoRA pentru a clasifica fraze în categoriile Tristețe, Bucurie, Frică, Surpriză.
1. Fuziona greutățile adaptorului cu modelul de bază.
1. Optimiza și cuantiza modelul în `int4`.

De asemenea, îți vom arăta cum să faci inferențe cu modelul ajustat folosind API-ul Generate al ONNX Runtime (ORT).

> **⚠️ Pentru ajustare, vei avea nevoie de un GPU potrivit - de exemplu, un A10, V100, A100.**

## 💾 Instalare

Creează un nou mediu virtual Python (de exemplu, folosind `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Apoi, instalează Olive și dependențele necesare pentru fluxul de lucru de ajustare:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustează Phi3 folosind Olive
Fișierul de configurare [Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) conține un *flux de lucru* cu următoarele *etape*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

La un nivel înalt, acest flux de lucru va:

1. Ajusta Phi3 (pentru 150 de pași, pe care îi poți modifica) folosind datele din [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fuziona greutățile adaptorului LoRA cu modelul de bază. Acest lucru va genera un singur artefact de model în format ONNX.
1. Model Builder va optimiza modelul pentru ONNX Runtime *și* va cuantiza modelul în `int4`.

Pentru a executa fluxul de lucru, rulează:

```bash
olive run --config phrase-classification.json
```

Când Olive finalizează, modelul tău Phi3 ajustat și optimizat `int4` va fi disponibil în: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrează Phi3 ajustat în aplicația ta 

Pentru a rula aplicația:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Răspunsul ar trebui să fie o clasificare într-un singur cuvânt a frazei (Tristețe/Bucurie/Frică/Surpriză).

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.