# Dostosowanie Phi3 za pomocą Olive

W tym przykładzie użyjesz Olive, aby:

1. Dostosować adapter LoRA do klasyfikowania fraz jako Smutek, Radość, Strach, Zaskoczenie.
1. Połączyć wagi adaptera z modelem bazowym.
1. Optymalizować i kwantyzować model do `int4`.

Pokażemy również, jak wykonać wnioskowanie na dostosowanym modelu przy użyciu API Generate w ONNX Runtime (ORT).

> **⚠️ Do dostosowywania potrzebujesz odpowiedniego GPU, na przykład A10, V100, A100.**

## 💾 Instalacja

Utwórz nową wirtualną przestrzeń Python (na przykład przy użyciu `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Następnie zainstaluj Olive i zależności wymagane do przepływu pracy związanego z dostosowywaniem:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Dostosowanie Phi3 za pomocą Olive
[Plik konfiguracyjny Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) zawiera *przepływ pracy* z następującymi *etapami*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na wysokim poziomie, ten przepływ pracy wykona:

1. Dostosowanie Phi3 (przez 150 kroków, które można zmodyfikować) przy użyciu danych z [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Połączenie wag adaptera LoRA z modelem bazowym. Wynikiem będzie pojedynczy artefakt modelu w formacie ONNX.
1. Model Builder zoptymalizuje model dla ONNX Runtime *i* zakwantyzuje model do `int4`.

Aby wykonać przepływ pracy, uruchom:

```bash
olive run --config phrase-classification.json
```

Po zakończeniu działania Olive, zoptymalizowany `int4` dostosowany model Phi3 będzie dostępny tutaj: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracja dostosowanego Phi3 z Twoją aplikacją 

Aby uruchomić aplikację:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpowiedź powinna być pojedynczym słowem klasyfikującym frazę (Smutek/Radość/Strach/Zaskoczenie).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego AI. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.