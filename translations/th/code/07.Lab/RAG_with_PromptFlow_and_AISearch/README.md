## RAG กับ PromptFlow และ AISearch

ในตัวอย่างนี้ เราจะสร้างแอปพลิเคชัน Retrieval Augmented Generation (RAG) โดยใช้ Phi3 เป็น SLM, AI Search เป็น vectorDB และ Prompt Flow เป็นเครื่องมือจัดการแบบ low-code

## คุณสมบัติ

- การติดตั้งที่ง่ายด้วย Docker
- สถาปัตยกรรมที่สามารถขยายได้เพื่อรองรับการทำงานของ AI
- วิธีการแบบ low-code โดยใช้ Prompt Flow

## ข้อกำหนดเบื้องต้น

ก่อนเริ่มต้น ให้ตรวจสอบว่าคุณมีสิ่งต่อไปนี้พร้อมแล้ว:

- ติดตั้ง Docker บนเครื่องของคุณ
- บัญชี Azure ที่มีสิทธิ์ในการสร้างและจัดการทรัพยากรคอนเทนเนอร์
- Azure AI Studio และ Azure AI Search ที่พร้อมใช้งาน
- โมเดล embedding สำหรับสร้างดัชนีของคุณ (สามารถใช้ Azure OpenAI embedding หรือ OS model จากแคตตาล็อกได้)
- Python 3.8 หรือใหม่กว่าที่ติดตั้งบนเครื่องของคุณ
- Azure Container Registry (หรือ registry ใดก็ได้ที่คุณเลือก)

## การติดตั้ง

1. สร้าง flow ใหม่ในโครงการ Azure AI Studio ของคุณโดยใช้ไฟล์ flow.yaml
2. ติดตั้ง Phi3 Model จากแคตตาล็อกโมเดล Azure AI และสร้างการเชื่อมต่อกับโครงการของคุณ [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. สร้าง vector index บน Azure AI Search โดยใช้เอกสารใดก็ได้ที่คุณเลือก [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. ติดตั้ง flow บน endpoint ที่จัดการไว้ และใช้มันในไฟล์ prompt-flow-frontend.py [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. โคลน repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. สร้าง Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. อัปโหลด Docker image ไปยัง Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## การใช้งาน

1. รัน Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. เข้าถึงแอปพลิเคชันผ่านเบราว์เซอร์ที่ `http://localhost:8501`

## ติดต่อ

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

บทความฉบับเต็ม: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดอันเกิดจากการใช้การแปลนี้