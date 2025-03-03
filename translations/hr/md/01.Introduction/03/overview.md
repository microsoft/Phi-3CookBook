U kontekstu Phi-3-mini, inferencija se odnosi na proces korištenja modela za predviđanja ili generiranje izlaznih podataka na temelju ulaznih podataka. Dopustite mi da vam pružim više detalja o Phi-3-mini i njegovim mogućnostima inferencije.

Phi-3-mini dio je serije Phi-3 modela koje je objavio Microsoft. Ovi modeli osmišljeni su kako bi redefinirali što je moguće s malim jezičnim modelima (SLM-ovima).

Evo nekoliko ključnih točaka o Phi-3-mini i njegovim mogućnostima inferencije:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima veličinu parametara od 3,8 milijardi.
- Može se pokretati ne samo na tradicionalnim računalnim uređajima već i na rubnim uređajima poput mobilnih uređaja i IoT uređaja.
- Objavljivanje Phi-3-mini omogućuje pojedincima i poduzećima implementaciju SLM-ova na različitim hardverskim uređajima, posebno u okruženjima s ograničenim resursima.
- Pokriva različite formate modela, uključujući tradicionalni PyTorch format, kvantiziranu verziju gguf formata i kvantiziranu verziju temeljenu na ONNX-u.

## **Pristup Phi-3-mini:**
Za pristup Phi-3-mini možete koristiti [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) u aplikaciji Copilot. Semantic Kernel je općenito kompatibilan s Azure OpenAI Service, open-source modelima na Hugging Faceu i lokalnim modelima.  
Također možete koristiti [Ollama](https://ollama.com) ili [LlamaEdge](https://llamaedge.com) za pozivanje kvantiziranih modela. Ollama omogućuje pojedinačnim korisnicima pozivanje različitih kvantiziranih modela, dok LlamaEdge osigurava dostupnost GGUF modela na više platformi.

## **Kvantizirani modeli:**
Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalnu inferenciju. Na primjer, možete izravno pokrenuti Ollama run Phi-3 ili ga konfigurirati offline koristeći Modelfile. Modelfile specificira putanju GGUF datoteke i format upita.

## **Mogućnosti generativne umjetne inteligencije:**
Kombinacija SLM-ova poput Phi-3-mini otvara nove mogućnosti za generativnu umjetnu inteligenciju. Inferencija je samo prvi korak; ovi modeli mogu se koristiti za različite zadatke u okruženjima s ograničenim resursima, niskom latencijom i ograničenim troškovima.

## **Otključavanje generativne umjetne inteligencije s Phi-3-mini: Vodič za inferenciju i implementaciju**
Naučite kako koristiti Semantic Kernel, Ollama/LlamaEdge i ONNX Runtime za pristup i inferenciju Phi-3-mini modela te istražite mogućnosti generativne umjetne inteligencije u raznim scenarijima primjene.

**Značajke**  
Inferencija modela phi3-mini u:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Ukratko, Phi-3-mini omogućuje programerima istraživanje različitih formata modela i korištenje generativne umjetne inteligencije u raznim scenarijima primjene.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prijevoda. Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.