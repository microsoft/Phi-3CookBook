# **Kvantizacija Phi-3.5 koristeći Apple MLX Framework**

MLX je okvir za istraživanje mašinskog učenja na Apple Silicon platformi, razvijen od strane Apple istraživačkog tima za mašinsko učenje.

MLX je dizajniran od strane istraživača mašinskog učenja za istraživače mašinskog učenja. Okvir je zamišljen da bude jednostavan za korišćenje, ali i dalje efikasan za treniranje i implementaciju modela. Dizajn samog okvira je takođe konceptualno jednostavan. Cilj je da istraživačima omogućimo lako proširenje i unapređenje MLX-a kako bi brzo istražili nove ideje.

LLM-ovi mogu biti ubrzani na Apple Silicon uređajima putem MLX-a, a modeli se mogu vrlo lako pokretati lokalno.

Sada Apple MLX Framework podržava konverziju kvantizacije za Phi-3.5-Instruct (**podrška za Apple MLX Framework**), Phi-3.5-Vision (**podrška za MLX-VLM Framework**), i Phi-3.5-MoE (**podrška za Apple MLX Framework**). Hajde da probamo sledeće:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Primeri za Phi-3.5 sa Apple MLX**

| Laboratorije    | Uvod | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod u Phi-3.5 Instruct  | Naučite kako da koristite Phi-3.5 Instruct sa Apple MLX frameworkom   |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (slike) | Naučite kako da koristite Phi-3.5 Vision za analizu slika sa Apple MLX frameworkom     |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (moE)   | Naučite kako da koristite Phi-3.5 MoE sa Apple MLX frameworkom  |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resursi**

1. Saznajte više o Apple MLX Framework-u [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква неспоразумевања или погрешна тумачења настала употребом овог превода.