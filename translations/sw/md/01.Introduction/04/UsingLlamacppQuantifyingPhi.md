# **Kuantisha Familia ya Phi kwa kutumia llama.cpp**

## **Llama.cpp ni nini**

llama.cpp ni maktaba ya programu ya chanzo huria iliyoandikwa kimsingi kwa C++ ambayo hufanya inference kwenye Mifano Mikubwa ya Lugha (LLMs) mbalimbali, kama vile Llama. Lengo lake kuu ni kutoa utendaji wa hali ya juu kwa inference ya LLM kwenye vifaa mbalimbali kwa maandalizi madogo. Zaidi ya hayo, kuna bindings za Python zinazopatikana kwa maktaba hii, zinazotoa API ya kiwango cha juu kwa ukamilishaji wa maandishi na seva ya wavuti inayooana na OpenAI.

Lengo kuu la llama.cpp ni kuwezesha inference ya LLM kwa maandalizi madogo na utendaji wa hali ya juu kwenye aina mbalimbali za vifaa - kwa ndani na kwenye wingu.

- Utekelezaji wa C/C++ safi bila utegemezi wowote
- Apple silicon ni kipaumbele - imerahisishwa kupitia ARM NEON, Accelerate na mifumo ya Metal
- Msaada wa AVX, AVX2 na AVX512 kwa miundo ya x86
- Kuquantisha namba nzima kwa biti 1.5, 2, 3, 4, 5, 6, na 8 kwa inference ya haraka na matumizi kidogo ya kumbukumbu
- Kernel maalum za CUDA kwa ajili ya kuendesha LLMs kwenye NVIDIA GPUs (msaada kwa AMD GPUs kupitia HIP)
- Msaada wa nyuma wa Vulkan na SYCL
- Inference ya mseto ya CPU+GPU ili kuharakisha sehemu mifano mikubwa zaidi ya uwezo wa jumla wa VRAM

## **Kuantisha Phi-3.5 kwa kutumia llama.cpp**

Mfano wa Phi-3.5-Instruct unaweza kuquantishwa kwa kutumia llama.cpp, lakini Phi-3.5-Vision na Phi-3.5-MoE bado hazijaungwa mkono. Umbizo linalobadilishwa na llama.cpp ni gguf, ambalo pia ndilo umbizo la kuquantisha linalotumika sana.

Kuna idadi kubwa ya mifano ya umbizo la GGUF iliyokwisha kuquantishwa kwenye Hugging Face. AI Foundry, Ollama, na LlamaEdge hutegemea llama.cpp, hivyo mifano ya GGUF pia hutumika mara nyingi.

### **GGUF ni nini**

GGUF ni umbizo la binary ambalo limerahisishwa kwa upakiaji na uhifadhi wa mifano kwa haraka, na kuifanya kuwa bora sana kwa madhumuni ya inference. GGUF imetengenezwa kwa ajili ya matumizi na GGML na watendaji wengine. GGUF ilitengenezwa na @ggerganov ambaye pia ndiye mtengenezaji wa llama.cpp, mfumo maarufu wa inference wa LLM wa C/C++. Mifano iliyotengenezwa awali kwenye mifumo kama PyTorch inaweza kubadilishwa kuwa umbizo la GGUF kwa matumizi na injini hizo.

### **ONNX dhidi ya GGUF**

ONNX ni umbizo la jadi la ujifunzaji wa mashine/ujifunzaji wa kina, ambalo linaungwa mkono vizuri kwenye Mifumo mbalimbali ya AI na lina hali nzuri za matumizi kwenye vifaa vya kingo. Kwa upande wa GGUF, msingi wake ni llama.cpp na inaweza kusemwa kuwa imeundwa katika enzi ya GenAI. Zote mbili zina matumizi yanayofanana. Ikiwa unataka utendaji bora katika vifaa vya kingo na tabaka za maombi, ONNX inaweza kuwa chaguo lako. Ikiwa unatumia mfumo wa derivative na teknolojia ya llama.cpp, basi GGUF inaweza kuwa bora zaidi.

### **Kuantisha Phi-3.5-Instruct kwa kutumia llama.cpp**

**1. Usanidi wa Mazingira**

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```

**2. Kuquantisha**

Kutumia llama.cpp kubadilisha Phi-3.5-Instruct kuwa FP16 GGUF

```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kuantisha Phi-3.5 kuwa INT4

```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```

**3. Kupima**

Sakinisha llama-cpp-python

```bash

pip install llama-cpp-python -U

```

***Kumbuka***

Ikiwa unatumia Apple Silicon, tafadhali sakinisha llama-cpp-python hivi

```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Kupima

```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```

## **Rasilimali**

1. Jifunze zaidi kuhusu llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Jifunze zaidi kuhusu GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.