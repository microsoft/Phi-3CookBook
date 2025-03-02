# Ajustar o Phi3 usando Olive

Neste exemplo, você usará o Olive para:

1. Ajustar um adaptador LoRA para classificar frases como Tristeza, Alegria, Medo ou Surpresa.
1. Mesclar os pesos do adaptador ao modelo base.
1. Otimizar e Quantizar o modelo em `int4`.

Também mostraremos como realizar inferências com o modelo ajustado usando a API Generate do ONNX Runtime (ORT).

> **⚠️ Para o ajuste fino, você precisará de uma GPU adequada disponível - por exemplo, uma A10, V100, A100.**

## 💾 Instalar

Crie um novo ambiente virtual Python (por exemplo, usando `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Em seguida, instale o Olive e as dependências para um fluxo de trabalho de ajuste fino:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajustar o Phi3 usando Olive

O [arquivo de configuração do Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) contém um *workflow* com os seguintes *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Em um nível geral, este fluxo de trabalho fará o seguinte:

1. Ajustará o Phi3 (por 150 etapas, que você pode modificar) usando os dados do arquivo [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Mesclará os pesos do adaptador LoRA ao modelo base. Isso resultará em um único artefato de modelo no formato ONNX.
1. O Model Builder otimizará o modelo para o runtime ONNX *e* quantizará o modelo em `int4`.

Para executar o fluxo de trabalho, rode:

```bash
olive run --config phrase-classification.json
```

Quando o Olive terminar, o modelo Phi3 ajustado e otimizado em `int4` estará disponível em: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrar o Phi3 ajustado em sua aplicação

Para executar o aplicativo:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A resposta deve ser uma classificação de uma única palavra para a frase (Tristeza/Alegria/Medo/Surpresa).

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.