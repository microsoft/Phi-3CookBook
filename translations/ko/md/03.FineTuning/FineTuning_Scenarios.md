## 세부 조정 시나리오

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.25759a0154a97ad90e43a6cace37d6bea87f0ac0236ada3ad5d4a1fbacc3bdf7.ko.png)

**플랫폼** 여기에는 Azure AI Foundry, Azure Machine Learning, AI Tools, Kaito, ONNX Runtime과 같은 다양한 기술이 포함됩니다.

**인프라** 여기에는 세부 조정 프로세스에서 필수적인 CPU와 FPGA가 포함됩니다. 각 기술의 아이콘을 보여드리겠습니다.

**도구 및 프레임워크** 여기에는 ONNX Runtime과 ONNX Runtime이 포함됩니다. 각 기술의 아이콘을 보여드리겠습니다.  
[ONNX Runtime 및 ONNX Runtime 아이콘 삽입]

Microsoft 기술을 사용한 세부 조정 프로세스는 다양한 구성 요소와 도구를 포함합니다. 이러한 기술을 이해하고 활용함으로써 애플리케이션을 효과적으로 세부 조정하고 더 나은 솔루션을 만들 수 있습니다.

## 서비스형 모델

호스팅된 세부 조정을 사용하여 컴퓨팅을 생성하고 관리할 필요 없이 모델을 세부 조정합니다.

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.6184d80a336ea9d7bb67a581e9e5d0b021cafdffff7ba257c2012e2123e0d77e.ko.png)

서버리스 세부 조정은 Phi-3-mini 및 Phi-3-medium 모델에서 사용할 수 있으며, 개발자가 클라우드 및 엣지 시나리오에 맞게 모델을 빠르고 쉽게 맞춤화할 수 있도록 합니다. 또한, Phi-3-small 모델이 이제 Models-as-a-Service 제공을 통해 사용 가능하다는 것을 발표했으며, 이를 통해 개발자는 기본 인프라를 관리하지 않고도 AI 개발을 빠르게 시작할 수 있습니다.

## 플랫폼형 모델

사용자가 자체 컴퓨팅을 관리하여 모델을 세부 조정합니다.

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.cf8b08ef05bf57f362da90834be87562502f4370de4a7325a9fb03b8c008e5e7.ko.png)

[세부 조정 샘플](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 세부 조정 시나리오

| | | | | | | |
|-|-|-|-|-|-|-|
|시나리오|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|사전 학습된 LLM을 특정 작업 또는 도메인에 맞게 조정|Yes|Yes|Yes|Yes|Yes|Yes|
|텍스트 분류, 개체명 인식, 기계 번역과 같은 NLP 작업을 위한 세부 조정|Yes|Yes|Yes|Yes|Yes|Yes|
|QA 작업을 위한 세부 조정|Yes|Yes|Yes|Yes|Yes|Yes|
|챗봇에서 인간과 유사한 응답을 생성하기 위한 세부 조정|Yes|Yes|Yes|Yes|Yes|Yes|
|음악, 예술 또는 기타 창의적 결과물을 생성하기 위한 세부 조정|Yes|Yes|Yes|Yes|Yes|Yes|
|컴퓨팅 및 재정적 비용 절감|Yes|Yes|No|Yes|Yes|No|
|메모리 사용량 감소|No|Yes|No|Yes|Yes|Yes|
|효율적인 세부 조정을 위한 적은 매개변수 사용|No|Yes|Yes|No|No|Yes|
|사용 가능한 모든 GPU 장치의 총 GPU 메모리에 접근할 수 있는 메모리 효율적인 데이터 병렬 처리 방식|No|No|No|Yes|Yes|Yes|

## 세부 조정 성능 예시

![Finetuning Performance](../../../../translated_images/Finetuningexamples.9dbf84557eef43e011eb7cadf51f51686f9245f7953e2712a27095ab7d18a6d1.ko.png)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어로 작성된 문서)를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해 당사는 책임을 지지 않습니다.