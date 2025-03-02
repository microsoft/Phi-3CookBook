# **Izvođenje Phi-3 na Androidu**

Pogledajmo kako možete izvoditi zaključivanje s Phi-3-mini na Android uređajima. Phi-3-mini je nova serija modela iz Microsofta koja omogućuje implementaciju velikih jezičnih modela (LLM-ova) na rubnim uređajima i IoT uređajima.

## Semantic Kernel i Zaključivanje

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacijski okvir koji vam omogućuje kreiranje aplikacija kompatibilnih s Azure OpenAI Service, OpenAI modelima, pa čak i lokalnim modelima. Ako ste novi u Semantic Kernelu, preporučujemo da pogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kako pristupiti Phi-3-mini koristeći Semantic Kernel

Možete ga kombinirati s Hugging Face Connectorom u Semantic Kernelu. Pogledajte ovaj [Primjer Koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Po zadanim postavkama, on odgovara ID-u modela na Hugging Face platformi. Međutim, također se možete povezati s lokalno izgrađenim Phi-3-mini poslužiteljem modela.

### Pozivanje Kvantiziranih Modela s Ollama ili LlamaEdge

Mnogi korisnici preferiraju korištenje kvantiziranih modela za lokalno pokretanje modela. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) omogućuju pojedinačnim korisnicima pozivanje različitih kvantiziranih modela:

#### Ollama

Možete direktno pokrenuti `ollama run Phi-3` ili ga konfigurirati offline kreiranjem `Modelfile` s putanjom do vaše `.gguf` datoteke.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primjer Koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ako želite koristiti `.gguf` datoteke u oblaku i na rubnim uređajima istovremeno, LlamaEdge je odličan izbor. Možete pogledati ovaj [primjer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) za početak.

### Instalacija i Pokretanje na Android Telefonima

1. **Preuzmite MLC Chat aplikaciju** (Besplatno) za Android telefone.
2. Preuzmite APK datoteku (148 MB) i instalirajte je na svoj uređaj.
3. Pokrenite MLC Chat aplikaciju. Vidjet ćete popis AI modela, uključujući Phi-3-mini.

Zaključno, Phi-3-mini otvara uzbudljive mogućnosti za generativnu umjetnu inteligenciju na rubnim uređajima, a možete odmah početi istraživati njegove mogućnosti na Androidu.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga automatskog prevođenja temeljenih na umjetnoj inteligenciji. Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.