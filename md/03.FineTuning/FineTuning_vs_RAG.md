## Finetuning vs RAG

## Retrieval Augmented Generation

RAG is data retrieval + text generation. The structured data and unstructured data of the enterprise are stored in the vector database. When searching for relevant content, the relevant summary and content are found to form a context, and the text completion capability of LLM/SLM is combined to generate content.

## RAG Process
![FinetuningvsRAG](../../imgs/03/intro/rag.png)

## Fine-tuning
Fine-tuning is based on improvement of a certain model. It does not need to start with the model algorithm, but data needs to be continuously accumulated. If you want more precise terminology and language expression in industry applications, fine-tuning is your better choice. But if your data changes frequently, fine-tuning can become complicated.

## How to choose
If our answer requires the introduction of external data, RAG is the best choice

If you need to output stable and precise industry knowledge, fine-tuning will be a good choice. RAG prioritizes pulling relevant content but might not always nail the specialized nuances.

Fine-tuning requires a high-quality data set, and if it is just a small range of data, it will not make much difference. RAG is more flexible
Fine-tuning is a black box, a metaphysics, and it is difficult to understand the internal mechanism. But RAG can make it easier to find the source of the data, thereby effectively adjusting hallucinations or content errors and providing better transparency.

