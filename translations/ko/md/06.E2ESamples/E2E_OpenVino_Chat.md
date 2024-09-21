[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

이 코드는 모델을 OpenVINO 형식으로 내보내고, 이를 로드하여 주어진 프롬프트에 대한 응답을 생성하는 예제입니다.

1. **모델 내보내기**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 이 명령어는 `optimum-cli` 도구를 사용하여 모델을 OpenVINO 형식으로 내보내며, 이는 효율적인 추론을 위해 최적화되어 있습니다.
   - 내보내는 모델은 `"microsoft/Phi-3-mini-4k-instruct"`이며, 과거 컨텍스트를 기반으로 텍스트를 생성하는 작업에 맞춰져 있습니다.
   - 모델의 가중치는 4비트 정수(`int4`)로 양자화되어 모델 크기를 줄이고 처리 속도를 높입니다.
   - `group-size`, `ratio`, `sym` 등의 다른 매개변수는 양자화 과정을 미세 조정하는 데 사용됩니다.
   - 내보낸 모델은 `./model/phi3-instruct/int4` 디렉토리에 저장됩니다.

2. **필요한 라이브러리 임포트**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 이 줄들은 `transformers` 라이브러리와 `optimum.intel.openvino` 모듈에서 클래스를 임포트하며, 이는 모델을 로드하고 사용하는 데 필요합니다.

3. **모델 디렉토리와 설정 구성**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir`는 모델 파일이 저장된 위치를 지정합니다.
   - `ov_config`는 OpenVINO 모델을 저지연으로 설정하고, 하나의 추론 스트림을 사용하며, 캐시 디렉토리를 사용하지 않도록 구성하는 딕셔너리입니다.

4. **모델 로드**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 이 줄은 지정된 디렉토리에서 모델을 로드하며, 앞서 정의한 설정을 사용합니다. 또한 필요시 원격 코드 실행을 허용합니다.

5. **토크나이저 로드**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 이 줄은 텍스트를 모델이 이해할 수 있는 토큰으로 변환하는 토크나이저를 로드합니다.

6. **토크나이저 인자 설정**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 이 딕셔너리는 토큰화된 출력에 특수 토큰을 추가하지 않도록 지정합니다.

7. **프롬프트 정의**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 이 문자열은 사용자가 AI 어시스턴트에게 자기소개를 요청하는 대화 프롬프트를 설정합니다.

8. **프롬프트 토큰화**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 이 줄은 프롬프트를 모델이 처리할 수 있는 토큰으로 변환하며, 결과를 PyTorch 텐서로 반환합니다.

9. **응답 생성**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 이 줄은 입력된 토큰을 기반으로 최대 1024개의 새로운 토큰으로 응답을 생성합니다.

10. **응답 디코딩**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 이 줄은 생성된 토큰을 다시 사람이 읽을 수 있는 문자열로 변환하며, 특수 토큰은 생략하고 첫 번째 결과를 가져옵니다.

면책 조항: 이 번역은 원본을 AI 모델에 의해 번역된 것이며 완벽하지 않을 수 있습니다. 출력된 내용을 검토하시고 필요한 수정 사항이 있으면 수정해 주시기 바랍니다.