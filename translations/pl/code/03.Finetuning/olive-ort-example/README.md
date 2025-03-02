# Dostosowanie Phi3 za pomocą Olive

W tym przykładzie użyjesz Olive, aby:

1. Dostosować adapter LoRA do klasyfikacji fraz na: Smutek, Radość, Strach, Zaskoczenie.
1. Scal wagę adaptera z modelem bazowym.
1. Optymalizować i kwantyzować model do `int4`.

Pokażemy również, jak przeprowadzić wnioskowanie z dostosowanego modelu za pomocą API Generate z ONNX Runtime (ORT).

> **⚠️ Do dostosowywania modelu potrzebujesz odpowiedniego GPU, na przykład A10, V100, A100.**

## 💾 Instalacja

Utwórz nową wirtualną przestrzeń Python (na przykład, używając `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Następnie zainstaluj Olive oraz zależności wymagane do procesu dostosowywania:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Dostosowanie Phi3 za pomocą Olive

[Plik konfiguracyjny Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) zawiera *workflow* z następującymi *przejściami*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Na wysokim poziomie ten workflow wykonuje:

1. Dostosowanie Phi3 (przez 150 kroków, które możesz zmodyfikować) z użyciem danych z pliku [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Scalanie wag adaptera LoRA z modelem bazowym. Wynikiem będzie pojedynczy artefakt modelu w formacie ONNX.
1. Model Builder zoptymalizuje model dla ONNX Runtime *oraz* zakwantyzuje model do `int4`.

Aby uruchomić workflow, wykonaj:

```bash
olive run --config phrase-classification.json
```

Po zakończeniu pracy Olive, zoptymalizowany model Phi3 w formacie `int4` będzie dostępny w: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integracja dostosowanego Phi3 z Twoją aplikacją 

Aby uruchomić aplikację:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Odpowiedź powinna być pojedynczym słowem klasyfikującym frazę (Smutek/Radość/Strach/Zaskoczenie).

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.