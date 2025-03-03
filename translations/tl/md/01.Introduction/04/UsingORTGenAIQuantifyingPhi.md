# **Pag-quantize ng Phi Family gamit ang Generative AI extensions para sa onnxruntime**

## **Ano ang Generative AI extensions para sa onnxruntime**

Ang mga extension na ito ay tumutulong sa iyo na magpatakbo ng generative AI gamit ang ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Nagbibigay ito ng generative AI loop para sa mga ONNX model, kabilang ang inference gamit ang ONNX Runtime, logits processing, paghahanap at sampling, at pamamahala ng KV cache. Maaaring tawagin ng mga developer ang high-level na generate() method, o patakbuhin ang bawat iteration ng modelo sa isang loop, na bumubuo ng isang token sa bawat pagkakataon, at opsyonal na i-update ang mga parameter ng generation sa loob ng loop. Sinusuportahan nito ang greedy/beam search at TopP, TopK sampling para bumuo ng mga token sequence, pati na rin ang built-in logits processing tulad ng repetition penalties. Madali mo ring maidaragdag ang custom na scoring.

Sa antas ng aplikasyon, maaari mong gamitin ang Generative AI extensions para sa onnxruntime upang bumuo ng mga aplikasyon gamit ang C++/ C# / Python. Sa antas ng modelo, maaari mo itong gamitin upang pagsamahin ang mga fine-tuned na modelo at gawin ang mga kaugnay na gawain sa quantitative deployment.

## **Pag-quantize ng Phi-3.5 gamit ang Generative AI extensions para sa onnxruntime**

### **Mga Sinusuportahang Modelo**

Sinusuportahan ng Generative AI extensions para sa onnxruntime ang conversion ng quantization para sa Microsoft Phi, Google Gemma, Mistral, at Meta LLaMA.

### **Model Builder sa Generative AI extensions para sa onnxruntime**

Ang Model Builder ay lubos na nagpapabilis sa paglikha ng mga optimized at quantized na ONNX model na tumatakbo gamit ang ONNX Runtime generate() API.

Sa pamamagitan ng Model Builder, maaari mong i-quantize ang modelo sa INT4, INT8, FP16, FP32, at pagsamahin ang iba't ibang hardware acceleration methods tulad ng CPU, CUDA, DirectML, Mobile, atbp.

Upang magamit ang Model Builder, kailangan mong i-install ang

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Pagkatapos ng pag-install, maaari mong patakbuhin ang Model Builder script mula sa terminal upang maisagawa ang conversion ng model format at quantization.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Unawain ang mga kaugnay na parameter:

1. **model_name** Ito ang modelo sa Hugging Face, tulad ng microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, atbp. Maaari rin itong ang path kung saan mo iniimbak ang modelo.

2. **path_to_output_folder** Ang path kung saan ise-save ang resulta ng quantized conversion.

3. **execution_provider** Suporta para sa iba't ibang hardware acceleration, tulad ng CPU, CUDA, DirectML.

4. **cache_dir_to_save_hf_files** Dito natin dina-download ang modelo mula sa Hugging Face at sine-save ito nang lokal.

***Tandaan:***

## **Paano gamitin ang Model Builder upang i-quantize ang Phi-3.5**

Sinusuportahan na ngayon ng Model Builder ang ONNX model quantization para sa Phi-3.5 Instruct at Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**CPU accelerated conversion ng quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA accelerated conversion ng quantized INT 4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. I-set up ang environment sa terminal:

```bash

mkdir models

cd models 

```

2. I-download ang microsoft/Phi-3.5-vision-instruct sa models folder:  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. I-download ang mga sumusunod na file sa iyong Phi-3.5-vision-instruct folder:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. I-download ang file na ito sa models folder:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Pumunta sa terminal:

   I-convert ang ONNX support gamit ang FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Tandaan:**

1. Sinusuportahan ng Model Builder ang conversion ng Phi-3.5-Instruct at Phi-3.5-Vision, ngunit hindi pa sinusuportahan ang Phi-3.5-MoE.

2. Upang magamit ang ONNX na quantized model, maaari mo itong gamitin sa pamamagitan ng Generative AI extensions para sa onnxruntime SDK.

3. Kailangan nating isaalang-alang ang mas responsableng AI, kaya pagkatapos ng conversion ng model quantization, inirerekomenda na magsagawa ng mas epektibong pagsusuri ng resulta.

4. Sa pamamagitan ng pag-quantize ng CPU INT4 model, maaari nating i-deploy ito sa Edge Device, na may mas magagandang aplikasyon, kaya nakumpleto natin ang Phi-3.5-Instruct sa paligid ng INT 4.

## **Mga Mapagkukunan**

1. Alamin ang higit pa tungkol sa Generative AI extensions para sa onnxruntime:  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions para sa onnxruntime GitHub Repo:  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagama't aming pinagsisikapan ang kawastuhan, pakitandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa wika nito ang dapat ituring na pangunahing sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng salin na ito.