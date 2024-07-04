## AI safety for Phi-3 models

The Phi family of models has been developed in alignment with [Microsoft’s Responsible AI principles](https://www.microsoft.com/ai/responsible-ai). 

## Best Practices 

Like other models,the Phi family of models can potentially behave in ways that are unfair, unreliable, or offensive. 

Some of the limiting behaviors of SLM and LLM you to be aware of include:

- **Quality of Service:** The Phi models are trained primarily on English text. Languages other than English will experience worse performance English language varieties with less representation in the training data might experience worse performance than standard American English.
- **Representation of Harms & Perpetuation of Stereotypes:** These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.
- **Inappropriate or Offensive Content:** These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.
Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
- **Limited Scope for Code:** Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.

Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). 

## Responsible AI Considerations

Like other language models, the Phi series models can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:

**Quality of Service:** the Phi models are trained primarily on English text. Languages other than English will experience worse performance. English language varieties with less representation in the training data might experience worse performance than standard American English.

**Representation of Harms & Perpetuation of Stereotypes:** These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.

**Inappropriate or Offensive Content:** these models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.
Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.

**Limited Scope for Code:** Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.

Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Important areas for consideration include:

**Allocation:** Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.

**High-Risk Scenarios:** Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.

**Misinformation:** Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).

**Generation of Harmful Content:** Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.

**Misuse:** Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.

### Finetuning and AI Content Safety
After fine-tuning a model, we highly recommend leveraging [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) measures to monitor the content generated by the models, identify and block potential risks, threats, and quality issues.

![Phi3AISafety](../../imgs/01/phi3aisafety.png)

[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) supports both text and image content. It can be deployed in the cloud, disconnected containers, and on edge/embedded devices.

## Overview of Azure AI Content Safety

Azure AI Content Safety is not a one-size-fits-all solution; it can be customized to align with businesses’ specific policies. Additionally, its multi-lingual models enable it to understand multiple languages simultaneously 

![AIContentSafety](../../imgs/01/AIcontentsafety.png)

- **Azure AI Content Safety**
- **Microsoft Developer** 
- **5 videos** 

Azure AI Content Safety service detects harmful user-generated and AI-generated content in applications and services. It includes text and image APIs that allow you to detect harmful or inappropriate material.

[AI Content Safety Playlist](https://www.youtube.com/playlist?list=PLlrxD0HtieHjaQ9bJjyp1T7FeCbmVcPkQ)