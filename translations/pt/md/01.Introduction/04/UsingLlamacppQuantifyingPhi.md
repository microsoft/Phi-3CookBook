# **Quantizando a Família Phi usando o llama.cpp**

## **O que é o llama.cpp**

llama.cpp é uma biblioteca de software de código aberto, escrita principalmente em C++, que realiza inferência em diversos Modelos de Linguagem de Grande Escala (LLMs), como o Llama. Seu principal objetivo é oferecer desempenho de ponta para inferência de LLMs em uma ampla gama de hardwares com configuração mínima. Além disso, há bindings em Python disponíveis para essa biblioteca, que fornecem uma API de alto nível para completar textos e um servidor web compatível com OpenAI.

O objetivo principal do llama.cpp é possibilitar a inferência de LLMs com configuração mínima e desempenho de ponta em uma grande variedade de hardwares - localmente e na nuvem.

- Implementação em C/C++ puro sem dependências
- Apple silicon é uma prioridade - otimizado via ARM NEON, frameworks Accelerate e Metal
- Suporte a AVX, AVX2 e AVX512 para arquiteturas x86
- Quantização de inteiros em 1,5 bits, 2 bits, 3 bits, 4 bits, 5 bits, 6 bits e 8 bits para inferência mais rápida e menor uso de memória
- Kernels CUDA personalizados para executar LLMs em GPUs NVIDIA (suporte para GPUs AMD via HIP)
- Suporte para backend Vulkan e SYCL
- Inferência híbrida CPU+GPU para acelerar parcialmente modelos maiores do que a capacidade total de VRAM

## **Quantizando Phi-3.5 com o llama.cpp**

O modelo Phi-3.5-Instruct pode ser quantizado usando o llama.cpp, mas os modelos Phi-3.5-Vision e Phi-3.5-MoE ainda não são suportados. O formato convertido pelo llama.cpp é o gguf, que também é o formato de quantização mais amplamente utilizado.

Há um grande número de modelos no formato GGUF quantizado no Hugging Face. AI Foundry, Ollama e LlamaEdge dependem do llama.cpp, então os modelos GGUF também são frequentemente utilizados.

### **O que é GGUF**

GGUF é um formato binário otimizado para carregamento e salvamento rápidos de modelos, tornando-o altamente eficiente para fins de inferência. GGUF é projetado para uso com GGML e outros executores. GGUF foi desenvolvido por @ggerganov, que também é o desenvolvedor do llama.cpp, um framework popular de inferência de LLM em C/C++. Modelos inicialmente desenvolvidos em frameworks como PyTorch podem ser convertidos para o formato GGUF para uso com esses motores.

### **ONNX vs GGUF**

ONNX é um formato tradicional de aprendizado de máquina/aprendizado profundo, bem suportado em diferentes frameworks de IA e com bons cenários de uso em dispositivos de borda. Quanto ao GGUF, ele é baseado no llama.cpp e pode ser considerado um produto da era do GenAI. Os dois têm usos semelhantes. Se você busca melhor desempenho em hardware embarcado e camadas de aplicação, o ONNX pode ser sua escolha. Se você utiliza o framework e a tecnologia derivados do llama.cpp, então o GGUF pode ser mais adequado.

### **Quantização do Phi-3.5-Instruct usando o llama.cpp**

**1. Configuração do Ambiente**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantização**

Usando o llama.cpp para converter o Phi-3.5-Instruct para FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizando o Phi-3.5 para INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testando**

Instale o llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Se você utiliza Apple Silicon, instale o llama-cpp-python desta forma


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testando 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Recursos**

1. Saiba mais sobre o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Saiba mais sobre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.