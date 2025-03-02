## প্রম্পটফ্লো এবং AISearch সহ RAG

এই উদাহরণে, আমরা Retrieval Augmented Generation (RAG) অ্যাপ্লিকেশন বাস্তবায়ন করব যেখানে Phi3 ব্যবহৃত হবে SLM হিসেবে, AI Search ব্যবহৃত হবে vectorDB হিসেবে এবং Prompt Flow ব্যবহৃত হবে লো-কোড অর্কেস্ট্রেটর হিসেবে।

## বৈশিষ্ট্যসমূহ

- ডকার ব্যবহার করে সহজে ডিপ্লয়মেন্ট।
- AI ওয়ার্কফ্লো পরিচালনার জন্য স্কেলেবল আর্কিটেকচার।
- Prompt Flow ব্যবহার করে লো-কোড পদ্ধতি।

## পূর্বশর্ত

শুরু করার আগে, নিশ্চিত করুন যে আপনার কাছে নিম্নলিখিতগুলি রয়েছে:

- আপনার লোকাল মেশিনে Docker ইনস্টল করা আছে।
- একটি Azure অ্যাকাউন্ট, যেখানে কন্টেইনার রিসোর্স তৈরি ও পরিচালনা করার অনুমতি রয়েছে।
- একটি Azure AI Studio এবং Azure AI Search ইনস্ট্যান্স।
- আপনার ইনডেক্স তৈরি করার জন্য একটি এমবেডিং মডেল (এটি Azure OpenAI এমবেডিং বা ক্যাটালগ থেকে একটি OS মডেল হতে পারে)।
- আপনার লোকাল মেশিনে Python 3.8 বা তার পরবর্তী সংস্করণ ইনস্টল করা।
- একটি Azure Container Registry (অথবা আপনার পছন্দমতো অন্য কোনো রেজিস্ট্রি)।

## ইনস্টলেশন

1. আপনার Azure AI Studio প্রজেক্টে flow.yaml ফাইল ব্যবহার করে একটি নতুন ফ্লো তৈরি করুন।
2. Azure AI মডেল ক্যাটালগ থেকে একটি Phi3 মডেল ডিপ্লয় করুন এবং আপনার প্রজেক্টে সংযোগ তৈরি করুন। [Phi-3 মডেলকে একটি সার্ভিস হিসেবে ডিপ্লয় করুন](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. আপনার পছন্দমতো কোনো ডকুমেন্ট ব্যবহার করে Azure AI Search-এ ভেক্টর ইনডেক্স তৈরি করুন। [Azure AI Search-এ ভেক্টর ইনডেক্স তৈরি করুন](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. একটি ম্যানেজড এন্ডপয়েন্টে ফ্লো ডিপ্লয় করুন এবং এটি prompt-flow-frontend.py ফাইলের মধ্যে ব্যবহার করুন। [একটি অনলাইন এন্ডপয়েন্টে ফ্লো ডিপ্লয় করুন](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. রিপোজিটরি ক্লোন করুন:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. ডকার ইমেজ বিল্ড করুন:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. ডকার ইমেজ Azure Container Registry-তে পুশ করুন:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ব্যবহার

1. ডকার কন্টেইনার চালান:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. আপনার ব্রাউজারে অ্যাপ্লিকেশনটি অ্যাক্সেস করুন `http://localhost:8501` এ।

## যোগাযোগ

ভ্যালেন্টিনা অল্টো - [লিঙ্কডইন](https://www.linkedin.com/in/valentina-alto-6a0590148/)

সম্পূর্ণ প্রবন্ধ: [Azure Model Catalog থেকে Phi-3-Medium মডেলকে একটি সার্ভিস হিসেবে ব্যবহার করে RAG](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে দয়া করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদের সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট যেকোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই। 