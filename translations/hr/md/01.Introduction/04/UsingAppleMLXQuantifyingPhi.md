# **Kvantizacija Phi-3.5 koristeći Apple MLX Framework**

MLX je okvir za istraživanje strojnog učenja na Apple Silicon uređajima, razvijen od strane Appleovog tima za istraživanje strojnog učenja.

MLX je osmišljen od strane istraživača strojnog učenja za istraživače strojnog učenja. Cilj okvira je biti jednostavan za korištenje, ali istovremeno učinkovit za treniranje i implementaciju modela. Dizajn samog okvira također je konceptualno jednostavan, s namjerom da istraživačima omogući lako proširivanje i unaprjeđivanje MLX-a radi bržeg istraživanja novih ideja.

LLM-ovi mogu biti ubrzani na Apple Silicon uređajima pomoću MLX-a, a modeli se mogu lokalno pokretati vrlo praktično.

Apple MLX Framework sada podržava kvantizacijsku konverziju za Phi-3.5-Instruct (**podrška za Apple MLX Framework**), Phi-3.5-Vision (**podrška za MLX-VLM Framework**) i Phi-3.5-MoE (**podrška za Apple MLX Framework**). Pogledajmo kako to funkcionira:

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

### **🤖 Primjeri za Phi-3.5 s Apple MLX**

| Laboratoriji    | Opis | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučite kako koristiti Phi-3.5 Instruct s Apple MLX okvirom   |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (slike) | Naučite kako koristiti Phi-3.5 Vision za analizu slika pomoću Apple MLX okvira     |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučite kako koristiti Phi-3.5 MoE s Apple MLX okvirom  |  [Idi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resursi**

1. Saznajte više o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorij [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću usluga strojnog prevođenja temeljenih na umjetnoj inteligenciji. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.