# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demonstração para apresentar WebGPU e o Padrão RAG

O Padrão RAG com o modelo Phi-3.5 Onnx Hosted utiliza a abordagem de Geração com Recuperação Aumentada (Retrieval-Augmented Generation), combinando o poder dos modelos Phi-3.5 com a hospedagem ONNX para implantações de IA eficientes. Esse padrão é fundamental para ajustar modelos para tarefas específicas de domínio, oferecendo uma combinação de qualidade, custo-benefício e compreensão de contexto estendido. Faz parte do conjunto Azure AI, que disponibiliza uma ampla seleção de modelos fáceis de encontrar, experimentar e usar, atendendo às necessidades de personalização de várias indústrias.

## O que é WebGPU 
WebGPU é uma API moderna de gráficos para a web, projetada para fornecer acesso eficiente à unidade de processamento gráfico (GPU) de um dispositivo diretamente a partir de navegadores. Pretende ser o sucessor do WebGL, oferecendo várias melhorias importantes:

1. **Compatibilidade com GPUs Modernas**: O WebGPU foi desenvolvido para funcionar perfeitamente com arquiteturas de GPU contemporâneas, aproveitando APIs de sistema como Vulkan, Metal e Direct3D 12.
2. **Desempenho Aprimorado**: Suporta cálculos de propósito geral na GPU e operações mais rápidas, tornando-o adequado tanto para renderização gráfica quanto para tarefas de aprendizado de máquina.
3. **Recursos Avançados**: O WebGPU oferece acesso a capacidades mais avançadas da GPU, permitindo cargas de trabalho computacionais e gráficas mais complexas e dinâmicas.
4. **Redução da Carga de Trabalho no JavaScript**: Ao delegar mais tarefas para a GPU, o WebGPU reduz significativamente a carga de trabalho no JavaScript, resultando em melhor desempenho e experiências mais suaves.

Atualmente, o WebGPU é compatível com navegadores como o Google Chrome, com trabalhos em andamento para expandir o suporte a outras plataformas.

### 03.WebGPU
Ambiente Necessário:

**Navegadores compatíveis:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Ativar WebGPU:

- No Chrome/Microsoft Edge 

Ative a flag `chrome://flags/#enable-unsafe-webgpu`.

#### Abra o Navegador:
Inicie o Google Chrome ou o Microsoft Edge.

#### Acesse a Página de Flags:
Na barra de endereço, digite `chrome://flags` e pressione Enter.

#### Procure pela Flag:
Na caixa de busca no topo da página, digite 'enable-unsafe-webgpu'.

#### Ative a Flag:
Encontre a flag #enable-unsafe-webgpu na lista de resultados.

Clique no menu suspenso ao lado dela e selecione Enabled.

#### Reinicie o Navegador:

Após ativar a flag, será necessário reiniciar o navegador para que as alterações entrem em vigor. Clique no botão Relaunch que aparece na parte inferior da página.

- Para Linux, inicie o navegador com `--enable-features=Vulkan`.
- O Safari 18 (macOS 15) tem o WebGPU ativado por padrão.
- No Firefox Nightly, digite about:config na barra de endereço e `set dom.webgpu.enabled to true`.

### Configurando a GPU para o Microsoft Edge 

Aqui estão os passos para configurar uma GPU de alto desempenho para o Microsoft Edge no Windows:

- **Abra as Configurações:** Clique no menu Iniciar e selecione Configurações.
- **Configurações do Sistema:** Vá para Sistema e depois para Tela.
- **Configurações de Gráficos:** Role para baixo e clique em Configurações de gráficos.
- **Escolha o Aplicativo:** Em “Escolha um aplicativo para definir preferência,” selecione Aplicativo de desktop e depois Procurar.
- **Selecione o Edge:** Navegue até a pasta de instalação do Edge (geralmente `C:\Program Files (x86)\Microsoft\Edge\Application`) e selecione `msedge.exe`.
- **Defina a Preferência:** Clique em Opções, escolha Alto desempenho e depois clique em Salvar.
Isso garantirá que o Microsoft Edge use sua GPU de alto desempenho para obter um melhor desempenho.
- **Reinicie** sua máquina para que essas configurações entrem em vigor.

### Exemplos: Por favor, [clique neste link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.