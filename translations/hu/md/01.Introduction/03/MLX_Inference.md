# **Phi-3 következtetés az Apple MLX keretrendszerrel**

## **Mi az MLX keretrendszer**

Az MLX egy gépi tanulási kutatásokhoz kifejlesztett tömbkeretrendszer Apple Silicon eszközökre, amelyet az Apple gépi tanulási kutatócsoportja hozott létre.

Az MLX-et gépi tanulási kutatók tervezték gépi tanulási kutatók számára. A keretrendszer célja, hogy felhasználóbarát legyen, miközben hatékonyan támogatja a modellek tanítását és telepítését. Maga a keretrendszer kialakítása is koncepcionálisan egyszerű. Célunk, hogy a kutatók könnyedén bővíthessék és fejleszthessék az MLX-et, lehetővé téve az új ötletek gyors feltérképezését.

Az LLM-ek Apple Silicon eszközökön felgyorsíthatók az MLX segítségével, és a modellek helyben, nagyon kényelmesen futtathatók.

## **Phi-3-mini következtetés MLX-szel**

### **1. Állítsd be az MLX környezeted**

1. Python 3.11.x
2. Telepítsd az MLX könyvtárat


```bash

pip install mlx-lm

```

### **2. Phi-3-mini futtatása terminálban MLX-szel**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Az eredmény (az én környezetem: Apple M1 Max, 64GB) a következő:

![Terminál](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.hu.png)

### **3. Phi-3-mini kvantálása MLX-szel terminálban**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Megjegyzés:*** A modellt az mlx_lm.convert segítségével lehet kvantálni, és az alapértelmezett kvantálás INT4. Ez a példa a Phi-3-mini INT4-re történő kvantálását mutatja be.

A modellt az mlx_lm.convert segítségével lehet kvantálni, és az alapértelmezett kvantálás INT4. Ez a példa a Phi-3-mini INT4-re történő kvantálását mutatja be. A kvantálás után a modell az alapértelmezett ./mlx_model könyvtárban kerül tárolásra.

A kvantált modellt tesztelhetjük MLX segítségével terminálból:


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Az eredmény a következő:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.hu.png)


### **4. Phi-3-mini futtatása MLX-szel Jupyter Notebookban**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.hu.png)

***Megjegyzés:*** Kérlek, olvasd el ezt a mintafájlt [kattints erre a linkre](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Erőforrások**

1. Tudj meg többet az Apple MLX keretrendszerről [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.