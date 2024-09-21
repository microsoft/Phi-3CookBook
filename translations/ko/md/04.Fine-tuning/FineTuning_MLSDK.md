
os 모듈을 가져오면 운영 체제에 의존하는 기능을 이식성 있게 사용할 수 있습니다. os.system 함수를 사용하여 특정 명령줄 인수를 사용하여 쉘에서 download-dataset.py 스크립트를 실행합니다. 인수는 다운로드할 데이터셋(HuggingFaceH4/ultrachat_200k), 다운로드할 디렉터리(ultrachat_200k_dataset), 그리고 데이터셋을 나눌 비율(5)을 지정합니다. os.system 함수는 실행한 명령의 종료 상태를 반환하며, 이 상태는 exit_status 변수에 저장됩니다. exit_status가 0이 아닌지 확인합니다. 유닉스 계열 운영 체제에서는 종료 상태가 0이면 명령이 성공했음을 의미하며, 다른 숫자는 오류를 나타냅니다. exit_status가 0이 아니면 데이터셋을 다운로드하는 중 오류가 발생했음을 나타내는 메시지와 함께 예외를 발생시킵니다. 요약하자면, 이 스크립트는 헬퍼 스크립트를 사용하여 데이터셋을 다운로드하는 명령을 실행하며, 명령이 실패하면 예외를 발생시킵니다.
```
# 운영 체제에 의존하는 기능을 사용할 수 있는 방법을 제공하는 os 모듈을 가져옵니다.
import os

# 특정 명령줄 인수를 사용하여 쉘에서 download-dataset.py 스크립트를 실행하기 위해 os.system 함수를 사용합니다.
# 인수는 다운로드할 데이터셋(HuggingFaceH4/ultrachat_200k), 다운로드할 디렉터리(ultrachat_200k_dataset), 그리고 데이터셋을 나눌 비율(5)을 지정합니다.
# os.system 함수는 실행한 명령의 종료 상태를 반환하며, 이 상태는 exit_status 변수에 저장됩니다.
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# exit_status가 0이 아닌지 확인합니다.
# 유닉스 계열 운영 체제에서는 종료 상태가 0이면 명령이 성공했음을 의미하며, 다른 숫자는 오류를 나타냅니다.
# exit_status가 0이 아니면 데이터셋을 다운로드하는 중 오류가 발생했음을 나타내는 메시지와 함께 예외를 발생시킵니다.
if exit_status != 0:
    raise Exception("Error downloading dataset")
```
### 데이터프레임으로 데이터 로드하기
이 Python 스크립트는 JSON Lines 파일을 pandas 데이터프레임으로 로드하고 첫 5개의 행을 표시합니다. 다음은 이 스크립트의 기능에 대한 설명입니다:

pandas 라이브러리를 가져옵니다. pandas는 강력한 데이터 조작 및 분석 라이브러리입니다.

pandas의 표시 옵션에서 최대 열 너비를 0으로 설정합니다. 이렇게 하면 데이터프레임을 출력할 때 각 열의 전체 텍스트가 잘리지 않고 표시됩니다.

pd.read_json 함수를 사용하여 ultrachat_200k_dataset 디렉터리의 train_sft.jsonl 파일을 데이터프레임으로 로드합니다. lines=True 인수는 파일이 각 줄이 개별 JSON 객체인 JSON Lines 형식임을 나타냅니다.

head 메서드를 사용하여 데이터프레임의 첫 5개의 행을 표시합니다. 데이터프레임에 5개 미만의 행이 있는 경우 모든 행을 표시합니다.

요약하자면, 이 스크립트는 JSON Lines 파일을 데이터프레임으로 로드하고 첫 5개의 행을 전체 열 텍스트와 함께 표시합니다.

```
# 강력한 데이터 조작 및 분석 라이브러리인 pandas를 가져옵니다.
import pandas as pd

# pandas의 표시 옵션에서 최대 열 너비를 0으로 설정합니다.
# 이렇게 하면 데이터프레임을 출력할 때 각 열의 전체 텍스트가 잘리지 않고 표시됩니다.
pd.set_option("display.max_colwidth", 0)

# pd.read_json 함수를 사용하여 ultrachat_200k_dataset 디렉터리의 train_sft.jsonl 파일을 데이터프레임으로 로드합니다.
# lines=True 인수는 파일이 각 줄이 개별 JSON 객체인 JSON Lines 형식임을 나타냅니다.
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# head 메서드를 사용하여 데이터프레임의 첫 5개의 행을 표시합니다.
# 데이터프레임에 5개 미만의 행이 있는 경우 모든 행을 표시합니다.
df.head()
```
## 5. 모델과 데이터를 입력으로 사용하여 파인 튜닝 작업 제출하기
chat-completion 파이프라인 구성 요소를 사용하는 작업을 만듭니다. 파인 튜닝에 지원되는 모든 매개변수에 대해 자세히 알아보세요.

### 파인 튜닝 매개변수 정의하기

파인 튜닝 매개변수는 두 가지 범주로 나눌 수 있습니다 - 훈련 매개변수, 최적화 매개변수

훈련 매개변수는 다음과 같은 훈련 측면을 정의합니다 -

- 사용할 옵티마이저, 스케줄러
- 파인 튜닝을 최적화할 메트릭
- 훈련 단계 수 및 배치 크기 등
- 최적화 매개변수는 GPU 메모리를 최적화하고 컴퓨팅 자원을 효과적으로 사용하는 데 도움을 줍니다.

아래는 이 범주에 속하는 몇 가지 매개변수입니다. 최적화 매개변수는 각 모델마다 다르며, 이러한 변동을 처리하기 위해 모델과 함께 패키지됩니다.

- deepspeed와 LoRA 활성화
- 혼합 정밀도 훈련 활성화
- 다중 노드 훈련 활성화

**Note:** 지도 학습 파인 튜닝은 정렬 손실 또는 치명적인 망각을 초래할 수 있습니다. 이러한 문제를 확인하고 파인 튜닝 후 정렬 단계를 실행하는 것을 권장합니다.

### 파인 튜닝 매개변수

이 Python 스크립트는 기계 학습 모델을 파인 튜닝하기 위한 매개변수를 설정합니다. 다음은 이 스크립트의 기능에 대한 설명입니다:

기본 훈련 매개변수를 설정합니다. 여기에는 훈련 에포크 수, 훈련 및 평가 배치 크기, 학습률, 학습률 스케줄러 유형이 포함됩니다.

기본 최적화 매개변수를 설정합니다. 여기에는 Layer-wise Relevance Propagation (LoRa) 및 DeepSpeed 적용 여부, DeepSpeed 단계가 포함됩니다.

훈련 및 최적화 매개변수를 finetune_parameters라는 단일 딕셔너리로 결합합니다.

foundation_model에 모델별 기본 매개변수가 있는지 확인합니다. 있는 경우 경고 메시지를 출력하고, finetune_parameters 딕셔너리를 모델별 기본값으로 업데이트합니다. ast.literal_eval 함수는 모델별 기본값을 문자열에서 Python 딕셔너리로 변환하는 데 사용됩니다.

실행에 사용할 최종 파인 튜닝 매개변수를 출력합니다.

요약하자면, 이 스크립트는 기계 학습 모델을 파인 튜닝하기 위한 매개변수를 설정하고 표시하며, 모델별 기본값으로 기본 매개변수를 덮어쓸 수 있는 기능을 제공합니다.

```
# 기본 훈련 매개변수를 설정합니다. 여기에는 훈련 에포크 수, 훈련 및 평가 배치 크기, 학습률, 학습률 스케줄러 유형이 포함됩니다.
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 기본 최적화 매개변수를 설정합니다. 여기에는 Layer-wise Relevance Propagation (LoRa) 및 DeepSpeed 적용 여부, DeepSpeed 단계가 포함됩니다.
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# 훈련 및 최적화 매개변수를 finetune_parameters라는 단일 딕셔너리로 결합합니다.
finetune_parameters = {**training_parameters, **optimization_parameters}

# foundation_model에 모델별 기본 매개변수가 있는지 확인합니다.
# 있는 경우 경고 메시지를 출력하고, finetune_parameters 딕셔너리를 모델별 기본값으로 업데이트합니다.
# ast.literal_eval 함수는 모델별 기본값을 문자열에서 Python 딕셔너리로 변환하는 데 사용됩니다.
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # 문자열을 Python 딕셔너리로 변환
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 실행에 사용할 최종 파인 튜닝 매개변수를 출력합니다.
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 훈련 파이프라인
이 Python 스크립트는 기계 학습 훈련 파이프라인의 표시 이름을 생성하는 함수를 정의하고, 이 함수를 호출하여 표시 이름을 생성하고 출력합니다. 다음은 이 스크립트의 기능에 대한 설명입니다:

get_pipeline_display_name 함수를 정의합니다. 이 함수는 훈련 파이프라인과 관련된 다양한 매개변수를 기반으로 표시 이름을 생성합니다.

함수 내부에서 장치당 배치 크기, 그라디언트 누적 단계 수, 노드당 GPU 수, 파인 튜닝에 사용되는 노드 수를 곱하여 총 배치 크기를 계산합니다.

학습률 스케줄러 유형, DeepSpeed 적용 여부, DeepSpeed 단계, Layer-wise Relevance Propagation (LoRa) 적용 여부, 모델 체크포인트 유지 한도, 최대 시퀀스 길이 등의 다양한 다른 매개변수를 가져옵니다.

이 모든 매개변수를 하이픈으로 구분하여 문자열을 구성합니다. DeepSpeed 또는 LoRa가 적용된 경우, 문자열에 DeepSpeed 단계 또는 LoRa를 포함하고, 그렇지 않은 경우 nods 또는 nolora를 포함합니다.

이 문자열을 반환하여 훈련 파이프라인의 표시 이름으로 사용합니다.

함수가 정의된 후, 함수를 호출하여 표시 이름을 생성하고 이를 출력합니다.

요약하자면, 이 스크립트는 다양한 매개변수를 기반으로 기계 학습 훈련 파이프라인의 표시 이름을 생성하고 이를 출력합니다.

```
# 훈련 파이프라인의 표시 이름을 생성하는 함수를 정의합니다.
def get_pipeline_display_name():
    # 장치당 배치 크기, 그라디언트 누적 단계 수, 노드당 GPU 수, 파인 튜닝에 사용되는 노드 수를 곱하여 총 배치 크기를 계산합니다.
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 학습률 스케줄러 유형을 가져옵니다.
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # DeepSpeed 적용 여부를 가져옵니다.
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # DeepSpeed 단계를 가져옵니다.
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # DeepSpeed가 적용된 경우, 표시 이름에 DeepSpeed 단계를 포함하고, 그렇지 않은 경우 nods를 포함합니다.
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # Layer-wise Relevance Propagation (LoRa) 적용 여부를 가져옵니다.
    lora = finetune_parameters.get("apply_lora", "false")
    # LoRa가 적용된 경우, 표시 이름에 lora를 포함하고, 그렇지 않은 경우 nolora를 포함합니다.
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 모델 체크포인트 유지 한도를 가져옵니다.
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 최대 시퀀스 길이를 가져옵니다.
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 이 모든 매개변수를 하이픈으로 구분하여 문자열을 구성합니다.
    return (
        model_name
        + "-"
        + "ultrachat"
        + "-"
        + f"bs{batch_size}"
        + "-"
        + f"{scheduler}"
        + "-"
        + ds_string
        + "-"
        + lora_string
        + f"-save_limit{save_limit}"
        + f"-seqlen{seq_len}"
    )

# 함수를 호출하여 표시 이름을 생성합니다.
pipeline_display_name = get_pipeline_display_name()
# 표시 이름을 출력합니다.
print(f"Display name used for the run: {pipeline_display_name}")
```
### 파이프라인 구성

이 Python 스크립트는 Azure Machine Learning SDK를 사용하여 기계 학습 파이프라인을 정의하고 구성합니다. 다음은 이 스크립트의 기능에 대한 설명입니다:

1. Azure AI ML SDK에서 필요한 모듈을 가져옵니다.

2. 레지스트리에서 "chat_completion_pipeline"이라는 파이프라인 구성 요소를 가져옵니다.

3. `@pipeline` 데코레이터와 `create_pipeline` 함수를 사용하여 파이프라인 작업을 정의합니다. 파이프라인의 이름은 `pipeline_display_name`으로 설정됩니다.

4. `create_pipeline` 함수 내부에서, 다양한 매개변수를 사용하여 가져온 파이프라인 구성 요소를 초기화합니다. 여기에는 모델 경로, 다양한 단계에 대한 컴퓨팅 클러스터, 훈련 및 테스트를 위한 데이터셋 분할, 파인 튜닝에 사용할 GPU 수 및 기타 파인 튜닝 매개변수가 포함됩니다.

5. 파인 튜닝 작업의 출력을 파이프라인 작업의 출력에 매핑합니다. 이렇게 하면 파인 튜닝된 모델을 쉽게 등록할 수 있습니다. 모델을 등록하는 것은 모델을 온라인 또는 배치 엔드포인트에 배포하는 데 필요합니다.

6. `create_pipeline` 함수를 호출하여 파이프라인 인스턴스를 생성합니다.

7. 이전 작업의 캐시된 결과를 사용하지 않도록 파이프라인의 `force_rerun` 설정을 `True`로 설정합니다.

8. 파이프라인의 `continue_on_step_failure` 설정을 `False`로 설정합니다. 이는 단계 중 하나라도 실패하면 파이프라인이 중지됨을 의미합니다.

요약하자면, 이 스크립트는 Azure Machine Learning SDK를 사용하여 채팅 완료 작업을 위한 기계 학습 파이프라인을 정의하고 구성합니다.

```
# Azure AI ML SDK에서 필요한 모듈을 가져옵니다.
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 레지스트리에서 "chat_completion_pipeline"이라는 파이프라인 구성 요소를 가져옵니다.
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# @pipeline 데코레이터와 create_pipeline 함수를 사용하여 파이프라인 작업을 정의합니다.
# 파이프라인의 이름은 pipeline_display_name으로 설정됩니다.
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 다양한 매개변수를 사용하여 가져온 파이프라인 구성 요소를 초기화합니다.
    # 여기에는 모델 경로, 다양한 단계에 대한 컴퓨팅 클러스터, 훈련 및 테스트를 위한 데이터셋 분할, 파인 튜닝에 사용할 GPU 수 및 기타 파인 튜닝 매개변수가 포함됩니다.
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 데이터셋 분할을 매개변수에 매핑합니다.
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 훈련 설정
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 사용할 GPU 수를 설정합니다.
        **finetune_parameters
    )
    return {
        # 파인 튜닝 작업의 출력을 파이프라인 작업의 출력에 매핑합니다.
        # 이렇게 하면 파인 튜닝된 모델을 쉽게 등록할 수 있습니다.
        # 모델을 등록하는 것은 모델을 온라인 또는 배치 엔드포인트에 배포하는 데 필요합니다.
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# create_pipeline 함수를 호출하여 파이프라인 인스턴스를 생성합니다.
pipeline_object = create_pipeline()

# 이전 작업의 캐시된 결과를 사용하지 않도록 설정합니다.
pipeline_object.settings.force_rerun = True

# 단계 중 하나라도 실패하면 파이프라인이 중지되도록 설정합니다.
pipeline_object.settings.continue_on_step_failure = False
```
### 작업 제출

이 Python 스크립트는 Azure Machine Learning 워크스페이스에 기계 학습 파이프라인 작업을 제출한 다음 작업이 완료될 때까지 기다립니다. 다음은 이 스크립트의 기능에 대한 설명입니다:

create_or_update 메서드를 호출하여 파이프라인 작업을 제출합니다. 실행할 파이프라인은 pipeline_object로 지정되며, 작업이 실행될 실험은 experiment_name으로 지정됩니다.

jobs 객체의 stream 메서드를 호출하여 파이프라인 작업이 완료될 때까지 기다립니다. 기다릴 작업은 pipeline_job 객체의 name 속성으로 지정됩니다.

요약하자면, 이 스크립트는 Azure Machine Learning 워크스페이스에 기계 학습 파이프라인 작업을 제출하고 작업이 완료
```
# Azure AI ML SDK에서 필요한 모듈을 임포트
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 파이프라인 작업에서 `trained_model` 출력이 사용 가능한지 확인
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 파이프라인 작업 이름과 출력 이름("trained_model")을 사용하여 학습된 모델의 경로를 구성
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 원본 모델 이름에 "-ultrachat-200k"를 추가하고 슬래시를 하이픈으로 대체하여 미세 조정된 모델 이름 정의
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 다양한 매개변수로 Model 객체를 생성하여 모델 등록 준비
# 여기에는 모델 경로, 모델 유형(MLflow 모델), 모델 이름 및 버전, 모델 설명이 포함됨
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 버전 충돌을 피하기 위해 타임스탬프를 버전으로 사용
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# Model 객체를 인수로 사용하여 workspace_ml_client의 models 객체의 create_or_update 메서드를 호출하여 모델 등록
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 등록된 모델 출력
print("registered model: \n", registered_model)
```
## 7. 미세 조정된 모델을 온라인 엔드포인트에 배포하기
온라인 엔드포인트는 모델을 사용해야 하는 애플리케이션과 통합할 수 있는 지속적인 REST API를 제공합니다.

### 엔드포인트 관리
이 Python 스크립트는 Azure Machine Learning에서 등록된 모델을 위한 관리형 온라인 엔드포인트를 생성합니다. 다음은 이 스크립트가 하는 일에 대한 설명입니다:

필요한 모듈을 Azure AI ML SDK에서 가져옵니다.

"ultrachat-completion-" 문자열에 타임스탬프를 추가하여 온라인 엔드포인트의 고유 이름을 정의합니다.

여러 매개변수를 포함한 ManagedOnlineEndpoint 객체를 생성하여 온라인 엔드포인트를 생성할 준비를 합니다. 여기에는 엔드포인트 이름, 엔드포인트 설명 및 인증 모드("key")가 포함됩니다.

workspace_ml_client의 begin_create_or_update 메서드를 ManagedOnlineEndpoint 객체와 함께 호출하여 온라인 엔드포인트를 생성합니다. 그런 다음 wait 메서드를 호출하여 생성 작업이 완료될 때까지 기다립니다.

요약하면, 이 스크립트는 Azure Machine Learning에서 등록된 모델을 위한 관리형 온라인 엔드포인트를 생성합니다.

```
# Azure AI ML SDK에서 필요한 모듈 가져오기
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# "ultrachat-completion-" 문자열에 타임스탬프를 추가하여 온라인 엔드포인트의 고유 이름 정의
online_endpoint_name = "ultrachat-completion-" + timestamp

# 여러 매개변수를 포함한 ManagedOnlineEndpoint 객체를 생성하여 온라인 엔드포인트를 생성할 준비
# 여기에는 엔드포인트 이름, 엔드포인트 설명 및 인증 모드("key")가 포함됩니다
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# workspace_ml_client의 begin_create_or_update 메서드를 ManagedOnlineEndpoint 객체와 함께 호출하여 온라인 엔드포인트 생성
# 그런 다음 wait 메서드를 호출하여 생성 작업이 완료될 때까지 기다립니다
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
배포를 지원하는 SKU 목록은 여기에서 찾을 수 있습니다 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML 모델 배포

이 Python 스크립트는 등록된 머신러닝 모델을 Azure Machine Learning의 관리형 온라인 엔드포인트에 배포합니다. 다음은 이 스크립트가 하는 일에 대한 설명입니다:

Python 추상 구문 트리(grammar) 처리를 위한 함수들을 제공하는 ast 모듈을 가져옵니다.

배포를 위한 인스턴스 유형을 "Standard_NC6s_v3"로 설정합니다.

foundation 모델에 inference_compute_allow_list 태그가 있는지 확인합니다. 만약 있다면, 태그 값을 문자열에서 Python 리스트로 변환하여 inference_computes_allow_list에 할당합니다. 그렇지 않으면 inference_computes_allow_list를 None으로 설정합니다.

지정된 인스턴스 유형이 허용 목록에 있는지 확인합니다. 만약 그렇지 않다면, 사용자가 허용 목록에서 인스턴스 유형을 선택하도록 메시지를 출력합니다.

여러 매개변수를 포함한 ManagedOnlineDeployment 객체를 생성하여 배포를 생성할 준비를 합니다. 여기에는 배포 이름, 엔드포인트 이름, 모델 ID, 인스턴스 유형 및 개수, 라이브니스 프로브 설정 및 요청 설정이 포함됩니다.

workspace_ml_client의 begin_create_or_update 메서드를 ManagedOnlineDeployment 객체와 함께 호출하여 배포를 생성합니다. 그런 다음 wait 메서드를 호출하여 생성 작업이 완료될 때까지 기다립니다.

엔드포인트 트래픽을 "demo" 배포로 100% 지정합니다.

workspace_ml_client의 begin_create_or_update 메서드를 endpoint 객체와 함께 호출하여 엔드포인트를 업데이트합니다. 그런 다음 result 메서드를 호출하여 업데이트 작업이 완료될 때까지 기다립니다.

요약하면, 이 스크립트는 등록된 머신러닝 모델을 Azure Machine Learning의 관리형 온라인 엔드포인트에 배포합니다.

```
# Python 추상 구문 트리(grammar) 처리를 위한 함수들을 제공하는 ast 모듈 가져오기
import ast

# 배포를 위한 인스턴스 유형 설정
instance_type = "Standard_NC6s_v3"

# foundation 모델에 `inference_compute_allow_list` 태그가 있는지 확인
if "inference_compute_allow_list" in foundation_model.tags:
    # 만약 있다면, 태그 값을 문자열에서 Python 리스트로 변환하여 `inference_computes_allow_list`에 할당
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 그렇지 않으면 `inference_computes_allow_list`를 `None`으로 설정
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# 지정된 인스턴스 유형이 허용 목록에 있는지 확인
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# 여러 매개변수를 포함한 `ManagedOnlineDeployment` 객체를 생성하여 배포를 생성할 준비
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# workspace_ml_client의 `begin_create_or_update` 메서드를 `ManagedOnlineDeployment` 객체와 함께 호출하여 배포 생성
# 그런 다음 wait 메서드를 호출하여 생성 작업이 완료될 때까지 기다립니다
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 엔드포인트 트래픽을 "demo" 배포로 100% 지정
endpoint.traffic = {"demo": 100}

# workspace_ml_client의 `begin_create_or_update` 메서드를 `endpoint` 객체와 함께 호출하여 엔드포인트 업데이트
# 그런 다음 result 메서드를 호출하여 업데이트 작업이 완료될 때까지 기다립니다
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. 샘플 데이터로 엔드포인트 테스트
테스트 데이터셋에서 일부 샘플 데이터를 가져와 온라인 엔드포인트에 제출하여 추론을 수행합니다. 그런 다음 예측된 레이블을 실제 레이블과 함께 표시합니다.

### 결과 읽기
이 Python 스크립트는 JSON Lines 파일을 pandas DataFrame으로 읽어들이고, 랜덤 샘플을 추출하며, 인덱스를 재설정합니다. 다음은 이 스크립트가 하는 일에 대한 설명입니다:

./ultrachat_200k_dataset/test_gen.jsonl 파일을 pandas DataFrame으로 읽어들입니다. 파일이 JSON Lines 형식이므로 read_json 함수에 lines=True 인수를 사용합니다. 이 형식에서는 각 줄이 별도의 JSON 객체입니다.

DataFrame에서 1개의 랜덤 행을 샘플링합니다. sample 함수에 n=1 인수를 사용하여 선택할 랜덤 행의 수를 지정합니다.

DataFrame의 인덱스를 재설정합니다. reset_index 함수에 drop=True 인수를 사용하여 원래 인덱스를 삭제하고 기본 정수 값의 새로운 인덱스로 대체합니다.

head 함수에 2 인수를 사용하여 DataFrame의 첫 두 행을 표시합니다. 그러나 샘플링 후 DataFrame에는 하나의 행만 포함되므로, 이 행만 표시됩니다.

요약하면, 이 스크립트는 JSON Lines 파일을 pandas DataFrame으로 읽어들이고, 1개의 랜덤 행을 샘플링하며, 인덱스를 재설정하고, 첫 행을 표시합니다.

```
# pandas 라이브러리 가져오기
import pandas as pd

# JSON Lines 파일 './ultrachat_200k_dataset/test_gen.jsonl'을 pandas DataFrame으로 읽어들임
# 'lines=True' 인수는 파일이 각 줄이 별도의 JSON 객체인 JSON Lines 형식임을 나타냄
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# DataFrame에서 1개의 랜덤 행 샘플링
# 'n=1' 인수는 선택할 랜덤 행의 수를 지정함
test_df = test_df.sample(n=1)

# DataFrame의 인덱스 재설정
# 'drop=True' 인수는 원래 인덱스를 삭제하고 기본 정수 값의 새로운 인덱스로 대체함을 나타냄
# 'inplace=True' 인수는 DataFrame을 제자리에서 수정함을 나타냄 (새 객체를 생성하지 않음)
test_df.reset_index(drop=True, inplace=True)

# DataFrame의 첫 두 행 표시
# 그러나 샘플링 후 DataFrame에는 하나의 행만 포함되므로, 이 행만 표시됨
test_df.head(2)
```
### JSON 객체 생성

이 Python 스크립트는 특정 매개변수를 포함한 JSON 객체를 생성하여 파일에 저장합니다. 다음은 이 스크립트가 하는 일에 대한 설명입니다:

json 모듈을 가져옵니다. 이 모듈은 JSON 데이터를 다루기 위한 함수를 제공합니다.

매개변수를 나타내는 키와 값을 가진 dictionary parameters를 생성합니다. 키는 "temperature", "top_p", "do_sample", "max_new_tokens"이며, 해당 값은 각각 0.6, 0.9, True, 200입니다.

두 개의 키 "input_data"와 "params"를 가진 또 다른 dictionary test_json을 생성합니다. "input_data"의 값은 "input_string"과 "parameters" 키를 가진 또 다른 dictionary입니다. "input_string"의 값은 test_df DataFrame의 첫 메시지를 포함하는 리스트입니다. "parameters"의 값은 이전에 생성된 parameters dictionary입니다. "params"의 값은 빈 dictionary입니다.

sample_score.json 파일을 엽니다.

```
# JSON 데이터를 다루기 위한 함수를 제공하는 json 모듈 가져오기
import json

# 매개변수를 나타내는 키와 값을 가진 dictionary `parameters` 생성
# 키는 "temperature", "top_p", "do_sample", "max_new_tokens"이며, 해당 값은 각각 0.6, 0.9, True, 200입니다
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 두 개의 키 "input_data"와 "params"를 가진 또 다른 dictionary `test_json` 생성
# "input_data"의 값은 "input_string"과 "parameters" 키를 가진 또 다른 dictionary
# "input_string"의 값은 test_df DataFrame의 첫 메시지를 포함하는 리스트
# "parameters"의 값은 이전에 생성된 parameters dictionary
# "params"의 값은 빈 dictionary
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# `./ultrachat_200k_dataset` 디렉터리에 있는 `sample_score.json` 파일을 쓰기 모드로 열기
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # `test_json` dictionary를 JSON 형식으로 파일에 쓰기 위해 `json.dump` 함수 사용
    json.dump(test_json, f)
```
### 엔드포인트 호출

이 Python 스크립트는 Azure Machine Learning에서 온라인 엔드포인트를 호출하여 JSON 파일을 점수화합니다. 다음은 이 스크립트가 하는 일에 대한 설명입니다:

workspace_ml_client 객체의 online_endpoints 속성의 invoke 메서드를 호출합니다. 이 메서드는 온라인 엔드포인트에 요청을 보내고 응답을 받기 위해 사용됩니다.

endpoint_name과 deployment_name 인수로 엔드포인트와 배포의 이름을 지정합니다. 이 경우, 엔드포인트 이름은 online_endpoint_name 변수에 저장되어 있으며, 배포 이름은 "demo"입니다.

request_file 인수로 점수화할 JSON 파일의 경로를 지정합니다. 이 경우, 파일은 ./ultrachat_200k_dataset/sample_score.json입니다.

엔드포인트의 응답을 response 변수에 저장합니다.

원시 응답을 출력합니다.

요약하면, 이 스크립트는 Azure Machine Learning에서 온라인 엔드포인트를 호출하여 JSON 파일을 점수화하고 응답을 출력합니다.

```
# Azure Machine Learning에서 온라인 엔드포인트를 호출하여 `sample_score.json` 파일을 점수화
# `workspace_ml_client` 객체의 `online_endpoints` 속성의 `invoke` 메서드는 온라인 엔드포인트에 요청을 보내고 응답을 받기 위해 사용됨
# `endpoint_name` 인수는 엔드포인트 이름을 지정하며, 이는 `online_endpoint_name` 변수에 저장됨
# `deployment_name` 인수는 배포 이름을 지정하며, 이는 "demo"임
# `request_file` 인수는 점수화할 JSON 파일의 경로를 지정하며, 이는 `./ultrachat_200k_dataset/sample_score.json`임
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 엔드포인트의 원시 응답 출력
print("raw response: \n", response, "\n")
```
## 9. 온라인 엔드포인트 삭제
엔드포인트를 삭제하지 않으면 엔드포인트에서 사용된 컴퓨팅 비용이 계속 청구되므로 온라인 엔드포인트를 삭제하는 것을 잊지 마세요. 이 Python 코드 줄은 Azure Machine Learning에서 온라인 엔드포인트를 삭제합니다. 다음은 이 코드가 하는 일에 대한 설명입니다:

workspace_ml_client 객체의 online_endpoints 속성의 begin_delete 메서드를 호출합니다. 이 메서드는 온라인 엔드포인트의 삭제를 시작하는 데 사용됩니다.

name 인수로 삭제할 엔드포인트의 이름을 지정합니다. 이 경우, 엔드포인트 이름은 online_endpoint_name 변수에 저장되어 있습니다.

wait 메서드를 호출하여 삭제 작업이 완료될 때까지 기다립니다. 이는 블로킹 작업으로, 삭제가 완료될 때까지 스크립트의 진행을 막습니다.

요약하면, 이 코드 줄은 Azure Machine Learning에서 온라인 엔드포인트의 삭제를 시작하고 작업이 완료될 때까지 기다립니다.

```
# Azure Machine Learning에서 온라인 엔드포인트 삭제
# `workspace_ml_client` 객체의 `online_endpoints` 속성의 `begin_delete` 메서드는 온라인 엔드포인트의 삭제를 시작하는 데 사용됨
# `name` 인수는 삭제할 엔드포인트의 이름을 지정하며, 이는 `online_endpoint_name` 변수에 저장됨
# `wait` 메서드를 호출하여 삭제 작업이 완료될 때까지 기다림. 이는 블로킹 작업으로, 삭제가 완료될 때까지 스크립트의 진행을 막음
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

면책 조항: 이 번역은 AI 모델에 의해 원본에서 번역되었으며 완벽하지 않을 수 있습니다. 출력물을 검토하시고 필요한 수정 사항을 반영해 주시기 바랍니다.