U kontekstu Phi-3-mini, inferencija se odnosi na proces korišćenja modela za pravljenje predikcija ili generisanje izlaza na osnovu ulaznih podataka. Evo više detalja o Phi-3-mini i njegovim mogućnostima inferencije.

Phi-3-mini je deo serije modela Phi-3 koje je izdao Microsoft. Ovi modeli su osmišljeni da redefinišu šta je moguće sa malim jezičkim modelima (SLM-ovima).

Evo ključnih tačaka o Phi-3-mini i njegovim mogućnostima inferencije:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima veličinu parametara od 3,8 milijardi.
- Može se koristiti ne samo na tradicionalnim računarima, već i na uređajima na ivici mreže, kao što su mobilni uređaji i IoT uređaji.
- Objavljivanje Phi-3-mini omogućava pojedincima i kompanijama da implementiraju SLM-ove na različitim hardverskim uređajima, posebno u okruženjima sa ograničenim resursima.
- Podržava različite formate modela, uključujući tradicionalni PyTorch format, kvantizovanu verziju gguf formata i ONNX kvantizovanu verziju.

## **Pristup Phi-3-mini:**
Da biste pristupili Phi-3-mini, možete koristiti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) u Copilot aplikaciji. Semantic Kernel je generalno kompatibilan sa Azure OpenAI Service, open-source modelima na Hugging Face platformi i lokalnim modelima.  
Takođe možete koristiti [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com) za pozivanje kvantizovanih modela. Ollama omogućava pojedinačnim korisnicima da pozivaju različite kvantizovane modele, dok LlamaEdge pruža dostupnost GGUF modela na različitim platformama.

## **Kvantizovani modeli:**
Mnogi korisnici preferiraju upotrebu kvantizovanih modela za lokalnu inferenciju. Na primer, možete direktno pokrenuti Ollama run Phi-3 ili ga konfigurirati offline pomoću Modelfile fajla. Modelfile specificira putanju do GGUF fajla i format upita.

## **Mogućnosti generativne AI:**
Kombinovanje SLM-ova poput Phi-3-mini otvara nove mogućnosti za generativnu veštačku inteligenciju. Inferencija je samo prvi korak; ovi modeli se mogu koristiti za različite zadatke u okruženjima sa ograničenim resursima, niskom latencijom i ograničenim budžetom.

## **Otključavanje generativne AI sa Phi-3-mini: Vodič za inferenciju i implementaciju**  
Saznajte kako koristiti Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime za pristup Phi-3-mini modelima i njihovu inferenciju, i istražite mogućnosti generativne AI u različitim aplikacionim scenarijima.

**Karakteristike**  
Inferencija Phi-3-mini modela u:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Ukratko, Phi-3-mini omogućava programerima da istraže različite formate modela i iskoriste generativnu veštačku inteligenciju u raznovrsnim aplikacionim scenarijima.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте на уму да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразумe или погрешна тумачења која могу произаћи из коришћења овог превода.