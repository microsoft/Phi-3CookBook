# **Inferenca Phi-3 na Androidu**

Poglejmo, kako lahko izvedete inferenco z modelom Phi-3-mini na napravah Android. Phi-3-mini je nova serija modelov podjetja Microsoft, ki omogoča uporabo Velikih Jezikovnih Modelov (LLMs) na robnih napravah in napravah IoT.

## Semantic Kernel in Inferenca

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikacijski okvir, ki omogoča ustvarjanje aplikacij, združljivih z Azure OpenAI Service, OpenAI modeli in celo lokalnimi modeli. Če ste novi pri Semantic Kernel, priporočamo, da si ogledate [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Dostop do Phi-3-mini s pomočjo Semantic Kernel

Phi-3-mini lahko povežete s Hugging Face Connector v Semantic Kernel. Oglejte si ta [vzorec kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Privzeto ustreza ID-ju modela na Hugging Face. Vendar pa se lahko povežete tudi z lokalno postavljenim strežnikom modela Phi-3-mini.

### Klicanje kvantiziranih modelov z Ollama ali LlamaEdge

Veliko uporabnikov raje uporablja kvantizirane modele za lokalno izvajanje. [Ollama](https://ollama.com/) in [LlamaEdge](https://llamaedge.com) omogočata posameznikom klicanje različnih kvantiziranih modelov:

#### Ollama

Model lahko neposredno zaženete z `ollama run Phi-3` ali ga konfigurirate brez povezave tako, da ustvarite `Modelfile` s potjo do vaše datoteke `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Vzorec kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Če želite uporabljati datoteke `.gguf` tako v oblaku kot na robnih napravah, je LlamaEdge odlična izbira. Za začetek si oglejte ta [vzorec kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Namestitev in zagon na Android telefonih

1. **Prenesite aplikacijo MLC Chat** (brezplačno) za Android telefone.
2. Prenesite datoteko APK (148 MB) in jo namestite na svojo napravo.
3. Zaženite aplikacijo MLC Chat. Prikazan bo seznam AI modelov, vključno z modelom Phi-3-mini.

Skratka, Phi-3-mini odpira vznemirljive možnosti za generativno umetno inteligenco na robnih napravah, zato lahko začnete raziskovati njegove zmogljivosti na Androidu.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.