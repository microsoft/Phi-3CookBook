# Lab. Otimize modelos de IA para inferência em dispositivos

## Introdução 

> [!IMPORTANT]
> Este laboratório requer uma **GPU Nvidia A10 ou A100** com drivers associados e toolkit CUDA (versão 12+) instalados.

> [!NOTE]
> Este é um laboratório de **35 minutos** que oferece uma introdução prática aos conceitos principais de otimização de modelos para inferência em dispositivos usando o OLIVE.

## Objetivos de Aprendizado

Ao final deste laboratório, você será capaz de usar o OLIVE para:

- Quantizar um modelo de IA utilizando o método de quantização AWQ.
- Ajustar um modelo de IA para uma tarefa específica.
- Gerar adaptadores LoRA (modelo ajustado) para inferência eficiente em dispositivos com o ONNX Runtime.

### O que é o Olive

Olive (*O*NNX *live*) é uma ferramenta de otimização de modelos com uma interface de linha de comando (CLI) que permite a entrega de modelos para o ONNX runtime +++https://onnxruntime.ai+++ com qualidade e desempenho.

![Fluxo do Olive](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.pt.png)

A entrada para o Olive é geralmente um modelo PyTorch ou Hugging Face, e a saída é um modelo ONNX otimizado, que é executado em um dispositivo (alvo de implantação) rodando o ONNX runtime. O Olive otimiza o modelo para o acelerador de IA do alvo de implantação (NPU, GPU, CPU) fornecido por um fornecedor de hardware como Qualcomm, AMD, Nvidia ou Intel.

O Olive executa um *workflow*, que é uma sequência ordenada de tarefas individuais de otimização de modelo chamadas *passes* - exemplos de passes incluem: compressão de modelo, captura de grafo, quantização, otimização de grafo. Cada passe possui um conjunto de parâmetros que podem ser ajustados para alcançar as melhores métricas, como precisão e latência, avaliadas pelo respectivo avaliador. O Olive utiliza uma estratégia de busca que emprega um algoritmo de busca para ajustar automaticamente cada passe individualmente ou em conjunto.

#### Benefícios do Olive

- **Reduzir frustração e tempo** de experimentação manual por tentativa e erro com diferentes técnicas de otimização de grafo, compressão e quantização. Defina suas restrições de qualidade e desempenho e deixe o Olive encontrar automaticamente o melhor modelo para você.
- **Mais de 40 componentes de otimização de modelo integrados** cobrindo técnicas de ponta em quantização, compressão, otimização de grafo e ajuste fino.
- **CLI fácil de usar** para tarefas comuns de otimização de modelos. Por exemplo, olive quantize, olive auto-opt, olive finetune.
- Embalagem e implantação de modelos integradas.
- Suporte para geração de modelos para **Multi LoRA serving**.
- Construção de workflows usando YAML/JSON para orquestrar tarefas de otimização e implantação de modelos.
- Integração com **Hugging Face** e **Azure AI**.
- Mecanismo de **cache** embutido para **economizar custos**.

## Instruções do Laboratório
> [!NOTE]
> Certifique-se de ter provisionado seu Azure AI Hub e Projeto e configurado seu recurso de computação A100 conforme o Laboratório 1.

### Etapa 0: Conecte-se ao seu Azure AI Compute

Você se conectará ao recurso de computação Azure AI usando o recurso remoto no **VS Code.** 

1. Abra o aplicativo desktop **VS Code**:
1. Abra o **command palette** usando **Shift+Ctrl+P**
1. No command palette, procure por **AzureML - remote: Connect to compute instance in New Window**.
1. Siga as instruções na tela para conectar-se ao recurso de computação. Isso envolverá selecionar sua Assinatura Azure, Grupo de Recursos, Projeto e Nome do Recurso de Computação configurados no Laboratório 1.
1. Depois de conectado ao nó de computação do Azure ML, isso será exibido no **canto inferior esquerdo do Visual Code** `><Azure ML: Compute Name`

### Etapa 1: Clone este repositório

No VS Code, você pode abrir um novo terminal com **Ctrl+J** e clonar este repositório:

No terminal, você verá o prompt

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone a solução 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Etapa 2: Abra a pasta no VS Code

Para abrir o VS Code na pasta relevante, execute o seguinte comando no terminal, que abrirá uma nova janela:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativamente, você pode abrir a pasta selecionando **File** > **Open Folder**. 

### Etapa 3: Dependências

Abra uma janela de terminal no VS Code no seu Azure AI Compute Instance (dica: **Ctrl+J**) e execute os seguintes comandos para instalar as dependências:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> A instalação de todas as dependências levará cerca de ~5 minutos.

Neste laboratório, você fará download e upload de modelos para o catálogo de modelos do Azure AI. Para acessar o catálogo de modelos, será necessário fazer login no Azure usando:

```bash
az login
```

> [!NOTE]
> Durante o login, será solicitado que você selecione sua assinatura. Certifique-se de configurar a assinatura para a fornecida neste laboratório.

### Etapa 4: Execute os comandos do Olive 

Abra uma janela de terminal no VS Code no seu Azure AI Compute Instance (dica: **Ctrl+J**) e certifique-se de que o ambiente conda `olive-ai` esteja ativado:

```bash
conda activate olive-ai
```

Em seguida, execute os seguintes comandos do Olive na linha de comando.

1. **Inspecione os dados:** Neste exemplo, você ajustará o modelo Phi-3.5-Mini para que ele seja especializado em responder a perguntas relacionadas a viagens. O código abaixo exibe os primeiros registros do conjunto de dados, que estão no formato JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Quantize o modelo:** Antes de treinar o modelo, você primeiro o quantiza com o seguinte comando que utiliza uma técnica chamada Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ quantiza os pesos de um modelo considerando as ativações produzidas durante a inferência. Isso significa que o processo de quantização leva em conta a distribuição real dos dados nas ativações, resultando em uma melhor preservação da precisão do modelo em comparação com métodos tradicionais de quantização de pesos.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    O processo de quantização AWQ leva **~8 minutos** para ser concluído, o que **reduzirá o tamanho do modelo de ~7,5GB para ~2,5GB**.
   
   Neste laboratório, mostramos como inserir modelos do Hugging Face (por exemplo: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` comando ajusta o modelo quantizado. Quantizar o modelo *antes* do ajuste fino, em vez de depois, oferece melhor precisão, pois o processo de ajuste fino recupera parte da perda da quantização.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    O ajuste fino (com 100 etapas) leva **~6 minutos** para ser concluído.

1. **Otimize:** Com o modelo treinado, agora você otimiza o modelo usando o argumento `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` do Olive - mas, para os fins deste laboratório, usaremos CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    A otimização leva **~5 minutos** para ser concluída.

### Etapa 5: Teste rápido de inferência do modelo

Para testar a inferência do modelo, crie um arquivo Python na sua pasta chamado **app.py** e copie e cole o seguinte código:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Execute o código usando:

```bash
python app.py
```

### Etapa 6: Faça upload do modelo para o Azure AI

Fazer upload do modelo para um repositório de modelos do Azure AI torna o modelo compartilhável com outros membros da sua equipe de desenvolvimento e também gerencia o controle de versão do modelo. Para fazer upload do modelo, execute o seguinte comando:

> [!NOTE]
> Atualize os campos `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` e o nome do Projeto Azure AI, e execute o seguinte comando 

```
az ml workspace show
```

Ou acessando +++ai.azure.com+++ e selecionando **management center** **project** **overview**

Atualize os `{}` com o nome do seu grupo de recursos e do Projeto Azure AI.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Você poderá então ver seu modelo carregado e implantá-lo em https://ml.azure.com/model/list

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.