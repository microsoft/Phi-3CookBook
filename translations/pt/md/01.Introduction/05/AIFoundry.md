# **Usando o Azure AI Foundry para avaliação**

![aistudo](../../../../../translated_images/AIFoundry.61da8c74bccc0241ce9a4cb53a170912245871de9235043afcb796ccbc076fdc.pt.png)

Como avaliar sua aplicação de IA generativa usando o [Azure AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo). Seja avaliando conversas de turno único ou múltiplos turnos, o Azure AI Foundry oferece ferramentas para avaliar o desempenho e a segurança do modelo. 

![aistudo](../../../../../translated_images/AIPortfolio.5aaa2b25e9157624a4542fe041d66a96a1c1ec6007e4e5aadd926c6ec8ce18b3.pt.png)

## Como avaliar aplicativos de IA generativa com o Azure AI Foundry
Para instruções mais detalhadas, consulte a [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo).

Aqui estão os passos para começar:

## Avaliando Modelos de IA Generativa no Azure AI Foundry

**Pré-requisitos**

- Um conjunto de dados de teste no formato CSV ou JSON.
- Um modelo de IA generativa implantado (como Phi-3, GPT 3.5, GPT 4 ou modelos Davinci).
- Um runtime com uma instância de computação para executar a avaliação.

## Métricas de Avaliação Integradas

O Azure AI Foundry permite avaliar tanto conversas de turno único quanto conversas complexas de múltiplos turnos.  
Para cenários de Recuperação com Geração Aumentada (RAG), onde o modelo é fundamentado em dados específicos, é possível avaliar o desempenho usando métricas de avaliação integradas.  
Além disso, você pode avaliar cenários gerais de perguntas e respostas de turno único (não-RAG).

## Criando uma Execução de Avaliação

Na interface do Azure AI Foundry, navegue até a página Evaluate ou Prompt Flow.  
Siga o assistente de criação de avaliação para configurar uma execução de avaliação. Forneça um nome opcional para sua avaliação.  
Selecione o cenário que se alinha com os objetivos da sua aplicação.  
Escolha uma ou mais métricas de avaliação para analisar a saída do modelo.

## Fluxo de Avaliação Personalizado (Opcional)

Para maior flexibilidade, é possível criar um fluxo de avaliação personalizado. Personalize o processo de avaliação com base nos seus requisitos específicos.

## Visualizando Resultados

Após executar a avaliação, registre, visualize e analise métricas de avaliação detalhadas no Azure AI Foundry. Obtenha insights sobre as capacidades e limitações da sua aplicação.



**Nota** O Azure AI Foundry está atualmente em versão prévia pública, portanto, use-o para fins de experimentação e desenvolvimento. Para cargas de trabalho em produção, considere outras opções. Explore a [documentação oficial do AI Foundry](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) para mais detalhes e instruções passo a passo.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática por IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.