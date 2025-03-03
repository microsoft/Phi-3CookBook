# **استخدام Phi-3 في أجهزة الأندرويد**

لنستعرض كيف يمكنك تنفيذ الاستدلال باستخدام Phi-3-mini على أجهزة الأندرويد. Phi-3-mini هي سلسلة جديدة من النماذج التي طورتها مايكروسوفت لتتيح نشر نماذج اللغة الكبيرة (LLMs) على الأجهزة الطرفية وأجهزة إنترنت الأشياء.

## Semantic Kernel والاستدلال

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) هو إطار عمل يساعدك في إنشاء تطبيقات متوافقة مع Azure OpenAI Service، ونماذج OpenAI، وحتى النماذج المحلية. إذا كنت جديدًا على Semantic Kernel، ننصحك بالاطلاع على [دليل الطهي الخاص بـ Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### الوصول إلى Phi-3-mini باستخدام Semantic Kernel

يمكنك دمجه مع موصل Hugging Face في Semantic Kernel. راجع هذا [الكود النموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

بشكل افتراضي، يتوافق مع معرف النموذج على Hugging Face. ومع ذلك، يمكنك أيضًا الاتصال بخادم نموذج Phi-3-mini الذي تم إنشاؤه محليًا.

### استدعاء النماذج المضغوطة باستخدام Ollama أو LlamaEdge

يفضل العديد من المستخدمين استخدام النماذج المضغوطة لتشغيل النماذج محليًا. [Ollama](https://ollama.com/) و[LlamaEdge](https://llamaedge.com) تتيحان للمستخدمين الأفراد استدعاء نماذج مضغوطة مختلفة:

#### Ollama

يمكنك تشغيل `ollama run Phi-3` مباشرة أو تكوينه في وضع عدم الاتصال عن طريق إنشاء `Modelfile` مع المسار إلى ملف `.gguf` الخاص بك.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[كود نموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

إذا كنت ترغب في استخدام ملفات `.gguf` في السحابة وعلى الأجهزة الطرفية في نفس الوقت، فإن LlamaEdge خيار رائع. يمكنك الرجوع إلى هذا [الكود النموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) للبدء.

### التثبيت والتشغيل على هواتف الأندرويد

1. **قم بتحميل تطبيق MLC Chat** (مجاني) لهواتف الأندرويد.  
2. قم بتنزيل ملف APK (حجمه 148 ميجابايت) وقم بتثبيته على جهازك.  
3. افتح تطبيق MLC Chat. ستظهر لك قائمة بنماذج الذكاء الاصطناعي، بما في ذلك Phi-3-mini.

باختصار، يفتح Phi-3-mini آفاقًا مثيرة للذكاء الاصطناعي التوليدي على الأجهزة الطرفية، ويمكنك البدء في استكشاف إمكانياته على الأندرويد.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمات ترجمة آلية تعتمد على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والموثوق. للحصول على معلومات حساسة أو هامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ نتيجة لاستخدام هذه الترجمة.