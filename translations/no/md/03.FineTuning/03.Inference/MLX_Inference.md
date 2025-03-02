# **Inference Phi-3 med Apple MLX-rammeverket**

## **Hva er MLX-rammeverket**

MLX er et rammeverk for matrisebasert maskinlæringsforskning på Apple Silicon, utviklet av Apple-maskinlæringsforskning.

MLX er designet av maskinlæringsforskere for maskinlæringsforskere. Rammeverket er ment å være brukervennlig, men samtidig effektivt for å trene og distribuere modeller. Selve designet av rammeverket er også konseptuelt enkelt. Målet er å gjøre det enkelt for forskere å utvide og forbedre MLX, slik at nye ideer raskt kan utforskes.

LLM-er kan akselereres på Apple Silicon-enheter via MLX, og modeller kan kjøres lokalt på en veldig praktisk måte.

## **Bruke MLX til å kjøre inferens på Phi-3-mini**

### **1. Sett opp ditt MLX-miljø**

1. Python 3.11.x  
2. Installer MLX-biblioteket  

```bash

pip install mlx-lm

```

### **2. Kjøre Phi-3-mini i Terminal med MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet (mitt miljø er Apple M1 Max, 64GB) er:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.no.png)

### **3. Kvantisering av Phi-3-mini med MLX i Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Merk:*** Modellen kan kvantiseres gjennom mlx_lm.convert, og standard kvantisering er INT4. Dette eksemplet kvantiserer Phi-3-mini til INT4.

Modellen kan kvantiseres gjennom mlx_lm.convert, og standard kvantisering er INT4. Dette eksemplet kvantiserer Phi-3-mini til INT4. Etter kvantisering lagres modellen i standardkatalogen ./mlx_model.

Vi kan teste den kvantiserte modellen med MLX fra terminalen:

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Resultatet er:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.no.png)

### **4. Kjøre Phi-3-mini med MLX i Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.no.png)

***Merk:*** Vennligst se dette eksempelet [klikk denne lenken](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Ressurser**

1. Lær mer om Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub-repositorium [https://github.com/ml-explore](https://github.com/ml-explore)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.