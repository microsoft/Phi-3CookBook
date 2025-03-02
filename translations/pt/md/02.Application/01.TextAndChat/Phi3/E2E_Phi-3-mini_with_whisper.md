# Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

## Visão Geral

O Chatbot Interativo Phi 3 Mini 4K Instruct é uma ferramenta que permite aos usuários interagir com a demonstração do Microsoft Phi 3 Mini 4K Instruct utilizando entrada de texto ou áudio. O chatbot pode ser usado para diversas tarefas, como tradução, atualizações climáticas e obtenção de informações gerais.

### Primeiros Passos

Para usar este chatbot, siga estas instruções:

1. Abra um novo [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Na janela principal do notebook, você verá uma interface de chat com uma caixa de entrada de texto e um botão "Enviar".
3. Para usar o chatbot baseado em texto, basta digitar sua mensagem na caixa de entrada de texto e clicar no botão "Enviar". O chatbot responderá com um arquivo de áudio que pode ser reproduzido diretamente no notebook.

**Nota**: Esta ferramenta requer uma GPU e acesso aos modelos Microsoft Phi-3 e OpenAI Whisper, utilizados para reconhecimento de fala e tradução.

### Requisitos de GPU

Para executar esta demonstração, você precisa de 12 GB de memória de GPU.

Os requisitos de memória para executar a demonstração **Microsoft-Phi-3-Mini-4K Instruct** em uma GPU dependerão de vários fatores, como o tamanho dos dados de entrada (áudio ou texto), o idioma usado para tradução, a velocidade do modelo e a memória disponível na GPU.

De modo geral, o modelo Whisper foi projetado para rodar em GPUs. A quantidade mínima recomendada de memória de GPU para rodar o modelo Whisper é 8 GB, mas ele pode aproveitar quantidades maiores de memória, se disponíveis.

É importante notar que o processamento de grandes quantidades de dados ou um alto volume de solicitações no modelo pode exigir mais memória de GPU e/ou causar problemas de desempenho. Recomenda-se testar seu caso de uso com diferentes configurações e monitorar o uso de memória para determinar as configurações ideais para suas necessidades específicas.

## Exemplo E2E para Chatbot Interativo Phi 3 Mini 4K Instruct com Whisper

O notebook Jupyter intitulado [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) demonstra como usar a demonstração do Microsoft Phi 3 Mini 4K Instruct para gerar texto a partir de entrada de áudio ou texto escrito. O notebook define várias funções:

1. `tts_file_name(text)`: Esta função gera um nome de arquivo com base no texto de entrada para salvar o arquivo de áudio gerado.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Esta função utiliza a API Edge TTS para gerar um arquivo de áudio a partir de uma lista de fragmentos de texto de entrada. Os parâmetros de entrada são a lista de fragmentos, a velocidade da fala, o nome da voz e o caminho de saída para salvar o arquivo de áudio gerado.
1. `talk(input_text)`: Esta função gera um arquivo de áudio utilizando a API Edge TTS e o salva com um nome de arquivo aleatório no diretório /content/audio. O parâmetro de entrada é o texto de entrada a ser convertido em fala.
1. `run_text_prompt(message, chat_history)`: Esta função utiliza a demonstração do Microsoft Phi 3 Mini 4K Instruct para gerar um arquivo de áudio a partir de uma mensagem de entrada e adicioná-lo ao histórico de chat.
1. `run_audio_prompt(audio, chat_history)`: Esta função converte um arquivo de áudio em texto utilizando a API do modelo Whisper e o passa para a função `run_text_prompt()`.
1. O código lança um aplicativo Gradio que permite aos usuários interagir com a demonstração Phi 3 Mini 4K Instruct digitando mensagens ou enviando arquivos de áudio. A saída é exibida como uma mensagem de texto dentro do aplicativo.

## Solução de Problemas

Instalando drivers Cuda para GPU

1. Certifique-se de que suas aplicações Linux estão atualizadas

    ```bash
    sudo apt update
    ```

1. Instale os drivers Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Registre o local do driver Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Verifique o tamanho da memória da GPU Nvidia (Requer 12 GB de memória de GPU)

    ```bash
    nvidia-smi
    ```

1. Esvazie o cache: Se você estiver usando PyTorch, pode chamar torch.cuda.empty_cache() para liberar toda a memória cache não utilizada, para que possa ser usada por outras aplicações de GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Verifique o Cuda da Nvidia

    ```bash
    nvcc --version
    ```

1. Realize as seguintes tarefas para criar um token do Hugging Face.

    - Navegue até a [página de configurações de token do Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Selecione **Novo token**.
    - Insira o **Nome** do projeto que deseja usar.
    - Selecione o **Tipo** como **Write**.

> **Nota**
>
> Se você encontrar o seguinte erro:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Para resolver isso, digite o seguinte comando no terminal.
>
> ```bash
> sudo ldconfig
> ```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.