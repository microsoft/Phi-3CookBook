# **Phi-3 ला LoRA सह फाइन-ट्यून करणे**

Microsoft च्या Phi-3 Mini भाषा मॉडेलला [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) चा वापर करून कस्टम चॅट इन्स्ट्रक्शन डेटासेटवर फाइन-ट्यून करणे.

LoRA संभाषण समज आणि प्रतिसाद निर्माण करण्याच्या क्षमतेत सुधारणा करण्यास मदत करेल.

## Phi-3 Mini फाइन-ट्यून करण्यासाठी टप्प्याटप्प्याचे मार्गदर्शन:

**आयात आणि सेटअप**

loralib इन्स्टॉल करणे

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

आवश्यक लायब्ररी जसे की datasets, transformers, peft, trl, आणि torch आयात करून सुरू करा. प्रशिक्षण प्रक्रियेचे ट्रॅकिंग करण्यासाठी लॉगिंग सेट करा.

तुम्ही काही लेयर्सला adapt करण्यासाठी त्यांना loralib मध्ये अंमलात आणलेल्या पर्यायांनी बदलू शकता. सध्या आम्ही फक्त nn.Linear, nn.Embedding, आणि nn.Conv2d यांचे समर्थन करतो. आम्ही MergedLinear चे देखील समर्थन करतो, जिथे एक nn.Linear अनेक लेयर्सचे प्रतिनिधित्व करते, जसे की काही attention qkv projection च्या अंमलबजावणीमध्ये (अधिक माहितीसाठी Additional Notes पाहा).

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

प्रशिक्षण लूप सुरू होण्यापूर्वी, फक्त LoRA पॅरामीटर्स ट्रेन करण्यायोग्य म्हणून चिन्हांकित करा.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

चेकपॉइंट सेव्ह करताना, फक्त LoRA पॅरामीटर्स असलेले state_dict तयार करा.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict वापरून चेकपॉइंट लोड करताना, strict=False सेट करणे सुनिश्चित करा.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

आता प्रशिक्षण नेहमीप्रमाणे सुरू ठेवता येईल.

**हायपरपॅरामीटर्स**

दोन डिक्शनरी परिभाषित करा: training_config आणि peft_config. training_config मध्ये प्रशिक्षणासाठी लागणारे हायपरपॅरामीटर्स असतील, जसे की learning rate, batch size, आणि लॉगिंग सेटिंग्ज.

peft_config मध्ये LoRA-संबंधित पॅरामीटर्स जसे की rank, dropout, आणि task type असतील.

**मॉडेल आणि टोकनायझर लोड करणे**

प्रशिक्षित Phi-3 मॉडेलचा मार्ग निर्दिष्ट करा (उदा., "microsoft/Phi-3-mini-4k-instruct"). मॉडेल सेटिंग्ज कॉन्फिगर करा, ज्यामध्ये cache वापर, डेटा प्रकार (मिश्रित प्रिसिजनसाठी bfloat16), आणि attention अंमलबजावणीचा समावेश आहे.

**प्रशिक्षण**

कस्टम चॅट इन्स्ट्रक्शन डेटासेट वापरून Phi-3 मॉडेल फाइन-ट्यून करा. कार्यक्षम adaptation साठी peft_config मधील LoRA सेटिंग्ज वापरा. निर्दिष्ट लॉगिंग धोरणाचा वापर करून प्रशिक्षण प्रगतीचे निरीक्षण करा.

मूल्यमापन आणि सेव्हिंग: फाइन-ट्यून केलेल्या मॉडेलचे मूल्यांकन करा. नंतर वापरासाठी प्रशिक्षणादरम्यान चेकपॉइंट्स सेव्ह करा.

**उदाहरणे**
- [या नमुना नोटबुकसह अधिक शिका](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python फाइन-ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub सह LoRA फाइन-ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face मॉडेल कार्डचे उदाहरण - LoRA फाइन-ट्यूनिंग नमुना](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [QLORA सह Hugging Face Hub फाइन-ट्यूनिंगचे उदाहरण](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**अस्वीकरण**:  
हा दस्तऐवज मशीन-आधारित एआय भाषांतर सेवांचा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा प्राधिकृत स्रोत मानावा. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्याने उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.