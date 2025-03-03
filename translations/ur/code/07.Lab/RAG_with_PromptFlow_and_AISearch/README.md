## پرامپٹ فلو اور اے آئی سرچ کے ساتھ RAG

اس مثال میں، ہم ایک Retrieval Augmented Generation (RAG) ایپلیکیشن نافذ کریں گے جو Phi3 کو SLM کے طور پر، AI Search کو vectorDB کے طور پر اور Prompt Flow کو کم کوڈ آرکیسٹریٹر کے طور پر استعمال کرے گی۔

## خصوصیات

- ڈوکر کا استعمال کرتے ہوئے آسان ڈپلائمنٹ۔
- اے آئی ورک فلو کو ہینڈل کرنے کے لیے اسکیل ایبل آرکیٹیکچر۔
- کم کوڈ اپروچ پرامپٹ فلو کے ذریعے۔

## شرائط

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل شرائط موجود ہیں:

- آپ کی لوکل مشین پر ڈوکر انسٹال ہو۔
- ایک Azure اکاؤنٹ جس میں کنٹینر ریسورسز بنانے اور مینیج کرنے کی اجازت ہو۔
- Azure AI Studio اور Azure AI Search کی انسٹینسز۔
- ایک ایمبیڈنگ ماڈل جو آپ کا انڈیکس بنائے (یہ Azure OpenAI ایمبیڈنگ یا کیٹلاگ سے کوئی بھی OS ماڈل ہو سکتا ہے)۔
- آپ کی لوکل مشین پر Python 3.8 یا اس سے جدید ورژن انسٹال ہو۔
- Azure Container Registry (یا آپ کی پسند کا کوئی بھی رجسٹری)۔

## انسٹالیشن

1. اپنے Azure AI Studio پروجیکٹ پر flow.yaml فائل کا استعمال کرتے ہوئے نیا فلو بنائیں۔
2. اپنے Azure AI ماڈل کیٹلاگ سے Phi3 ماڈل ڈپلائے کریں اور اپنے پروجیکٹ کے ساتھ کنکشن بنائیں۔ [Phi-3 کو Model as a Service کے طور پر ڈپلائے کریں](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Azure AI Search پر کسی بھی دستاویز کا استعمال کرتے ہوئے ویکٹر انڈیکس بنائیں۔ [Azure AI Search پر ویکٹر انڈیکس بنائیں](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. فلو کو ایک مینیجڈ اینڈ پوائنٹ پر ڈپلائے کریں اور اسے prompt-flow-frontend.py فائل میں استعمال کریں۔ [آن لائن اینڈ پوائنٹ پر فلو ڈپلائے کریں](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ریپوزٹری کلون کریں:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. ڈوکر امیج بنائیں:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ڈوکر امیج کو Azure Container Registry پر پش کریں:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## استعمال

1. ڈوکر کنٹینر چلائیں:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. اپنے براؤزر میں ایپلیکیشن تک رسائی حاصل کریں: `http://localhost:8501`

## رابطہ

ویلنٹینا آلٹو - [لنکڈ اِن](https://www.linkedin.com/in/valentina-alto-6a0590148/)

مکمل آرٹیکل: [Azure Model Catalog سے Phi-3-Medium کو Model as a Service کے طور پر استعمال کرتے ہوئے RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے پوری کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقصانات ہو سکتے ہیں۔ اصل دستاویز، جو اس کی مقامی زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔