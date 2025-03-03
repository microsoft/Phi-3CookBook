## प्रॉम्प्टफ्लो आणि AISearch सह RAG

या उदाहरणात, आपण Retrieval Augmented Generation (RAG) अॅप्लिकेशन लागू करणार आहोत, ज्यामध्ये Phi3 SLM म्हणून, AI Search vectorDB म्हणून आणि Prompt Flow लो-कोड ऑर्केस्ट्रेटर म्हणून वापरणार आहोत.

## वैशिष्ट्ये

- Docker वापरून सोपी तैनाती.
- AI वर्कफ्लो हाताळण्यासाठी स्केलेबल आर्किटेक्चर.
- Prompt Flow वापरून लो-कोड दृष्टिकोन.

## पूर्वअट

सुरुवात करण्यापूर्वी, खालील गोष्टी पूर्ण केल्या आहेत याची खात्री करा:

- तुमच्या स्थानिक मशीनवर Docker स्थापित केलेले असणे आवश्यक आहे.
- कंटेनर संसाधने तयार आणि व्यवस्थापित करण्यासाठी परवानग्यांसह Azure खाते.
- Azure AI Studio आणि Azure AI Search इन्स्टन्सेस.
- तुमचा इंडेक्स तयार करण्यासाठी एखादा एम्बेडिंग मॉडेल (Azure OpenAI embedding किंवा कॅटलॉगमधील OS मॉडेल).
- तुमच्या स्थानिक मशीनवर Python 3.8 किंवा त्यानंतरची आवृत्ती स्थापित केलेली असावी.
- Azure Container Registry (किंवा तुमच्या आवडीनुसार कोणतीही रजिस्ट्री).

## स्थापना

1. flow.yaml फाइल वापरून Azure AI Studio प्रकल्पावर नवीन फ्लो तयार करा.
2. Azure AI मॉडेल कॅटलॉगमधून Phi3 मॉडेल तैनात करा आणि तुमच्या प्रकल्पाशी कनेक्शन तयार करा. [Phi-3 मॉडेल म्हणून तैनात करा](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. तुमच्या पसंतीच्या कोणत्याही दस्तऐवजाचा वापर करून Azure AI Search वर व्हेक्टर इंडेक्स तयार करा. [Azure AI Search वर व्हेक्टर इंडेक्स तयार करा](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. फ्लो एका व्यवस्थापित एन्डपॉईंटवर तैनात करा आणि ते prompt-flow-frontend.py फाइलमध्ये वापरा. [ऑनलाइन एन्डपॉईंटवर फ्लो तैनात करा](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. रेपॉझिटरी क्लोन करा:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker इमेज तयार करा:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker इमेज Azure Container Registry वर पुश करा:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## वापर

1. Docker कंटेनर चालवा:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. तुमच्या ब्राउझरमध्ये `http://localhost:8501` वर अॅप्लिकेशन ऍक्सेस करा.

## संपर्क

वॅलेंटिना अल्टो - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

संपूर्ण लेख: [Azure Model Catalog मधून Phi-3-Medium मॉडेल म्हणून RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**अस्वीकरण**:  
हा दस्तऐवज मशीन-आधारित एआय अनुवाद सेवांचा वापर करून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज अधिकृत स्रोत मानावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर केल्यामुळे होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.