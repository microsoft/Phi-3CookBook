# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern

The RAG Pattern with Phi-3.5 Onnx Hosted model leverages the Retrieval-Augmented Generation approach, combining the power of Phi-3.5 models with ONNX hosting for efficient AI deployments. This pattern is instrumental in fine-tuning models for domain-specific tasks, offering a blend of quality, cost-effectiveness, and long-context understanding. It’s part of Azure AI’s suite, providing a wide selection of models that are easy to find, try, and use, catering to the customization needs of various industries. 

## What is WebGPU 
WebGPU is a modern web graphics API designed to provide efficient access to a device's graphics processing unit (GPU) directly from web browsers. It is intended to be the successor to WebGL, offering several key improvements:

1. **Compatibility with Modern GPUs**: WebGPU is built to work seamlessly with contemporary GPU architectures, leveraging system APIs like Vulkan, Metal, and Direct3D 12.
2. **Enhanced Performance**: It supports general-purpose GPU computations and faster operations, making it suitable for both graphics rendering and machine learning tasks.
3. **Advanced Features**: WebGPU provides access to more advanced GPU capabilities, enabling more complex and dynamic graphics and computational workloads.
4. **Reduced JavaScript Workload**: By offloading more tasks to the GPU, WebGPU significantly reduces the workload on JavaScript, leading to better performance and smoother experiences.

WebGPU is currently supported in browsers like Google Chrome, with ongoing work to expand support to other platforms.

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
Find the #enable-unsafe-webgpu flag in the list of results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:

After enabling the flag, you’ll need to restart your browser for the changes to take effect. Click the Relaunch button that appears at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Here are the steps to set up a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click on the Start menu and select Settings.
- **System Settings:** Go to System and then Display.
- **Graphics Settings:** Scroll down and click on Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and then click Save.
This will ensure that Microsoft Edge uses your high-performance GPU for better performance. 
- **Restart** your machine for these setting to take effect 

### Samples : Please [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)