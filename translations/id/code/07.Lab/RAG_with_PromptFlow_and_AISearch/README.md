## RAG dengan PromptFlow dan AISearch

Dalam contoh ini, kita akan mengimplementasikan aplikasi Retrieval Augmented Generation (RAG) dengan memanfaatkan Phi3 sebagai SLM, AI Search sebagai vectorDB, dan Prompt Flow sebagai orkestrator low-code.

## Fitur

- Penerapan mudah menggunakan Docker.
- Arsitektur yang dapat diskalakan untuk menangani alur kerja AI.
- Pendekatan low-code menggunakan Prompt Flow.

## Prasyarat

Sebelum memulai, pastikan Anda telah memenuhi persyaratan berikut:

- Docker terinstal di komputer lokal Anda.
- Akun Azure dengan izin untuk membuat dan mengelola sumber daya kontainer.
- Instans Azure AI Studio dan Azure AI Search.
- Model embedding untuk membuat indeks Anda (bisa berupa Azure OpenAI embedding atau model OS dari katalog).
- Python 3.8 atau versi lebih baru terinstal di komputer lokal Anda.
- Azure Container Registry (atau registry pilihan Anda).

## Instalasi

1. Buat flow baru di Proyek Azure AI Studio Anda menggunakan file flow.yaml.
2. Deploy Model Phi3 dari katalog model Azure AI Anda dan buat koneksi ke proyek Anda. [Deploy Phi-3 sebagai Model sebagai Layanan](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Buat indeks vektor di Azure AI Search menggunakan dokumen pilihan Anda. [Buat indeks vektor di Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Deploy flow pada endpoint yang dikelola dan gunakan di file prompt-flow-frontend.py. [Deploy flow pada endpoint online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone repositori:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bangun image Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Dorong image Docker ke Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Penggunaan

1. Jalankan kontainer Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Akses aplikasi di browser Anda di `http://localhost:8501`.

## Kontak

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Artikel Lengkap: [RAG dengan Phi-3-Medium sebagai Model sebagai Layanan dari Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berusaha untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan layanan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.