# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo showcasing WebGPU and the RAG Pattern

The RAG Pattern with the Phi-3.5 Onnx Hosted model utilizes the Retrieval-Augmented Generation method, combining the capabilities of Phi-3.5 models with ONNX hosting for efficient AI deployments. This approach is key to fine-tuning models for specific domains, offering a balance of quality, cost efficiency, and the ability to handle long contexts. It is part of Azure AI’s suite, which provides a broad range of models that are easy to discover, test, and implement, catering to the customization needs of various industries.

## What is WebGPU
WebGPU is a modern web graphics API designed to give direct, efficient access to a device’s graphics processing unit (GPU) through web browsers. It is intended to succeed WebGL, offering several significant advancements:

1. **Compatibility with Modern GPUs**: WebGPU is designed to work effortlessly with current GPU architectures, utilizing system APIs like Vulkan, Metal, and Direct3D 12.
2. **Improved Performance**: It supports general-purpose GPU computations and faster operations, making it ideal for both graphics rendering and machine learning workloads.
3. **Advanced Features**: WebGPU enables access to more sophisticated GPU capabilities, allowing for more complex and dynamic graphics and computational tasks.
4. **Reduced JavaScript Workload**: By offloading more tasks to the GPU, WebGPU significantly decreases the workload on JavaScript, resulting in better performance and smoother user experiences.

WebGPU is currently supported in browsers like Google Chrome, with efforts underway to expand support to additional platforms.

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
In the search box at the top of the page, type 'enable-unsafe-webgpu'

#### Enable the Flag:
Locate the #enable-unsafe-webgpu flag in the search results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:

Once the flag is enabled, you’ll need to restart your browser for the changes to take effect. Click the Relaunch button at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, type about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Follow these steps to configure a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click the Start menu and choose Settings.
- **System Settings:** Navigate to System and then Display.
- **Graphics Settings:** Scroll down and click Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.
- **Select Edge:** Go to the Edge installation folder (typically `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and then click Save.
This ensures that Microsoft Edge uses your high-performance GPU for optimal performance.
- **Restart** your computer for these settings to take effect.

### Samples: Please [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.