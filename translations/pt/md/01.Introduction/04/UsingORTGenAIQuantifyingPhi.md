# **Quantizando a Família Phi usando extensões de IA Generativa para onnxruntime**

## **O que são as extensões de IA Generativa para onnxruntime**

Essas extensões ajudam a executar IA generativa com ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Elas fornecem o loop de IA generativa para modelos ONNX, incluindo inferência com ONNX Runtime, processamento de logits, busca e amostragem, e gerenciamento de cache KV. Os desenvolvedores podem chamar um método de alto nível, generate(), ou executar cada iteração do modelo em um loop, gerando um token por vez e, opcionalmente, atualizando os parâmetros de geração dentro do loop. Há suporte para busca gulosa/beam search e amostragem TopP, TopK para gerar sequências de tokens, além de processamento de logits integrado, como penalidades por repetição. Também é fácil adicionar pontuações personalizadas.

No nível da aplicação, você pode usar as extensões de IA Generativa para onnxruntime para construir aplicações em C++/C#/Python. No nível do modelo, é possível usá-las para combinar modelos ajustados e realizar trabalhos relacionados ao deployment quantitativo.

## **Quantizando Phi-3.5 com extensões de IA Generativa para onnxruntime**

### **Modelos Suportados**

As extensões de IA Generativa para onnxruntime suportam a conversão quantizada dos modelos Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Model Builder nas extensões de IA Generativa para onnxruntime**

O Model Builder acelera significativamente a criação de modelos ONNX otimizados e quantizados que funcionam com a API generate() do ONNX Runtime.

Com o Model Builder, você pode quantizar o modelo para INT4, INT8, FP16, FP32 e combinar diferentes métodos de aceleração de hardware, como CPU, CUDA, DirectML, Mobile, entre outros.

Para usar o Model Builder, é necessário instalá-lo:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Após a instalação, você pode executar o script do Model Builder no terminal para realizar a conversão de formato e quantização do modelo.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Entenda os parâmetros relevantes:

1. **model_name** Este é o modelo no Hugging Face, como microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Também pode ser o caminho onde você armazenou o modelo.

2. **path_to_output_folder** Caminho onde será salva a conversão quantizada.

3. **execution_provider** Suporte para diferentes acelerações de hardware, como cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Fazemos o download do modelo do Hugging Face e o armazenamos localmente em cache.

***Nota:***

## **Como usar o Model Builder para quantizar Phi-3.5**

O Model Builder agora suporta a quantização de modelos ONNX para Phi-3.5 Instruct e Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversão quantizada INT 4 acelerada por CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversão quantizada INT 4 acelerada por CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configure o ambiente no terminal:

```bash

mkdir models

cd models 

```

2. Faça o download do modelo microsoft/Phi-3.5-vision-instruct na pasta models:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Faça o download destes arquivos para a pasta Phi-3.5-vision-instruct:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Baixe este arquivo para a pasta models:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. No terminal, converta o suporte ONNX com FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Nota:**

1. O Model Builder atualmente suporta a conversão de Phi-3.5-Instruct e Phi-3.5-Vision, mas não de Phi-3.5-MoE.

2. Para usar o modelo quantizado do ONNX, você pode utilizá-lo através do SDK das extensões de IA Generativa para onnxruntime.

3. É importante considerar práticas de IA responsável. Após a conversão de quantização do modelo, recomenda-se realizar testes mais eficazes nos resultados.

4. Ao quantizar o modelo CPU INT4, podemos implantá-lo em dispositivos de borda, o que oferece melhores cenários de aplicação. Por isso, concluímos a quantização do Phi-3.5-Instruct em INT4.

## **Recursos**

1. Saiba mais sobre as extensões de IA Generativa para onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Repositório no GitHub das extensões de IA Generativa para onnxruntime:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.