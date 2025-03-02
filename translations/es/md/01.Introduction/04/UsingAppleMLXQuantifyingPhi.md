# **Cuantización de Phi-3.5 usando el Framework Apple MLX**

MLX es un framework de arrays para la investigación en aprendizaje automático en dispositivos Apple Silicon, desarrollado por el equipo de investigación de aprendizaje automático de Apple.

MLX está diseñado por y para investigadores en aprendizaje automático. El framework busca ser fácil de usar, pero al mismo tiempo eficiente para entrenar y desplegar modelos. Su diseño es conceptualmente simple, lo que facilita a los investigadores extender y mejorar MLX con el objetivo de explorar nuevas ideas rápidamente.

Los modelos de lenguaje de gran escala (LLMs) pueden acelerarse en dispositivos Apple Silicon mediante MLX, y los modelos pueden ejecutarse localmente de manera muy conveniente.

Ahora el Framework Apple MLX admite la conversión con cuantización de Phi-3.5-Instruct (**soporte del Framework Apple MLX**), Phi-3.5-Vision (**soporte del Framework MLX-VLM**) y Phi-3.5-MoE (**soporte del Framework Apple MLX**). Probémoslo a continuación:

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

### **🤖 Ejemplos para Phi-3.5 con Apple MLX**

| Laboratorios    | Introducción | Ir |
| -------- | ------- |  ------- |
| 🚀 Lab-Introducción a Phi-3.5 Instruct  | Aprende a usar Phi-3.5 Instruct con el framework Apple MLX   |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introducción a Phi-3.5 Vision (imagen) | Aprende a usar Phi-3.5 Vision para analizar imágenes con el framework Apple MLX     |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introducción a Phi-3.5 Vision (moE)   | Aprende a usar Phi-3.5 MoE con el framework Apple MLX  |  [Ir](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Recursos**

1. Aprende sobre el Framework Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repositorio GitHub de Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repositorio GitHub de MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.