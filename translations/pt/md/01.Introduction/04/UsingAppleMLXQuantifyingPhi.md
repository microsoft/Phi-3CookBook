# **Quantizando o Phi-3.5 usando o Apple MLX Framework**

MLX é um framework de arrays para pesquisa em aprendizado de máquina no Apple Silicon, desenvolvido pela equipe de pesquisa em aprendizado de máquina da Apple.

O MLX foi projetado por pesquisadores de aprendizado de máquina para pesquisadores de aprendizado de máquina. O framework é feito para ser fácil de usar, mas ainda assim eficiente para treinar e implementar modelos. O design do framework também é conceitualmente simples. Nosso objetivo é facilitar para que pesquisadores estendam e melhorem o MLX, permitindo a exploração rápida de novas ideias.

Modelos de linguagem grande (LLMs) podem ser acelerados em dispositivos Apple Silicon através do MLX, e os modelos podem ser executados localmente de forma muito conveniente.

Atualmente, o Apple MLX Framework suporta a conversão de quantização do Phi-3.5-Instruct (**suporte ao Apple MLX Framework**), Phi-3.5-Vision (**suporte ao MLX-VLM Framework**) e Phi-3.5-MoE (**suporte ao Apple MLX Framework**). Vamos experimentar a seguir:

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

### **🤖 Exemplos para o Phi-3.5 com Apple MLX**

| Laboratórios | Introdução | Acesse |
| ------------ | ---------- | ------ |
| 🚀 Lab-Introdução ao Phi-3.5 Instruct  | Aprenda como usar o Phi-3.5 Instruct com o framework Apple MLX   |  [Acesse](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introdução ao Phi-3.5 Vision (imagem) | Aprenda como usar o Phi-3.5 Vision para analisar imagens com o framework Apple MLX     |  [Acesse](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introdução ao Phi-3.5 Vision (MoE)   | Aprenda como usar o Phi-3.5 MoE com o framework Apple MLX  |  [Acesse](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositório GitHub do Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositório GitHub do MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.