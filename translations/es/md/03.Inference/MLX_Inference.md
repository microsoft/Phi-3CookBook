# **Inferencia Phi-3 con el Framework Apple MLX**

## **Qué es el Framework MLX**

MLX es un framework de arrays para investigación en aprendizaje automático en dispositivos Apple silicon, desarrollado por el equipo de investigación en aprendizaje automático de Apple.

MLX está diseñado por y para investigadores en aprendizaje automático. El framework busca ser fácil de usar, pero al mismo tiempo eficiente para entrenar y desplegar modelos. Su diseño es conceptualmente simple, con la intención de que los investigadores puedan extender y mejorar MLX fácilmente, facilitando la exploración rápida de nuevas ideas.

Los LLMs pueden ser acelerados en dispositivos Apple Silicon a través de MLX, y los modelos se pueden ejecutar localmente de manera muy conveniente.

## **Usando MLX para inferencia con Phi-3-mini**

### **1. Configura tu entorno MLX**

1. Python 3.11.x
2. Instalar la biblioteca MLX

```bash

pip install mlx-lm

```

### **2. Ejecutando Phi-3-mini en la Terminal con MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

El resultado (mi entorno es Apple M1 Max, 64GB) es

![Terminal](../../../../translated_images/01.5cb5f10f82619d0a98bc3584bf81264105a33d9d8559f125418a93b8d7527728.es.png)

### **3. Cuantizando Phi-3-mini con MLX en la Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Nota:*** El modelo se puede cuantizar mediante mlx_lm.convert, y la cuantización predeterminada es INT4. Este ejemplo cuantiza Phi-3-mini a INT4

El modelo se puede cuantizar mediante mlx_lm.convert, y la cuantización predeterminada es INT4. Este ejemplo cuantiza Phi-3-mini a INT4. Después de la cuantización, se almacenará en el directorio predeterminado ./mlx_model

Podemos probar el modelo cuantizado con MLX desde la terminal

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

El resultado es

![INT4](../../../../translated_images/02.6ca278966b75435a31021b0a6f1f3b377102d7e59e7b90daf8f017c1a9876cb2.es.png)

### **4. Ejecutando Phi-3-mini con MLX en Jupyter Notebook**

![Notebook](../../../../translated_images/03.5b701d4bfe17c5d20c075f7d4c8d1201b8073c8e8196b364a9a19cbe684dd26a.es.png)

***Nota:*** Por favor, lee este ejemplo [haz clic en este enlace](../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Recursos**

1. Aprende sobre el Framework Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Repositorio de Apple MLX en GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

Aviso legal: La traducción fue realizada a partir del original por un modelo de inteligencia artificial y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.