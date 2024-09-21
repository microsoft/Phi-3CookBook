# 提到的關鍵技術包括

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - 一個基於DirectX 12構建的硬體加速機器學習的低階API。
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - 由Nvidia開發的平行計算平台和應用程式介面（API）模型，允許在圖形處理單元（GPU）上進行通用處理。
3. [ONNX](https://onnx.ai/) (開放神經網絡交換格式) - 一個設計用來表示機器學習模型的開放格式，提供不同機器學習框架之間的互操作性。
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (通用圖形更新格式) - 用於表示和更新機器學習模型的格式，特別適用於能在CPU上有效運行的小型語言模型，支持4-8位量化。

## DirectML

DirectML是一個使硬體加速機器學習成為可能的低階API。它基於DirectX 12構建，以利用GPU加速並且不依賴特定廠商，這意味著它不需要對代碼進行更改就能在不同的GPU廠商之間運行。它主要用於在GPU上進行模型訓練和推理工作。

在硬體支持方面，DirectML設計用於與各種GPU協同工作，包括AMD的集成和獨立GPU、Intel的集成GPU和NVIDIA的獨立GPU。它是Windows AI平台的一部分，並在Windows 10和11上受到支持，允許在任何Windows設備上進行模型訓練和推理。

關於DirectML的更新和機會包括支持多達150個ONNX操作符，並被ONNX runtime和WinML使用。它得到了主要的集成硬體供應商（IHVs）的支持，每個供應商實現了各種元命令。

## CUDA

CUDA，全稱為計算統一設備架構，是由Nvidia創建的平行計算平台和應用程式介面（API）模型。它允許軟體開發者使用支持CUDA的圖形處理單元（GPU）進行通用目的處理——這種方法稱為GPGPU（圖形處理單元上的通用計算）。CUDA是Nvidia GPU加速的一個關鍵推動力，廣泛應用於各種領域，包括機器學習、科學計算和視頻處理。

CUDA的硬體支持特定於Nvidia的GPU，因為它是由Nvidia開發的專有技術。每種架構支持特定版本的CUDA工具包，該工具包提供了開發者用於構建和運行CUDA應用程式所需的庫和工具。

## ONNX

ONNX（開放神經網絡交換格式）是一個設計用來表示機器學習模型的開放格式。它提供了一個可擴展的計算圖模型的定義，以及內置操作符和標準數據類型的定義。ONNX允許開發者在不同的機器學習框架之間移動模型，實現互操作性，使創建和部署AI應用程式變得更加容易。

Phi3 mini可以在包括伺服器平台、Windows、Linux和Mac桌面以及移動CPU在內的各種設備上使用ONNX Runtime在CPU和GPU上運行。我們添加的優化配置包括：

- 用於int4 DML的ONNX模型：通過AWQ量化為int4
- 用於fp16 CUDA的ONNX模型
- 用於int4 CUDA的ONNX模型：通過RTN量化為int4
- 用於int4 CPU和移動設備的ONNX模型：通過RTN量化為int4

## Llama.cpp

Llama.cpp是一個用C++編寫的開源軟體庫。它在各種大型語言模型（LLMs）上執行推理，包括Llama。與ggml庫（通用張量庫）共同開發，llama.cpp旨在比原始Python實現提供更快的推理和更低的內存使用。它支持硬體優化、量化，並提供簡單的API和示例。如果你對高效的LLM推理感興趣，llama.cpp值得一試，因為Phi3可以運行Llama.cpp。

## GGUF

GGUF（通用圖形更新格式）是一種用於表示和更新機器學習模型的格式。它特別適用於能在CPU上以4-8位量化有效運行的小型語言模型（SLMs）。GGUF對於快速原型設計以及在邊緣設備或CI/CD管道中的批量作業非常有益。

免責聲明：此翻譯由 AI 模型從原文翻譯而來，可能不夠完美。請檢查輸出並進行必要的修正。