# **在 AI PC 中使用 Phi-3 进行推理**

随着生成式人工智能的发展以及边缘设备硬件性能的提升，越来越多的生成式AI模型现在可以集成到用户的自带设备（BYOD）中。AI PC就是其中之一。从2024年开始，英特尔、AMD和高通与PC制造商合作推出了AI PC，通过硬件改造来促进本地化生成式AI模型的部署。在这里，我们将重点关注英特尔AI PC，并探讨如何在英特尔AI PC上部署Phi-3。

### **NPU是什么?**

NPU（神经处理单元）是专为加速神经网络运算和AI任务而特别设计的专用处理器或大型SoC（片上系统）上的处理单元。与通用CPU和GPU不同，NPU针对数据驱动的并行计算进行了优化，使其在处理大量多媒体数据（如视频和图像）以及神经网络数据方面具有高效性能。它们在处理AI相关任务方面特别擅长，例如语音识别、视频通话中的背景模糊以及物体检测等照片或视频编辑过程。

## **NPU vs GPU** 
尽管许多AI和机器学习工作负载都在GPU上运行，但GPU和NPU之间存在着显著区别。GPU以其并行计算能力而闻名，但并非所有GPU在处理图形之外都同样高效。而NPU则专为神经网络运算中的复杂计算而设计，使其在AI任务中具有很高的效率。

总之，NPU是加速AI计算的数学天才，它们在新兴的AI PC时代中发挥着关键作用！

***本示例基于英特尔最新的英特尔酷睿超级处理器。***

## **1. 使用 NPU 运行 Phi-3 模型**

从Intel® Core™超级处理器（以前称为Meteor Lake）开始，Intel® NPU 设备是与英特尔客户端 CPU 集成的 AI 推理加速器。它能够节能高效地执行人工神经网络任务。

![Latency](../../../../imgs/03/AIPC/aipcphitokenlatency.png)

![Latency770](../../../../imgs/03/AIPC/aipcphitokenlatency770.png)

**英特尔 NPU 加速库**

英特尔NPU加速库（Intel NPU Acceleration Library） [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) 是一个Python库，旨在通过利用英特尔神经处理单元（NPU）在兼容硬件上执行高速计算来提高应用程序的效率。

以下是在英特尔酷睿超级处理器驱动的AI PC上运行的Phi-3-mini示例。

![DemoPhiIntelAIPC](../../../../imgs/03/AIPC/aipcphi3-mini.gif)

使用pip工具安装Python库

```bash

   pip install intel-npu-acceleration-library

```

***注意*** 该项目仍在开发中，但参考模型已经非常完整。


### **使用英特尔 NPU 加速库运行 Phi-3**

使用英特尔 NPU 加速，该库不会影响传统的编码过程。您只需要使用该库对原始 Phi-3 模型进行量化，例如 FP16、INT8、INT4 等。


```python

from transformers import AutoTokenizer, pipeline,TextStreamer
import intel_npu_acceleration_library as npu_lib
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

model = npu_lib.NPUModelForCausalLM.from_pretrained(
                                    model_id,
                                    torch_dtype="auto",
                                    dtype=npu_lib.int4,
                                    trust_remote_code=True
                                )

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)

```
量化成功后，继续执行调用 NPU 运行 Phi-3 模型的操作。


```python

generation_args = {
            "max_new_tokens": 1024,
            "return_full_text": False,
            "temperature": 0.3,
            "do_sample": False,
            "streamer": text_streamer,
        }

pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)


```

在执行代码时，我们可以通过任务管理器查看 NPU 的运行状态。

![NPU](../../../../imgs/03/AIPC/aipc_NPU.png)


***示例*** : [AIPC_NPU_DEMO.ipynb](../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)


## **2. 使用 DirectML + ONNX Runtime 运行 Phi-3 模型**

### **什么是 DirectML?**

[DirectML](https://github.com/microsoft/DirectML) 是一个高性能、硬件加速的基于 DirectX 12 的机器学习库。DirectML 提供了 GPU 加速的常见机器学习任务，支持广泛的硬件和驱动程序，包括来自 AMD、英特尔、NVIDIA 和高通等厂商的所有 DirectX 12 兼容的 GPU。

当作为独立应用时，DirectML API 是一个低级别的 DirectX 12 库，适用于高性能、低延迟的应用程序，例如框架、游戏和其他实时应用程序。DirectML 与 Direct3D 12 的无缝互操作性以及其低开销和硬件兼容性使其成为加速机器学习的理想选择，既需要高性能，又需要跨硬件的结果可靠性和可预测性。

***注意*** : 最新的 DirectML 已支持 NPU(https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### DirectML 和 CUDA 的能力和性能:

**DirectML** 是由微软开发的一个机器学习库。它旨在加速 Windows 设备上的机器学习工作负载，包括台式机、笔记本电脑和边缘设备。
- 基于DX12: DirectML 建立在 DirectX 12（DX12）之上，为 GPU 提供了广泛的硬件支持，包括 NVIDIA 和 AMD。
- 更广泛的支持: 由于它利用了 DX12，DirectML 可以与任何支持 DX12 的 GPU 一起工作，甚至是集成 GPU。
- 图像处理: DirectML 使用神经网络处理图像和其他数据，使其适用于图像识别、物体检测等任务。
- 设置简单: 设置 DirectML 非常简单，不需要来自 GPU 制造商的特定 SDK 或库。
- 性能: 在某些情况下，DirectML 的性能表现良好，对于某些工作负载，它的速度甚至可能比 CUDA 更快。
- 局限性: 然而，也有一些情况下 DirectML 可能会较慢，特别是对于大批量的 float16。

**CUDA** 是 NVIDIA 的并行计算平台和编程模型。它允许开发者利用 NVIDIA GPU 的力量进行通用计算，包括机器学习和科学模拟。
- NVIDIA 特定: CUDA 与 NVIDIA GPU 紧密集成，专为它们设计。
- 高度优化: 它为 GPU 加速任务提供了出色的性能，特别是在使用 NVIDIA GPU 时。
- 广泛使用: 许多机器学习框架和库（如 TensorFlow 和 PyTorch）都支持 CUDA。
- 定制: 开发人员可以为特定任务微调 CUDA 设置，从而获得最佳性能。
- 局限性: 然而，CUDA 对 NVIDIA 硬件的依赖可能会在需要跨不同 GPU 的更广泛兼容性时产生限制。

### 在 DirectML 和 CUDA 中选择:
在 DirectML 和 CUDA 之间的选择取决于您的具体用例、硬件可用性和偏好。如果您寻求更广泛的兼容性和简便的设置，DirectML 可能是一个不错的选择。然而，如果您拥有 NVIDIA GPU 并需要高度优化的性能，CUDA 仍然是一个有力的竞争者。总之，DirectML 和 CUDA 都有各自的优缺点，因此在做决策时要考虑您的需求和可用硬件。

### **ONNX Runtime 的生成式AI**

在 AI 时代，AI 模型的可移植性非常重要。ONNX Runtime 可以轻松地将训练好的模型部署到不同的设备上。开发者不需要关注推理框架，只需使用统一的 API 完成模型推理。在生成式 AI 时代，ONNX Runtime 也进行了代码优化（https://onnxruntime.ai/docs/genai/）。通过优化后的 ONNX Runtime，可以在不同的终端上推理量化的生成 AI 模型。在 ONNX Runtime 的生成 AI 中，您可以通过 Python、C#、C/C++ 调用 AI 模型的推理 API。当然，要在 iPhone 上部署，可以利用 C++ 的 ONNX Runtime 生成式 AI 推理 API。

[示例代码](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***利用ONNX Runtime库编译生成式AI***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**安装库**


```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

以下是运行结果：

![DML](../../../../imgs/03/AIPC/aipc_DML.png)

***示例*** : [AIPC_DirectML_DEMO.ipynb](../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. 使用 Intel OpenVino 运行 Phi-3 模型**

### **什么是OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) 是一个用于优化和部署深度学习模型的开源工具包。它为视觉、音频和语言模型提供了加速深度学习性能，支持 TensorFlow、PyTorch 等流行框架。您可以开始使用 OpenVINO。OpenVINO 也可以与 CPU 和 GPU 结合使用，运行 Phi3 模型。

***注意***: 目前，OpenVINO 还不支持 NPU。


### **安装 OpenVINO 库**


```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **使用 OpenVINO 运行 Phi-3**

与 NPU 类似，OpenVINO 通过运行量化模型来完成生成 AI 模型的调用。我们首先需要对 Phi-3 模型进行量化，并通过 optimum-cli 在命令行上完成模型量化。

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

转换后的格式如下图所示：

![openvino_convert](../../../../imgs/03/AIPC/aipc_OpenVINO_convert.png)


通过 OVModelForCausalLM 加载模型路径（model_dir）、相关配置（ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}）以及硬件加速设备（GPU.0）。

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

在执行代码时，我们可以通过任务管理器查看 GPU 的运行状态。

![openvino_gpu](../../../../imgs/03/AIPC/aipc_OpenVINO_GPU.png)

***示例*** : [AIPC_OpenVino_Demo.ipynb](../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***注意*** : 以上三种方法各有优缺点，但建议在 AI PC 推理中使用 NPU 加速。















