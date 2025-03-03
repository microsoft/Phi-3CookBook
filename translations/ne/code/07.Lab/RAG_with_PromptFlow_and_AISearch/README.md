## RAG with PromptFlow र AISearch

यस उदाहरणमा, हामी Retrieval Augmented Generation (RAG) एप्लिकेसन लागू गर्नेछौं, जसमा Phi3 लाई SLM, AI Search लाई vectorDB, र Prompt Flow लाई कम-कोड ओरकेस्ट्रेटरको रूपमा प्रयोग गरिनेछ।

## विशेषताहरू

- Docker को प्रयोग गरेर सजिलो परिनियोजन।  
- AI वर्कफ्लोहरूलाई व्यवस्थापन गर्न स्केलेबल आर्किटेक्चर।  
- Prompt Flow प्रयोग गरेर कम कोड दृष्टिकोण।  

## आवश्यकताहरू

सुरु गर्नु अघि, तपाईंसँग तलका आवश्यकताहरू पूरा भएको सुनिश्चित गर्नुहोस्:  

- तपाईंको स्थानीय मेसिनमा Docker स्थापना भएको।  
- Azure खाता, जसमा कन्टेनर स्रोतहरू सिर्जना र व्यवस्थापन गर्न अनुमति छ।  
- Azure AI Studio र Azure AI Search को उदाहरणहरू।  
- तपाईंको इन्डेक्स सिर्जना गर्न एम्बेडिङ मोडेल (यो Azure OpenAI एम्बेडिङ वा क्याटलगबाट कुनै OS मोडेल हुन सक्छ)।  
- तपाईंको स्थानीय मेसिनमा Python 3.8 वा पछिल्लो संस्करण स्थापना भएको।  
- Azure Container Registry (वा तपाईंको रोजाइको कुनै पनि रजिस्ट्री)।  

## स्थापना प्रक्रिया

1. flow.yaml फाइल प्रयोग गरेर तपाईंको Azure AI Studio प्रोजेक्टमा नयाँ फ्लो सिर्जना गर्नुहोस्।  
2. Azure AI मोडेल क्याटलगबाट Phi3 मोडेल परिनियोजन गर्नुहोस् र तपाईंको प्रोजेक्टसँग जडान गर्नुहोस्। [Phi-3 लाई Model as a Service को रूपमा परिनियोजन गर्नुहोस्](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)  
3. तपाईंको रोजाइको कुनै पनि कागजात प्रयोग गरेर Azure AI Search मा भेक्टर इन्डेक्स सिर्जना गर्नुहोस्। [Azure AI Search मा भेक्टर इन्डेक्स सिर्जना गर्नुहोस्](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)  
4. फ्लोलाई म्यानेज गरिएको एन्डप्वाइन्टमा परिनियोजन गर्नुहोस् र यसलाई prompt-flow-frontend.py फाइलमा प्रयोग गर्नुहोस्। [अनलाइन एन्डप्वाइन्टमा फ्लो परिनियोजन गर्नुहोस्](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)  
5. रिपोजिटरी क्लोन गर्नुहोस्:  

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```  

6. Docker इमेज बनाउनुहोस्:  

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```  

7. Docker इमेजलाई Azure Container Registry मा पठाउनुहोस्:  

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```  

## प्रयोग

1. Docker कन्टेनर चलाउनुहोस्:  

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```  

2. तपाईंको ब्राउजरमा एप्लिकेसन `http://localhost:8501` मा पहुँच गर्नुहोस्।  

## सम्पर्क

भ्यालेन्टिना आल्टो - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)  

पूरा लेख: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)  

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको छ। यद्यपि हामी शुद्धताका लागि प्रयास गर्छौं, कृपया जानकार रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।