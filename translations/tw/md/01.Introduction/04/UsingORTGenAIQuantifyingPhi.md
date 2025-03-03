# **使用 Generative AI extensions for onnxruntime 量化 Phi 系列模型**

## **什麼是 Generative AI extensions for onnxruntime**

此擴展幫助您使用 ONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）運行生成式 AI。它為 ONNX 模型提供生成式 AI 的完整循環，包括使用 ONNX Runtime 進行推理、處理 logits、搜索與採樣以及管理 KV 快取。開發者可以調用高階的 generate() 方法，或者在循環中逐次運行模型生成一個 token，並根據需要在循環內更新生成參數。它支持貪婪/束搜索以及 TopP、TopK 採樣來生成 token 序列，還內建 logits 處理功能，如重複懲罰。此外，您還可以輕鬆添加自定義評分。

在應用層級，您可以使用 Generative AI extensions for onnxruntime 建構基於 C++/ C# / Python 的應用程式。在模型層級，您可以用它來合併微調模型並執行相關的量化部署工作。

## **使用 Generative AI extensions for onnxruntime 量化 Phi-3.5**

### **支持的模型**

Generative AI extensions for onnxruntime 支持對 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。

### **Generative AI extensions for onnxruntime 的模型構建工具**

模型構建工具極大地加速了創建經過優化和量化的 ONNX 模型的過程，這些模型可以使用 ONNX Runtime 的 generate() API 運行。

通過模型構建工具，您可以將模型量化為 INT4、INT8、FP16、FP32，並結合不同的硬體加速方法，如 CPU、CUDA、DirectML、Mobile 等。

要使用模型構建工具，您需要安裝：

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝完成後，您可以從終端運行模型構建工具腳本，執行模型格式和量化轉換。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

瞭解相關參數：

1. **model_name** 這是 Hugging Face 上的模型名稱，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等，也可以是您存儲模型的路徑。

2. **path_to_output_folder** 量化轉換後的保存路徑。

3. **execution_provider** 不同的硬體加速支持，例如 cpu、cuda、DirectML。

4. **cache_dir_to_save_hf_files** 我們從 Hugging Face 下載模型並將其緩存到本地的路徑。

***注意：***

## **如何使用模型構建工具量化 Phi-3.5**

模型構建工具現在支持對 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化。

### **Phi-3.5-Instruct**

**基於 CPU 加速的 INT 4 量化轉換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**基於 CUDA 加速的 INT 4 量化轉換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在終端中設置環境：

```bash

mkdir models

cd models 

```

2. 在 models 資料夾中下載 microsoft/Phi-3.5-vision-instruct  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請將以下檔案下載到您的 Phi-3.5-vision-instruct 資料夾：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 將以下檔案下載到 models 資料夾：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 在終端中執行：

   使用 FP32 格式轉換 ONNX 支持：

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. 模型構建工具目前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的轉換，但尚不支持 Phi-3.5-MoE。

2. 要使用 ONNX 的量化模型，您可以通過 Generative AI extensions for onnxruntime SDK 使用。

3. 我們需要考慮更負責任的 AI，因此在模型量化轉換後，建議進行更有效的結果測試。

4. 通過量化 CPU INT4 模型，我們可以將其部署到邊緣設備，這具有更好的應用場景，因此我們已針對 Phi-3.5-Instruct 完成了 INT 4 的量化。

## **資源**

1. 瞭解更多關於 Generative AI extensions for onnxruntime 的信息：  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo：  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為權威來源。如涉及關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或誤讀概不負責。