# 提到的關鍵技術包括

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - 一個基於 DirectX 12 架構的低階 API，用於硬體加速的機器學習。
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - 由 Nvidia 開發的平行運算平台和應用程式介面（API）模型，使圖形處理單元（GPU）能夠進行通用運算。
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - 一個開放格式，旨在表示機器學習模型，提供不同 ML 框架之間的互操作性。
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - 用於表示和更新機器學習模型的格式，特別適用於能在 CPU 上有效運行的小型語言模型，支援 4-8 位元量化。

## DirectML

DirectML 是一個低階 API，能夠實現硬體加速的機器學習。它基於 DirectX 12 構建，以利用 GPU 加速，且不依賴於特定廠商，意味著不需要修改代碼即可在不同的 GPU 廠商之間運行。它主要用於 GPU 上的模型訓練和推理工作負載。

在硬體支援方面，DirectML 設計為支援廣泛的 GPU，包括 AMD 的集成和獨立 GPU、Intel 的集成 GPU 和 NVIDIA 的獨立 GPU。它是 Windows AI 平台的一部分，支援 Windows 10 和 11，允許在任何 Windows 設備上進行模型訓練和推理。

有關 DirectML 的更新和機會，包括支援多達 150 個 ONNX 操作符，並被 ONNX runtime 和 WinML 使用。它得到了主要集成硬體廠商（IHVs）的支持，每個廠商都實現了各種元命令。

## CUDA

CUDA，全名為 Compute Unified Device Architecture，是由 Nvidia 創建的平行運算平台和應用程式介面（API）模型。它允許軟體開發人員使用 CUDA 支援的圖形處理單元（GPU）進行通用運算——這種方法稱為 GPGPU（圖形處理單元上的通用運算）。CUDA 是 Nvidia GPU 加速的重要支持技術，廣泛應用於機器學習、科學計算和視頻處理等領域。

CUDA 的硬體支援特定於 Nvidia 的 GPU，因為它是 Nvidia 開發的專有技術。每個架構支援特定版本的 CUDA 工具包，該工具包提供了必要的庫和工具，供開發人員構建和運行 CUDA 應用程式。

## ONNX

ONNX（Open Neural Network Exchange）是一個開放格式，旨在表示機器學習模型。它提供了一個可擴展的計算圖模型定義，以及內建操作符和標準數據類型的定義。ONNX 允許開發人員在不同的 ML 框架之間移動模型，實現互操作性，並使創建和部署 AI 應用程式變得更加容易。

Phi3 mini 可以在包括伺服器平台、Windows、Linux 和 Mac 桌面以及移動 CPU 在內的設備上，使用 ONNX Runtime 在 CPU 和 GPU 上運行。
我們添加的優化配置包括：

- 用於 int4 DML 的 ONNX 模型：通過 AWQ 量化為 int4
- 用於 fp16 CUDA 的 ONNX 模型
- 用於 int4 CUDA 的 ONNX 模型：通過 RTN 量化為 int4
- 用於 int4 CPU 和移動設備的 ONNX 模型：通過 RTN 量化為 int4

## Llama.cpp

Llama.cpp 是一個用 C++ 編寫的開源軟體庫。它對各種大型語言模型（LLMs）進行推理，包括 Llama。與 ggml 庫（通用張量庫）一起開發，llama.cpp 旨在提供比原始 Python 實現更快的推理速度和更低的內存使用。它支援硬體優化、量化，並提供簡單的 API 和範例。如果你對高效的 LLM 推理感興趣，llama.cpp 值得探索，因為 Phi3 可以運行 Llama.cpp。

## GGUF

GGUF（Generic Graph Update Format）是一種用於表示和更新機器學習模型的格式。它對於能在 CPU 上有效運行的較小型語言模型（SLMs）特別有用，支援 4-8 位元量化。GGUF 有助於快速原型設計，並在邊緣設備或 CI/CD 管道等批處理作業中運行模型。

**免責聲明**：
本文檔是使用基於機器的AI翻譯服務進行翻譯的。儘管我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件作為權威來源。對於關鍵信息，建議使用專業的人力翻譯。我們不對因使用此翻譯而引起的任何誤解或誤讀承擔責任。