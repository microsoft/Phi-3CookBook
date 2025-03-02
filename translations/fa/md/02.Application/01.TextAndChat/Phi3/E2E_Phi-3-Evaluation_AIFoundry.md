# ارزیابی مدل‌های Phi-3 / Phi-3.5 با تنظیم دقیق در Azure AI Foundry با تمرکز بر اصول مسئولانه هوش مصنوعی مایکروسافت

این نمونه جامع (E2E) بر اساس راهنمای "[ارزیابی مدل‌های Phi-3 / 3.5 تنظیم‌شده در Azure AI Foundry با تمرکز بر اصول مسئولانه هوش مصنوعی مایکروسافت](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" از جامعه فنی مایکروسافت تهیه شده است.

## مقدمه

### چگونه می‌توانید ایمنی و عملکرد مدل‌های Phi-3 / Phi-3.5 تنظیم‌شده را در Azure AI Foundry ارزیابی کنید؟

تنظیم دقیق یک مدل گاهی می‌تواند منجر به پاسخ‌های ناخواسته یا نامطلوب شود. برای اطمینان از اینکه مدل ایمن و کارآمد باقی می‌ماند، ارزیابی پتانسیل مدل در تولید محتوای مضر و توانایی آن در ارائه پاسخ‌های دقیق، مرتبط و منسجم ضروری است. در این آموزش، یاد خواهید گرفت که چگونه ایمنی و عملکرد مدل‌های Phi-3 / Phi-3.5 تنظیم‌شده را که با Prompt flow در Azure AI Foundry ادغام شده‌اند، ارزیابی کنید.

این فرآیند ارزیابی در Azure AI Foundry به این شکل است:

![معماری آموزش.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fa.png)

*منبع تصویر: [ارزیابی برنامه‌های کاربردی هوش مصنوعی تولیدی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> برای اطلاعات بیشتر و منابع اضافی درباره Phi-3 / Phi-3.5، لطفاً به [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) مراجعه کنید.

### پیش‌نیازها

- [Python](https://www.python.org/downloads)
- [اشتراک Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- مدل Phi-3 / Phi-3.5 تنظیم‌شده

### فهرست مطالب

1. [**سناریو ۱: معرفی ارزیابی Prompt flow در Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [معرفی ارزیابی ایمنی](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [معرفی ارزیابی عملکرد](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**سناریو ۲: ارزیابی مدل Phi-3 / Phi-3.5 در Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [قبل از شروع](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [استقرار Azure OpenAI برای ارزیابی مدل Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ارزیابی مدل Phi-3 / Phi-3.5 تنظیم‌شده با استفاده از ارزیابی Prompt flow در Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [تبریک!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **سناریو ۱: معرفی ارزیابی Prompt flow در Azure AI Foundry**

### معرفی ارزیابی ایمنی

برای اطمینان از اینکه مدل هوش مصنوعی شما اخلاقی و ایمن است، ارزیابی آن بر اساس اصول مسئولانه هوش مصنوعی مایکروسافت بسیار مهم است. در Azure AI Foundry، ارزیابی‌های ایمنی به شما امکان می‌دهند تا آسیب‌پذیری مدل خود را در برابر حملات jailbreak و پتانسیل آن برای تولید محتوای مضر بررسی کنید، که این موارد مستقیماً با این اصول همسو هستند.

![ارزیابی ایمنی.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.fa.png)

*منبع تصویر: [ارزیابی برنامه‌های کاربردی هوش مصنوعی تولیدی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### اصول مسئولانه هوش مصنوعی مایکروسافت

قبل از شروع مراحل فنی، درک اصول مسئولانه هوش مصنوعی مایکروسافت ضروری است. این اصول یک چارچوب اخلاقی هستند که برای هدایت توسعه، استقرار و بهره‌برداری مسئولانه از سیستم‌های هوش مصنوعی طراحی شده‌اند. این اصول تضمین می‌کنند که فناوری‌های هوش مصنوعی به شیوه‌ای عادلانه، شفاف و فراگیر طراحی، توسعه و پیاده‌سازی شوند. این اصول اساس ارزیابی ایمنی مدل‌های هوش مصنوعی را تشکیل می‌دهند.

اصول مسئولانه هوش مصنوعی مایکروسافت شامل موارد زیر است:

- **عدالت و شمول‌پذیری**: سیستم‌های هوش مصنوعی باید با همه افراد به صورت عادلانه رفتار کنند و از تأثیرگذاری متفاوت بر گروه‌های مشابه اجتناب کنند. به عنوان مثال، هنگامی که سیستم‌های هوش مصنوعی در مورد درمان پزشکی، درخواست وام یا استخدام مشاوره می‌دهند، باید برای همه افرادی که علائم، شرایط مالی یا صلاحیت‌های حرفه‌ای مشابه دارند، توصیه‌های یکسانی ارائه دهند.

- **قابلیت اطمینان و ایمنی**: برای ایجاد اعتماد، ضروری است که سیستم‌های هوش مصنوعی به صورت قابل اعتماد، ایمن و مداوم عمل کنند. این سیستم‌ها باید بتوانند به گونه‌ای که در ابتدا طراحی شده‌اند عمل کنند، به شرایط پیش‌بینی نشده به صورت ایمن پاسخ دهند و در برابر دستکاری‌های مضر مقاومت کنند. رفتار آنها و انواع شرایطی که می‌توانند مدیریت کنند، نشان‌دهنده دامنه موقعیت‌ها و شرایطی است که توسعه‌دهندگان در طول طراحی و آزمایش پیش‌بینی کرده‌اند.

- **شفافیت**: هنگامی که سیستم‌های هوش مصنوعی به تصمیم‌گیری‌هایی کمک می‌کنند که تأثیرات عظیمی بر زندگی افراد دارند، ضروری است که مردم بفهمند این تصمیمات چگونه گرفته شده‌اند. به عنوان مثال، یک بانک ممکن است از یک سیستم هوش مصنوعی برای تصمیم‌گیری در مورد اعتبارسنجی افراد استفاده کند. یک شرکت ممکن است از یک سیستم هوش مصنوعی برای تعیین واجد شرایط‌ترین نامزدها برای استخدام استفاده کند.

- **حریم خصوصی و امنیت**: با گسترش هوش مصنوعی، محافظت از حریم خصوصی و امنیت اطلاعات شخصی و تجاری اهمیت بیشتری پیدا می‌کند. در هوش مصنوعی، حریم خصوصی و امنیت داده‌ها نیازمند توجه دقیق است، زیرا دسترسی به داده‌ها برای سیستم‌های هوش مصنوعی ضروری است تا پیش‌بینی‌ها و تصمیم‌گیری‌های دقیق و آگاهانه درباره افراد انجام دهند.

- **پاسخگویی**: افرادی که سیستم‌های هوش مصنوعی را طراحی و پیاده‌سازی می‌کنند، باید در قبال نحوه عملکرد سیستم‌هایشان پاسخگو باشند. سازمان‌ها باید از استانداردهای صنعتی برای توسعه هنجارهای پاسخگویی استفاده کنند. این هنجارها می‌توانند اطمینان حاصل کنند که سیستم‌های هوش مصنوعی در هیچ تصمیمی که زندگی افراد را تحت تأثیر قرار می‌دهد، قدرت نهایی ندارند. همچنین می‌توانند اطمینان حاصل کنند که انسان‌ها کنترل معناداری بر سیستم‌های هوش مصنوعی بسیار خودمختار دارند.

![مرکز اصول مسئولانه.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.fa.png)

*منبع تصویر: [هوش مصنوعی مسئولانه چیست؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> برای یادگیری بیشتر درباره اصول مسئولانه هوش مصنوعی مایکروسافت، به [هوش مصنوعی مسئولانه چیست؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) مراجعه کنید.

#### معیارهای ایمنی

در این آموزش، ایمنی مدل تنظیم‌شده Phi-3 را با استفاده از معیارهای ایمنی Azure AI Foundry ارزیابی خواهید کرد. این معیارها به شما کمک می‌کنند تا پتانسیل مدل برای تولید محتوای مضر و آسیب‌پذیری آن در برابر حملات jailbreak را ارزیابی کنید. معیارهای ایمنی شامل موارد زیر هستند:

- **محتوای مرتبط با خودآسیبی**: بررسی می‌کند که آیا مدل تمایل به تولید محتوای مرتبط با خودآسیبی دارد.
- **محتوای نفرت‌انگیز و ناعادلانه**: بررسی می‌کند که آیا مدل تمایل به تولید محتوای نفرت‌انگیز یا ناعادلانه دارد.
- **محتوای خشونت‌آمیز**: بررسی می‌کند که آیا مدل تمایل به تولید محتوای خشونت‌آمیز دارد.
- **محتوای جنسی**: بررسی می‌کند که آیا مدل تمایل به تولید محتوای جنسی نامناسب دارد.

ارزیابی این جنبه‌ها تضمین می‌کند که مدل هوش مصنوعی محتوای مضر یا توهین‌آمیز تولید نمی‌کند و با ارزش‌های اجتماعی و استانداردهای نظارتی همسو است.

![ارزیابی بر اساس ایمنی.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.fa.png)

### معرفی ارزیابی عملکرد

برای اطمینان از اینکه مدل هوش مصنوعی شما همان‌طور که انتظار می‌رود عمل می‌کند، ارزیابی عملکرد آن بر اساس معیارهای عملکرد بسیار مهم است. در Azure AI Foundry، ارزیابی‌های عملکرد به شما امکان می‌دهند تا اثربخشی مدل خود را در تولید پاسخ‌های دقیق، مرتبط و منسجم بررسی کنید.

![ارزیابی عملکرد.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.fa.png)

*منبع تصویر: [ارزیابی برنامه‌های کاربردی هوش مصنوعی تولیدی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### معیارهای عملکرد

در این آموزش، عملکرد مدل تنظیم‌شده Phi-3 / Phi-3.5 را با استفاده از معیارهای عملکرد Azure AI Foundry ارزیابی خواهید کرد. این معیارها به شما کمک می‌کنند تا اثربخشی مدل در تولید پاسخ‌های دقیق، مرتبط و منسجم را بررسی کنید. معیارهای عملکرد شامل موارد زیر هستند:

- **پایه‌گذاری**: ارزیابی می‌کند که پاسخ‌های تولید شده چقدر با اطلاعات منبع ورودی همخوانی دارند.
- **ارتباط**: میزان ارتباط پاسخ‌های تولید شده با سؤالات داده شده را ارزیابی می‌کند.
- **انسجام**: بررسی می‌کند که متن تولید شده چقدر روان است، به طور طبیعی خوانده می‌شود و شبیه زبان انسانی است.
- **روانی**: مهارت زبانی متن تولید شده را ارزیابی می‌کند.
- **شباهت به GPT**: پاسخ تولید شده را با پاسخ مرجع از نظر شباهت مقایسه می‌کند.
- **امتیاز F1**: نسبت کلمات مشترک بین پاسخ تولید شده و داده‌های منبع را محاسبه می‌کند.

این معیارها به شما کمک می‌کنند تا اثربخشی مدل در تولید پاسخ‌های دقیق، مرتبط و منسجم را ارزیابی کنید.

![ارزیابی بر اساس عملکرد.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.fa.png)

## **سناریو ۲: ارزیابی مدل Phi-3 / Phi-3.5 در Azure AI Foundry**

### قبل از شروع

این آموزش دنباله‌ای بر پست‌های وبلاگ قبلی، "[تنظیم دقیق و ادغام مدل‌های Phi-3 سفارشی با Prompt Flow: راهنمای گام به گام](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" و "[تنظیم دقیق و ادغام مدل‌های Phi-3 سفارشی با Prompt Flow در Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" است. در این پست‌ها، فرآیند تنظیم دقیق یک مدل Phi-3 / Phi-3.5 در Azure AI Foundry و ادغام آن با Prompt flow توضیح داده شده است.

در این آموزش، یک مدل Azure OpenAI را به عنوان ارزیاب در Azure AI Foundry مستقر کرده و از آن برای ارزیابی مدل تنظیم‌شده Phi-3 / Phi-3.5 خود استفاده خواهید کرد.

قبل از شروع این آموزش، اطمینان حاصل کنید که پیش‌نیازهای زیر را، همان‌طور که در آموزش‌های قبلی توضیح داده شده است، دارید:

1. یک مجموعه داده آماده برای ارزیابی مدل تنظیم‌شده Phi-3 / Phi-3.5.
1. یک مدل Phi-3 / Phi-3.5 که تنظیم دقیق شده و در Azure Machine Learning مستقر شده است.
1. یک Prompt flow که با مدل تنظیم‌شده Phi-3 / Phi-3.5 شما در Azure AI Foundry ادغام شده است.

> [!NOTE]
> شما از فایل *test_data.jsonl* که در پوشه داده‌ها از مجموعه داده **ULTRACHAT_200k** دانلود شده در پست‌های وبلاگ قبلی قرار دارد، به عنوان مجموعه داده برای ارزیابی مدل تنظیم‌شده Phi-3 / Phi-3.5 استفاده خواهید کرد.

#### ادغام مدل سفارشی Phi-3 / Phi-3.5 با Prompt flow در Azure AI Foundry (رویکرد مبتنی بر کد)

> [!NOTE]
> اگر از رویکرد کم‌کد توضیح داده شده در "[تنظیم دقیق و ادغام مدل‌های Phi-3 سفارشی با Prompt Flow در Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" استفاده کرده‌اید، می‌توانید این تمرین را رد کرده و به تمرین بعدی بروید.
> با این حال، اگر از رویکرد مبتنی بر کد توضیح داده شده در "[تنظیم دقیق و ادغام مدل‌های Phi-3 سفارشی با Prompt Flow: راهنمای گام به گام](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" برای تنظیم دقیق و استقرار مدل Phi-3 / Phi-3.5 خود استفاده کرده‌اید، فرآیند اتصال مدل شما به Prompt flow کمی متفاوت است. این فرآیند را در این تمرین خواهید آموخت.

برای ادامه، باید مدل تنظیم‌شده Phi-3 / Phi-3.5 خود را در Prompt flow در Azure AI Foundry ادغام کنید.

#### ایجاد هاب در Azure AI Foundry

قبل از ایجاد پروژه، باید یک هاب ایجاد کنید. هاب مانند یک گروه منابع عمل می‌کند و به شما امکان می‌دهد چندین پروژه را در Azure AI Foundry سازماندهی و مدیریت کنید.

1. وارد [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) شوید.

1. از زبانه سمت چپ **All hubs** را انتخاب کنید.

1. از منوی ناوبری **+ New hub** را انتخاب کنید.

    ![ایجاد هاب.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.fa.png)

1. وظایف زیر را انجام دهید:

    - **نام هاب** را وارد کنید. باید مقدار منحصربه‌فردی باشد.
    - **اشتراک Azure** خود را انتخاب کنید.
    - **گروه منابع** مورد نظر خود را انتخاب کنید (در صورت نیاز یک گروه جدید ایجاد کنید).
    - **موقعیت مکانی** مورد نظر خود را انتخاب کنید.
    - **اتصال به خدمات هوش مصنوعی Azure** را انتخاب کنید (در صورت نیاز یک مورد جدید ایجاد کنید).
    - **اتصال به Azure AI Search** را روی **Skip connecting** تنظیم کنید.
![پر کردن هاب.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.fa.png)

1. **Next** را انتخاب کنید.

#### ایجاد پروژه Azure AI Foundry

1. در هابی که ایجاد کرده‌اید، از تب سمت چپ **All projects** را انتخاب کنید.

1. از منوی ناوبری **+ New project** را انتخاب کنید.

   ![انتخاب پروژه جدید.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.fa.png)

1. **نام پروژه** را وارد کنید. این نام باید یکتا باشد.

   ![ایجاد پروژه.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.fa.png)

1. **Create a project** را انتخاب کنید.

#### اضافه کردن یک اتصال سفارشی برای مدل بهینه‌شده Phi-3 / Phi-3.5

برای ادغام مدل سفارشی Phi-3 / Phi-3.5 خود با Prompt flow، باید نقطه پایانی مدل و کلید آن را در یک اتصال سفارشی ذخیره کنید. این تنظیمات دسترسی به مدل سفارشی شما در Prompt flow را تضمین می‌کند.

#### تنظیم کلید API و آدرس نقطه پایانی مدل بهینه‌شده Phi-3 / Phi-3.5

1. به [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) مراجعه کنید.

1. به فضای کاری Azure Machine Learning که ایجاد کرده‌اید بروید.

1. از تب سمت چپ **Endpoints** را انتخاب کنید.

   ![انتخاب نقاط پایانی.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.fa.png)

1. نقطه پایانی که ایجاد کرده‌اید را انتخاب کنید.

   ![انتخاب نقاط پایانی ایجادشده.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.fa.png)

1. از منوی ناوبری **Consume** را انتخاب کنید.

1. **REST endpoint** و **Primary key** خود را کپی کنید.

   ![کپی کلید API و آدرس نقطه پایانی.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.fa.png)

#### اضافه کردن اتصال سفارشی

1. به [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) مراجعه کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. در پروژه‌ای که ایجاد کرده‌اید، از تب سمت چپ **Settings** را انتخاب کنید.

1. **+ New connection** را انتخاب کنید.

   ![انتخاب اتصال جدید.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.fa.png)

1. از منوی ناوبری **Custom keys** را انتخاب کنید.

   ![انتخاب کلیدهای سفارشی.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.fa.png)

1. مراحل زیر را انجام دهید:

   - **+ Add key value pairs** را انتخاب کنید.
   - برای نام کلید، **endpoint** وارد کنید و آدرس نقطه پایانی که از Azure ML Studio کپی کرده‌اید را در فیلد مقدار قرار دهید.
   - دوباره **+ Add key value pairs** را انتخاب کنید.
   - برای نام کلید، **key** وارد کنید و کلیدی که از Azure ML Studio کپی کرده‌اید را در فیلد مقدار قرار دهید.
   - پس از اضافه کردن کلیدها، **is secret** را انتخاب کنید تا از نمایش کلید جلوگیری شود.

   ![اضافه کردن اتصال.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.fa.png)

1. **Add connection** را انتخاب کنید.

#### ایجاد Prompt flow

شما یک اتصال سفارشی در Azure AI Foundry اضافه کرده‌اید. اکنون، با استفاده از مراحل زیر یک Prompt flow ایجاد کنید. سپس، این Prompt flow را به اتصال سفارشی متصل کنید تا مدل بهینه‌شده را در Prompt flow استفاده کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

1. از تب سمت چپ **Prompt flow** را انتخاب کنید.

1. از منوی ناوبری **+ Create** را انتخاب کنید.

   ![انتخاب Prompt flow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.fa.png)

1. از منوی ناوبری **Chat flow** را انتخاب کنید.

   ![انتخاب chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.fa.png)

1. **نام پوشه** را وارد کنید.

   ![انتخاب chat flow.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.fa.png)

1. **Create** را انتخاب کنید.

#### تنظیم Prompt flow برای چت با مدل سفارشی Phi-3 / Phi-3.5

شما باید مدل بهینه‌شده Phi-3 / Phi-3.5 را در یک Prompt flow ادغام کنید. با این حال، Prompt flow موجود برای این منظور طراحی نشده است. بنابراین، باید Prompt flow را بازطراحی کنید تا ادغام مدل سفارشی ممکن شود.

1. در Prompt flow، مراحل زیر را برای بازسازی جریان موجود انجام دهید:

   - **Raw file mode** را انتخاب کنید.
   - تمام کدهای موجود در فایل *flow.dag.yml* را حذف کنید.
   - کد زیر را به فایل *flow.dag.yml* اضافه کنید.

     ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

   - **Save** را انتخاب کنید.

   ![انتخاب حالت فایل خام.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.fa.png)

1. کد زیر را به فایل *integrate_with_promptflow.py* اضافه کنید تا مدل سفارشی Phi-3 / Phi-3.5 در Prompt flow استفاده شود.

   ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

   ![چسباندن کد Prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.fa.png)

> [!NOTE]  
> برای اطلاعات بیشتر در مورد استفاده از Prompt flow در Azure AI Foundry، می‌توانید به [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) مراجعه کنید.

1. **Chat input** و **Chat output** را انتخاب کنید تا امکان چت با مدل شما فراهم شود.

   ![انتخاب ورودی و خروجی.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.fa.png)

1. اکنون آماده چت با مدل سفارشی Phi-3 / Phi-3.5 خود هستید. در تمرین بعدی، یاد خواهید گرفت که چگونه Prompt flow را شروع کرده و از آن برای چت با مدل بهینه‌شده Phi-3 / Phi-3.5 استفاده کنید.

> [!NOTE]  
>  
> جریان بازطراحی‌شده باید شبیه تصویر زیر باشد:  
>  
> ![نمونه جریان](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.fa.png)

#### شروع Prompt flow

1. برای شروع Prompt flow، **Start compute sessions** را انتخاب کنید.

   ![شروع جلسه محاسباتی.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.fa.png)

1. برای تازه‌سازی پارامترها، **Validate and parse input** را انتخاب کنید.

   ![اعتبارسنجی ورودی.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.fa.png)

1. **Value** اتصال را به اتصال سفارشی که ایجاد کرده‌اید انتخاب کنید. برای مثال، *connection*.

   ![اتصال.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.fa.png)

#### چت با مدل سفارشی Phi-3 / Phi-3.5

1. **Chat** را انتخاب کنید.

   ![انتخاب چت.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.fa.png)

1. نمونه‌ای از نتایج: اکنون می‌توانید با مدل سفارشی Phi-3 / Phi-3.5 خود چت کنید. توصیه می‌شود سوالاتی بر اساس داده‌های استفاده‌شده برای بهینه‌سازی بپرسید.

   ![چت با Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.fa.png)

### استقرار Azure OpenAI برای ارزیابی مدل Phi-3 / Phi-3.5

برای ارزیابی مدل Phi-3 / Phi-3.5 در Azure AI Foundry، باید یک مدل Azure OpenAI مستقر کنید. این مدل برای ارزیابی عملکرد مدل Phi-3 / Phi-3.5 استفاده خواهد شد.

#### استقرار Azure OpenAI

1. وارد [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) شوید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

   ![انتخاب پروژه.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fa.png)

1. در پروژه‌ای که ایجاد کرده‌اید، از تب سمت چپ **Deployments** را انتخاب کنید.

1. از منوی ناوبری **+ Deploy model** را انتخاب کنید.

1. **Deploy base model** را انتخاب کنید.

   ![انتخاب استقرار.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.fa.png)

1. مدل Azure OpenAI موردنظر خود را انتخاب کنید. برای مثال، **gpt-4o**.

   ![انتخاب مدل Azure OpenAI.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.fa.png)

1. **Confirm** را انتخاب کنید.

### ارزیابی مدل بهینه‌شده Phi-3 / Phi-3.5 با استفاده از ارزیابی Prompt flow در Azure AI Foundry

### شروع یک ارزیابی جدید

1. به [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) مراجعه کنید.

1. به پروژه Azure AI Foundry که ایجاد کرده‌اید بروید.

   ![انتخاب پروژه.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.fa.png)

1. در پروژه‌ای که ایجاد کرده‌اید، از تب سمت چپ **Evaluation** را انتخاب کنید.

1. از منوی ناوبری **+ New evaluation** را انتخاب کنید.
![انتخاب ارزیابی.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.fa.png)

1. **Prompt flow** را برای ارزیابی انتخاب کنید.

   ![انتخاب ارزیابی Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.fa.png)

1. کارهای زیر را انجام دهید:

   - نام ارزیابی را وارد کنید. این نام باید یکتا باشد.
   - **پرسش و پاسخ بدون زمینه** را به‌عنوان نوع کار انتخاب کنید. زیرا مجموعه داده **ULTRACHAT_200k** که در این آموزش استفاده شده است، شامل زمینه نمی‌باشد.
   - جریان پرامپتی که می‌خواهید ارزیابی کنید را انتخاب کنید.

   ![ارزیابی Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.fa.png)

1. **Next** را انتخاب کنید.

1. کارهای زیر را انجام دهید:

   - **Add your dataset** را برای بارگذاری مجموعه داده انتخاب کنید. به‌عنوان مثال، می‌توانید فایل مجموعه داده تست مانند *test_data.json1* را که هنگام دانلود مجموعه داده **ULTRACHAT_200k** ارائه می‌شود، بارگذاری کنید.
   - ستون مناسب مجموعه داده را که با مجموعه داده شما مطابقت دارد، انتخاب کنید. به‌عنوان مثال، اگر از مجموعه داده **ULTRACHAT_200k** استفاده می‌کنید، **${data.prompt}** را به‌عنوان ستون مجموعه داده انتخاب کنید.

   ![ارزیابی Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.fa.png)

1. **Next** را انتخاب کنید.

1. کارهای زیر را برای پیکربندی معیارهای عملکرد و کیفیت انجام دهید:

   - معیارهای عملکرد و کیفیتی که می‌خواهید استفاده کنید را انتخاب کنید.
   - مدل Azure OpenAI که برای ارزیابی ایجاد کرده‌اید را انتخاب کنید. به‌عنوان مثال، **gpt-4o** را انتخاب کنید.

   ![ارزیابی Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.fa.png)

1. کارهای زیر را برای پیکربندی معیارهای ریسک و ایمنی انجام دهید:

   - معیارهای ریسک و ایمنی که می‌خواهید استفاده کنید را انتخاب کنید.
   - آستانه‌ای که برای محاسبه نرخ نقص می‌خواهید استفاده کنید را انتخاب کنید. به‌عنوان مثال، **متوسط** را انتخاب کنید.
   - برای **پرسش**، **Data source** را به **{$data.prompt}** تنظیم کنید.
   - برای **پاسخ**، **Data source** را به **{$run.outputs.answer}** تنظیم کنید.
   - برای **ground_truth**، **Data source** را به **{$data.message}** تنظیم کنید.

   ![ارزیابی Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.fa.png)

1. **Next** را انتخاب کنید.

1. **Submit** را برای شروع ارزیابی انتخاب کنید.

1. ارزیابی مدتی طول می‌کشد تا تکمیل شود. می‌توانید پیشرفت را در زبانه **Evaluation** مشاهده کنید.

### بررسی نتایج ارزیابی

> [!NOTE]
> نتایج ارائه‌شده در زیر برای نشان دادن فرآیند ارزیابی است. در این آموزش، از مدلی استفاده شده است که بر روی مجموعه داده‌ای نسبتاً کوچک تنظیم شده است، که ممکن است به نتایج کمتر بهینه منجر شود. نتایج واقعی ممکن است بسته به اندازه، کیفیت و تنوع مجموعه داده مورد استفاده و همچنین پیکربندی خاص مدل به‌طور قابل‌توجهی متفاوت باشد.

پس از تکمیل ارزیابی، می‌توانید نتایج معیارهای عملکرد و ایمنی را بررسی کنید.

1. معیارهای عملکرد و کیفیت:

   - اثربخشی مدل در تولید پاسخ‌های منسجم، روان و مرتبط را ارزیابی کنید.

   ![نتیجه ارزیابی.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.fa.png)

1. معیارهای ریسک و ایمنی:

   - اطمینان حاصل کنید که خروجی‌های مدل ایمن هستند و با اصول AI مسئولانه همخوانی دارند و از محتوای مضر یا توهین‌آمیز اجتناب می‌کنند.

   ![نتیجه ارزیابی.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.fa.png)

1. می‌توانید برای مشاهده **نتایج معیارهای جزئی** به پایین اسکرول کنید.

   ![نتیجه ارزیابی.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.fa.png)

1. با ارزیابی مدل سفارشی Phi-3 / Phi-3.5 خود در برابر معیارهای عملکرد و ایمنی، می‌توانید اطمینان حاصل کنید که مدل نه تنها مؤثر است، بلکه با اصول AI مسئولانه همخوانی دارد و آماده استقرار در دنیای واقعی است.

## تبریک!

### شما این آموزش را تکمیل کردید

شما با موفقیت مدل Phi-3 تنظیم‌شده را که با Prompt flow در Azure AI Foundry ادغام شده است، ارزیابی کردید. این یک گام مهم در اطمینان از این است که مدل‌های AI شما نه تنها عملکرد خوبی دارند، بلکه با اصول AI مسئولانه مایکروسافت همخوانی دارند تا به شما در ساخت برنامه‌های AI قابل‌اعتماد و قابل‌اطمینان کمک کنند.

![معماری.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.fa.png)

## پاک‌سازی منابع Azure

منابع Azure خود را پاک کنید تا از هزینه‌های اضافی به حساب شما جلوگیری شود. به پورتال Azure بروید و منابع زیر را حذف کنید:

- منبع Azure Machine Learning.
- نقطه پایانی مدل Azure Machine Learning.
- منبع پروژه Azure AI Foundry.
- منبع Prompt flow در Azure AI Foundry.

### مراحل بعدی

#### مستندات

- [ارزیابی سیستم‌های AI با استفاده از داشبورد AI مسئولانه](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [معیارهای ارزیابی و نظارت برای AI تولیدی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [مستندات Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [مستندات Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### محتوای آموزشی

- [مقدمه‌ای بر رویکرد AI مسئولانه مایکروسافت](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [مقدمه‌ای بر Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### مرجع

- [AI مسئولانه چیست؟](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [اعلام ابزارهای جدید در Azure AI برای کمک به ساخت برنامه‌های AI تولیدی امن‌تر و قابل‌اعتمادتر](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [ارزیابی برنامه‌های AI تولیدی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.