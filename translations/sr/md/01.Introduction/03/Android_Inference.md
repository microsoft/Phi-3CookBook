# **Inference Phi-3 na Androidu**

Hajde da istražimo kako možete da izvodite inferenciju sa Phi-3-mini na Android uređajima. Phi-3-mini je nova serija modela iz Microsoft-a koja omogućava primenu velikih jezičkih modela (LLMs) na uređajima na ivici mreže i IoT uređajima.

## Semantic Kernel i Inferencija

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacioni okvir koji vam omogućava da kreirate aplikacije kompatibilne sa Azure OpenAI Service, OpenAI modelima, pa čak i lokalnim modelima. Ako ste novi u Semantic Kernel-u, predlažemo da pogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Pristup Phi-3-mini pomoću Semantic Kernel-a

Možete ga kombinovati sa Hugging Face konektorom u Semantic Kernel-u. Pogledajte ovaj [primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Podrazumevano, on se odnosi na ID modela na Hugging Face-u. Međutim, možete se povezati i sa lokalno postavljenim serverom za Phi-3-mini model.

### Pozivanje Kvantizovanih Modela sa Ollama ili LlamaEdge

Mnogi korisnici preferiraju korišćenje kvantizovanih modela za lokalno pokretanje modela. [Ollama](https://ollama.com/) i [LlamaEdge](https://llamaedge.com) omogućavaju individualnim korisnicima da pozivaju različite kvantizovane modele:

#### Ollama

Možete direktno pokrenuti `ollama run Phi-3` ili ga konfigurisati offline kreiranjem `Modelfile` sa putanjom do vaše `.gguf` datoteke.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ako želite da koristite `.gguf` datoteke u oblaku i na uređajima na ivici mreže istovremeno, LlamaEdge je odličan izbor. Možete pogledati ovaj [primer koda](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) za početak.

### Instalacija i Pokretanje na Android Telefonima

1. **Preuzmite MLC Chat aplikaciju** (besplatno) za Android telefone.
2. Preuzmite APK datoteku (148MB) i instalirajte je na vaš uređaj.
3. Pokrenite MLC Chat aplikaciju. Videćete listu AI modela, uključujući Phi-3-mini.

Ukratko, Phi-3-mini otvara uzbudljive mogućnosti za generativnu AI tehnologiju na uređajima na ivici mreže, i možete odmah početi da istražujete njegove mogućnosti na Androidu.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских AI услуга за превођење. Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неразумевања која могу произаћи из коришћења овог превода.