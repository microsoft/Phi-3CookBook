### Example Scenario

Imagine you have an image (`demo.png`) and you want to generate Python code that processes this image and saves a new version of it (`phi-3-vision.jpg`). 

The code above automates this process by:

1. Setting up the environment and necessary configurations.
2. Creating a prompt that instructs the model to generate the required Python code.
3. Sending the prompt to the model and collecting the generated code.
4. Extracting and running the generated code.
5. Displaying the original and processed images.

This approach leverages the power of AI to automate image processing tasks, making it easier and faster to achieve your goals. 

[Sample Code Solution](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Let's break down what the entire code does step by step:

1. **Install Required Package**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    This command installs the `langchain_nvidia_ai_endpoints` package, ensuring it's the latest version.

2. **Import Necessary Modules**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    These imports bring in the necessary modules for interacting with the NVIDIA AI endpoints, handling passwords securely, interacting with the operating system, and encoding/decoding data in base64 format.

3. **Set Up API Key**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    This code checks if the `NVIDIA_API_KEY` environment variable is set. If not, it prompts the user to enter their API key securely.

4. **Define Model and Image Path**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    This sets the model to be used, creates an instance of `ChatNVIDIA` with the specified model, and defines the path to the image file.

5. **Create Text Prompt**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    This defines a text prompt instructing the model to generate Python code for processing an image.

6. **Encode Image in Base64**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    This code reads the image file, encodes it in base64, and creates an HTML image tag with the encoded data.

7. **Combine Text and Image into Prompt**:
    ```python
    prompt = f"{text} {image}"
    ```
    This combines the text prompt and the HTML image tag into a single string.

8. **Generate Code Using ChatNVIDIA**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    This code sends the prompt to the `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` string.

9. **Extract Python Code from Generated Content**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    This extracts the actual Python code from the generated content by removing the markdown formatting.

10. **Run the Generated Code**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    This runs the extracted Python code as a subprocess and captures its output.

11. **Display Images**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    These lines display the images using the `IPython.display` module.

