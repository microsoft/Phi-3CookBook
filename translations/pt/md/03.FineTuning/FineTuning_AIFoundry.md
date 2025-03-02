# Ajustando o Phi-3 com o Azure AI Foundry

Vamos explorar como ajustar o modelo de linguagem Phi-3 Mini da Microsoft usando o Azure AI Foundry. O ajuste fino permite adaptar o Phi-3 Mini a tarefas específicas, tornando-o ainda mais poderoso e consciente do contexto.

## Considerações

- **Capacidades:** Quais modelos podem ser ajustados? O que o modelo base pode fazer após o ajuste?
- **Custo:** Qual é o modelo de precificação para ajuste fino?
- **Personalização:** Até que ponto posso modificar o modelo base – e de que maneiras?
- **Praticidade:** Como o ajuste fino realmente funciona – preciso escrever código personalizado? Preciso trazer minha própria infraestrutura?
- **Segurança:** Modelos ajustados podem apresentar riscos de segurança – existem proteções para evitar danos não intencionais?

![Modelos AIFoundry](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.pt.png)

## Preparação para o ajuste fino

### Pré-requisitos

> [!NOTE]
> Para os modelos da família Phi-3, o modelo de ajuste fino pay-as-you-go está disponível apenas em hubs criados na região **East US 2**.

- Uma assinatura do Azure. Se você não tem uma assinatura, crie uma [conta paga do Azure](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) para começar.

- Um [projeto do AI Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Controles de acesso baseados em função do Azure (Azure RBAC) são usados para conceder acesso às operações no Azure AI Foundry. Para realizar os passos deste artigo, sua conta de usuário deve ter o papel __Azure AI Developer__ no grupo de recursos.

### Registro do provedor de assinatura

Verifique se a assinatura está registrada no provedor de recursos `Microsoft.Network`.

1. Faça login no [portal do Azure](https://portal.azure.com).
1. Selecione **Assinaturas** no menu à esquerda.
1. Escolha a assinatura que deseja usar.
1. Clique em **Configurações do projeto de IA** > **Provedores de recursos** no menu à esquerda.
1. Confirme que **Microsoft.Network** está na lista de provedores de recursos. Caso contrário, adicione-o.

### Preparação dos dados

Prepare seus dados de treinamento e validação para ajustar o modelo. Seus conjuntos de dados de treinamento e validação devem conter exemplos de entrada e saída que representem como você deseja que o modelo funcione.

Certifique-se de que todos os exemplos de treinamento sigam o formato esperado para inferência. Para ajustar os modelos de forma eficaz, garanta um conjunto de dados equilibrado e diversificado.

Isso inclui manter o equilíbrio dos dados, abranger diversos cenários e refinar periodicamente os dados de treinamento para alinhá-los às expectativas do mundo real, levando a respostas mais precisas e equilibradas do modelo.

Diferentes tipos de modelos requerem formatos diferentes de dados de treinamento.

### Conclusão de Chat

Os dados de treinamento e validação **devem** estar no formato de documento JSON Lines (JSONL). Para `Phi-3-mini-128k-instruct`, o conjunto de dados de ajuste fino deve estar no formato conversacional utilizado pela API de conclusão de chat.

### Exemplo de formato de arquivo

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

O tipo de arquivo suportado é JSON Lines. Os arquivos são carregados no armazenamento padrão e disponibilizados em seu projeto.

## Ajustando o Phi-3 com o Azure AI Foundry

O Azure AI Foundry permite que você adapte modelos de linguagem grandes aos seus próprios conjuntos de dados usando um processo conhecido como ajuste fino. O ajuste fino proporciona grande valor, permitindo personalização e otimização para tarefas e aplicações específicas. Isso resulta em melhor desempenho, eficiência de custos, menor latência e saídas personalizadas.

![Ajuste fino AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.pt.png)

### Criar um Novo Projeto

1. Faça login no [Azure AI Foundry](https://ai.azure.com).

1. Selecione **+Novo projeto** para criar um novo projeto no Azure AI Foundry.

    ![Selecionar Ajuste Fino](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.pt.png)

1. Realize as seguintes tarefas:

    - Nome do **Hub do projeto**. Deve ser um valor único.
    - Selecione o **Hub** a ser usado (crie um novo, se necessário).

    ![Criar Projeto](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.pt.png)

1. Realize as seguintes tarefas para criar um novo hub:

    - Insira o **Nome do Hub**. Deve ser um valor único.
    - Selecione sua **Assinatura do Azure**.
    - Escolha o **Grupo de recursos** a ser usado (crie um novo, se necessário).
    - Escolha a **Localização** desejada.
    - Selecione **Conectar Serviços de IA do Azure** para usar (crie um novo, se necessário).
    - Escolha **Pular conexão** para **Conectar Pesquisa de IA do Azure**.

    ![Criar Hub](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.pt.png)

1. Clique em **Próximo**.
1. Selecione **Criar um projeto**.

### Preparação de Dados

Antes do ajuste fino, reúna ou crie um conjunto de dados relevante para sua tarefa, como instruções de chat, pares de perguntas e respostas ou outros dados textuais pertinentes. Limpe e pré-processe esses dados removendo ruídos, lidando com valores ausentes e tokenizando o texto.

### Ajustando os modelos Phi-3 no Azure AI Foundry

> [!NOTE]
> O ajuste fino dos modelos Phi-3 é atualmente suportado em projetos localizados na região East US 2.

1. Selecione **Catálogo de modelos** no menu lateral esquerdo.

1. Digite *phi-3* na **barra de pesquisa** e selecione o modelo phi-3 que deseja usar.

    ![Selecionar Modelo](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.pt.png)

1. Clique em **Ajustar**.

    ![Selecionar Ajuste Fino](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.pt.png)

1. Insira o **Nome do modelo ajustado**.

    ![Nome do Modelo Ajustado](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.pt.png)

1. Clique em **Próximo**.

1. Realize as seguintes tarefas:

    - Selecione **tipo de tarefa** como **Conclusão de Chat**.
    - Escolha os **Dados de treinamento** que deseja usar. Você pode carregá-los através do Azure AI Foundry ou de seu ambiente local.

    ![Selecionar Dados de Treinamento](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.pt.png)

1. Clique em **Próximo**.

1. Carregue os **Dados de validação** que deseja usar, ou selecione **Divisão automática dos dados de treinamento**.

    ![Selecionar Dados de Validação](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.pt.png)

1. Clique em **Próximo**.

1. Realize as seguintes tarefas:

    - Escolha o **Multiplicador do tamanho do lote** que deseja usar.
    - Defina a **Taxa de aprendizado**.
    - Escolha o número de **Épocas**.

    ![Configurações de Ajuste Fino](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.pt.png)

1. Clique em **Enviar** para iniciar o processo de ajuste fino.

    ![Enviar Ajuste Fino](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.pt.png)

1. Assim que o modelo for ajustado, o status será exibido como **Concluído**, como mostrado na imagem abaixo. Agora você pode implantar o modelo e usá-lo em sua própria aplicação, no playground ou no fluxo de prompts. Para mais informações, veja [Como implantar a família de modelos Phi-3 com Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![Ajuste Concluído](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.pt.png)

> [!NOTE]
> Para informações mais detalhadas sobre o ajuste fino do Phi-3, visite [Ajuste fino de modelos Phi-3 no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Limpando seus modelos ajustados

Você pode excluir um modelo ajustado da lista de modelos ajustados no [Azure AI Foundry](https://ai.azure.com) ou da página de detalhes do modelo. Selecione o modelo ajustado que deseja excluir na página de Ajuste Fino e clique no botão Excluir.

> [!NOTE]
> Não é possível excluir um modelo personalizado se ele tiver uma implantação existente. Primeiro, exclua a implantação do modelo antes de excluí-lo.

## Custos e cotas

### Considerações sobre custo e cota para ajuste fino de modelos Phi-3

Os modelos Phi ajustados como serviço são oferecidos pela Microsoft e integrados ao Azure AI Foundry para uso. Você pode encontrar os preços ao [implantar](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) ou ajustar os modelos na aba Preços e Termos no assistente de implantação.

## Filtragem de conteúdo

Os modelos implantados como serviço com o modelo pay-as-you-go são protegidos pelo Azure AI Content Safety. Quando implantados em endpoints em tempo real, é possível optar por desativar essa funcionalidade. Com o Azure AI Content Safety ativado, tanto o prompt quanto a conclusão passam por um conjunto de modelos de classificação projetados para detectar e prevenir a geração de conteúdo prejudicial. O sistema de filtragem de conteúdo detecta e toma medidas em categorias específicas de conteúdo potencialmente prejudicial nos prompts de entrada e nas respostas geradas. Saiba mais sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Configuração de Ajuste Fino**

Hiperparâmetros: Defina hiperparâmetros como taxa de aprendizado, tamanho do lote e número de épocas de treinamento.

**Função de Perda**

Escolha uma função de perda adequada para sua tarefa (por exemplo, entropia cruzada).

**Otimizador**

Selecione um otimizador (por exemplo, Adam) para atualizações de gradiente durante o treinamento.

**Processo de Ajuste Fino**

- Carregar Modelo Pré-Treinado: Carregue o checkpoint do Phi-3 Mini.
- Adicionar Camadas Personalizadas: Adicione camadas específicas para a tarefa (por exemplo, cabeçalho de classificação para instruções de chat).

**Treine o Modelo**
Ajuste o modelo usando seu conjunto de dados preparado. Monitore o progresso do treinamento e ajuste os hiperparâmetros conforme necessário.

**Avaliação e Validação**

Conjunto de Validação: Divida seus dados em conjuntos de treinamento e validação.

**Avalie o Desempenho**

Use métricas como acurácia, F1-score ou perplexidade para avaliar o desempenho do modelo.

## Salvar Modelo Ajustado

**Checkpoint**
Salve o checkpoint do modelo ajustado para uso futuro.

## Implantação

- Implante como um Serviço Web: Implante seu modelo ajustado como um serviço web no Azure AI Foundry.
- Teste o Endpoint: Envie consultas de teste para o endpoint implantado para verificar sua funcionalidade.

## Iterar e Melhorar

Iteração: Se o desempenho não for satisfatório, ajuste os hiperparâmetros, adicione mais dados ou realize mais épocas de ajuste fino.

## Monitorar e Refinar

Monitore continuamente o comportamento do modelo e refine conforme necessário.

## Personalizar e Expandir

Tarefas Personalizadas: O Phi-3 Mini pode ser ajustado para várias tarefas além de instruções de chat. Explore outros casos de uso!
Experimente: Teste diferentes arquiteturas, combinações de camadas e técnicas para melhorar o desempenho.

> [!NOTE]
> O ajuste fino é um processo iterativo. Experimente, aprenda e adapte seu modelo para alcançar os melhores resultados para sua tarefa específica!

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automatizada por IA. Embora nos esforcemos para alcançar a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.