## RAG với PromptFlow và AISearch

Trong ví dụ này, chúng ta sẽ triển khai một ứng dụng Retrieval Augmented Generation (RAG) sử dụng Phi3 làm SLM, AI Search làm vectorDB và Prompt Flow như một trình điều phối low-code.

## Tính năng

- Triển khai dễ dàng với Docker.
- Kiến trúc có khả năng mở rộng để xử lý các luồng công việc AI.
- Tiếp cận low-code với Prompt Flow.

## Yêu cầu trước

Trước khi bắt đầu, hãy đảm bảo bạn đã đáp ứng các yêu cầu sau:

- Đã cài đặt Docker trên máy tính của bạn.
- Tài khoản Azure có quyền tạo và quản lý tài nguyên container.
- Có Azure AI Studio và các phiên bản Azure AI Search.
- Một mô hình embedding để tạo index của bạn (có thể là Azure OpenAI embedding hoặc một mô hình mã nguồn mở từ danh mục).
- Đã cài đặt Python 3.8 hoặc phiên bản mới hơn trên máy tính của bạn.
- Một Azure Container Registry (hoặc bất kỳ registry nào bạn chọn).

## Cài đặt

1. Tạo một flow mới trên Dự án Azure AI Studio của bạn bằng tệp flow.yaml.
2. Triển khai một Mô hình Phi3 từ danh mục mô hình Azure AI và tạo kết nối với dự án của bạn. [Triển khai Phi-3 như một Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Tạo vector index trên Azure AI Search bằng bất kỳ tài liệu nào bạn chọn. [Tạo vector index trên Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Triển khai flow trên một endpoint được quản lý và sử dụng nó trong tệp prompt-flow-frontend.py. [Triển khai một flow trên endpoint trực tuyến](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Build Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Đẩy Docker image lên Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Sử dụng

1. Chạy container Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Truy cập ứng dụng trong trình duyệt tại `http://localhost:8501`.

## Liên hệ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Bài viết đầy đủ: [RAG với Phi-3-Medium như một Model as a Service từ Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.