**Dostosowywanie Phi-3 za pomocą QLoRA**

Dostosowywanie modelu językowego Phi-3 Mini firmy Microsoft za pomocą [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).  

QLoRA pomoże poprawić zrozumienie konwersacyjne i generowanie odpowiedzi.  

Aby załadować modele w trybie 4-bitowym z użyciem transformers i bitsandbytes, musisz zainstalować accelerate i transformers ze źródła oraz upewnić się, że masz najnowszą wersję biblioteki bitsandbytes.

**Przykłady**  
- [Dowiedz się więcej z tego przykładowego notebooka](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Przykład dostosowywania w Pythonie](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Przykład dostosowywania na Hugging Face Hub za pomocą LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Przykład dostosowywania na Hugging Face Hub za pomocą QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.