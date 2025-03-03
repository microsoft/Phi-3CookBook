## Scenariusze dostrajania

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.pl.png)

**Platforma** Obejmuje różne technologie, takie jak Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito i ONNX Runtime.

**Infrastruktura** Obejmuje CPU i FPGA, które są kluczowe dla procesu dostrajania. Pokażę teraz ikony dla każdej z tych technologii.

**Narzędzia i frameworki** Obejmuje ONNX Runtime i ONNX Runtime. Pokażę teraz ikony dla każdej z tych technologii.  
[Wstaw ikony dla ONNX Runtime i ONNX Runtime]

Proces dostrajania z użyciem technologii Microsoft obejmuje różne komponenty i narzędzia. Dzięki zrozumieniu i wykorzystaniu tych technologii możemy skutecznie dostrajać nasze aplikacje i tworzyć lepsze rozwiązania.

## Model jako Usługa

Dostrój model, korzystając z hostowanego dostrajania, bez konieczności tworzenia i zarządzania infrastrukturą obliczeniową.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.pl.png)

Dostrajanie bezserwerowe jest dostępne dla modeli Phi-3-mini i Phi-3-medium, co umożliwia programistom szybkie i łatwe dostosowywanie modeli do scenariuszy w chmurze i na urządzeniach brzegowych, bez konieczności organizowania infrastruktury obliczeniowej. Ogłosiliśmy również, że model Phi-3-small jest teraz dostępny w ramach oferty Model-as-a-Service, co pozwala programistom szybko i łatwo rozpocząć pracę z AI, bez zarządzania podstawową infrastrukturą.

## Model jako Platforma

Użytkownicy zarządzają własną infrastrukturą obliczeniową, aby dostroić swoje modele.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.pl.png)

[Przykład dostrajania](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## Scenariusze dostrajania

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenariusz|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adaptacja wstępnie wytrenowanych LLM do konkretnych zadań lub dziedzin|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostrajanie dla zadań NLP, takich jak klasyfikacja tekstu, rozpoznawanie nazwanych encji i tłumaczenie maszynowe|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostrajanie dla zadań QA|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostrajanie do generowania odpowiedzi przypominających ludzkie w chatbotach|Tak|Tak|Tak|Tak|Tak|Tak|
|Dostrajanie do generowania muzyki, sztuki lub innych form kreatywności|Tak|Tak|Tak|Tak|Tak|Tak|
|Redukcja kosztów obliczeniowych i finansowych|Tak|Tak|Nie|Tak|Tak|Nie|
|Zmniejszenie użycia pamięci|Nie|Tak|Nie|Tak|Tak|Tak|
|Wykorzystanie mniejszej liczby parametrów dla efektywnego dostrajania|Nie|Tak|Tak|Nie|Nie|Tak|
|Pamięciooszczędna forma równoległości danych, umożliwiająca dostęp do łącznej pamięci GPU wszystkich dostępnych urządzeń GPU|Nie|Nie|Nie|Tak|Tak|Tak|

## Przykłady wydajności dostrajania

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.pl.png)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.