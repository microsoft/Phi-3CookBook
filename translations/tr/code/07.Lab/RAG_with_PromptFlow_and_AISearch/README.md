## PromptFlow ve AISearch ile RAG

Bu örnekte, Phi3'ü SLM, AI Search'ü vectorDB ve Prompt Flow'u düşük kodlu bir düzenleyici olarak kullanarak bir Retrieval Augmented Generation (RAG) uygulaması gerçekleştireceğiz.

## Özellikler

- Docker kullanarak kolay kurulum.
- Yapay zeka iş akışlarını yönetmek için ölçeklenebilir mimari.
- Prompt Flow ile düşük kod yaklaşımı.

## Ön Koşullar

Başlamadan önce aşağıdaki gereksinimleri karşıladığınızdan emin olun:

- Yerel makinenizde kurulu bir Docker.
- Konteyner kaynakları oluşturma ve yönetme yetkisine sahip bir Azure hesabı.
- Bir Azure AI Studio ve Azure AI Search örneği.
- Dizin oluşturmak için bir gömme modeli (Azure OpenAI gömme modeli veya katalogdan bir OS modeli olabilir).
- Yerel makinenizde kurulu Python 3.8 veya daha yeni bir sürüm.
- Bir Azure Container Registry (veya tercih ettiğiniz başka bir kayıt defteri).

## Kurulum

1. flow.yaml dosyasını kullanarak Azure AI Studio Projenizde yeni bir akış oluşturun.
2. Azure AI model kataloğunuzdan bir Phi3 Modeli dağıtın ve projeye bağlantısını oluşturun. [Phi-3'ü Model as a Service olarak Dağıtma](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Seçtiğiniz herhangi bir belgeyi kullanarak Azure AI Search üzerinde bir vektör dizini oluşturun. [Azure AI Search üzerinde vektör dizini oluşturma](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Akışı yönetilen bir uç noktaya dağıtın ve prompt-flow-frontend.py dosyasında kullanın. [Çevrimiçi bir uç noktaya akış dağıtma](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Depoyu klonlayın:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker imajını oluşturun:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker imajını Azure Container Registry'e gönderin:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Kullanım

1. Docker konteynerini çalıştırın:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Uygulamaya tarayıcınızdan `http://localhost:8501` adresinden erişin.

## İletişim

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Tam Makale: [Azure Model Kataloğundan Model as a Service olarak Phi-3-Medium ile RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanabilecek yanlış anlama veya yorumlamalardan sorumlu değiliz.