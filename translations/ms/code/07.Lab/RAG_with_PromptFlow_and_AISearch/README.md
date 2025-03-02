## RAG dengan PromptFlow dan AISearch

Dalam contoh ini, kita akan melaksanakan aplikasi Retrieval Augmented Generation (RAG) dengan menggunakan Phi3 sebagai SLM, AI Search sebagai vectorDB, dan Prompt Flow sebagai pengatur alur kerja low-code.

## Ciri-ciri

- Penyebaran mudah menggunakan Docker.
- Seni bina berskala untuk mengendalikan alur kerja AI.
- Pendekatan low-code menggunakan Prompt Flow.

## Prasyarat

Sebelum memulakan, pastikan anda telah memenuhi keperluan berikut:

- Docker dipasang pada mesin tempatan anda.
- Akaun Azure dengan kebenaran untuk mencipta dan mengurus sumber kontena.
- Azure AI Studio dan instans Azure AI Search.
- Model embedding untuk mencipta indeks anda (boleh menggunakan embedding Azure OpenAI atau model OS dari katalog).
- Python 3.8 atau lebih terkini dipasang pada mesin tempatan anda.
- Azure Container Registry (atau mana-mana registry pilihan anda).

## Pemasangan

1. Cipta aliran baharu dalam Projek Azure AI Studio anda menggunakan fail flow.yaml.
2. Sebarkan Model Phi3 dari katalog model Azure AI anda dan sambungkan ke projek anda. [Sebarkan Phi-3 sebagai Model sebagai Perkhidmatan](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Cipta indeks vektor pada Azure AI Search menggunakan mana-mana dokumen pilihan anda. [Cipta indeks vektor pada Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Sebarkan aliran pada endpoint yang diuruskan dan gunakannya dalam fail prompt-flow-frontend.py. [Sebarkan aliran pada endpoint dalam talian](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klon repositori:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bina imej Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Tolak imej Docker ke Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Penggunaan

1. Jalankan kontena Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Akses aplikasi di pelayar anda di `http://localhost:8501`.

## Hubungi

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Artikel penuh: [RAG dengan Phi-3-Medium sebagai Model sebagai Perkhidmatan dari Katalog Model Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab ke atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.