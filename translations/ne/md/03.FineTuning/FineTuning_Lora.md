# **Phi-3 लाई Lora को साथ फाइन-ट्यूनिंग**

Microsoft को Phi-3 Mini भाषा मोडेललाई [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) प्रयोग गरेर कस्टम च्याट इन्स्ट्रक्शन डेटासेटमा फाइन-ट्यून गर्ने प्रक्रिया।

LORA ले संवादात्मक बुझाइ र प्रतिक्रिया निर्माणलाई सुधार गर्न मद्दत गर्दछ।

## Phi-3 Mini लाई फाइन-ट्यून गर्ने चरणबद्ध मार्गनिर्देशन:

**इम्पोर्ट र सेटअप**

loralib स्थापना गर्दै

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक पुस्तकालयहरू जस्तै datasets, transformers, peft, trl, र torch लाई इम्पोर्ट गरेर सुरु गर्नुहोस्।  
प्रशिक्षण प्रक्रियालाई ट्र्याक गर्नको लागि लगिङ सेटअप गर्नुहोस्।  

तपाईंले केही लेयरहरूलाई loralib मा कार्यान्वयन गरिएका समकक्षहरूसँग प्रतिस्थापन गरेर अनुकूलन गर्न सक्छन्। हालको लागि, हामी nn.Linear, nn.Embedding, र nn.Conv2d लाई मात्र समर्थन गर्छौं। हामी MergedLinear लाई पनि समर्थन गर्छौं, जुन एकल nn.Linear ले एक भन्दा बढी लेयरहरूको प्रतिनिधित्व गर्छ, जस्तै ध्यान qkv प्रोजेक्शनको केही कार्यान्वयनहरूमा (थप नोटहरू हेर्नुहोस्)।

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

प्रशिक्षण लूप सुरु हुनु अघि, केवल LoRA प्यारामिटरहरूलाई प्रशिक्षणयोग्यको रूपमा मार्क गर्नुहोस्।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपोइन्ट सेभ गर्दा, केवल LoRA प्यारामिटरहरू समावेश हुने state_dict उत्पन्न गर्नुहोस्।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```  

load_state_dict प्रयोग गरेर चेकपोइन्ट लोड गर्दा, strict=False सेट गर्न निश्चित गर्नुहोस्।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

अब, सामान्य रूपमा प्रशिक्षण अगाडि बढ्न सक्छ।

**हाइपरप्यारामिटरहरू**

दुईवटा डिक्सनरी परिभाषित गर्नुहोस्: training_config र peft_config।  
training_config ले प्रशिक्षणका लागि लर्निङ रेट, ब्याच साइज, र लगिङ सेटिङ्स जस्ता हाइपरप्यारामिटरहरू समावेश गर्दछ।  

peft_config ले LoRA-सँग सम्बन्धित प्यारामिटरहरू जस्तै rank, dropout, र task type निर्दिष्ट गर्दछ।  

**मोडेल र टोकनाइजर लोड गर्दै**

पूर्व-प्रशिक्षित Phi-3 मोडेलको पथ निर्दिष्ट गर्नुहोस् (जस्तै, "microsoft/Phi-3-mini-4k-instruct")।  
मोडेल सेटिङहरू कन्फिगर गर्नुहोस्, जसमा cache प्रयोग, डेटा प्रकार (मिश्रित प्रिसिजनको लागि bfloat16), र ध्यान कार्यान्वयन समावेश छन्।  

**प्रशिक्षण**

कस्टम च्याट इन्स्ट्रक्शन डेटासेट प्रयोग गरेर Phi-3 मोडेललाई फाइन-ट्यून गर्नुहोस्।  
peft_config बाट LoRA सेटिङहरू प्रयोग गरेर प्रभावकारी अनुकूलन सुनिश्चित गर्नुहोस्।  
निर्दिष्ट लगिङ रणनीतिहरू प्रयोग गरेर प्रशिक्षण प्रगतिको अनुगमन गर्नुहोस्।  

**मूल्यांकन र सेभिङ:**  
फाइन-ट्यून गरिएको मोडेलको मूल्यांकन गर्नुहोस्।  
पछि प्रयोगको लागि प्रशिक्षणको क्रममा चेकपोइन्टहरू सेभ गर्नुहोस्।  

**नमूनाहरू**
- [यस नमूना नोटबुकसँग थप जान्नुहोस्](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python फाइन-ट्यूनिङ नमूनाको उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub मा LORA को साथ फाइन-ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face मोडेल कार्डको उदाहरण - LORA फाइन-ट्यूनिङ नमूना](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub मा QLORA को साथ फाइन-ट्यूनिङको उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)  

**अस्वीकरण**:  
यो दस्तावेज़ मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी यथासम्भव सही अनुवाद प्रदान गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।