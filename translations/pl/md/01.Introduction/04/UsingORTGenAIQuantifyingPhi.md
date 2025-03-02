# **Kwantyzacja rodziny Phi za pomocą rozszerzeń Generative AI dla onnxruntime**

## **Czym są rozszerzenia Generative AI dla onnxruntime**

Te rozszerzenia umożliwiają uruchamianie generatywnej AI z ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Zapewniają pętlę generatywnej AI dla modeli ONNX, w tym wnioskowanie z ONNX Runtime, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV. Programiści mogą wywoływać metodę wysokiego poziomu `generate()`, albo uruchamiać każdą iterację modelu w pętli, generując token po tokenie i opcjonalnie aktualizując parametry generacji w trakcie pętli. Obsługiwane są takie techniki jak greedy/beam search oraz próbkowanie TopP i TopK do generowania sekwencji tokenów, a także wbudowane przetwarzanie logitów, takie jak kary za powtórzenia. Można również łatwo dodać własne metody oceny.

Na poziomie aplikacji możesz używać rozszerzeń Generative AI dla onnxruntime do budowania aplikacji w językach C++/C#/Python. Na poziomie modelu możesz je wykorzystać do łączenia modeli dostosowanych do konkretnych zadań i wykonywania związanych z tym działań wdrożeniowych.

## **Kwantyzacja Phi-3.5 za pomocą rozszerzeń Generative AI dla onnxruntime**

### **Obsługiwane modele**

Rozszerzenia Generative AI dla onnxruntime obsługują konwersję kwantyzacyjną modeli takich jak Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Kreator modeli w rozszerzeniach Generative AI dla onnxruntime**

Kreator modeli znacznie przyspiesza tworzenie zoptymalizowanych i kwantyzowanych modeli ONNX, które działają z API `generate()` w ONNX Runtime.

Za pomocą Kreatora modeli możesz kwantyzować model do INT4, INT8, FP16, FP32 i łączyć różne metody przyspieszenia sprzętowego, takie jak CPU, CUDA, DirectML, Mobile itp.

Aby użyć Kreatora modeli, musisz zainstalować:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Po instalacji możesz uruchomić skrypt Kreatora modeli z terminala, aby przeprowadzić konwersję formatu i kwantyzacji modelu.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Wyjaśnienie parametrów:

1. **model_name** To nazwa modelu na Hugging Face, np. microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct itp. Może to być również ścieżka do lokalnie przechowywanego modelu.

2. **path_to_output_folder** Ścieżka zapisu dla skwantyzowanego modelu.

3. **execution_provider** Obsługa różnych akceleratorów sprzętowych, takich jak CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Pobieramy model z Hugging Face i zapisujemy go lokalnie w pamięci podręcznej.

***Uwaga:***

## **Jak używać Kreatora modeli do kwantyzacji Phi-3.5**

Kreator modeli obecnie obsługuje kwantyzację modeli ONNX dla Phi-3.5 Instruct i Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Konwersja do INT4 z przyspieszeniem CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Konwersja do INT4 z przyspieszeniem CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ustaw środowisko w terminalu:

```bash

mkdir models

cd models 

```

2. Pobierz model microsoft/Phi-3.5-vision-instruct do folderu `models`:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Pobierz następujące pliki do folderu Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Pobierz ten plik do folderu `models`:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Przejdź do terminala:

    Konwertuj obsługę ONNX na FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Uwaga:**

1. Kreator modeli obecnie obsługuje konwersję Phi-3.5-Instruct i Phi-3.5-Vision, ale nie obsługuje Phi-3.5-MoE.

2. Aby używać skwantyzowanego modelu ONNX, można go obsługiwać za pomocą SDK rozszerzeń Generative AI dla onnxruntime.

3. Należy uwzględnić bardziej odpowiedzialne podejście do AI, dlatego po konwersji modelu do kwantyzacji zaleca się przeprowadzenie dokładnych testów wyników.

4. Kwantyzując model CPU INT4, możemy wdrożyć go na urządzeniach brzegowych, co zapewnia lepsze scenariusze zastosowań. Dlatego ukończono kwantyzację Phi-3.5-Instruct do INT4.

## **Zasoby**

1. Dowiedz się więcej o rozszerzeniach Generative AI dla onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repozytorium GitHub rozszerzeń Generative AI dla onnxruntime:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło nadrzędne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.