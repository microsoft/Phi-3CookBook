# **Dostosowywanie Phi-3 za pomocą Lora**

Dostosowywanie modelu językowego Phi-3 Mini firmy Microsoft za pomocą [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na bazie niestandardowego zestawu danych z instrukcjami do czatu.

LoRA pomoże poprawić zrozumienie konwersacyjne i generowanie odpowiedzi.

## Przewodnik krok po kroku dotyczący dostosowywania Phi-3 Mini:

**Importy i konfiguracja**

Instalowanie loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Rozpocznij od zaimportowania niezbędnych bibliotek, takich jak datasets, transformers, peft, trl i torch. Skonfiguruj logowanie, aby śledzić proces treningowy.

Możesz zdecydować się na dostosowanie niektórych warstw, zastępując je odpowiednikami zaimplementowanymi w loralib. Obecnie obsługujemy tylko nn.Linear, nn.Embedding i nn.Conv2d. Obsługujemy również MergedLinear w przypadkach, gdy pojedynczy nn.Linear reprezentuje więcej niż jedną warstwę, na przykład w niektórych implementacjach projekcji qkv w mechanizmie uwagi (zobacz Dodatkowe uwagi, aby dowiedzieć się więcej).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Przed rozpoczęciem pętli treningowej oznacz jako trenowalne tylko parametry LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Podczas zapisywania punktu kontrolnego wygeneruj state_dict zawierający wyłącznie parametry LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Podczas ładowania punktu kontrolnego za pomocą load_state_dict upewnij się, że ustawiono strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Teraz trening może przebiegać jak zwykle.

**Hiperparametry**

Zdefiniuj dwa słowniki: training_config i peft_config. training_config zawiera hiperparametry treningowe, takie jak współczynnik uczenia się, rozmiar partii i ustawienia logowania.

peft_config określa parametry związane z LoRA, takie jak rank, dropout i typ zadania.

**Ładowanie modelu i tokenizera**

Określ ścieżkę do wstępnie wytrenowanego modelu Phi-3 (np. "microsoft/Phi-3-mini-4k-instruct"). Skonfiguruj ustawienia modelu, w tym użycie pamięci podręcznej, typ danych (bfloat16 dla mieszanej precyzji) i implementację mechanizmu uwagi.

**Trening**

Dostosuj model Phi-3 za pomocą niestandardowego zestawu danych z instrukcjami do czatu. Wykorzystaj ustawienia LoRA z peft_config dla efektywnej adaptacji. Monitoruj postępy treningu za pomocą określonej strategii logowania.  
Ocena i zapis: Oceń dostosowany model. Zapisuj punkty kontrolne podczas treningu do późniejszego użytku.

**Przykłady**
- [Dowiedz się więcej dzięki temu przykładowemu notatnikowi](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Przykład skryptu Python do dostosowywania](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Przykład dostosowywania na platformie Hugging Face Hub za pomocą LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Przykładowa karta modelu Hugging Face - dostosowywanie za pomocą LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Przykład dostosowywania na platformie Hugging Face Hub za pomocą QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług tłumaczenia opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby zapewnić precyzję, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.