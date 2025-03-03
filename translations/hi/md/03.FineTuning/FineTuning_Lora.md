# **Phi-3 को LoRA के साथ फाइन-ट्यून करना**

Microsoft के Phi-3 Mini भाषा मॉडल को [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) का उपयोग करके एक कस्टम चैट निर्देश डेटासेट पर फाइन-ट्यून करना। 

LoRA संवादात्मक समझ और प्रतिक्रिया निर्माण को बेहतर बनाने में मदद करेगा। 

## Phi-3 Mini को फाइन-ट्यून करने के लिए चरण-दर-चरण गाइड:

**इंपोर्ट्स और सेटअप** 

loralib इंस्टॉल करना

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक लाइब्रेरी जैसे datasets, transformers, peft, trl, और torch को इंपोर्ट करके शुरू करें। 
ट्रेनिंग प्रक्रिया को ट्रैक करने के लिए लॉगिंग सेट करें।

आप कुछ लेयर्स को अनुकूलित करने के लिए उन्हें loralib में लागू समकक्षों से बदलने का विकल्प चुन सकते हैं। फिलहाल हम केवल nn.Linear, nn.Embedding, और nn.Conv2d को सपोर्ट करते हैं। हम ऐसे मामलों के लिए MergedLinear को भी सपोर्ट करते हैं जहां एक nn.Linear एक से अधिक लेयर्स का प्रतिनिधित्व करता है, जैसे कि ध्यान qkv प्रोजेक्शन के कुछ कार्यान्वयनों में (अधिक जानकारी के लिए Additional Notes देखें)।

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

ट्रेनिंग लूप शुरू होने से पहले, केवल LoRA पैरामीटर्स को ट्रेन करने योग्य के रूप में चिह्नित करें।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव करते समय, ऐसा state_dict जनरेट करें जिसमें केवल LoRA पैरामीटर्स हों।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict का उपयोग करते समय चेकपॉइंट लोड करते समय, strict=False सेट करना सुनिश्चित करें।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

अब ट्रेनिंग सामान्य रूप से शुरू हो सकती है।

**हाइपरपैरामीटर्स** 

दो डिक्शनरीज़ को परिभाषित करें: training_config और peft_config। training_config में ट्रेनिंग के लिए हाइपरपैरामीटर्स शामिल होते हैं, जैसे कि लर्निंग रेट, बैच साइज, और लॉगिंग सेटिंग्स।

peft_config में LoRA से संबंधित पैरामीटर्स जैसे rank, dropout, और task type निर्दिष्ट करें।

**मॉडल और टोकनाइज़र लोड करना** 

प्रशिक्षित Phi-3 मॉडल का पथ निर्दिष्ट करें (उदाहरण के लिए, "microsoft/Phi-3-mini-4k-instruct")। मॉडल सेटिंग्स को कॉन्फ़िगर करें, जिसमें कैश का उपयोग, डेटा प्रकार (मिश्रित प्रिसिशन के लिए bfloat16), और ध्यान कार्यान्वयन शामिल है।

**ट्रेनिंग** 

कस्टम चैट निर्देश डेटासेट का उपयोग करके Phi-3 मॉडल को फाइन-ट्यून करें। प्रभावी अनुकूलन के लिए peft_config से LoRA सेटिंग्स का उपयोग करें। निर्दिष्ट लॉगिंग रणनीति का उपयोग करके ट्रेनिंग प्रगति की निगरानी करें।
मूल्यांकन और सहेजना: फाइन-ट्यून किए गए मॉडल का मूल्यांकन करें। 
बाद में उपयोग के लिए ट्रेनिंग के दौरान चेकपॉइंट्स को सेव करें।

**उदाहरण**
- [इस सैंपल नोटबुक के साथ अधिक जानें](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइन-ट्यूनिंग सैंपल का उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub पर LoRA के साथ फाइन-ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face मॉडल कार्ड का उदाहरण - LoRA फाइन-ट्यूनिंग सैंपल](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub पर QLORA के साथ फाइन-ट्यूनिंग का उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में लिखा गया मूल दस्तावेज़ ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।