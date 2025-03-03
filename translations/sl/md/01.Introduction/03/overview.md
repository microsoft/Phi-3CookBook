V kontekstu Phi-3-mini sklepanje pomeni proces uporabe modela za napovedovanje ali generiranje izhodov na podlagi vhodnih podatkov. Tukaj je več podrobnosti o Phi-3-mini in njegovih zmožnostih sklepanja.

Phi-3-mini je del serije modelov Phi-3, ki jih je izdal Microsoft. Ti modeli so zasnovani za preoblikovanje možnosti, ki jih ponujajo majhni jezikovni modeli (SLM-ji).

Spodaj so ključne točke o Phi-3-mini in njegovih zmožnostih sklepanja:

## **Pregled Phi-3-mini:**
- Phi-3-mini ima velikost parametrov 3,8 milijarde.
- Model lahko deluje ne samo na tradicionalnih računalniških napravah, temveč tudi na robnih napravah, kot so mobilne naprave in IoT naprave.
- Izdaja Phi-3-mini omogoča posameznikom in podjetjem uvajanje SLM-jev na različnih strojnih napravah, še posebej v okolju z omejenimi viri.
- Model podpira različne formate, vključno s tradicionalnim PyTorch formatom, kvantizirano različico v gguf formatu in kvantizirano različico na osnovi ONNX.

## **Dostop do Phi-3-mini:**
Za dostop do Phi-3-mini lahko uporabite [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) v aplikaciji Copilot. Semantic Kernel je običajno združljiv z Azure OpenAI Service, odprtokodnimi modeli na Hugging Face in lokalnimi modeli.  
Lahko uporabite tudi [Ollama](https://ollama.com) ali [LlamaEdge](https://llamaedge.com) za klicanje kvantiziranih modelov. Ollama omogoča posameznim uporabnikom klicanje različnih kvantiziranih modelov, medtem ko LlamaEdge zagotavlja medplatformsko dostopnost za GGUF modele.

## **Kvantizirani modeli:**
Mnogi uporabniki raje uporabljajo kvantizirane modele za lokalno sklepanje. Na primer, lahko neposredno zaženete Ollama run Phi-3 ali ga konfigurirate brez povezave z uporabo Modelfile. Modelfile določa pot do GGUF datoteke in format poziva.

## **Možnosti generativne umetne inteligence:**
Združevanje SLM-jev, kot je Phi-3-mini, odpira nove možnosti za generativno umetno inteligenco. Sklepanje je le prvi korak; ti modeli se lahko uporabljajo za različne naloge v okoljih z omejenimi viri, nizko zakasnitvijo in omejenimi stroški.

## **Odklepanje generativne umetne inteligence s Phi-3-mini: Vodnik za sklepanje in uvajanje**  
Naučite se uporabljati Semantic Kernel, Ollama/LlamaEdge in ONNX Runtime za dostop in sklepanje modelov Phi-3-mini ter raziskujte možnosti generativne umetne inteligence v različnih aplikacijskih scenarijih.

**Značilnosti**  
Sklepanje modela phi3-mini v:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Skratka, Phi-3-mini razvijalcem omogoča raziskovanje različnih formatov modelov in uporabo generativne umetne inteligence v različnih aplikacijskih scenarijih.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja, ki temeljijo na umetni inteligenci. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeških prevajalcev. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.