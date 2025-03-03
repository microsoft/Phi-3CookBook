## فی لیبز کا سی شارپ کے ساتھ تعارف

یہ لیبز کا ایک انتخاب ہے جو یہ دکھاتا ہے کہ .NET ماحول میں مختلف طاقتور فی ماڈلز کے ورژنز کو کیسے شامل کیا جا سکتا ہے۔

## ضروریات

نمونہ چلانے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں انسٹال ہیں:

**.NET 9:** اپنے کمپیوٹر پر [.NET کا تازہ ترین ورژن](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) انسٹال کریں۔

**(اختیاری) ویژول اسٹوڈیو یا ویژول اسٹوڈیو کوڈ:** آپ کو ایک IDE یا کوڈ ایڈیٹر کی ضرورت ہوگی جو .NET پروجیکٹس چلا سکے۔ [ویژول اسٹوڈیو](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [ویژول اسٹوڈیو کوڈ](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) تجویز کیے جاتے ہیں۔

**git کا استعمال کرتے ہوئے** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) سے دستیاب Phi-3، Phi3.5 یا Phi-4 ورژنز میں سے کسی ایک کو لوکل طور پر کلون کریں۔

**Phi-4 ONNX ماڈلز ڈاؤنلوڈ کریں** اور اپنی لوکل مشین پر محفوظ کریں:

### ماڈلز کو محفوظ کرنے والے فولڈر پر جائیں

```bash
cd c:\phi\models
```

### lfs کے لیے سپورٹ شامل کریں

```bash
git lfs install 
```

### Phi-4 منی انسٹرکٹ ماڈل اور Phi-4 ملٹی ماڈل ماڈل کو کلون اور ڈاؤنلوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ماڈلز ڈاؤنلوڈ کریں** اور اپنی لوکل مشین پر محفوظ کریں:

### Phi-3 منی 4K انسٹرکٹ ماڈل اور Phi-3 وژن 128K ماڈل کو کلون اور ڈاؤنلوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**اہم:** موجودہ ڈیموز ماڈلز کے ONNX ورژنز کو استعمال کرنے کے لیے ڈیزائن کیے گئے ہیں۔ اوپر دیے گئے مراحل درج ذیل ماڈلز کو کلون کرتے ہیں۔

## لیبز کے بارے میں

مرکزی سلوشن میں کئی نمونہ لیبز شامل ہیں جو سی شارپ کے ساتھ فی ماڈلز کی صلاحیتوں کو ظاہر کرتے ہیں۔

| پروجیکٹ | ماڈل | تفصیل |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | ایک نمونہ کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتا ہے۔ یہ پروجیکٹ لوکل ONNX Phi-3 ماڈل کو `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` کے ذریعے لوڈ کرتا ہے۔

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. پروجیکٹ کو اس کمانڈ کے ساتھ چلائیں:

    ```bash
    dotnet run
    ```

1. نمونہ پروجیکٹ صارف سے ان پٹ مانگتا ہے اور لوکل موڈ کے ذریعے جواب دیتا ہے۔

   چلنے والے ڈیمو کی مثال اس طرح کی ہوگی:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**اعلانِ لاتعلقی**:  
یہ دستاویز مشین پر مبنی اے آئی ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی اصل زبان میں مستند ذریعہ تصور کی جانی چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔