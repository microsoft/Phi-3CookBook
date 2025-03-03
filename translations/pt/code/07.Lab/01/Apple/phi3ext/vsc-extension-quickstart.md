# Bem-vindo à sua Extensão do VS Code

## O que há na pasta

* Esta pasta contém todos os arquivos necessários para sua extensão.
* `package.json` - este é o arquivo de manifesto no qual você declara sua extensão e comando.
  * O plugin de exemplo registra um comando e define seu título e nome. Com essas informações, o VS Code pode exibir o comando no painel de comandos. Ainda não é necessário carregar o plugin.
* `src/extension.ts` - este é o arquivo principal onde você fornecerá a implementação do seu comando.
  * O arquivo exporta uma função, `activate`, que é chamada na primeira vez que sua extensão é ativada (neste caso, ao executar o comando). Dentro da função `activate`, chamamos `registerCommand`.
  * Passamos a função contendo a implementação do comando como segundo parâmetro para `registerCommand`.

## Configuração

* Instale as extensões recomendadas (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner e dbaeumer.vscode-eslint)

## Comece a usar imediatamente

* Pressione `F5` para abrir uma nova janela com sua extensão carregada.
* Execute seu comando no painel de comandos pressionando (`Ctrl+Shift+P` ou `Cmd+Shift+P` no Mac) e digitando `Hello World`.
* Configure pontos de interrupção no seu código dentro de `src/extension.ts` para depurar sua extensão.
* Encontre a saída da sua extensão no console de depuração.

## Faça alterações

* Você pode reiniciar a extensão a partir da barra de ferramentas de depuração após alterar o código em `src/extension.ts`.
* Você também pode recarregar (`Ctrl+R` ou `Cmd+R` no Mac) a janela do VS Code com sua extensão para carregar suas alterações.

## Explore a API

* Você pode abrir o conjunto completo da nossa API ao abrir o arquivo `node_modules/@types/vscode/index.d.ts`.

## Execute testes

* Instale o [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Execute a tarefa "watch" via o comando **Tasks: Run Task**. Certifique-se de que ela esteja em execução, ou os testes podem não ser detectados.
* Abra a visualização de Testes na barra de atividades e clique no botão "Run Test", ou use o atalho `Ctrl/Cmd + ; A`.
* Veja a saída do resultado do teste na visualização de Resultados de Teste.
* Faça alterações em `src/test/extension.test.ts` ou crie novos arquivos de teste dentro da pasta `test`.
  * O executor de testes fornecido considerará apenas arquivos que correspondam ao padrão de nome `**.test.ts`.
  * Você pode criar pastas dentro da pasta `test` para organizar seus testes da maneira que preferir.

## Vá além

* Reduza o tamanho da extensão e melhore o tempo de inicialização ao [empacotar sua extensão](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publique sua extensão](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) no marketplace de extensões do VS Code.
* Automatize builds configurando [Integração Contínua](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.