# **Inference Phi-3 s Apple MLX Frameworkom**

## **Što je MLX Framework**

MLX je okvir za strojno učenje na Apple Siliconu, razvijen od strane Appleovog istraživačkog tima za strojno učenje.

MLX je dizajniran od istraživača strojnog učenja za istraživače strojnog učenja. Okvir je osmišljen tako da bude jednostavan za korištenje, ali i dalje učinkovit za treniranje i implementaciju modela. Sam dizajn okvira je konceptualno jednostavan. Cilj je omogućiti istraživačima lako proširivanje i poboljšavanje MLX-a kako bi brzo mogli istraživati nove ideje.

LLM-ovi se mogu ubrzati na uređajima s Apple Siliconom putem MLX-a, a modeli se mogu lokalno pokretati vrlo praktično.

## **Korištenje MLX-a za inferenciju Phi-3-mini**

### **1. Postavite svoj MLX okruženje**

1. Python 3.11.x  
2. Instalirajte MLX biblioteku  

```bash

pip install mlx-lm

```

### **2. Pokretanje Phi-3-mini u Terminalu pomoću MLX-a**  

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat (moje okruženje je Apple M1 Max, 64GB) je:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.hr.png)

### **3. Kvantizacija Phi-3-mini s MLX-om u Terminalu**  

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Napomena:*** Model se može kvantizirati pomoću mlx_lm.convert, a zadana kvantizacija je INT4. Ovaj primjer kvantizira Phi-3-mini u INT4.

Model se može kvantizirati pomoću mlx_lm.convert, a zadana kvantizacija je INT4. Ovaj primjer kvantizira Phi-3-mini u INT4. Nakon kvantizacije, bit će spremljen u zadani direktorij ./mlx_model.

Možemo testirati model kvantiziran s MLX-om iz terminala.  

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Rezultat je:  

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.hr.png)

### **4. Pokretanje Phi-3-mini s MLX-om u Jupyter Notebooku**  

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.hr.png)

***Napomena:*** Molimo pročitajte ovaj primjer [kliknite na ovu poveznicu](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Resursi**

1. Saznajte više o Apple MLX Frameworku [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)  

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojno baziranog AI prijevoda. Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.