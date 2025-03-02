## Phi ল্যাবসে স্বাগতম C# ব্যবহার করে

এখানে কিছু ল্যাব রয়েছে, যা দেখায় কীভাবে .NET পরিবেশে Phi মডেলের বিভিন্ন শক্তিশালী সংস্করণকে ইন্টিগ্রেট করা যায়।

## প্রয়োজনীয়তা

নমুনা চালানোর আগে নিশ্চিত করুন যে আপনার কাছে নিম্নলিখিতগুলি ইনস্টল করা আছে:

**.NET 9:** আপনার মেশিনে [নতুনতম .NET সংস্করণ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ইনস্টল করা আছে কিনা তা নিশ্চিত করুন।

**(ঐচ্ছিক) Visual Studio বা Visual Studio Code:** .NET প্রকল্প চালানোর জন্য একটি IDE বা কোড এডিটর প্রয়োজন। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) বা [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) সুপারিশ করা হয়।

**git ব্যবহার করে** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) থেকে উপলব্ধ Phi-3, Phi3.5 বা Phi-4 সংস্করণগুলির যেকোনো একটি স্থানীয়ভাবে ক্লোন করুন।

**Phi-4 ONNX মডেল ডাউনলোড করুন** আপনার লোকাল মেশিনে:

### মডেল সংরক্ষণ করার জন্য ফোল্ডারে যান

```bash
cd c:\phi\models
```

### lfs সমর্থন যোগ করুন

```bash
git lfs install 
```

### Phi-4 mini instruct মডেল এবং Phi-4 multi modal মডেল ক্লোন এবং ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX মডেল ডাউনলোড করুন** আপনার লোকাল মেশিনে:

### Phi-3 mini 4K instruct মডেল এবং Phi-3 vision 128K মডেল ক্লোন এবং ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**গুরুত্বপূর্ণ:** বর্তমান ডেমোগুলি মডেলের ONNX সংস্করণ ব্যবহার করার জন্য ডিজাইন করা হয়েছে। পূর্ববর্তী ধাপগুলি নিম্নলিখিত মডেলগুলিকে ক্লোন করে।

## ল্যাব সম্পর্কে

মূল সলিউশনে বেশ কিছু নমুনা ল্যাব রয়েছে, যা C# ব্যবহার করে Phi মডেলের ক্ষমতাগুলি প্রদর্শন করে।

| প্রকল্প | মডেল | বিবরণ |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 বা Phi-3.5 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন জিজ্ঞাসা করার অনুমতি দেয়। প্রকল্পটি `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` ব্যবহার করে একটি লোকাল ONNX Phi-3 মডেল লোড করে।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. কমান্ড দিয়ে প্রকল্পটি চালান

    ```bash
    dotnet run
    ```

1. নমুনা প্রকল্পটি ব্যবহারকারীর ইনপুট চাইবে এবং লোকাল মোড ব্যবহার করে উত্তর দেবে।

   চলমান ডেমোটি এরকম দেখাবে:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ সেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।