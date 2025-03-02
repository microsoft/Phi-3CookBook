# Usando GPU do Windows para criar uma solução Prompt flow com Phi-3.5-Instruct ONNX

O documento a seguir é um exemplo de como usar o PromptFlow com ONNX (Open Neural Network Exchange) para desenvolver aplicações de IA baseadas nos modelos Phi-3.

O PromptFlow é um conjunto de ferramentas de desenvolvimento projetado para simplificar o ciclo de desenvolvimento de ponta a ponta de aplicações de IA baseadas em LLMs (Large Language Models), desde a concepção e prototipagem até os testes e avaliação.

Ao integrar o PromptFlow com ONNX, os desenvolvedores podem:

- **Otimizar o desempenho do modelo**: Usar o ONNX para inferência e implantação eficientes do modelo.
- **Simplificar o desenvolvimento**: Utilizar o PromptFlow para gerenciar o fluxo de trabalho e automatizar tarefas repetitivas.
- **Melhorar a colaboração**: Facilitar a colaboração entre os membros da equipe, fornecendo um ambiente de desenvolvimento unificado.

**Prompt flow** é um conjunto de ferramentas de desenvolvimento projetado para simplificar o ciclo de desenvolvimento de ponta a ponta de aplicações de IA baseadas em LLM, desde a concepção, prototipagem, testes, avaliação até a implantação e monitoramento em produção. Ele torna a engenharia de prompts muito mais fácil e permite que você construa aplicações LLM com qualidade de produção.

O Prompt flow pode se conectar ao OpenAI, Azure OpenAI Service e modelos personalizáveis (Huggingface, LLM/SLM locais). Nosso objetivo é implantar o modelo ONNX quantizado do Phi-3.5 em aplicações locais. O Prompt flow pode nos ajudar a planejar melhor nossos negócios e a criar soluções locais baseadas no Phi-3.5. Neste exemplo, combinaremos a biblioteca GenAI do ONNX Runtime para concluir a solução Prompt flow baseada na GPU do Windows.

## **Instalação**

### **ONNX Runtime GenAI para GPU do Windows**

Leia este guia para configurar o ONNX Runtime GenAI para GPU do Windows [clique aqui](./ORTWindowGPUGuideline.md)

### **Configurar o Prompt flow no VSCode**

1. Instale a extensão Prompt flow para o VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.pt.png)

2. Após instalar a extensão Prompt flow para o VS Code, clique na extensão e escolha **Installation dependencies**. Siga este guia para instalar o SDK do Prompt flow no seu ambiente.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.pt.png)

3. Baixe o [Código de Exemplo](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) e use o VS Code para abrir este exemplo.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.pt.png)

4. Abra o arquivo **flow.dag.yaml** para escolher o ambiente Python.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.pt.png)

   Abra o arquivo **chat_phi3_ort.py** para alterar a localização do modelo Phi-3.5-instruct ONNX.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.pt.png)

5. Execute seu Prompt flow para testar.

Abra o arquivo **flow.dag.yaml** e clique no editor visual.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.pt.png)

Depois de clicar, execute-o para testar.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.pt.png)

1. Você pode executar em lote no terminal para verificar mais resultados.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Você pode verificar os resultados no seu navegador padrão.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.pt.png)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.