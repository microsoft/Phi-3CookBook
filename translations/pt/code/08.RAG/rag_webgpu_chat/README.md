Phi-3-mini WebGPU RAG Chatbot

## Demonstração para exibir WebGPU e o padrão RAG
O padrão RAG com o modelo hospedado Phi-3 Onnx utiliza a abordagem de Geração Aumentada por Recuperação, combinando o poder dos modelos Phi-3 com a hospedagem ONNX para implantações de IA eficientes. Esse padrão é essencial para ajustar modelos a tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contexto estendido. Faz parte da suíte de IA do Azure, que fornece uma ampla seleção de modelos fáceis de encontrar, testar e usar, atendendo às necessidades de personalização de diversas indústrias. Os modelos Phi-3, incluindo Phi-3-mini, Phi-3-small e Phi-3-medium, estão disponíveis no Catálogo de Modelos do Azure AI e podem ser ajustados e implantados de forma autônoma ou por meio de plataformas como HuggingFace e ONNX, destacando o compromisso da Microsoft com soluções de IA acessíveis e eficientes.

## O que é WebGPU 
WebGPU é uma API gráfica moderna para a web, projetada para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente a partir de navegadores. Ela foi desenvolvida para ser a sucessora do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs modernas**: O WebGPU foi criado para funcionar perfeitamente com arquiteturas de GPU contemporâneas, aproveitando APIs de sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho aprimorado**: Suporta cálculos gerais na GPU e operações mais rápidas, sendo adequado tanto para renderização gráfica quanto para tarefas de aprendizado de máquina.
3. **Recursos avançados**: Oferece acesso a capacidades mais avançadas da GPU, possibilitando cargas de trabalho computacionais e gráficas mais complexas e dinâmicas.
4. **Redução da carga no JavaScript**: Ao transferir mais tarefas para a GPU, o WebGPU reduz significativamente a carga no JavaScript, resultando em melhor desempenho e experiências mais fluidas.

Atualmente, o WebGPU é compatível com navegadores como Google Chrome, com esforços contínuos para expandir o suporte a outras plataformas.

### 03.WebGPU
Ambiente necessário:

**Navegadores compatíveis:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Ativar WebGPU:

- No Chrome/Microsoft Edge 

Ative a flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abra seu navegador:
Inicie o Google Chrome ou Microsoft Edge.

#### Acesse a página de Flags:
Na barra de endereços, digite `chrome://flags` e pressione Enter.

#### Procure a Flag:
Na caixa de pesquisa no topo da página, digite 'enable-unsafe-webgpu'.

#### Ative a Flag:
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado dela e selecione Enabled.

#### Reinicie o navegador:

Depois de ativar a flag, será necessário reiniciar o navegador para que as alterações entrem em vigor. Clique no botão Relaunch que aparece na parte inferior da página.

- Para Linux, inicie o navegador com `--enable-features=Vulkan`.
- O Safari 18 (macOS 15) já possui o WebGPU ativado por padrão.
- No Firefox Nightly, digite about:config na barra de endereços e `set dom.webgpu.enabled to true`.

### Configurando a GPU para Microsoft Edge 

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra as Configurações:** Clique no menu Iniciar e selecione Configurações.
- **Configurações do Sistema:** Vá para Sistema e depois para Tela.
- **Configurações de Gráficos:** Role para baixo e clique em Configurações de gráficos.
- **Escolha o Aplicativo:** Em “Escolher um aplicativo para definir preferência,” selecione Aplicativo de desktop e depois Procurar.
- **Selecione o Edge:** Navegue até a pasta de instalação do Edge (geralmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.
- **Defina a Preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Salvar.
Isso garantirá que o Microsoft Edge utilize sua GPU de alto desempenho para melhor desempenho. 
- **Reinicie** sua máquina para que essas configurações entrem em vigor.

### Abra seu Codespace:
Navegue até seu repositório no GitHub.
Clique no botão Code e selecione Open with Codespaces.

Se você ainda não tiver um Codespace, pode criar um clicando em New codespace.

**Nota** Instalando o ambiente Node em seu Codespace
Executar um demo npm a partir de um Codespace do GitHub é uma ótima maneira de testar e desenvolver seu projeto. Aqui está um guia passo a passo para ajudá-lo a começar:

### Configure seu ambiente:
Depois que seu Codespace estiver aberto, certifique-se de que o Node.js e o npm estão instalados. Você pode verificar isso executando:
```
node -v
```
```
npm -v
```

Se não estiverem instalados, você pode instalá-los usando:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navegue até o diretório do seu projeto:
Use o terminal para navegar até o diretório onde seu projeto npm está localizado:
```
cd path/to/your/project
```

### Instale as dependências:
Execute o seguinte comando para instalar todas as dependências necessárias listadas em seu arquivo package.json:

```
npm install
```

### Execute o Demo:
Depois que as dependências estiverem instaladas, você pode executar seu script de demonstração. Isso geralmente é especificado na seção de scripts do seu package.json. Por exemplo, se o script de demonstração se chama start, você pode executar:

```
npm run build
```
```
npm run dev
```

### Acesse o Demo:
Se sua demonstração envolver um servidor web, o Codespaces fornecerá uma URL para acessá-lo. Procure uma notificação ou verifique a aba Ports para encontrar a URL.

**Nota:** O modelo precisa ser armazenado em cache no navegador, então pode levar algum tempo para carregar.

### Demonstração RAG
Faça upload do arquivo markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Selecione seu arquivo:
Clique no botão que diz “Escolher arquivo” para selecionar o documento que deseja fazer upload.

### Faça o upload do documento:
Depois de selecionar seu arquivo, clique no botão “Upload” para carregar seu documento para o RAG (Geração Aumentada por Recuperação).

### Inicie seu chat:
Depois que o documento for carregado, você pode iniciar uma sessão de chat usando o RAG com base no conteúdo do seu documento.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.