# Lab. Optymalizacja modeli AI do inferencji na urządzeniu

## Wprowadzenie

> [!IMPORTANT]
> Do wykonania tego laboratorium wymagany jest **GPU Nvidia A10 lub A100** z odpowiednimi sterownikami oraz zainstalowanym zestawem narzędzi CUDA (wersja 12+).

> [!NOTE]
> To laboratorium zajmie około **35 minut** i wprowadzi Cię praktycznie w podstawowe pojęcia związane z optymalizacją modeli do inferencji na urządzeniu przy użyciu OLIVE.

## Cele nauki

Po ukończeniu tego laboratorium będziesz w stanie używać OLIVE do:

- Kwantyzacji modelu AI za pomocą metody kwantyzacji AWQ.
- Dostosowywania modelu AI do konkretnego zadania.
- Generowania adapterów LoRA (dostosowanego modelu) dla efektywnej inferencji na urządzeniu z użyciem ONNX Runtime.

### Czym jest Olive

Olive (*O*NNX *live*) to zestaw narzędzi do optymalizacji modeli z dołączonym interfejsem CLI, który umożliwia dostarczanie modeli dla ONNX Runtime +++https://onnxruntime.ai+++ z zachowaniem jakości i wydajności.

![Schemat Olive](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.pl.png)

Wejściem dla Olive jest zazwyczaj model PyTorch lub Hugging Face, a wyjściem zoptymalizowany model ONNX, który jest uruchamiany na urządzeniu (cel wdrożenia) korzystającym z ONNX Runtime. Olive optymalizuje model pod kątem akceleratora AI (NPU, GPU, CPU) dostarczanego przez producenta sprzętu, takiego jak Qualcomm, AMD, Nvidia czy Intel.

Olive wykonuje *workflow*, czyli uporządkowaną sekwencję indywidualnych zadań optymalizacji modelu, zwanych *passami*. Przykładowe passy to: kompresja modelu, przechwytywanie grafu, kwantyzacja, optymalizacja grafu. Każdy pass ma zestaw parametrów, które można dostroić, aby osiągnąć najlepsze metryki, takie jak dokładność i opóźnienie, oceniane przez odpowiedni ewaluator. Olive stosuje strategię wyszukiwania, która używa algorytmu wyszukiwania do automatycznego dostrajania poszczególnych passów lub ich zestawów.

#### Korzyści z Olive

- **Zmniejszenie frustracji i czasu** spędzanego na eksperymentach metodą prób i błędów z różnymi technikami optymalizacji grafu, kompresji i kwantyzacji. Zdefiniuj swoje ograniczenia jakości i wydajności, a Olive automatycznie znajdzie najlepszy model dla Ciebie.
- **Ponad 40 wbudowanych komponentów optymalizacji modeli**, obejmujących najnowsze techniki w zakresie kwantyzacji, kompresji, optymalizacji grafu i dostrajania.
- **Łatwy w użyciu interfejs CLI** do typowych zadań optymalizacji modeli, takich jak `olive quantize`, `olive auto-opt`, `olive finetune`.
- Wbudowane pakowanie i wdrażanie modeli.
- Obsługa generowania modeli dla **Multi LoRA serving**.
- Tworzenie workflow za pomocą YAML/JSON do orkiestracji zadań optymalizacji i wdrażania modeli.
- Integracja z **Hugging Face** i **Azure AI**.
- Wbudowany mechanizm **cache**, który pozwala **oszczędzać koszty**.

## Instrukcje do laboratorium

> [!NOTE]
> Upewnij się, że skonfigurowałeś Azure AI Hub, projekt oraz instancję obliczeniową A100 zgodnie z instrukcjami z Laboratorium 1.

### Krok 0: Połącz się z Azure AI Compute

Połączysz się z Azure AI Compute, korzystając z funkcji zdalnej w **VS Code.**

1. Otwórz aplikację **VS Code** na swoim komputerze.
1. Otwórz **Command Palette** za pomocą **Shift+Ctrl+P**.
1. W Command Palette wyszukaj **AzureML - remote: Connect to compute instance in New Window**.
1. Postępuj zgodnie z instrukcjami na ekranie, aby połączyć się z instancją Compute. Będziesz musiał wybrać swoją subskrypcję Azure, grupę zasobów, projekt oraz nazwę instancji Compute, które skonfigurowałeś w Laboratorium 1.
1. Po połączeniu z instancją Compute Azure ML, informacja o tym będzie widoczna w **lewym dolnym rogu Visual Code** `><Azure ML: Compute Name`.

### Krok 1: Sklonuj to repozytorium

W VS Code otwórz nowy terminal za pomocą **Ctrl+J** i sklonuj to repozytorium:

W terminalu powinien pojawić się prompt:

```
azureuser@computername:~/cloudfiles/code$ 
```  
Sklonuj rozwiązanie  

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```  

### Krok 2: Otwórz folder w VS Code

Aby otworzyć VS Code w odpowiednim folderze, wykonaj następujące polecenie w terminalu, co otworzy nowe okno:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```  

Alternatywnie możesz otworzyć folder, wybierając **File** > **Open Folder**.

### Krok 3: Zależności

Otwórz okno terminala w VS Code na instancji Azure AI Compute (wskazówka: **Ctrl+J**) i wykonaj następujące polecenia, aby zainstalować zależności:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```  

> [!NOTE]
> Instalacja wszystkich zależności zajmie około **5 minut**.

W tym laboratorium będziesz pobierać i przesyłać modele do katalogu modeli Azure AI. Aby uzyskać dostęp do katalogu modeli, musisz zalogować się do Azure za pomocą:

```bash
az login
```  

> [!NOTE]
> Podczas logowania zostaniesz poproszony o wybranie subskrypcji. Upewnij się, że wybrałeś subskrypcję przypisaną do tego laboratorium.

### Krok 4: Wykonaj polecenia Olive

Otwórz okno terminala w VS Code na instancji Azure AI Compute (wskazówka: **Ctrl+J**) i upewnij się, że aktywowane jest środowisko `olive-ai` conda:

```bash
conda activate olive-ai
```  

Następnie wykonaj poniższe polecenia Olive w wierszu poleceń.

1. **Przeglądaj dane:** W tym przykładzie dostroisz model Phi-3.5-Mini, aby specjalizował się w odpowiadaniu na pytania związane z podróżami. Kod poniżej wyświetla kilka pierwszych rekordów zestawu danych w formacie JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```  

1. **Kwantyzuj model:** Przed trenowaniem modelu najpierw wykonaj kwantyzację za pomocą następującego polecenia, które wykorzystuje technikę Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantyzuje wagi modelu, uwzględniając aktywacje generowane podczas inferencji. Oznacza to, że proces kwantyzacji bierze pod uwagę rzeczywisty rozkład danych w aktywacjach, co prowadzi do lepszego zachowania dokładności modelu w porównaniu do tradycyjnych metod kwantyzacji wag.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```  

    Proces kwantyzacji AWQ zajmuje około **8 minut** i **zmniejsza rozmiar modelu z ~7,5 GB do ~2,5 GB**.

    W tym laboratorium pokażemy, jak wprowadzać modele z Hugging Face (na przykład: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` dostraja skwantyzowany model. Kwantyzacja modelu *przed* dostrajaniem, zamiast po nim, daje lepszą dokładność, ponieważ proces dostrajania odzyskuje część strat wynikających z kwantyzacji.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```  

    Proces dostrajania zajmuje około **6 minut** (100 kroków).

1. **Optymalizuj:** Po dostrojeniu modelu możesz go zoptymalizować za pomocą polecenia `olive auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` z Olive - w tym laboratorium użyjemy CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```  

    Proces optymalizacji zajmuje około **5 minut**.

### Krok 5: Szybki test inferencji modelu

Aby przetestować inferencję modelu, utwórz plik Python w swoim folderze o nazwie **app.py** i skopiuj poniższy kod:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```  

Wykonaj kod za pomocą:

```bash
python app.py
```  

### Krok 6: Prześlij model do Azure AI

Przesłanie modelu do repozytorium modeli Azure AI umożliwia jego udostępnienie innym członkom zespołu deweloperskiego oraz zapewnia kontrolę wersji modelu. Aby przesłać model, uruchom następujące polecenie:

> [!NOTE]
> Zaktualizuj `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` oraz nazwę projektu Azure AI, a następnie uruchom poniższe polecenie.

```
az ml workspace show
```  

Lub przejdź do +++ai.azure.com+++ i wybierz **management center** > **project** > **overview**.

Zaktualizuj pola `{}` nazwą swojej grupy zasobów i nazwą projektu Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
Następnie możesz zobaczyć przesłany model i wdrożyć go na stronie https://ml.azure.com/model/list.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.