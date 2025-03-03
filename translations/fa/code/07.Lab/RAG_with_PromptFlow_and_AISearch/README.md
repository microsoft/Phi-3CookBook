## RAG با PromptFlow و AISearch

در این مثال، ما یک برنامه تولید محتوا با بازیابی (RAG) را پیاده‌سازی خواهیم کرد که از Phi3 به عنوان SLM، AI Search به عنوان vectorDB و Prompt Flow به عنوان ارکستراتور کم‌کد استفاده می‌کند.

## ویژگی‌ها

- استقرار آسان با استفاده از Docker.
- معماری مقیاس‌پذیر برای مدیریت جریان‌های کاری هوش مصنوعی.
- رویکرد کم‌کد با استفاده از Prompt Flow.

## پیش‌نیازها

پیش از شروع، اطمینان حاصل کنید که موارد زیر فراهم هستند:

- Docker روی دستگاه محلی شما نصب شده باشد.
- یک حساب Azure با دسترسی برای ایجاد و مدیریت منابع کانتینری.
- نمونه‌های Azure AI Studio و Azure AI Search.
- یک مدل embedding برای ایجاد ایندکس شما (می‌تواند یک embedding از Azure OpenAI یا یک مدل OS از کاتالوگ باشد).
- پایتون نسخه 3.8 یا جدیدتر روی دستگاه محلی شما نصب شده باشد.
- یک Azure Container Registry (یا هر رجیستری دلخواه شما).

## نصب

1. یک جریان جدید در پروژه Azure AI Studio خود با استفاده از فایل flow.yaml ایجاد کنید.
2. یک مدل Phi3 را از کاتالوگ مدل Azure AI مستقر کرده و ارتباط آن را با پروژه خود برقرار کنید. [استقرار Phi-3 به عنوان یک مدل به عنوان سرویس](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ایندکس وکتور را در Azure AI Search با استفاده از هر سند دلخواه خود ایجاد کنید. [ایجاد ایندکس وکتور در Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. جریان را روی یک نقطه پایانی مدیریت‌شده مستقر کنید و از آن در فایل prompt-flow-frontend.py استفاده کنید. [استقرار جریان روی یک نقطه پایانی آنلاین](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. مخزن را کلون کنید:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. تصویر Docker را بسازید:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. تصویر Docker را به Azure Container Registry ارسال کنید:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استفاده

1. کانتینر Docker را اجرا کنید:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. برنامه را در مرورگر خود در آدرس `http://localhost:8501` باز کنید.

## تماس

والنتینا آلتو - [لینکدین](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مقاله کامل: [RAG با Phi-3-Medium به عنوان یک مدل به عنوان سرویس از کاتالوگ مدل Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.