# **Kuantisha Phi-3.5 kwa kutumia Mfumo wa Apple MLX**

MLX ni mfumo wa safu wa utafiti wa kujifunza kwa mashine kwenye vifaa vya Apple silicon, ulioletwa kwako na utafiti wa kujifunza kwa mashine wa Apple.

MLX umetengenezwa na watafiti wa kujifunza kwa mashine kwa ajili ya watafiti wa kujifunza kwa mashine. Mfumo huu umekusudiwa kuwa rahisi kutumia, lakini bado ufanisi wa kufundisha na kupeleka mifano. Muundo wa mfumo wenyewe pia ni rahisi kueleweka. Tunakusudia kuwafanya watafiti waendelee na kuboresha MLX kwa urahisi kwa lengo la kuchunguza haraka mawazo mapya.

LLMs zinaweza kuharakishwa kwenye vifaa vya Apple Silicon kupitia MLX, na mifano inaweza kuendeshwa kwa urahisi ndani ya kifaa.

Sasa Mfumo wa Apple MLX unasaidia ubadilishaji wa kuquantisha wa Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), na Phi-3.5-MoE(**Apple MLX Framework support**). Hebu tujaribu ifuatayo:

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

### **🤖 Sampuli za Phi-3.5 na Apple MLX**

| Maabara    | Utangulizi | Nenda |
| -------- | ------- |  ------- |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Instruct  | Jifunze jinsi ya kutumia Phi-3.5 Instruct na mfumo wa Apple MLX   |  [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Vision (picha) | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchanganua picha kwa mfumo wa Apple MLX     |  [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Vision (moE)   | Jifunze jinsi ya kutumia Phi-3.5 MoE na mfumo wa Apple MLX  |  [Nenda](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Rasilimali**

1. Jifunze kuhusu Mfumo wa Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Rejesta ya GitHub ya Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Rejesta ya GitHub ya MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokamilika. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo rasmi. Kwa maelezo muhimu, inashauriwa kutumia huduma za wataalamu wa tafsiri ya kibinadamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.