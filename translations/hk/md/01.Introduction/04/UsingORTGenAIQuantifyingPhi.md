# **使用 Generative AI extensions for onnxruntime 量化 Phi 家族模型**

## **什麼是 Generative AI extensions for onnxruntime**

這個擴展幫助你使用 ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) 執行生成式 AI。它為 ONNX 模型提供生成式 AI 的完整流程，包括使用 ONNX Runtime 進行推理、處理 logits、搜尋和採樣，以及 KV 緩存管理。開發者可以調用高層級的 `generate()` 方法，或在迴圈中逐步執行模型，每次生成一個 token，並且可以選擇性地在迴圈中更新生成參數。它支持貪婪搜尋/束搜尋以及 TopP、TopK 採樣來生成 token 序列，還內建了例如重複懲罰的 logits 處理功能。你也可以輕鬆地添加自定義評分。

在應用層面，你可以使用 Generative AI extensions for onnxruntime 用 C++ / C# / Python 構建應用程序。在模型層面，你可以用它來合併微調模型以及進行相關的量化部署工作。

## **使用 Generative AI extensions for onnxruntime 量化 Phi-3.5**

### **支持的模型**

Generative AI extensions for onnxruntime 支持對 Microsoft Phi、Google Gemma、Mistral、Meta LLaMA 的量化轉換。

### **Generative AI extensions for onnxruntime 的模型構建器**

模型構建器大大加速了創建可優化且量化的 ONNX 模型，這些模型可以通過 ONNX Runtime 的 `generate()` API 運行。

通過模型構建器，你可以將模型量化為 INT4、INT8、FP16、FP32，並結合不同的硬件加速方法，例如 CPU、CUDA、DirectML、Mobile 等。

使用模型構建器需要安裝：

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安裝完成後，你可以從終端運行模型構建器腳本，進行模型格式和量化轉換。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相關參數：

1. **model_name**：這是 Hugging Face 上的模型名稱，例如 `microsoft/Phi-3.5-mini-instruct`，`microsoft/Phi-3.5-vision-instruct` 等。也可以是你存儲模型的路徑。

2. **path_to_output_folder**：量化轉換的保存路徑。

3. **execution_provider**：不同的硬件加速支持，例如 cpu、cuda、DirectML。

4. **cache_dir_to_save_hf_files**：我們從 Hugging Face 下載模型並緩存到本地的路徑。

***注意：***

## **如何使用模型構建器量化 Phi-3.5**

模型構建器現在支持 Phi-3.5 Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化。

### **Phi-3.5-Instruct**

**CPU 加速的 INT 4 量化轉換**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA 加速的 INT 4 量化轉換**

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

2. 在 models 資料夾中下載 `microsoft/Phi-3.5-vision-instruct`  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 請下載以下文件到你的 Phi-3.5-vision-instruct 資料夾：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 下載以下文件到 models 資料夾：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 打開終端：

   使用 FP32 支持轉換 ONNX：

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. 模型構建器目前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的轉換，但不支持 Phi-3.5-MoE。

2. 使用 ONNX 的量化模型時，可以通過 Generative AI extensions for onnxruntime SDK 使用。

3. 我們需要考慮更負責任的 AI，因此在模型量化轉換後，建議進行更有效的結果測試。

4. 通過量化 CPU INT4 模型，我們可以將其部署到邊緣設備，這樣會有更好的應用場景，因此我們圍繞 INT 4 完成了 Phi-3.5-Instruct 的處理。

## **資源**

1. 了解更多有關 Generative AI extensions for onnxruntime 的信息：[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime 的 GitHub 倉庫：[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免責聲明**：  
此文件經由機器翻譯服務翻譯而成。儘管我們努力確保準確性，請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。