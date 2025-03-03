# **دليل استخدام OnnxRuntime GenAI على نظام ويندوز مع GPU**

يوفر هذا الدليل خطوات إعداد واستخدام ONNX Runtime (ORT) مع وحدات معالجة الرسومات (GPU) على نظام ويندوز. تم تصميمه لمساعدتك على الاستفادة من تسريع GPU لنماذجك، مما يحسن الأداء والكفاءة.

يوفر هذا المستند إرشادات حول:

- **إعداد البيئة**: تعليمات تثبيت التبعيات الضرورية مثل CUDA وcuDNN وONNX Runtime.
- **التكوين**: كيفية إعداد البيئة وتهيئة ONNX Runtime لاستخدام موارد GPU بشكل فعال.
- **نصائح تحسين الأداء**: نصائح لتعديل إعدادات GPU للحصول على أفضل أداء.

### **1. بايثون 3.10.x /3.11.8**

   ***ملاحظة*** يُنصح باستخدام [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) كبيئة بايثون.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***تذكير*** إذا كنت قد قمت بتثبيت أي مكتبة ONNX تتعلق ببايثون، يُرجى إلغاء تثبيتها.

### **2. تثبيت CMake باستخدام winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. تثبيت Visual Studio 2022 - تطوير سطح المكتب باستخدام C++**

   ***ملاحظة*** إذا كنت لا ترغب في الترجمة، يمكنك تخطي هذه الخطوة.

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.ar.png)

### **4. تثبيت تعريف NVIDIA**

1. **تعريف NVIDIA GPU**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***تذكير*** يُرجى استخدام الإعدادات الافتراضية أثناء التثبيت.

### **5. إعداد بيئة NVIDIA**

انسخ ملفات lib وbin وinclude الخاصة بـ NVIDIA CUDNN 9.4 إلى نظيراتها في NVIDIA CUDA 12.4.

- انسخ الملفات من *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* إلى *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*.

- انسخ الملفات من *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* إلى *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*.

- انسخ الملفات من *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* إلى *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*.

### **6. تحميل Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. تشغيل InferencePhi35Instruct.ipynb**

   افتح [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) وقم بتنفيذه.

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.ar.png)

### **8. ترجمة ORT GenAI GPU**

   ***ملاحظة***

   1. يُرجى إلغاء تثبيت جميع مكتبات onnx وonnxruntime وonnxruntime-genai أولاً.

   ```bash

   pip list 
   
   ```

   ثم قم بإلغاء تثبيت جميع مكتبات onnxruntime، مثل:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. تحقق من دعم امتدادات Visual Studio.

   تحقق من وجود المسار C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras، وتأكد من وجود المجلد C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration.

   إذا لم يتم العثور عليه، تحقق من مجلدات تعريف Cuda Toolkit الأخرى وانسخ المجلد visual_studio_integration ومحتوياته إلى C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration.

   - إذا كنت لا ترغب في الترجمة، يمكنك تخطي هذه الخطوة.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - قم بتحميل [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip).

   - قم بفك ضغط الملف onnxruntime-win-x64-gpu-1.19.2.zip، وأعد تسميته إلى **ort**، ثم انسخ مجلد ort إلى onnxruntime-genai.

   - باستخدام Windows Terminal، انتقل إلى Developer Command Prompt لـ VS 2022، ثم انتقل إلى onnxruntime-genai.

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.ar.png)

   - قم بترجمته باستخدام بيئة بايثون الخاصة بك.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. في حين أننا نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.