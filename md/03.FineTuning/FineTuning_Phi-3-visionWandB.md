# Phi-3-Vision-128K-Instruct Project Overview

## The Model

The Phi-3-Vision-128K-Instruct, a lightweight, state-of-the-art multimodal model, is at the core of this project. It is part of the Phi-3 model family and supports a context length of up to 128,000 tokens. The model was trained on a diverse dataset that includes synthetic data and carefully filtered publicly available websites, emphasizing high-quality, reasoning-intensive content. The training process included supervised fine-tuning and direct preference optimization to ensure precise adherence to instructions, as well as robust safety measures.

## Creating sample data is crucial for several reasons:

1. **Testing**: Sample data allows you to test your application under various scenarios without affecting real data. This is especially important in the development and staging phases.

2. **Performance Tuning**: With sample data that mimics the scale and complexity of real data, you can identify performance bottlenecks and optimize your application accordingly.

3. **Prototyping**: Sample data can be used to create prototypes and mockups, which can help in understanding user requirements and getting feedback.

4. **Data Analysis**: In data science, sample data is often used for exploratory data analysis, model training, and algorithm testing.

5. **Security**: Using sample data in development and testing environments can help prevent accidental data leaks of sensitive real data.

6. **Learning**: If you're learning a new technology or tool, working with sample data can provide a practical way to apply what you've learned.

Remember, the quality of your sample data can significantly impact these activities. It should be as close as possible to the real data in terms of structure and variability.

### Sample Data Creation
[Generate DataSet Script](./CreatingSampleData.md)

## Dataset

A good example of sample dataset is [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (available on Huggingface). 
The Sample data set  of Burberry products along with metadata on the products category, price, and title with a total of 3,040 rows, each representing a unique product. This dataset lets us test the model's ability to understand and interpret visual data, generating descriptive text that capture intricate visual details and brand-specific characteristics.

**Note:** You can use any dataset which includes images.

## Complex Reasoning

The model needs to reason about prices and naming given only the image. This requires the model to not only recognize visual features but also understand their implications in terms of product value and branding. By synthesizing accurate textual descriptions from images, the project highlights the potential of integrating visual data to enhance the performance and versatility of models in real-world applications.

## Phi-3 Vision Architecture

The model architecture is a multimodal version of a Phi-3. It processes both text and image data, integrating these inputs into a unified sequence for comprehensive understanding and generation tasks. The model uses separate embedding layers for text and images. Text tokens are converted into dense vectors, while images are processed through a CLIP vision model to extract feature embeddings. These image embeddings are then projected to match the text embeddings' dimensions, ensuring they can be seamlessly integrated.

## Integration of Text and Image Embeddings

Special tokens within the text sequence indicate where the image embeddings should be inserted. During processing, these special tokens are replaced with the corresponding image embeddings, allowing the model to handle text and images as a single sequence. The prompt for our dataset is formatted using the special <|image|> token as follows:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Sample Code
- [Phi-3-Vision Training Script](../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)
