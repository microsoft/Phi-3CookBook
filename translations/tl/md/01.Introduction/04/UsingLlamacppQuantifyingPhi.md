# **Pagku-quantize ng Phi Family gamit ang llama.cpp**

## **Ano ang llama.cpp**

Ang llama.cpp ay isang open-source na software library na pangunahing nakasulat sa C++ na gumaganap ng inference sa iba't ibang Large Language Models (LLMs), tulad ng Llama. Ang pangunahing layunin nito ay magbigay ng makabagong performance para sa LLM inference sa iba't ibang hardware na may minimal na setup. Bukod dito, may mga Python bindings din na magagamit para sa library na ito, na nag-aalok ng high-level API para sa text completion at isang OpenAI-compatible na web server.

Ang pangunahing layunin ng llama.cpp ay paganahin ang LLM inference na may minimal na setup at makabagong performance sa iba't ibang hardware - lokal man o nasa cloud.

- Plain C/C++ implementation na walang anumang dependencies
- Ang Apple silicon ay isang pangunahing prayoridad - optimized gamit ang ARM NEON, Accelerate, at Metal frameworks
- May suporta para sa AVX, AVX2, at AVX512 para sa x86 architectures
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, at 8-bit na integer quantization para sa mas mabilis na inference at mas mababang paggamit ng memory
- Custom CUDA kernels para sa pagpapatakbo ng LLMs sa NVIDIA GPUs (may suporta rin para sa AMD GPUs gamit ang HIP)
- Vulkan at SYCL backend support
- Hybrid na inference gamit ang CPU+GPU para mapabilis ang mga modelong mas malaki kaysa sa kabuuang kapasidad ng VRAM

## **Pagku-quantize ng Phi-3.5 gamit ang llama.cpp**

Ang Phi-3.5-Instruct model ay maaaring ma-quantize gamit ang llama.cpp, ngunit ang Phi-3.5-Vision at Phi-3.5-MoE ay hindi pa suportado. Ang format na kino-convert ng llama.cpp ay gguf, na siya ring pinakalaganap na ginagamit na quantization format.

Maraming mga quantized GGUF format models sa Hugging Face. Ang AI Foundry, Ollama, at LlamaEdge ay umaasa sa llama.cpp, kaya madalas ding ginagamit ang GGUF models.

### **Ano ang GGUF**

Ang GGUF ay isang binary format na optimized para sa mabilisang pag-load at pag-save ng mga modelo, kaya't napakahusay nito para sa inference purposes. Ang GGUF ay idinisenyo para gamitin sa GGML at iba pang executors. Ang GGUF ay binuo ni @ggerganov, na siya ring developer ng llama.cpp, isang sikat na C/C++ LLM inference framework. Ang mga modelong unang binuo gamit ang frameworks tulad ng PyTorch ay maaaring i-convert sa GGUF format para magamit sa mga engines na ito.

### **ONNX vs GGUF**

Ang ONNX ay isang tradisyunal na format para sa machine learning/deep learning, na mahusay ang suporta sa iba't ibang AI Frameworks at may magagandang use cases sa edge devices. Sa kabilang banda, ang GGUF ay nakabase sa llama.cpp at maaaring sabihing produkto ng GenAI era. Magkakapareho ang gamit ng dalawa. Kung nais mo ng mas mahusay na performance sa embedded hardware at application layers, maaaring ONNX ang piliin mo. Kung gumagamit ka ng mga derivative framework at teknolohiya ng llama.cpp, maaaring mas angkop ang GGUF.

### **Pagku-quantize ng Phi-3.5-Instruct gamit ang llama.cpp**

**1. Konfigurasyon ng Environment**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

Gamit ang llama.cpp, i-convert ang Phi-3.5-Instruct sa FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Pagku-quantize ng Phi-3.5 sa INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Pagsusuri**

I-install ang llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Tandaan*** 

Kung gumagamit ka ng Apple Silicon, i-install ang llama-cpp-python sa ganitong paraan


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Pagsusuri 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Mga Resources**

1. Alamin ang higit pa tungkol sa llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Alamin ang higit pa tungkol sa GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagama't pinagsisikapan naming maging wasto, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.