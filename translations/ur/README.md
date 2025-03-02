# Phi کُک بُک: مائیکروسافٹ کے Phi ماڈلز کے ساتھ عملی مثالیں

Phi مائیکروسافٹ کے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔

Phi اس وقت سب سے طاقتور اور کم لاگت والا چھوٹا لینگویج ماڈل (SLM) ہے، جو مختلف زبانوں، استدلال، متن/چیٹ جنریشن، کوڈنگ، تصاویر، آڈیو اور دیگر منظرناموں میں بہترین کارکردگی کے بینچ مارکس رکھتا ہے۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر ڈپلائے کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آسانی سے جنریٹیو AI ایپلیکیشنز بنا سکتے ہیں۔

ان وسائل کا استعمال شروع کرنے کے لیے ان مراحل پر عمل کریں:
1. **ریپوزٹری کو فورک کریں**: یہاں کلک کریں [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ریپوزٹری کو کلون کریں**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**مائیکروسافٹ AI ڈسکارڈ کمیونٹی میں شامل ہوں اور ماہرین اور دیگر ڈویلپرز سے ملاقات کریں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ur.png)

## فہرست

- تعارف
  - [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)
  - [اپنا ماحول سیٹ اپ کریں](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [اہم ٹیکنالوجیز کو سمجھیں](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ماڈلز کے لیے AI سیفٹی](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ہارڈویئر سپورٹ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [مختلف پلیٹ فارمز پر Phi ماڈلز کی دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub مارکیٹ پلیس ماڈلز](https://github.com/marketplace/models)
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Phi کی انفرنس
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Phi فیملی کی انفرنس
    - [iOS میں Phi کی انفرنس](./md/01.Introduction/03/iOS_Inference.md)
    - [Android میں Phi کی انفرنس](./md/01.Introduction/03/Android_Inference.md)
- [جیٹسن میں فی کا انفرنس](./md/01.Introduction/03/Jetson_Inference.md)
    - [اے آئی پی سی میں فی کا انفرنس](./md/01.Introduction/03/AIPC_Inference.md)
    - [ایپل ایم ایل ایکس فریم ورک کے ساتھ فی کا انفرنس](./md/01.Introduction/03/MLX_Inference.md)
    - [لوکل سرور میں فی کا انفرنس](./md/01.Introduction/03/Local_Server_Inference.md)
    - [اے آئی ٹول کٹ کے ذریعے ریموٹ سرور میں فی کا انفرنس](./md/01.Introduction/03/Remote_Interence.md)
    - [رسٹ کے ساتھ فی کا انفرنس](./md/01.Introduction/03/Rust_Inference.md)
    - [لوکل میں ویژن کے ساتھ فی کا انفرنس](./md/01.Introduction/03/Vision_Inference.md)
    - [کائٹو اے کے ایس، ایزور کنٹینرز (آفیشل سپورٹ) کے ساتھ فی کا انفرنس](./md/01.Introduction/03/Kaito_Inference.md)
- [فی فیملی کو کوانٹیفائی کرنا](./md/01.Introduction/04/QuantifyingPhi.md)
    - [لاما.سی پی پی کا استعمال کرتے ہوئے فی-3.5 / 4 کو کوانٹیفائی کرنا](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [اونکس رن ٹائم کے جنریٹو اے آئی ایکسٹینشنز کا استعمال کرتے ہوئے فی-3.5 / 4 کو کوانٹیفائی کرنا](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [انٹیل اوپن وینو کا استعمال کرتے ہوئے فی-3.5 / 4 کو کوانٹیفائی کرنا](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [ایپل ایم ایل ایکس فریم ورک کا استعمال کرتے ہوئے فی-3.5 / 4 کو کوانٹیفائی کرنا](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- فی کا تجزیہ
    - [ریسپانسبل اے آئی](./md/01.Introduction/05/ResponsibleAI.md)
    - [تجزیے کے لیے ایزور اے آئی فاؤنڈری](./md/01.Introduction/05/AIFoundry.md)
    - [تجزیے کے لیے پرامپٹ فلو کا استعمال](./md/01.Introduction/05/Promptflow.md)

- ایزور اے آئی سرچ کے ساتھ آر اے جی
    - [ایزور اے آئی سرچ کے ساتھ فی-4-منی اور فی-4-ملٹی موڈل (آر اے جی) کا استعمال کیسے کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- فی ایپلیکیشن ڈیولپمنٹ کے نمونے
  - ٹیکسٹ اور چیٹ ایپلیکیشنز
    - فی-4 کے نمونے 🆕
      - [📓] [فی-4-منی اونکس ماڈل کے ساتھ چیٹ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [لوکل اونکس ماڈل .نیٹ کے ساتھ فی-4 کے ساتھ چیٹ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [اونکس کا استعمال کرتے ہوئے سیمنٹک کرنل کے ساتھ فی-4 چیٹ .نیٹ کنسول ایپ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - فی-3 / 3.5 کے نمونے
      - [براؤزر میں فی-3، اونکس رن ٹائم ویب اور ویب جی پی یو کا استعمال کرتے ہوئے لوکل چیٹ بوٹ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [اوپن وینو چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ملٹی ماڈل - انٹرایکٹو فی-3-منی اور اوپن اے آئی وسپر](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [ایم ایل فلو - ایک ریپر بنانا اور ایم ایل فلو کے ساتھ فی-3 کا استعمال](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ماڈل آپٹمائزیشن - اونکس رن ٹائم ویب کے لیے فی-3-منی ماڈل کو اولیو کے ساتھ آپٹمائز کرنے کا طریقہ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [ون یو آئی 3 ایپ فی-3-منی-4ک-انسٹرکٹ-اونکس کے ساتھ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [ون یو آئی 3 ملٹی ماڈل اے آئی پاورڈ نوٹس ایپ کا نمونہ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [فی-3 کے کسٹم ماڈلز کو فائن ٹیون اور پرامپٹ فلو کے ساتھ انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ایزور اے آئی فاؤنڈری میں پرامپٹ فلو کے ساتھ فی-3 کے کسٹم ماڈلز کو فائن ٹیون اور انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [مائیکروسافٹ کے ریسپانسبل اے آئی اصولوں پر توجہ دیتے ہوئے ایزور اے آئی فاؤنڈری میں فائن ٹیون کیے گئے فی-3 / فی-3.5 ماڈل کا تجزیہ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct زبان کی پیش گوئی کا نمونہ (چینی/انگریزی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [ونڈوز GPU کا استعمال کرتے ہوئے Phi-3.5-Instruct ONNX کے ساتھ پرامپٹ فلو حل بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [مائیکروسافٹ Phi-3.5 tflite کا استعمال کرتے ہوئے اینڈرائیڈ ایپ بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [مقامی ONNX Phi-3 ماڈل کا استعمال کرتے ہوئے Microsoft.ML.OnnxRuntime کے ساتھ Q&A .NET مثال](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [سیمینٹک کرنل اور Phi-3 کے ساتھ کنسول چیٹ .NET ایپ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK کوڈ پر مبنی نمونے 
    - Phi-4 نمونے 🆕
      - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے پروجیکٹ کوڈ بنائیں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 نمونے
      - [مائیکروسافٹ Phi-3 فیملی کے ساتھ اپنا Visual Studio Code GitHub Copilot Chat بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub ماڈلز کے ذریعے Phi-3.5 کے ساتھ اپنا Visual Studio Code چیٹ کوپائلٹ ایجنٹ بنائیں](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - جدید استدلال کے نمونے
    - Phi-4 نمونے 🆕
      - [📓] [Phi-4-mini استدلال کے نمونے](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - ڈیموز
      - [Phi-4-mini ڈیموز جو Hugging Face Spaces پر ہوسٹ کیے گئے ہیں](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ڈیموز جو Hugging Face Spaces پر ہوسٹ کیے گئے ہیں](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - وژن کے نمونے
    - Phi-4 نمونے 🆕
      - [📓] [تصاویر پڑھنے اور کوڈ جنریٹ کرنے کے لیے Phi-4-multimodal کا استعمال کریں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 نمونے
      -  [📓][Phi-3-vision-تصویر سے متن تک متن](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ایمبیڈنگ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ڈیمو: Phi-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - بصری زبان کا معاون - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision ملٹی فریم یا ملٹی امیج نمونہ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision مقامی ONNX ماڈل کا استعمال کرتے ہوئے Microsoft.ML.OnnxRuntime .NET کے ساتھ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [مینو پر مبنی Phi-3 Vision مقامی ONNX ماڈل کا استعمال کرتے ہوئے Microsoft.ML.OnnxRuntime .NET کے ساتھ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - آڈیو کے نمونے
    - Phi-4 نمونے 🆕
      - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے آڈیو ٹرانسکرپٹ نکالنا](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal آڈیو نمونہ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal تقریر کا ترجمہ نمونہ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن Phi-4-multimodal آڈیو کا استعمال کرتے ہوئے آڈیو فائل کا تجزیہ کرنے اور ٹرانسکرپٹ جنریٹ کرنے کے لیے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE کے نمونے
    - Phi-3 / 3.5 نمونے
      - [📓] [Phi-3.5 ماہرین کے مرکب ماڈلز (MoEs) سماجی میڈیا نمونہ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ Retrieval-Augmented Generation (RAG) پائپ لائن بنانا](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - فنکشن کالنگ کے نمونے
    - Phi-4 نمونے 🆕
      -  [📓] [Phi-4-mini کے ساتھ فنکشن کالنگ کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
  - ملٹی موڈل مکسنگ کے نمونے
    - Phi-4 نمونے 🆕
- [📓] [ٹیکنالوجی صحافی کے طور پر Phi-4-multimodal کا استعمال](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
  - [.NET کنسول ایپلیکیشن کا استعمال کرتے ہوئے Phi-4-multimodal سے تصاویر کا تجزیہ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi کے نمونوں کی فائن ٹوننگ  
  - [فائن ٹوننگ کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [فائن ٹوننگ بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [فائن ٹوننگ: Phi-3 کو ایک انڈسٹری ماہر بنائیں](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Phi-3 کو VS کوڈ کے AI ٹول کٹ کے ساتھ فائن ٹون کریں](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure مشین لرننگ سروس کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive کے ساتھ فائن ٹوننگ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab کے ساتھ فائن ٹوننگ](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights اور Bias کے ساتھ Phi-3-vision کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX فریم ورک کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision کی فائن ٹوننگ (آفیشل سپورٹ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS، Azure Containers کے ساتھ Phi-3 کی فائن ٹوننگ (آفیشل سپورٹ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 اور 3.5 Vision کی فائن ٹوننگ](https://github.com/2U1/Phi3-Vision-Finetune)

- عملی لیب  
  - [جدید ماڈلز کو دریافت کریں: LLMs، SLMs، مقامی ترقی اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP کی صلاحیت کو کھولنا: Microsoft Olive کے ساتھ فائن ٹوننگ](https://github.com/azure/Ignite_FineTuning_workshop)

- تعلیمی تحقیقاتی مقالے اور اشاعتیں  
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 تکنیکی رپورٹ: ایک انتہائی قابل زبان ماڈل جو آپ کے فون پر مقامی طور پر چلتا ہے](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)  
  - [چھوٹے زبان ماڈلز کو ان-وہیکل فنکشن کالنگ کے لیے بہتر بنانا](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) PHI-3 کو ملٹیپل چوائس سوالات کے جواب کے لیے فائن ٹون کرنا: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)

## Phi ماڈلز کا استعمال

### Azure AI Foundry پر Phi  

آپ Microsoft Phi کا استعمال سیکھ سکتے ہیں اور اپنے مختلف ہارڈ ویئر ڈیوائسز پر E2E حل تیار کر سکتے ہیں۔ Phi کا تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنی ضروریات کے مطابق Phi کو اپنی مرضی کے مطابق بنائیں [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) پر۔ مزید معلومات کے لیے [Azure AI Foundry پر آغاز کریں](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) دیکھیں۔

**پلے گراؤنڈ**  
ہر ماڈل کا ایک مخصوص پلے گراؤنڈ ہوتا ہے جہاں آپ ماڈل کو ٹیسٹ کر سکتے ہیں [Azure AI Playground](https://aka.ms/try-phi3)۔

### GitHub ماڈلز پر Phi  

آپ Microsoft Phi کا استعمال سیکھ سکتے ہیں اور اپنے مختلف ہارڈ ویئر ڈیوائسز پر E2E حل تیار کر سکتے ہیں۔ Phi کا تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنی ضروریات کے مطابق Phi کو اپنی مرضی کے مطابق بنائیں [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) پر۔ مزید معلومات کے لیے [GitHub Model Catalog پر آغاز کریں](/md/02.QuickStart/GitHubModel_QuickStart.md) دیکھیں۔

**پلے گراؤنڈ**  
ہر ماڈل کے لیے ایک مخصوص [پلے گراؤنڈ موجود ہے جہاں ماڈل کو آزمایا جا سکتا ہے](/md/02.QuickStart/GitHubModel_QuickStart.md)۔

### Hugging Face پر Phi

آپ اس ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔

**پلے گراؤنڈ**  
[Hugging Chat پلے گراؤنڈ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## ذمہ دار AI

Microsoft اپنے گاہکوں کو اپنی AI مصنوعات ذمہ داری سے استعمال کرنے میں مدد دینے، اپنے تجربات کا اشتراک کرنے، اور شفافیت نوٹسز اور اثرات کے تجزیوں جیسے ٹولز کے ذریعے اعتماد پر مبنی شراکت داری قائم کرنے کے لیے پرعزم ہے۔ ان میں سے کئی وسائل [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔  
Microsoft کا ذمہ دار AI کے لیے طریقہ کار ہمارے AI اصولوں پر مبنی ہے، جن میں انصاف، اعتبار اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی شامل ہیں۔

بڑے پیمانے پر قدرتی زبان، تصویر، اور آواز کے ماڈلز - جیسا کہ اس نمونے میں استعمال کیے گئے ہیں - ممکنہ طور پر غیر منصفانہ، غیر معتبر، یا توہین آمیز رویہ اختیار کر سکتے ہیں، جس سے نقصان پہنچ سکتا ہے۔ خطرات اور حدود کے بارے میں آگاہی کے لیے براہ کرم [Azure OpenAI سروس شفافیت نوٹ](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) کا مطالعہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ آپ اپنی آرکیٹیکچر میں ایک حفاظتی نظام شامل کریں جو نقصان دہ رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلی کیشنز اور سروسز میں نقصان دہ صارف کے تیار کردہ اور AI کے تیار کردہ مواد کا پتہ لگانے کی صلاحیت رکھتا ہے۔ Azure AI Content Safety میں ٹیکسٹ اور امیج APIs شامل ہیں جو نقصان دہ مواد کا پتہ لگانے کی اجازت دیتے ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو نقصان دہ مواد کا پتہ لگانے کے لیے مختلف طریقوں کے کوڈ کے نمونے دیکھنے، دریافت کرنے، اور آزمانے کی سہولت فراہم کرتی ہے۔ درج ذیل [کوئیک اسٹارٹ ڈاکیومنٹیشن](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) سروس کو درخواست دینے کے عمل کی رہنمائی کرتی ہے۔

ایک اور پہلو جس پر غور کیا جانا چاہیے وہ مجموعی ایپلی کیشن کی کارکردگی ہے۔ کثیر ماڈل اور کثیر وضعی ایپلی کیشنز کے ساتھ، ہم کارکردگی کو اس بات کے طور پر سمجھتے ہیں کہ سسٹم آپ اور آپ کے صارفین کی توقعات کے مطابق کارکردگی دکھائے، بشمول نقصان دہ آؤٹ پٹ پیدا نہ کرنا۔ یہ ضروری ہے کہ آپ اپنی مجموعی ایپلی کیشن کی کارکردگی کا جائزہ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) کا استعمال کرتے ہوئے لیں۔ آپ کے پاس [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) کے ساتھ تخلیق اور جائزہ لینے کی صلاحیت بھی موجود ہے۔

آپ اپنے AI ایپلی کیشن کا جائزہ اپنے ڈویلپمنٹ ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) کا استعمال کرتے ہوئے لے سکتے ہیں۔ چاہے یہ ایک ٹیسٹ ڈیٹا سیٹ ہو یا ایک ہدف، آپ کے جنریٹو AI ایپلی کیشن کے جنریشنز کو بلٹ ان ایویلیوٹرز یا آپ کی پسند کے کسٹم ایویلیوٹرز کے ذریعے مقداری طور پر ناپا جاتا ہے۔ Azure AI Evaluation SDK کے ساتھ اپنے سسٹم کا جائزہ لینے کے لیے شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) کی پیروی کر سکتے ہیں۔ ایک بار جب آپ ایویلیوایشن رن انجام دیتے ہیں، تو آپ [Azure AI Foundry میں نتائج کو دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈ مارکس

اس پروجیکٹ میں پروجیکٹس، مصنوعات، یا خدمات کے لیے ٹریڈ مارکس یا لوگوز شامل ہو سکتے ہیں۔ Microsoft کے ٹریڈ مارکس یا لوگوز کے مجاز استعمال کو [Microsoft کے ٹریڈ مارک اور برانڈ گائیڈلائنز](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کے مطابق ہونا چاہیے۔  
اس پروجیکٹ کے ترمیم شدہ ورژنز میں Microsoft کے ٹریڈ مارکس یا لوگوز کا ایسا استعمال نہ کریں جو الجھن پیدا کرے یا Microsoft کی سرپرستی کا اشارہ دے۔ تیسرے فریق کے ٹریڈ مارکس یا لوگوز کا کوئی بھی استعمال ان کے متعلقہ فریقین کی پالیسیوں کے تابع ہے۔

**اعلانِ لاتعلقی**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔