# Ajustar o Phi3 usando Olive

Neste exemplo, você usará o Olive para:

1. Ajustar um adaptador LoRA para classificar frases em Sad, Joy, Fear, Surprise.
1. Mesclar os pesos do adaptador ao modelo base.
1. Otimizar e quantizar o modelo em `int4`.

Também mostraremos como realizar inferências no modelo ajustado usando a API Generate do ONNX Runtime (ORT).

> **⚠️ Para o ajuste, você precisará de uma GPU adequada - por exemplo, A10, V100, A100.**

## 💾 Instalar

Crie um novo ambiente virtual Python (por exemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Em seguida, instale o Olive e as dependências necessárias para o fluxo de trabalho de ajuste:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar o Phi3 usando Olive
O [arquivo de configuração do Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contém um *workflow* com os seguintes *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

De forma geral, este fluxo de trabalho irá:

1. Ajustar o Phi3 (por 150 etapas, que você pode modificar) usando os dados de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Mesclar os pesos do adaptador LoRA ao modelo base. Isso resultará em um único artefato de modelo no formato ONNX.
1. O Model Builder otimizará o modelo para o ONNX Runtime *e* quantizará o modelo em `int4`.

Para executar o fluxo de trabalho, execute:

```bash
olive run --config phrase-classification.json
```

Quando o Olive finalizar, seu modelo Phi3 ajustado e otimizado em `int4` estará disponível em: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar o Phi3 ajustado ao seu aplicativo 

Para executar o aplicativo:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A resposta deve ser uma única palavra classificando a frase (Sad/Joy/Fear/Surprise).

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.