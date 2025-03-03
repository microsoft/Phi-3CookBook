# **Ajustando o Phi-3 com LoRA**

Ajuste fino do modelo de linguagem Phi-3 Mini da Microsoft usando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) em um conjunto de dados personalizado de instruções de chat.

O LoRA ajudará a melhorar a compreensão conversacional e a geração de respostas.

## Guia passo a passo para ajustar o Phi-3 Mini:

**Importações e Configuração**

Instalando loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Comece importando as bibliotecas necessárias, como datasets, transformers, peft, trl e torch. Configure o log para acompanhar o processo de treinamento.

Você pode optar por adaptar algumas camadas substituindo-as por equivalentes implementados no loralib. No momento, suportamos apenas nn.Linear, nn.Embedding e nn.Conv2d. Também suportamos um MergedLinear para casos em que um único nn.Linear representa mais de uma camada, como em algumas implementações da projeção de atenção qkv (veja Notas Adicionais para mais detalhes).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Antes de o loop de treinamento começar, marque apenas os parâmetros do LoRA como treináveis.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ao salvar um checkpoint, gere um state_dict que contenha apenas os parâmetros do LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Ao carregar um checkpoint usando load_state_dict, certifique-se de definir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Agora o treinamento pode prosseguir normalmente.

**Hiperparâmetros**

Defina dois dicionários: training_config e peft_config. training_config inclui hiperparâmetros para o treinamento, como taxa de aprendizado, tamanho do lote e configurações de log.

peft_config especifica parâmetros relacionados ao LoRA, como rank, dropout e tipo de tarefa.

**Carregamento do Modelo e Tokenizer**

Especifique o caminho para o modelo Phi-3 pré-treinado (por exemplo, "microsoft/Phi-3-mini-4k-instruct"). Configure as definições do modelo, incluindo uso de cache, tipo de dado (bfloat16 para precisão mista) e implementação de atenção.

**Treinamento**

Ajuste fino do modelo Phi-3 usando o conjunto de dados personalizado de instruções de chat. Utilize as configurações do LoRA do peft_config para uma adaptação eficiente. Monitore o progresso do treinamento usando a estratégia de log especificada.  
Avaliação e Salvamento: Avalie o modelo ajustado.  
Salve checkpoints durante o treinamento para uso posterior.

**Exemplos**
- [Saiba mais com este notebook de exemplo](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplo de Script de Ajuste Fino em Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemplo de Ajuste Fino no Hugging Face Hub com LoRA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemplo de Model Card no Hugging Face - Ajuste Fino com LoRA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemplo de Ajuste Fino no Hugging Face Hub com QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automatizada por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.