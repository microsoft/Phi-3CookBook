# **Quantification de la famille Phi avec llama.cpp**

## **Qu'est-ce que llama.cpp ?**

llama.cpp est une bibliothèque logicielle open-source principalement écrite en C++ qui effectue des inférences sur divers grands modèles de langage (LLMs), comme Llama. Son principal objectif est d'offrir des performances de pointe pour l'inférence de LLM sur une large gamme de matériel avec une configuration minimale. De plus, des liaisons Python sont disponibles pour cette bibliothèque, fournissant une API de haut niveau pour la complétion de texte et un serveur web compatible OpenAI.

L'objectif principal de llama.cpp est de permettre une inférence LLM avec une configuration minimale et des performances de pointe sur une grande variété de matériel, localement et dans le cloud.

- Implémentation en C/C++ pure sans aucune dépendance
- Apple Silicon est un citoyen de première classe - optimisé via ARM NEON, Accelerate et Metal frameworks
- Prise en charge de AVX, AVX2 et AVX512 pour les architectures x86
- Quantification entière en 1,5 bit, 2 bits, 3 bits, 4 bits, 5 bits, 6 bits et 8 bits pour une inférence plus rapide et une utilisation réduite de la mémoire
- Kernels CUDA personnalisés pour exécuter des LLM sur des GPU NVIDIA (prise en charge des GPU AMD via HIP)
- Prise en charge des backends Vulkan et SYCL
- Inférence hybride CPU+GPU pour accélérer partiellement les modèles plus grands que la capacité totale de VRAM

## **Quantification de Phi-3.5 avec llama.cpp**

Le modèle Phi-3.5-Instruct peut être quantifié à l'aide de llama.cpp, mais Phi-3.5-Vision et Phi-3.5-MoE ne sont pas encore pris en charge. Le format converti par llama.cpp est gguf, qui est également le format de quantification le plus largement utilisé.

Il existe un grand nombre de modèles au format GGUF quantifié sur Hugging Face. AI Foundry, Ollama et LlamaEdge reposent sur llama.cpp, c'est pourquoi les modèles GGUF sont également souvent utilisés.

### **Qu'est-ce que GGUF ?**

GGUF est un format binaire optimisé pour un chargement et une sauvegarde rapides des modèles, ce qui le rend très efficace pour les inférences. GGUF est conçu pour être utilisé avec GGML et d'autres exécutants. GGUF a été développé par @ggerganov, qui est également le développeur de llama.cpp, un cadre d'inférence LLM populaire en C/C++. Les modèles initialement développés dans des frameworks comme PyTorch peuvent être convertis au format GGUF pour être utilisés avec ces moteurs.

### **ONNX vs GGUF**

ONNX est un format traditionnel d'apprentissage machine/apprentissage profond, bien pris en charge dans différents frameworks d'IA et offrant de bons cas d'utilisation sur les dispositifs en périphérie. Quant à GGUF, il est basé sur llama.cpp et peut être considéré comme produit à l'ère de la génération d'IA (GenAI). Les deux ont des usages similaires. Si vous recherchez de meilleures performances sur du matériel embarqué et dans des couches applicatives, ONNX peut être votre choix. Si vous utilisez le cadre et la technologie dérivés de llama.cpp, alors GGUF pourrait être préférable.

### **Quantification de Phi-3.5-Instruct avec llama.cpp**

**1. Configuration de l'environnement**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantification**

Utilisation de llama.cpp pour convertir Phi-3.5-Instruct en FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantification de Phi-3.5 en INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test**

Installation de llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Remarque*** 

Si vous utilisez Apple Silicon, installez llama-cpp-python comme suit :


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressources**

1. En savoir plus sur llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. En savoir plus sur GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.