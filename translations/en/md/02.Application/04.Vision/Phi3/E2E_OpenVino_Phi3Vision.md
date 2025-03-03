This demo demonstrates how to use a pretrained model to generate Python code based on an image and a text prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Here's a step-by-step explanation:

1. **Imports and Setup**:
   - The required libraries and modules are imported, including `requests`, `PIL` for image processing, and `transformers` for managing the model and processing.

2. **Loading and Displaying the Image**:
   - An image file (`demo.png`) is opened using the `PIL` library and displayed.

3. **Defining the Prompt**:
   - A message is crafted that incorporates the image and requests the generation of Python code to process the image and save it using `plt` (matplotlib).

4. **Loading the Processor**:
   - The `AutoProcessor` is loaded from a pretrained model located in the `out_dir` directory. This processor will manage the text and image inputs.

5. **Creating the Prompt**:
   - The `apply_chat_template` method is employed to format the message into a prompt that the model can use.

6. **Processing the Inputs**:
   - The prompt and image are converted into tensors that the model can interpret.

7. **Setting Generation Arguments**:
   - Parameters for the model's code generation are defined, including the maximum number of new tokens to generate and whether to use sampling for the output.

8. **Generating the Code**:
   - The model generates Python code based on the provided inputs and generation parameters. The `TextStreamer` is used to process the output, skipping the prompt and special tokens.

9. **Output**:
   - The generated Python code is printed, which includes the necessary steps to process the image and save it as outlined in the prompt.

This demo showcases how to utilize a pretrained model with OpenVino to dynamically generate code based on user inputs and images.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.