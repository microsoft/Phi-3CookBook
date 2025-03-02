# Contribuindo

Este projeto recebe de braços abertos contribuições e sugestões. A maioria das contribuições exige que você concorde com um Contrato de Licença de Contribuinte (CLA), declarando que você tem o direito de, e realmente concede, os direitos para que possamos usar sua contribuição. Para mais detalhes, visite [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Quando você enviar um pull request, um bot do CLA determinará automaticamente se você precisa fornecer um CLA e marcará o PR de forma apropriada (por exemplo, verificação de status, comentário). Basta seguir as instruções fornecidas pelo bot. Você só precisará fazer isso uma vez para todos os repositórios que utilizam nosso CLA.

## Código de Conduta

Este projeto adotou o [Código de Conduta de Código Aberto da Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Para mais informações, leia as [Perguntas Frequentes sobre o Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou entre em contato com [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer dúvidas ou comentários adicionais.

## Cuidados ao criar issues

Por favor, não abra issues no GitHub para perguntas gerais de suporte, pois a lista do GitHub deve ser usada para solicitações de funcionalidades e relatórios de bugs. Desta forma, podemos rastrear mais facilmente problemas reais ou bugs no código e manter a discussão geral separada do código em si.

## Como Contribuir

### Diretrizes para Pull Requests

Ao enviar um pull request (PR) para o repositório Phi-3 CookBook, siga as diretrizes abaixo:

- **Faça um fork do repositório**: Sempre faça um fork do repositório para sua própria conta antes de realizar modificações.

- **Pull requests separados (PR)**:
  - Envie cada tipo de alteração em um pull request separado. Por exemplo, correções de bugs e atualizações de documentação devem ser enviadas em PRs distintos.
  - Correções de erros de digitação e pequenas atualizações de documentação podem ser combinadas em um único PR, se apropriado.

- **Resolva conflitos de mesclagem**: Se o seu pull request mostrar conflitos de mesclagem, atualize sua branch local `main` para espelhar o repositório principal antes de fazer suas modificações.

- **Envio de traduções**: Ao enviar um PR de tradução, certifique-se de que a pasta de tradução inclua traduções para todos os arquivos da pasta original.

### Diretrizes para Tradução

> [!IMPORTANT]
>
> Ao traduzir texto neste repositório, não use tradução automática. Apenas se voluntarie para traduções em idiomas nos quais você seja proficiente.

Se você é fluente em um idioma que não seja o inglês, pode ajudar traduzindo o conteúdo. Siga estas etapas para garantir que suas contribuições de tradução sejam integradas corretamente, utilizando as diretrizes abaixo:

- **Crie uma pasta de tradução**: Navegue até a seção apropriada e crie uma pasta de tradução para o idioma que você está contribuindo. Por exemplo:
  - Para a seção de introdução: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Para a seção de início rápido: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Continue este padrão para outras seções (03.Inference, 04.Finetuning, etc.)

- **Atualize os caminhos relativos**: Ao traduzir, ajuste a estrutura da pasta adicionando `../../` ao início dos caminhos relativos dentro dos arquivos markdown para garantir que os links funcionem corretamente. Por exemplo, altere da seguinte forma:
  - Mude `(../../imgs/01/phi3aisafety.png)` para `(../../../../imgs/01/phi3aisafety.png)`

- **Organize suas traduções**: Cada arquivo traduzido deve ser colocado na pasta de tradução correspondente à seção. Por exemplo, se você estiver traduzindo a seção de introdução para o espanhol, deve criar o seguinte:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Envie um PR completo**: Certifique-se de que todos os arquivos traduzidos para uma seção sejam incluídos em um único PR. Não aceitamos traduções parciais para uma seção. Ao enviar um PR de tradução, certifique-se de que a pasta de tradução inclua traduções para todos os arquivos da pasta original.

### Diretrizes de Redação

Para garantir consistência em todos os documentos, siga as diretrizes abaixo:

- **Formatação de URLs**: Coloque todas as URLs entre colchetes seguidos por parênteses, sem espaços extras ao redor ou dentro deles. Por exemplo: `[example](https://example.com)`.

- **Links relativos**: Use `./` para links relativos apontando para arquivos ou pastas no diretório atual, e `../` para aqueles em um diretório pai. Por exemplo: `[example](../../path/to/file)` ou `[example](../../../path/to/file)`.

- **Evite locais específicos de países**: Certifique-se de que seus links não incluam locais específicos de países. Por exemplo, evite `/en-us/` ou `/en/`.

- **Armazenamento de imagens**: Armazene todas as imagens na pasta `./imgs`.

- **Nomes descritivos para imagens**: Nomeie as imagens de forma descritiva, utilizando caracteres em inglês, números e hífens. Por exemplo: `example-image.jpg`.

## Workflows do GitHub

Quando você enviar um pull request, os seguintes workflows serão acionados para validar as alterações. Siga as instruções abaixo para garantir que seu pull request passe nas verificações dos workflows:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Este workflow garante que todos os caminhos relativos em seus arquivos estão corretos.

1. Para garantir que seus links estejam funcionando corretamente, realize as seguintes tarefas usando o VS Code:
    - Passe o mouse sobre qualquer link em seus arquivos.
    - Pressione **Ctrl + Clique** para navegar até o link.
    - Se você clicar em um link e ele não funcionar localmente, isso acionará o workflow e ele não funcionará no GitHub.

1. Para corrigir este problema, realize as seguintes tarefas usando as sugestões de caminho fornecidas pelo VS Code:
    - Digite `./` ou `../`.
    - O VS Code irá sugerir as opções disponíveis com base no que você digitou.
    - Siga o caminho clicando no arquivo ou pasta desejado para garantir que o caminho esteja correto.

Depois de adicionar o caminho relativo correto, salve e envie suas alterações.

### Check URLs Don't Have Locale

Este workflow garante que nenhuma URL da web inclua um local específico de país. Como este repositório é acessível globalmente, é importante garantir que as URLs não contenham o local do seu país.

1. Para verificar se suas URLs não possuem locais de países, realize as seguintes tarefas:

    - Verifique por textos como `/en-us/`, `/en/`, ou qualquer outro local de idioma nas URLs.
    - Se esses textos não estiverem presentes em suas URLs, você passará nesta verificação.

1. Para corrigir este problema, realize as seguintes tarefas:
    - Abra o caminho do arquivo destacado pelo workflow.
    - Remova o local do país das URLs.

Depois de remover o local do país, salve e envie suas alterações.

### Check Broken Urls

Este workflow garante que qualquer URL da web em seus arquivos esteja funcionando e retornando o código de status 200.

1. Para verificar se suas URLs estão funcionando corretamente, realize as seguintes tarefas:
    - Verifique o status das URLs em seus arquivos.

2. Para corrigir quaisquer URLs quebradas, realize as seguintes tarefas:
    - Abra o arquivo que contém a URL quebrada.
    - Atualize a URL para a correta.

Depois de corrigir as URLs, salve e envie suas alterações.

> [!NOTE]
>
> Pode haver casos em que a verificação de URL falhe, mesmo que o link esteja acessível. Isso pode ocorrer por várias razões, incluindo:
>
> - **Restrições de rede:** Os servidores de ações do GitHub podem ter restrições de rede que impedem o acesso a certas URLs.
> - **Problemas de tempo limite:** URLs que demoram muito para responder podem gerar um erro de tempo limite no workflow.
> - **Problemas temporários no servidor:** Interrupções ou manutenção temporária do servidor podem tornar uma URL temporariamente indisponível durante a validação.

**Aviso Legal**:  
Este documento foi traduzido usando serviços de tradução automatizada por IA. Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.