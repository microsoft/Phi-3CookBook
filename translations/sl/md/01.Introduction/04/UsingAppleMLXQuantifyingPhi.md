# **Kvantiacija Phi-3.5 z uporabo Apple MLX Frameworka**

MLX je ogrodje za delo s tabelami, namenjeno raziskavam strojnega učenja na Apple Silicon napravah, ki ga je razvila Appleova raziskovalna skupina za strojno učenje.

MLX je zasnovan s strani raziskovalcev strojnega učenja za raziskovalce strojnega učenja. Ogrodje je uporabniku prijazno, hkrati pa omogoča učinkovito treniranje in uvajanje modelov. Sama zasnova ogrodja je konceptualno preprosta. Naš cilj je raziskovalcem omogočiti enostavno razširitev in izboljšanje MLX, da bi lahko hitro preizkušali nove ideje.

LLM-je je mogoče pospešiti na napravah z Apple Silicon prek MLX, kar omogoča priročno lokalno izvajanje modelov.

Zdaj Apple MLX Framework podpira kvantizacijsko pretvorbo za Phi-3.5-Instruct (**podpora Apple MLX Frameworka**), Phi-3.5-Vision (**podpora MLX-VLM Frameworka**) in Phi-3.5-MoE (**podpora Apple MLX Frameworka**). Poskusimo naslednje:

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

### **🤖 Primeri za Phi-3.5 z Apple MLX**

| Laboratoriji | Opis | Pojdi |
| ------------ | ----- | ----- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučite se uporabljati Phi-3.5 Instruct z ogrodjem Apple MLX   |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (slike) | Naučite se uporabljati Phi-3.5 Vision za analizo slik z ogrodjem Apple MLX     |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Naučite se uporabljati Phi-3.5 MoE z ogrodjem Apple MLX  |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Viri**

1. Več o Apple MLX Frameworku [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub repozitorij [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub repozitorij [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo strojnih prevajalskih storitev na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.