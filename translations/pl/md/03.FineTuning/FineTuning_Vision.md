# Przepis na dostrajanie Phi-3.5-vision

To oficjalne wsparcie dla dostrajania Phi-3.5-vision przy użyciu bibliotek huggingface.  
Przejdź do katalogu z kodem [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) przed wykonaniem poniższych poleceń.

## Instalacja

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Szybki start

Udostępniamy dwa przykładowe skrypty do dostrajania, jeden dla DocVQA, a drugi dla klasyfikacji obraźliwych memów.

Minimalne wymagania sprzętowe: 4x RTX8000 (48 GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision teraz oficjalnie obsługuje wejścia z wieloma obrazami. Oto przykład dostrajania dla NLVR2:

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Przewodnik użytkownika

W zależności od sprzętu użytkownicy mogą wybrać różne strategie dostrajania. Obsługujemy pełne dostrajanie (z Deepspeed Zero-2) z opcjonalnie zamrożonymi parametrami wizji oraz LoRA (w tym 4-bitowe QLoRA).  
Ogólnie zalecamy pełne dostrajanie z flash attention i bf16, jeśli jest to możliwe.

### Przewodnik dotyczący konwersji własnego zbioru danych do wymaganego formatu

Używamy minimalnego zbioru danych do klasyfikacji wideo (podzbiór UCF-101) jako przykładu end-to-end, aby pokazać, jak przekonwertować własny zbiór danych na wymagany format i dostroić Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Przekonwertowane dane będą wyglądać tak:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

Dla adnotacji `jsonl` każda linia powinna być słownikiem o następującej strukturze:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Należy zauważyć, że `conversations` to lista, co pozwala na obsługę wieloetapowych rozmów, jeśli takie dane są dostępne.

## Wnioskowanie o limit GPU w Azure

### Wymagania wstępne

Konto Azure z rolą Współtwórca (lub inną rolą, która obejmuje dostęp Współtwórcy).  

Jeśli nie masz konta Azure, utwórz [bezpłatne konto przed rozpoczęciem](https://azure.microsoft.com).

### Wniosek o zwiększenie limitu

Możesz złożyć wniosek o zwiększenie limitu bezpośrednio w sekcji Moje limity. Postępuj zgodnie z poniższymi krokami, aby zażądać zwiększenia limitu. W tym przykładzie możesz wybrać dowolny regulowany limit w swojej subskrypcji.

Zaloguj się do [portalu Azure](https://portal.azure.com).  

Wpisz „limity” w polu wyszukiwania, a następnie wybierz Limity.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stronie Przegląd wybierz dostawcę, np. Compute lub AML.  

**Uwaga**: Dla wszystkich dostawców innych niż Compute zobaczysz kolumnę Wniosek o zwiększenie zamiast kolumny Regulowanej opisanej poniżej. Tam możesz zażądać zwiększenia konkretnego limitu lub utworzyć zgłoszenie do pomocy technicznej w celu zwiększenia limitu.

Na stronie Moje limity, w kolumnie Nazwa limitu, wybierz limit, który chcesz zwiększyć. Upewnij się, że kolumna Regulowany pokazuje Tak dla tego limitu.

Na górze strony wybierz Nowy wniosek o limit, a następnie wprowadź nową wartość limitu.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

W panelu Nowy wniosek o limit wprowadź wartość liczbową dla nowego limitu, a następnie wybierz Prześlij.

Twój wniosek zostanie przeanalizowany, a Ty zostaniesz powiadomiony, czy może zostać zrealizowany. Zwykle dzieje się to w ciągu kilku minut.

Jeśli Twój wniosek nie zostanie zrealizowany, zobaczysz link do utworzenia zgłoszenia do pomocy technicznej. Korzystając z tego linku, inżynier pomocy technicznej pomoże Ci w realizacji wniosku o zwiększenie limitu.

## Sugerowane SKU maszyn GPU w Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Oto kilka przykładów:

### Jeśli posiadasz GPU A100 lub H100

Pełne dostrajanie zazwyczaj daje najlepsze wyniki. Możesz użyć poniższego polecenia, aby dostroić Phi-3-V do klasyfikacji obraźliwych memów.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jeśli posiadasz Standard_ND40rs_v2 8x V100-32GB GPU

Pełne dostrajanie Phi-3-V do klasyfikacji obraźliwych memów jest nadal możliwe. Jednak należy się spodziewać znacznie niższej przepustowości w porównaniu z GPU A100 lub H100 z powodu braku wsparcia dla flash attention.  
Dokładność może również zostać obniżona z powodu braku wsparcia dla bf16 (zamiast tego używane jest szkolenie w mieszanej precyzji fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jeśli nie masz dostępu do GPU klasy centrum danych

LoRA może być jedynym wyborem. Możesz użyć poniższego polecenia, aby dostroić Phi-3-V do klasyfikacji obraźliwych memów.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Dla GPU Turing+ obsługiwane jest QLoRA.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Sugerowane hiperparametry i oczekiwana dokładność

### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda szkolenia | Zamrożony model wizji | typ danych | ranga LoRA | alfa LoRA | rozmiar partii | tempo uczenia | epoki | Dokładność  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
pełne dostrajanie |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
pełne dostrajanie | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
wyniki LoRA wkrótce |  |  |  |  |  |  |  |  |  

### UWAGA

Poniższe wyniki DocVQA i obraźliwych memów opierają się na wcześniejszej wersji (Phi-3-vision).  
Nowe wyniki z Phi-3.5-vision zostaną zaktualizowane wkrótce.

### DocVQA (UWAGA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda szkolenia | typ danych | ranga LoRA | alfa LoRA | rozmiar partii | tempo uczenia | epoki | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
pełne dostrajanie | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
pełne dostrajanie | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
zamrożony model obrazu | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
zamrożony model obrazu | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |  

### Obraźliwe memy (UWAGA: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Metoda szkolenia | typ danych | ranga LoRA | alfa LoRA | rozmiar partii | tempo uczenia | epoki | Dokładność  
--- | --- | --- | --- | --- | --- | --- | --- |  
pełne dostrajanie | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
pełne dostrajanie | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
zamrożony model obrazu | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
zamrożony model obrazu | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |  

## Benchmarking prędkości (UWAGA: Phi-3-vision)

Nowe wyniki benchmarków dla Phi-3.5-vision zostaną zaktualizowane wkrótce.

Benchmarking prędkości został przeprowadzony na zbiorze danych DocVQA. Średnia długość sekwencji w tym zbiorze danych wynosi 2443.23 tokenów (z użyciem `num_crops=16` dla modelu obrazu).

### 8x A100-80GB (Ampere)

Metoda szkolenia | \# węzłów | GPU | flash attention | Efektywny rozmiar partii | Przepustowość (img/s) | Przyspieszenie | Szczytowe użycie pamięci GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
pełne dostrajanie | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
pełne dostrajanie | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
pełne dostrajanie | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
pełne dostrajanie | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
zamrożony model obrazu | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
zamrożony model obrazu | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Metoda szkolenia | \# węzłów | GPU | flash attention | Efektywny rozmiar partii | Przepustowość (img/s) | Przyspieszenie | Szczytowe użycie pamięci GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
pełne dostrajanie | 1 | 8 | | 64 | 2.462 |  1x | ~32  
pełne dostrajanie | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
pełne dostrajanie | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
zamrożony model obrazu | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Znane problemy

- Brak możliwości uruchomienia flash attention z fp16 (bf16 jest zawsze zalecane, jeśli jest dostępne, a wszystkie GPU obsługujące flash attention również obsługują bf16).  
- Brak wsparcia dla zapisywania pośrednich punktów kontrolnych i wznawiania treningu.  

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za wiążące źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.