# **Quantification de Phi-3.5 avec le Framework Apple MLX**

MLX est un framework matriciel pour la recherche en apprentissage automatique sur les puces Apple Silicon, développé par l'équipe de recherche en apprentissage automatique d'Apple.

MLX est conçu par des chercheurs en apprentissage automatique pour des chercheurs en apprentissage automatique. Ce framework se veut convivial tout en restant efficace pour entraîner et déployer des modèles. Sa conception est également volontairement simple sur le plan conceptuel. Nous souhaitons faciliter l'extension et l'amélioration de MLX par les chercheurs afin d'explorer rapidement de nouvelles idées.

Les LLM peuvent être accélérés sur les appareils équipés d'Apple Silicon grâce à MLX, permettant d'exécuter les modèles localement de manière très pratique.

Le Framework Apple MLX prend désormais en charge la conversion par quantification de Phi-3.5-Instruct (**prise en charge par le Framework Apple MLX**), Phi-3.5-Vision (**prise en charge par le Framework MLX-VLM**) et Phi-3.5-MoE (**prise en charge par le Framework Apple MLX**). Passons à l'essai :

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

### **🤖 Exemples pour Phi-3.5 avec Apple MLX**

| Labs    | Présentation | Aller |
| -------- | ------- |  ------- |
| 🚀 Lab-Présentation Phi-3.5 Instruct  | Découvrez comment utiliser Phi-3.5 Instruct avec le framework Apple MLX   |  [Aller](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (image) | Découvrez comment utiliser Phi-3.5 Vision pour analyser des images avec le framework Apple MLX     |  [Aller](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Présentation Phi-3.5 Vision (moE)   | Découvrez comment utiliser Phi-3.5 MoE avec le framework Apple MLX  |  [Aller](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Ressources**

1. En savoir plus sur le Framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Dépôt GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Dépôt GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.