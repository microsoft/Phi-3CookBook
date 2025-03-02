## خوش‌آمدید به آزمایشگاه‌های Phi با استفاده از C#

در اینجا مجموعه‌ای از آزمایشگاه‌ها وجود دارد که نحوه‌ی ادغام نسخه‌های قدرتمند مختلف مدل‌های Phi در محیط .NET را نمایش می‌دهند.

## پیش‌نیازها

قبل از اجرای نمونه‌ها، مطمئن شوید که موارد زیر نصب شده‌اند:

**.NET 9:** اطمینان حاصل کنید که [آخرین نسخه .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) روی دستگاه شما نصب شده است.

**(اختیاری) Visual Studio یا Visual Studio Code:** به یک IDE یا ویرایشگر کد نیاز دارید که بتواند پروژه‌های .NET را اجرا کند. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) توصیه می‌شوند.

**استفاده از git** یکی از نسخه‌های موجود Phi-3، Phi3.5 یا Phi-4 را از [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) به صورت محلی کلون کنید.

**مدل‌های Phi-4 ONNX** را روی دستگاه خود دانلود کنید:

### به پوشه‌ای که مدل‌ها در آن ذخیره می‌شوند بروید

```bash
cd c:\phi\models
```

### پشتیبانی از lfs را اضافه کنید

```bash
git lfs install 
```

### مدل Phi-4 mini instruct و مدل Phi-4 multi modal را کلون و دانلود کنید

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**مدل‌های Phi-3 ONNX** را روی دستگاه خود دانلود کنید:

### مدل Phi-3 mini 4K instruct و مدل Phi-3 vision 128K را کلون و دانلود کنید

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**مهم:** دموهای فعلی برای استفاده از نسخه‌های ONNX مدل طراحی شده‌اند. مراحل بالا مدل‌های زیر را کلون می‌کنند.

## درباره آزمایشگاه‌ها

راه‌حل اصلی شامل چندین آزمایشگاه نمونه است که قابلیت‌های مدل‌های Phi را با استفاده از C# نمایش می‌دهند.

| پروژه | مدل | توضیحات |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | نمونه‌ای از یک کنسول چت که به کاربر اجازه می‌دهد سوال بپرسد. این پروژه یک مدل محلی ONNX Phi-3 را با استفاده از `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` بارگذاری می‌کند.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. پروژه را با فرمان زیر اجرا کنید:

    ```bash
    dotnet run
    ```

1. پروژه نمونه از کاربر ورودی می‌گیرد و با استفاده از حالت محلی پاسخ می‌دهد.

   اجرای دمو مشابه این است:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.