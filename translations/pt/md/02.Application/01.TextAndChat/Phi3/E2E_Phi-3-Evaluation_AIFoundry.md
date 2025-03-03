# Avaliar o Modelo Fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry com Foco nos Princípios de IA Responsável da Microsoft

Este exemplo de ponta a ponta (E2E) é baseado no guia "[Avaliar Modelos Fine-tuned Phi-3 / 3.5 no Azure AI Foundry com Foco na IA Responsável da Microsoft](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" da Comunidade Técnica da Microsoft.

## Visão Geral

### Como você pode avaliar a segurança e o desempenho de um modelo fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry?

O ajuste fino de um modelo pode, às vezes, levar a respostas indesejadas ou não intencionais. Para garantir que o modelo permaneça seguro e eficaz, é importante avaliar o potencial do modelo de gerar conteúdo prejudicial e sua capacidade de produzir respostas precisas, relevantes e coerentes. Neste tutorial, você aprenderá como avaliar a segurança e o desempenho de um modelo fine-tuned Phi-3 / Phi-3.5 integrado com o Prompt flow no Azure AI Foundry.

Aqui está o processo de avaliação do Azure AI Foundry.

![Arquitetura do tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pt.png)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Para informações mais detalhadas e para explorar recursos adicionais sobre Phi-3 / Phi-3.5, visite o [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Pré-requisitos

- [Python](https://www.python.org/downloads)
- [Assinatura do Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modelo Fine-tuned Phi-3 / Phi-3.5

### Índice

1. [**Cenário 1: Introdução à avaliação do Prompt flow no Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introdução à avaliação de segurança](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introdução à avaliação de desempenho](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Antes de começar](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implantar o Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Avaliar o modelo fine-tuned Phi-3 / Phi-3.5 usando o Prompt flow do Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Parabéns!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Cenário 1: Introdução à avaliação do Prompt flow no Azure AI Foundry**

### Introdução à avaliação de segurança

Para garantir que seu modelo de IA seja ético e seguro, é crucial avaliá-lo com base nos Princípios de IA Responsável da Microsoft. No Azure AI Foundry, as avaliações de segurança permitem avaliar a vulnerabilidade do modelo a ataques de jailbreak e seu potencial de gerar conteúdo prejudicial, alinhando-se diretamente a esses princípios.

![Avaliação de segurança.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.pt.png)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Princípios de IA Responsável da Microsoft

Antes de iniciar os passos técnicos, é essencial entender os Princípios de IA Responsável da Microsoft, um framework ético projetado para orientar o desenvolvimento, a implementação e a operação responsável de sistemas de IA. Esses princípios garantem que as tecnologias de IA sejam criadas de forma justa, transparente e inclusiva. Eles são a base para avaliar a segurança de modelos de IA.

Os Princípios de IA Responsável da Microsoft incluem:

- **Equidade e Inclusão**: Sistemas de IA devem tratar todos de forma justa e evitar afetar grupos semelhantes de maneira desigual. Por exemplo, ao fornecer orientações sobre tratamentos médicos, aplicações de crédito ou emprego, os sistemas devem oferecer as mesmas recomendações para pessoas em condições semelhantes.

- **Confiabilidade e Segurança**: Para construir confiança, é fundamental que os sistemas de IA operem de forma confiável, segura e consistente. Esses sistemas devem funcionar conforme projetados, responder de forma segura a condições imprevistas e resistir a manipulações prejudiciais.

- **Transparência**: Quando sistemas de IA ajudam a tomar decisões que impactam significativamente a vida das pessoas, é essencial que elas entendam como essas decisões foram feitas. Por exemplo, um banco pode usar um sistema de IA para decidir a concessão de crédito, ou uma empresa pode usar IA para selecionar candidatos mais qualificados para uma vaga.

- **Privacidade e Segurança**: Com o aumento da presença da IA, proteger a privacidade e a segurança das informações pessoais e empresariais tornou-se mais importante e complexo. A privacidade e a segurança de dados exigem atenção especial, já que o acesso a dados é essencial para que os sistemas de IA façam previsões e decisões precisas.

- **Responsabilidade**: As pessoas que projetam e implementam sistemas de IA devem ser responsáveis por seu funcionamento. Organizações devem adotar padrões da indústria para desenvolver normas de responsabilidade, garantindo que sistemas de IA não sejam a autoridade final em decisões que impactem vidas humanas.

![Hub de IA Responsável.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.pt.png)

*Fonte da Imagem: [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Para saber mais sobre os Princípios de IA Responsável da Microsoft, visite [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Métricas de segurança

Neste tutorial, você avaliará a segurança do modelo fine-tuned Phi-3 usando as métricas de segurança do Azure AI Foundry. Essas métricas ajudam a avaliar o potencial do modelo de gerar conteúdo prejudicial e sua vulnerabilidade a ataques de jailbreak. As métricas de segurança incluem:

- **Conteúdo Relacionado a Autoagressão**: Avalia se o modelo tem tendência a produzir conteúdo relacionado a autoagressão.
- **Conteúdo Odioso e Injusto**: Avalia se o modelo tem tendência a produzir conteúdo odioso ou injusto.
- **Conteúdo Violento**: Avalia se o modelo tem tendência a produzir conteúdo violento.
- **Conteúdo Sexual**: Avalia se o modelo tem tendência a produzir conteúdo sexual inapropriado.

Avaliar esses aspectos garante que o modelo de IA não produza conteúdo prejudicial ou ofensivo, alinhando-o com valores sociais e padrões regulatórios.

![Avaliar com base na segurança.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.pt.png)

### Introdução à avaliação de desempenho

Para garantir que seu modelo de IA esteja funcionando como esperado, é importante avaliar seu desempenho com base em métricas de desempenho. No Azure AI Foundry, as avaliações de desempenho permitem avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes.

![Avaliação de desempenho.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.pt.png)

*Fonte da Imagem: [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Métricas de desempenho

Neste tutorial, você avaliará o desempenho do modelo fine-tuned Phi-3 / Phi-3.5 usando as métricas de desempenho do Azure AI Foundry. Essas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes. As métricas de desempenho incluem:

- **Baseamento**: Avalia o quão bem as respostas geradas se alinham às informações da fonte de entrada.
- **Relevância**: Avalia a pertinência das respostas geradas às perguntas dadas.
- **Coerência**: Avalia a fluidez do texto gerado, sua naturalidade e semelhança com a linguagem humana.
- **Fluência**: Avalia a proficiência linguística do texto gerado.
- **Similaridade GPT**: Compara a resposta gerada com a verdade de referência para similaridade.
- **Pontuação F1**: Calcula a proporção de palavras compartilhadas entre a resposta gerada e os dados da fonte.

Essas métricas ajudam a avaliar a eficácia do modelo em gerar respostas precisas, relevantes e coerentes.

![Avaliar com base no desempenho.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.pt.png)

## **Cenário 2: Avaliando o modelo Phi-3 / Phi-3.5 no Azure AI Foundry**

### Antes de começar

Este tutorial é uma continuação dos posts anteriores, "[Ajustar e Integrar Modelos Customizados Phi-3 com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Ajustar e Integrar Modelos Customizados Phi-3 com Prompt Flow no Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." Nesses posts, percorremos o processo de ajuste fino de um modelo Phi-3 / Phi-3.5 no Azure AI Foundry e sua integração com o Prompt flow.

Neste tutorial, você implantará um modelo Azure OpenAI como avaliador no Azure AI Foundry e o usará para avaliar seu modelo fine-tuned Phi-3 / Phi-3.5.

Antes de começar este tutorial, certifique-se de ter os seguintes pré-requisitos, conforme descrito nos tutoriais anteriores:

1. Um conjunto de dados preparado para avaliar o modelo fine-tuned Phi-3 / Phi-3.5.
1. Um modelo Phi-3 / Phi-3.5 que foi ajustado e implantado no Azure Machine Learning.
1. Um Prompt flow integrado ao seu modelo fine-tuned Phi-3 / Phi-3.5 no Azure AI Foundry.

> [!NOTE]
> Você usará o arquivo *test_data.jsonl*, localizado na pasta de dados do conjunto de dados **ULTRACHAT_200k** baixado nos posts anteriores, como o conjunto de dados para avaliar o modelo fine-tuned Phi-3 / Phi-3.5.

#### Integrar o modelo customizado Phi-3 / Phi-3.5 com Prompt flow no Azure AI Foundry (Abordagem baseada em código)

> [!NOTE]
> Se você seguiu a abordagem de baixo código descrita em "[Ajustar e Integrar Modelos Customizados Phi-3 com Prompt Flow no Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", você pode pular este exercício e prosseguir para o próximo.
> No entanto, se você seguiu a abordagem baseada em código descrita em "[Ajustar e Integrar Modelos Customizados Phi-3 com Prompt Flow: Guia Passo a Passo](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" para ajustar e implantar seu modelo Phi-3 / Phi-3.5, o processo de conectar seu modelo ao Prompt flow é ligeiramente diferente. Você aprenderá esse processo neste exercício.

Para prosseguir, você precisa integrar seu modelo fine-tuned Phi-3 / Phi-3.5 ao Prompt flow no Azure AI Foundry.

#### Criar Hub no Azure AI Foundry

Você precisa criar um Hub antes de criar o Projeto. Um Hub funciona como um Grupo de Recursos, permitindo que você organize e gerencie múltiplos Projetos dentro do Azure AI Foundry.

1. Faça login no [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Selecione **Todos os hubs** na aba lateral esquerda.

1. Selecione **+ Novo hub** no menu de navegação.

    ![Criar hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.pt.png)

1. Realize as seguintes tarefas:

    - Insira o **Nome do Hub**. Deve ser um valor único.
    - Selecione sua **Assinatura** do Azure.
    - Escolha o **Grupo de Recursos** a ser usado (crie um novo se necessário).
    - Selecione a **Localização** desejada.
    - Escolha o **Conectar Serviços de IA do Azure** a ser usado (crie um novo se necessário).
    - Selecione **Conectar Pesquisa do Azure AI** para **Pular conexão**.
![Preencher hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.pt.png)

1. Selecione **Próximo**.

#### Criar Projeto Azure AI Foundry

1. No Hub que você criou, selecione **Todos os projetos** na aba lateral esquerda.

1. Selecione **+ Novo projeto** no menu de navegação.

    ![Selecionar novo projeto.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.pt.png)

1. Insira **Nome do projeto**. Ele deve ser um valor único.

    ![Criar projeto.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.pt.png)

1. Selecione **Criar um projeto**.

#### Adicionar uma conexão personalizada para o modelo ajustado Phi-3 / Phi-3.5

Para integrar seu modelo personalizado Phi-3 / Phi-3.5 ao Prompt flow, você precisa salvar o endpoint e a chave do modelo em uma conexão personalizada. Essa configuração garante acesso ao seu modelo personalizado no Prompt flow.

#### Configurar chave de API e URI do endpoint do modelo ajustado Phi-3 / Phi-3.5

1. Visite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navegue até o workspace do Azure Machine Learning que você criou.

1. Selecione **Endpoints** na aba lateral esquerda.

    ![Selecionar endpoints.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.pt.png)

1. Selecione o endpoint que você criou.

    ![Selecionar endpoint criado.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.pt.png)

1. Selecione **Consumir** no menu de navegação.

1. Copie seu **REST endpoint** e **Chave primária**.

    ![Copiar chave de API e URI do endpoint.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.pt.png)

#### Adicionar a Conexão Personalizada

1. Visite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

1. No projeto que você criou, selecione **Configurações** na aba lateral esquerda.

1. Selecione **+ Nova conexão**.

    ![Selecionar nova conexão.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.pt.png)

1. Selecione **Chaves personalizadas** no menu de navegação.

    ![Selecionar chaves personalizadas.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.pt.png)

1. Realize as seguintes tarefas:

    - Selecione **+ Adicionar pares de chave e valor**.
    - Para o nome da chave, insira **endpoint** e cole o endpoint que você copiou do Azure ML Studio no campo de valor.
    - Selecione **+ Adicionar pares de chave e valor** novamente.
    - Para o nome da chave, insira **key** e cole a chave que você copiou do Azure ML Studio no campo de valor.
    - Após adicionar as chaves, selecione **é segredo** para evitar que a chave seja exposta.

    ![Adicionar conexão.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.pt.png)

1. Selecione **Adicionar conexão**.

#### Criar Prompt flow

Você adicionou uma conexão personalizada no Azure AI Foundry. Agora, vamos criar um Prompt flow usando as etapas a seguir. Em seguida, você conectará esse Prompt flow à conexão personalizada para usar o modelo ajustado dentro do Prompt flow.

1. Navegue até o projeto Azure AI Foundry que você criou.

1. Selecione **Prompt flow** na aba lateral esquerda.

1. Selecione **+ Criar** no menu de navegação.

    ![Selecionar Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.pt.png)

1. Selecione **Chat flow** no menu de navegação.

    ![Selecionar chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.pt.png)

1. Insira **Nome da pasta** para usar.

    ![Selecionar chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.pt.png)

1. Selecione **Criar**.

#### Configurar Prompt flow para conversar com seu modelo ajustado Phi-3 / Phi-3.5

Você precisa integrar o modelo ajustado Phi-3 / Phi-3.5 a um Prompt flow. No entanto, o Prompt flow existente não foi projetado para esse propósito. Portanto, você deve redesenhar o Prompt flow para habilitar a integração do modelo personalizado.

1. No Prompt flow, realize as seguintes tarefas para reconstruir o fluxo existente:

    - Selecione **Modo de arquivo bruto**.
    - Exclua todo o código existente no arquivo *flow.dag.yml*.
    - Adicione o seguinte código ao arquivo *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Selecione **Salvar**.

    ![Selecionar modo de arquivo bruto.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.pt.png)

1. Adicione o seguinte código ao arquivo *integrate_with_promptflow.py* para usar o modelo personalizado Phi-3 / Phi-3.5 no Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Colar código do Prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.pt.png)

> [!NOTE]  
> Para mais informações detalhadas sobre como usar Prompt flow no Azure AI Foundry, você pode consultar [Prompt flow no Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecione **Entrada do chat**, **Saída do chat** para habilitar o chat com seu modelo.

    ![Selecionar Entrada Saída.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.pt.png)

1. Agora você está pronto para conversar com seu modelo ajustado Phi-3 / Phi-3.5. No próximo exercício, você aprenderá como iniciar o Prompt flow e usá-lo para interagir com seu modelo ajustado Phi-3 / Phi-3.5.

> [!NOTE]  
> O fluxo reconstruído deve se parecer com a imagem abaixo:  
> ![Exemplo de fluxo](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.pt.png)

#### Iniciar Prompt flow

1. Selecione **Iniciar sessões de computação** para iniciar o Prompt flow.

    ![Iniciar sessão de computação.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.pt.png)

1. Selecione **Validar e analisar entrada** para renovar os parâmetros.

    ![Validar entrada.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.pt.png)

1. Selecione o **Valor** da **conexão** para a conexão personalizada que você criou. Por exemplo, *connection*.

    ![Conexão.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.pt.png)

#### Conversar com seu modelo ajustado Phi-3 / Phi-3.5

1. Selecione **Chat**.

    ![Selecionar chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.pt.png)

1. Aqui está um exemplo dos resultados: Agora você pode conversar com seu modelo ajustado Phi-3 / Phi-3.5. Recomenda-se fazer perguntas com base nos dados usados para o ajuste fino.

    ![Conversar com Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.pt.png)

### Implantar Azure OpenAI para avaliar o modelo Phi-3 / Phi-3.5

Para avaliar o modelo Phi-3 / Phi-3.5 no Azure AI Foundry, você precisa implantar um modelo Azure OpenAI. Esse modelo será usado para avaliar o desempenho do modelo Phi-3 / Phi-3.5.

#### Implantar Azure OpenAI

1. Faça login em [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Selecionar Projeto.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pt.png)

1. No projeto que você criou, selecione **Implantações** na aba lateral esquerda.

1. Selecione **+ Implantar modelo** no menu de navegação.

1. Selecione **Implantar modelo base**.

    ![Selecionar Implantações.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.pt.png)

1. Selecione o modelo Azure OpenAI que você gostaria de usar. Por exemplo, **gpt-4o**.

    ![Selecionar modelo Azure OpenAI desejado.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.pt.png)

1. Selecione **Confirmar**.

### Avaliar o modelo ajustado Phi-3 / Phi-3.5 usando a avaliação do Prompt flow no Azure AI Foundry

### Iniciar uma nova avaliação

1. Visite [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Navegue até o projeto Azure AI Foundry que você criou.

    ![Selecionar Projeto.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.pt.png)

1. No projeto que você criou, selecione **Avaliação** na aba lateral esquerda.

1. Selecione **+ Nova avaliação** no menu de navegação.
![Selecione a avaliação.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.pt.png)

1. Selecione a avaliação **Prompt flow**.

    ![Selecione a avaliação Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.pt.png)

1. Realize as seguintes tarefas:

    - Insira o nome da avaliação. Deve ser um valor único.
    - Selecione **Pergunta e resposta sem contexto** como o tipo de tarefa. Isso porque o conjunto de dados **ULTRACHAT_200k** utilizado neste tutorial não contém contexto.
    - Selecione o fluxo de prompt que você deseja avaliar.

    ![Avaliação Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.pt.png)

1. Selecione **Próximo**.

1. Realize as seguintes tarefas:

    - Selecione **Adicionar seu conjunto de dados** para fazer o upload do conjunto de dados. Por exemplo, você pode carregar o arquivo de teste, como *test_data.json1*, que está incluído ao baixar o conjunto de dados **ULTRACHAT_200k**.
    - Selecione a **Coluna do conjunto de dados** apropriada que corresponde ao seu conjunto de dados. Por exemplo, se você estiver usando o conjunto de dados **ULTRACHAT_200k**, selecione **${data.prompt}** como a coluna do conjunto de dados.

    ![Avaliação Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.pt.png)

1. Selecione **Próximo**.

1. Realize as seguintes tarefas para configurar as métricas de desempenho e qualidade:

    - Selecione as métricas de desempenho e qualidade que deseja usar.
    - Selecione o modelo Azure OpenAI que você criou para avaliação. Por exemplo, selecione **gpt-4o**.

    ![Avaliação Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.pt.png)

1. Realize as seguintes tarefas para configurar as métricas de risco e segurança:

    - Selecione as métricas de risco e segurança que deseja usar.
    - Selecione o limite para calcular a taxa de defeitos que deseja usar. Por exemplo, selecione **Médio**.
    - Para **pergunta**, selecione **Fonte de dados** como **{$data.prompt}**.
    - Para **resposta**, selecione **Fonte de dados** como **{$run.outputs.answer}**.
    - Para **ground_truth**, selecione **Fonte de dados** como **{$data.message}**.

    ![Avaliação Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.pt.png)

1. Selecione **Próximo**.

1. Selecione **Enviar** para iniciar a avaliação.

1. A avaliação levará algum tempo para ser concluída. Você pode monitorar o progresso na aba **Avaliação**.

### Revisar os Resultados da Avaliação

> [!NOTE]
> Os resultados apresentados abaixo têm como objetivo ilustrar o processo de avaliação. Neste tutorial, usamos um modelo ajustado com um conjunto de dados relativamente pequeno, o que pode levar a resultados subótimos. Os resultados reais podem variar significativamente dependendo do tamanho, qualidade e diversidade do conjunto de dados utilizado, bem como da configuração específica do modelo.

Após a conclusão da avaliação, você pode revisar os resultados das métricas de desempenho e segurança.

1. Métricas de desempenho e qualidade:

    - Avalie a eficácia do modelo em gerar respostas coerentes, fluentes e relevantes.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.pt.png)

1. Métricas de risco e segurança:

    - Certifique-se de que as saídas do modelo sejam seguras e estejam alinhadas com os Princípios de IA Responsável, evitando qualquer conteúdo prejudicial ou ofensivo.

    ![Resultado da avaliação.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.pt.png)

1. Você pode rolar para baixo para visualizar os **Resultados detalhados das métricas**.

    ![Resultado da avaliação.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.pt.png)

1. Ao avaliar seu modelo personalizado Phi-3 / Phi-3.5 em relação às métricas de desempenho e segurança, você pode confirmar que o modelo não apenas é eficaz, mas também segue práticas responsáveis de IA, tornando-o pronto para implantação no mundo real.

## Parabéns!

### Você concluiu este tutorial

Você avaliou com sucesso o modelo ajustado Phi-3 integrado ao Prompt flow no Azure AI Foundry. Este é um passo importante para garantir que seus modelos de IA não apenas tenham um bom desempenho, mas também estejam alinhados com os princípios de IA Responsável da Microsoft, ajudando a construir aplicações de IA confiáveis e seguras.

![Arquitetura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.pt.png)

## Limpeza de Recursos do Azure

Limpe seus recursos do Azure para evitar cobranças adicionais na sua conta. Acesse o portal do Azure e exclua os seguintes recursos:

- O recurso Azure Machine Learning.
- O endpoint do modelo Azure Machine Learning.
- O recurso do projeto Azure AI Foundry.
- O recurso Prompt flow do Azure AI Foundry.

### Próximos Passos

#### Documentação

- [Avaliar sistemas de IA usando o painel de IA Responsável](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Métricas de avaliação e monitoramento para IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentação do Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Conteúdo de Treinamento

- [Introdução à abordagem de IA Responsável da Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introdução ao Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Referência

- [O que é IA Responsável?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Anunciando novas ferramentas no Azure AI para ajudar a construir aplicações de IA generativa mais seguras e confiáveis](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Avaliação de aplicações de IA generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.