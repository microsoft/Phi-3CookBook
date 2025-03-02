# **Fine-tuning Phi-3 met Microsoft Olive**

[Olive](https://github.com/microsoft/OLive?WT.mc_id=aiml-138114-kinfeylo) is een gebruiksvriendelijke hardwaregerichte modeloptimalisatietool die toonaangevende technieken op het gebied van modelcompressie, optimalisatie en compilatie samenbrengt.

Het is ontworpen om het proces van het optimaliseren van machine learning-modellen te vereenvoudigen, zodat ze optimaal gebruikmaken van specifieke hardwarearchitecturen.

Of je nu werkt aan cloudgebaseerde applicaties of edge-apparaten, met Olive kun je je modellen moeiteloos en effectief optimaliseren.

## Belangrijkste kenmerken:
- Olive verzamelt en automatiseert optimalisatietechnieken voor specifieke hardwaredoelen.
- Geen enkele optimalisatietechniek is geschikt voor alle scenario's, dus Olive biedt uitbreidbaarheid door experts in staat te stellen hun innovaties in optimalisatie toe te voegen.

## Verminder de technische inspanning:
- Ontwikkelaars moeten vaak meerdere hardware-specifieke toolchains leren en gebruiken om getrainde modellen voor implementatie voor te bereiden en te optimaliseren.
- Olive vereenvoudigt dit proces door optimalisatietechnieken voor de gewenste hardware te automatiseren.

## Klaar-voor-gebruik End-to-End Optimalisatieoplossing:

Door geïntegreerde technieken samen te stellen en af te stemmen, biedt Olive een uniforme oplossing voor end-to-end optimalisatie.
Het houdt rekening met beperkingen zoals nauwkeurigheid en latentie tijdens het optimaliseren van modellen.

## Microsoft Olive gebruiken voor fine-tuning

Microsoft Olive is een zeer gebruiksvriendelijke open source modeloptimalisatietool die zowel fine-tuning als referentie in het veld van generatieve kunstmatige intelligentie dekt. Met eenvoudige configuratie, gecombineerd met het gebruik van open source kleine taalmodellen en gerelateerde runtime-omgevingen (AzureML / lokale GPU, CPU, DirectML), kun je de fine-tuning of referentie van het model voltooien via automatische optimalisatie en het beste model vinden om te implementeren in de cloud of op edge-apparaten. Hiermee kunnen bedrijven hun eigen branche-specifieke modellen bouwen, zowel lokaal als in de cloud.

![intro](../../../../translated_images/intro.dcc44a1aafcf58bf979b9a69384ffea98b5b599ac034dde94937a94a29260332.nl.png)

## Phi-3 Fine-tuning met Microsoft Olive 

![FinetuningwithOlive](../../../../translated_images/olivefinetune.7a9c66b3310981030c47cf637befed8fa1ea1acd0f5acec5ac090a8f3f904a45.nl.png)

## Phi-3 Olive Voorbeeldcode en Voorbeeld
In dit voorbeeld gebruik je Olive om:

- Een LoRA-adapter te fine-tunen om zinnen te classificeren in Verdriet, Blijdschap, Angst, Verrassing.
- De adaptergewichten samen te voegen met het basismodel.
- Het model te optimaliseren en te kwantiseren naar int4.

[Voorbeeldcode](../../code/03.Finetuning/olive-ort-example/README.md)

### Microsoft Olive installeren

De installatie van Microsoft Olive is zeer eenvoudig en kan worden uitgevoerd voor CPU, GPU, DirectML en Azure ML.

```bash
pip install olive-ai
```

Als je een ONNX-model wilt uitvoeren met een CPU, kun je dit gebruiken:

```bash
pip install olive-ai[cpu]
```

Als je een ONNX-model wilt uitvoeren met een GPU, kun je dit gebruiken:

```python
pip install olive-ai[gpu]
```

Als je Azure ML wilt gebruiken, gebruik dan:

```python
pip install git+https://github.com/microsoft/Olive#egg=olive-ai[azureml]
```

**Let op**
OS-vereisten: Ubuntu 20.04 / 22.04 

### **Microsoft Olive's Config.json**

Na installatie kun je verschillende model-specifieke instellingen configureren via het Config-bestand, waaronder data, rekenkracht, training, implementatie en modelgeneratie.

**1. Data**

Op Microsoft Olive kan zowel lokaal als cloud-data worden gebruikt voor training, en dit kan worden ingesteld in de configuratie.

*Instellingen voor lokale data*

Je kunt eenvoudig het dataset instellen dat nodig is voor fine-tuning, meestal in json-formaat, en dit aanpassen aan de datatemplate. Dit moet worden aangepast op basis van de eisen van het model (bijvoorbeeld aanpassen aan het formaat dat vereist is door Microsoft Phi-3-mini. Als je andere modellen hebt, raadpleeg dan de vereiste fine-tuningformaten van die modellen).

```json

    "data_configs": [
        {
            "name": "dataset_default_train",
            "type": "HuggingfaceContainer",
            "load_dataset_config": {
                "params": {
                    "data_name": "json", 
                    "data_files":"dataset/dataset-classification.json",
                    "split": "train"
                }
            },
            "pre_process_data_config": {
                "params": {
                    "dataset_type": "corpus",
                    "text_cols": [
                            "phrase",
                            "tone"
                    ],
                    "text_template": "### Text: {phrase}\n### The tone is:\n{tone}",
                    "corpus_strategy": "join",
                    "source_max_len": 2048,
                    "pad_to_max_len": false,
                    "use_attention_mask": false
                }
            }
        }
    ],
```

**Instellingen voor cloud-databronnen**

Door de datastore van Azure AI Studio/Azure Machine Learning Service te koppelen, kun je data in de cloud gebruiken. Je kunt verschillende databronnen in Azure AI Studio/Azure Machine Learning Service introduceren via Microsoft Fabric en Azure Data als ondersteuning voor fine-tuning.

```json

    "data_configs": [
        {
            "name": "dataset_default_train",
            "type": "HuggingfaceContainer",
            "load_dataset_config": {
                "params": {
                    "data_name": "json", 
                    "data_files": {
                        "type": "azureml_datastore",
                        "config": {
                            "azureml_client": {
                                "subscription_id": "Your Azure Subscrition ID",
                                "resource_group": "Your Azure Resource Group",
                                "workspace_name": "Your Azure ML Workspaces name"
                            },
                            "datastore_name": "workspaceblobstore",
                            "relative_path": "Your train_data.json Azure ML Location"
                        }
                    },
                    "split": "train"
                }
            },
            "pre_process_data_config": {
                "params": {
                    "dataset_type": "corpus",
                    "text_cols": [
                            "Question",
                            "Best Answer"
                    ],
                    "text_template": "<|user|>\n{Question}<|end|>\n<|assistant|>\n{Best Answer}\n<|end|>",
                    "corpus_strategy": "join",
                    "source_max_len": 2048,
                    "pad_to_max_len": false,
                    "use_attention_mask": false
                }
            }
        }
    ],
    
```

**2. Rekenkrachtconfiguratie**

Als je lokaal wilt werken, kun je direct lokale dataresources gebruiken. Als je de resources van Azure AI Studio / Azure Machine Learning Service wilt gebruiken, moet je de relevante Azure-parameters en computernamen configureren.

```json

    "systems": {
        "aml": {
            "type": "AzureML",
            "config": {
                "accelerators": ["gpu"],
                "hf_token": true,
                "aml_compute": "Your Azure AI Studio / Azure Machine Learning Service Compute Name",
                "aml_docker_config": {
                    "base_image": "Your Azure AI Studio / Azure Machine Learning Service docker",
                    "conda_file_path": "conda.yaml"
                }
            }
        },
        "azure_arc": {
            "type": "AzureML",
            "config": {
                "accelerators": ["gpu"],
                "aml_compute": "Your Azure AI Studio / Azure Machine Learning Service Compute Name",
                "aml_docker_config": {
                    "base_image": "Your Azure AI Studio / Azure Machine Learning Service docker",
                    "conda_file_path": "conda.yaml"
                }
            }
        }
    },
```

***Let op***

Omdat het via een container op Azure AI Studio/Azure Machine Learning Service wordt uitgevoerd, moet de benodigde omgeving worden geconfigureerd. Dit wordt ingesteld in de conda.yaml-omgeving.

```yaml

name: project_environment
channels:
  - defaults
dependencies:
  - python=3.8.13
  - pip=22.3.1
  - pip:
      - einops
      - accelerate
      - azure-keyvault-secrets
      - azure-identity
      - bitsandbytes
      - datasets
      - huggingface_hub
      - peft
      - scipy
      - sentencepiece
      - torch>=2.2.0
      - transformers
      - git+https://github.com/microsoft/Olive@jiapli/mlflow_loading_fix#egg=olive-ai[gpu]
      - --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ 
      - ort-nightly-gpu==1.18.0.dev20240307004
      - --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-genai/pypi/simple/
      - onnxruntime-genai-cuda

    

```

**3. Kies je SLM**

Je kunt het model direct gebruiken van Hugging Face, of combineren met de Model Catalog van Azure AI Studio / Azure Machine Learning om een model te selecteren. In het onderstaande codevoorbeeld gebruiken we Microsoft Phi-3-mini als voorbeeld.

Als je het model lokaal hebt, kun je deze methode gebruiken:

```json

    "input_model":{
        "type": "PyTorchModel",
        "config": {
            "hf_config": {
                "model_name": "model-cache/microsoft/phi-3-mini",
                "task": "text-generation",
                "model_loading_args": {
                    "trust_remote_code": true
                }
            }
        }
    },
```

Als je een model wilt gebruiken van Azure AI Studio / Azure Machine Learning Service, kun je deze methode gebruiken:

```json

    "input_model":{
        "type": "PyTorchModel",
        "config": {
            "model_path": {
                "type": "azureml_registry_model",
                "config": {
                    "name": "microsoft/Phi-3-mini-4k-instruct",
                    "registry_name": "azureml-msr",
                    "version": "11"
                }
            },
             "model_file_format": "PyTorch.MLflow",
             "hf_config": {
                "model_name": "microsoft/Phi-3-mini-4k-instruct",
                "task": "text-generation",
                "from_pretrained_args": {
                    "trust_remote_code": true
                }
            }
        }
    },
```

**Let op:**
We moeten integreren met Azure AI Studio / Azure Machine Learning Service, dus let bij het instellen van het model op de versienummering en gerelateerde naamgeving.

Alle modellen op Azure moeten worden ingesteld op PyTorch.MLflow.

Je hebt een Hugging Face-account nodig en moet de sleutel koppelen aan de Key-waarde van Azure AI Studio / Azure Machine Learning.

**4. Algoritme**

Microsoft Olive heeft de Lora- en QLora-fine-tuningalgoritmen goed geïntegreerd. Je hoeft alleen enkele relevante parameters te configureren. Hier neem ik QLora als voorbeeld.

```json
        "lora": {
            "type": "LoRA",
            "config": {
                "target_modules": [
                    "o_proj",
                    "qkv_proj"
                ],
                "double_quant": true,
                "lora_r": 64,
                "lora_alpha": 64,
                "lora_dropout": 0.1,
                "train_data_config": "dataset_default_train",
                "eval_dataset_size": 0.3,
                "training_args": {
                    "seed": 0,
                    "data_seed": 42,
                    "per_device_train_batch_size": 1,
                    "per_device_eval_batch_size": 1,
                    "gradient_accumulation_steps": 4,
                    "gradient_checkpointing": false,
                    "learning_rate": 0.0001,
                    "num_train_epochs": 3,
                    "max_steps": 10,
                    "logging_steps": 10,
                    "evaluation_strategy": "steps",
                    "eval_steps": 187,
                    "group_by_length": true,
                    "adam_beta2": 0.999,
                    "max_grad_norm": 0.3
                }
            }
        },
```

Als je kwantisatieconversie wilt uitvoeren, ondersteunt de hoofdbranch van Microsoft Olive al de onnxruntime-genai-methode. Je kunt dit instellen op basis van je behoeften:

1. Adaptergewichten samenvoegen met het basismodel.
2. Het model converteren naar een onnx-model met de gewenste precisie via ModelBuilder.

Bijvoorbeeld conversie naar gekwantiseerde INT4.

```json

        "merge_adapter_weights": {
            "type": "MergeAdapterWeights"
        },
        "builder": {
            "type": "ModelBuilder",
            "config": {
                "precision": "int4"
            }
        }
```

**Let op** 
- Als je QLoRA gebruikt, wordt kwantisatieconversie met ONNXRuntime-genai momenteel niet ondersteund.

- Hier moet worden opgemerkt dat je de bovenstaande stappen kunt instellen op basis van je eigen behoeften. Het is niet nodig om alle bovenstaande stappen volledig te configureren. Afhankelijk van je behoeften kun je direct de stappen van het algoritme gebruiken zonder fine-tuning. Tot slot moet je de relevante engines configureren.

```json

    "engine": {
        "log_severity_level": 0,
        "host": "aml",
        "target": "aml",
        "search_strategy": false,
        "execution_providers": ["CUDAExecutionProvider"],
        "cache_dir": "../model-cache/models/phi3-finetuned/cache",
        "output_dir" : "../model-cache/models/phi3-finetuned"
    }
```

**5. Fine-tuning voltooid**

Voer in de opdrachtregel het volgende uit in de directory van olive-config.json:

```bash
olive run --config olive-config.json  
```

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gebaseerde vertaaldiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.