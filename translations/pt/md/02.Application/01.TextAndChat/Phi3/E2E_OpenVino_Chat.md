[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Este código exporta um modelo para o formato OpenVINO, carrega-o e o utiliza para gerar uma resposta a um prompt fornecido.

1. **Exportando o Modelo**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Este comando usa o `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importando Bibliotecas Necessárias**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Estas linhas importam classes do módulo `transformers` library and the `optimum.intel.openvino`, que são necessárias para carregar e usar o modelo.

3. **Configurando o Diretório e a Configuração do Modelo**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` é um dicionário que configura o modelo OpenVINO para priorizar baixa latência, usar um fluxo de inferência e não utilizar um diretório de cache.

4. **Carregando o Modelo**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Esta linha carrega o modelo do diretório especificado, utilizando as configurações definidas anteriormente. Também permite a execução remota de código, se necessário.

5. **Carregando o Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Esta linha carrega o tokenizer, que é responsável por converter texto em tokens que o modelo pode entender.

6. **Configurando os Argumentos do Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Este dicionário especifica que tokens especiais não devem ser adicionados à saída tokenizada.

7. **Definindo o Prompt**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Esta string configura um prompt de conversa onde o usuário pede ao assistente de IA para se apresentar.

8. **Tokenizando o Prompt**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Esta linha converte o prompt em tokens que o modelo pode processar, retornando o resultado como tensores PyTorch.

9. **Gerando uma Resposta**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Esta linha utiliza o modelo para gerar uma resposta com base nos tokens de entrada, com um máximo de 1024 novos tokens.

10. **Decodificando a Resposta**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Esta linha converte os tokens gerados de volta em uma string legível, ignorando quaisquer tokens especiais, e recupera o primeiro resultado.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.