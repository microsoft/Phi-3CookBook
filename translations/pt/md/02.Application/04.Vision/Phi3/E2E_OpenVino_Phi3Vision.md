Este demo demonstra como usar um modelo pré-treinado para gerar código Python com base em uma imagem e um texto de comando.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Aqui está uma explicação passo a passo:

1. **Importações e Configuração**:
   - As bibliotecas e módulos necessários são importados, incluindo `requests`, `PIL` para processamento de imagens e `transformers` para manipular o modelo e processar os dados.

2. **Carregando e Exibindo a Imagem**:
   - Um arquivo de imagem (`demo.png`) é aberto usando a biblioteca `PIL` e exibido.

3. **Definindo o Comando**:
   - Uma mensagem é criada que inclui a imagem e uma solicitação para gerar código Python que processe a imagem e a salve usando `plt` (matplotlib).

4. **Carregando o Processador**:
   - O `AutoProcessor` é carregado de um modelo pré-treinado especificado pelo diretório `out_dir`. Este processador irá lidar com as entradas de texto e imagem.

5. **Criando o Comando**:
   - O método `apply_chat_template` é usado para formatar a mensagem em um comando adequado para o modelo.

6. **Processando as Entradas**:
   - O comando e a imagem são processados em tensores que o modelo pode entender.

7. **Definindo Argumentos de Geração**:
   - Argumentos para o processo de geração do modelo são definidos, incluindo o número máximo de novos tokens a serem gerados e se a saída será amostrada.

8. **Gerando o Código**:
   - O modelo gera o código Python com base nas entradas e nos argumentos de geração. O `TextStreamer` é usado para manipular a saída, ignorando o comando e os tokens especiais.

9. **Saída**:
   - O código gerado é exibido, devendo incluir o código Python para processar a imagem e salvá-la conforme especificado no comando.

Este demo ilustra como aproveitar um modelo pré-treinado usando OpenVino para gerar código dinamicamente com base na entrada do usuário e em imagens.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.