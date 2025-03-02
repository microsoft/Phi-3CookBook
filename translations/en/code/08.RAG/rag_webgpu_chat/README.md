Phi-3-mini WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern
The RAG Pattern with the Phi-3 Onnx Hosted model uses the Retrieval-Augmented Generation approach, combining the capabilities of Phi-3 models with ONNX hosting for efficient AI deployment. This approach is key for fine-tuning models to handle domain-specific tasks, offering a balance of quality, cost efficiency, and the ability to process long contexts. It’s part of Azure AI’s offerings, which include a wide variety of models that are easy to locate, test, and use, meeting the customization needs of different industries. The Phi-3 models, such as Phi-3-mini, Phi-3-small, and Phi-3-medium, are accessible in the Azure AI Model Catalog and can be fine-tuned and deployed either independently or through platforms like HuggingFace and ONNX, highlighting Microsoft’s dedication to accessible and efficient AI solutions.

## What is WebGPU
WebGPU is a modern web graphics API designed to give direct and efficient access to a device's graphics processing unit (GPU) from web browsers. It is intended as the successor to WebGL and offers several notable improvements:

1. **Compatibility with Modern GPUs**: WebGPU is designed to work seamlessly with current GPU architectures, utilizing system APIs such as Vulkan, Metal, and Direct3D 12.
2. **Improved Performance**: It supports general-purpose GPU computations and faster operations, making it suitable for both rendering graphics and performing machine learning tasks.
3. **Advanced Features**: WebGPU provides access to more sophisticated GPU capabilities, allowing for more complex and dynamic graphics and computational tasks.
4. **Reduced JavaScript Workload**: By delegating more tasks to the GPU, WebGPU significantly reduces the workload on JavaScript, resulting in better performance and smoother experiences.

WebGPU is currently supported in browsers like Google Chrome, with ongoing efforts to extend support to other platforms.

### 03.WebGPU
Required Environment:

**Supported browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Enable WebGPU:

- In Chrome/Microsoft Edge 

Enable the `chrome://flags/#enable-unsafe-webgpu` flag.

#### Open Your Browser:
Launch Google Chrome or Microsoft Edge.

#### Access the Flags Page:
In the address bar, type `chrome://flags` and press Enter.

#### Search for the Flag:
In the search box at the top of the page, type 'enable-unsafe-webgpu.'

#### Enable the Flag:
Find the #enable-unsafe-webgpu flag in the list of results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:

After enabling the flag, you’ll need to restart your browser for the changes to take effect. Click the Relaunch button that appears at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Here are the steps to configure a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click on the Start menu and select Settings.
- **System Settings:** Go to System and then Display.
- **Graphics Settings:** Scroll down and click on Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and then click Save.
This will ensure that Microsoft Edge uses your high-performance GPU for better performance. 
- **Restart** your machine for these settings to take effect. 

### Open Your Codespace:
Navigate to your repository on GitHub.
Click on the Code button and select Open with Codespaces.

If you don’t have a Codespace yet, you can create one by clicking New codespace.

**Note** Installing Node Environment in your codespace
Running an npm demo from a GitHub Codespace is a great way to test and develop your project. Here’s a step-by-step guide to help you get started:

### Set Up Your Environment:
Once your Codespace is open, ensure you have Node.js and npm installed. You can check this by running:
```
node -v
```
```
npm -v
```

If they are not installed, you can install them using:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigate to Your Project Directory:
Use the terminal to navigate to the directory where your npm project is located:
```
cd path/to/your/project
```

### Install Dependencies:
Run the following command to install all the necessary dependencies listed in your package.json file:

```
npm install
```

### Run the Demo:
Once the dependencies are installed, you can run your demo script. This is usually specified in the scripts section of your package.json. For example, if your demo script is named start, you can run:

```
npm run build
```
```
npm run dev
```

### Access the Demo:
If your demo involves a web server, Codespaces will provide a URL to access it. Look for a notification or check the Ports tab to find the URL.

**Note:** The model needs to be cached in the browser, so it may take some time to load. 

### RAG Demo
Upload the markdown file `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Select Your File:
Click on the button that says “Choose File” to pick the document you want to upload.

### Upload the Document:
After selecting your file, click the “Upload” button to load your document for RAG (Retrieval-Augmented Generation).

### Start Your Chat:
Once the document is uploaded, you can start a chat session using RAG based on the content of your document.

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.