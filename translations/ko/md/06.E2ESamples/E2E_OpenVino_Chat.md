[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

이 코드는 모델을 OpenVINO 형식으로 내보내고, 이를 로드하여 주어진 프롬프트에 대한 응답을 생성합니다.

1. **모델 내보내기**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 이 명령어는 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`를 사용합니다.

2. **필요한 라이브러리 가져오기**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 이 줄들은 `transformers` library and the `optimum.intel.openvino` 모듈에서 클래스를 가져옵니다. 이 클래스들은 모델을 로드하고 사용하는 데 필요합니다.

3. **모델 디렉토리 및 구성 설정**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config`는 OpenVINO 모델이 낮은 지연 시간을 우선시하고, 하나의 추론 스트림을 사용하며, 캐시 디렉토리를 사용하지 않도록 설정하는 딕셔너리입니다.

4. **모델 로드하기**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 이 줄은 지정된 디렉토리에서 모델을 로드하며, 이전에 정의된 구성 설정을 사용합니다. 필요하다면 원격 코드 실행도 허용합니다.

5. **토크나이저 로드하기**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 이 줄은 텍스트를 모델이 이해할 수 있는 토큰으로 변환하는 역할을 하는 토크나이저를 로드합니다.

6. **토크나이저 인수 설정하기**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 이 딕셔너리는 특수 토큰을 토크나이즈된 출력에 추가하지 않도록 지정합니다.

7. **프롬프트 정의하기**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 이 문자열은 사용자가 AI 어시스턴트에게 자기소개를 요청하는 대화 프롬프트를 설정합니다.

8. **프롬프트 토크나이즈하기**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 이 줄은 프롬프트를 모델이 처리할 수 있는 토큰으로 변환하여, 결과를 PyTorch 텐서로 반환합니다.

9. **응답 생성하기**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 이 줄은 입력 토큰을 기반으로 최대 1024개의 새로운 토큰을 생성하여 모델이 응답을 생성하도록 합니다.

10. **응답 디코딩하기**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 이 줄은 생성된 토큰을 사람이 읽을 수 있는 문자열로 변환하며, 특수 토큰을 건너뛰고 첫 번째 결과를 가져옵니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 우리는 정확성을 위해 노력하지만, 자동 번역에는 오류나 부정확성이 있을 수 있음을 유의하시기 바랍니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.