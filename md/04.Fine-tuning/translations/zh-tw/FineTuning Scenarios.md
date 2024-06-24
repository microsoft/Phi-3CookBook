## 微調場景

| | | | | | | |
|-|-|-|-|-|-|-|
|Scenario|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|Adapting pre-trained LLMs to specific tasks or domains|是|是|是|是|是|是|
|Fine-tuning for NLP tasks such as text classification, named entity recognition, and machine translation|是|是|是|是|是|是|
|Fine-tuning for QA tasks|是|是|是|是|是|是|
|Fine-tuning for generating human-like responses in chatbots|是|是|是|是|是|是|
|Fine-tuning for generating music, art, or other forms of creativity|是|是|是|是|是|是|
|Reducing computational and financial costs|是|是|否|是|是|否|
|Reducing memory usage|否|是|否|是|是|是|
|Using fewer parameters for efficient finetuning|否|是|是|否|否|是|
|Memory-efficient form of data parallelism that gives access to the aggregate GPU memory of all the GPU devices available|否|否|否|是|是|是

## 調整效能範例

![微調效能](../../../../imgs/04/00/Finetuningexamples.png)

