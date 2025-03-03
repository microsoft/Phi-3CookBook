# **Pagku-quantize ng Phi-3.5 gamit ang Apple MLX Framework**

Ang MLX ay isang array framework para sa pananaliksik sa machine learning sa Apple silicon, na dinala sa inyo ng Apple machine learning research.

Ang MLX ay dinisenyo ng mga mananaliksik ng machine learning para sa kapwa mananaliksik. Ang framework na ito ay nilalayong maging user-friendly ngunit nananatiling epektibo para sa pag-train at pag-deploy ng mga modelo. Ang disenyo ng framework ay konseptwal na simple rin. Layunin naming gawing madali para sa mga mananaliksik na palawakin at pagandahin ang MLX upang mabilis na makapagsaliksik ng mga bagong ideya.

Ang mga LLM ay maaaring mapabilis sa mga Apple Silicon device gamit ang MLX, at ang mga modelo ay madaling mapatakbo nang lokal.

Ngayon, sinusuportahan na ng Apple MLX Framework ang conversion ng quantization para sa Phi-3.5-Instruct(**Suporta ng Apple MLX Framework**), Phi-3.5-Vision(**Suporta ng MLX-VLM Framework**), at Phi-3.5-MoE(**Suporta ng Apple MLX Framework**). Subukan natin ito ngayon:

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

### **🤖 Mga Halimbawa para sa Phi-3.5 gamit ang Apple MLX**

| Mga Lab    | Introduksyon | Pumunta |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Alamin kung paano gamitin ang Phi-3.5 Instruct gamit ang Apple MLX framework   |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Alamin kung paano gamitin ang Phi-3.5 Vision para mag-analyze ng mga imahe gamit ang Apple MLX framework     |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Alamin kung paano gamitin ang Phi-3.5 MoE gamit ang Apple MLX framework  |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Mga Mapagkukunan**

1. Alamin ang tungkol sa Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Rep [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI-based na pagsasalin. Bagama't pinagsisikapan naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot sa anumang maling pagkaunawa o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.