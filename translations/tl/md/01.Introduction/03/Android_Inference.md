# **Inference Phi-3 sa Android**

Tuklasin natin kung paano mag-perform ng inference gamit ang Phi-3-mini sa mga Android device. Ang Phi-3-mini ay isang bagong serye ng mga modelo mula sa Microsoft na nagbibigay-daan sa pag-deploy ng Large Language Models (LLMs) sa edge devices at IoT devices.

## Semantic Kernel at Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ay isang application framework na nagbibigay-daan sa paggawa ng mga application na compatible sa Azure OpenAI Service, OpenAI models, at maging sa mga lokal na modelo. Kung bago ka sa Semantic Kernel, inirerekomenda naming tingnan mo ang [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Para Ma-access ang Phi-3-mini Gamit ang Semantic Kernel

Maaari mong pagsamahin ito sa Hugging Face Connector sa Semantic Kernel. Tingnan ang [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

By default, ito ay tumutugma sa model ID sa Hugging Face. Gayunpaman, maaari ka ring kumonekta sa isang locally built na Phi-3-mini model server.

### Pagtawag sa Quantized Models gamit ang Ollama o LlamaEdge

Maraming gumagamit ang mas pinipiling gumamit ng quantized models upang paganahin ang mga modelo nang lokal. Ang [Ollama](https://ollama.com/) at [LlamaEdge](https://llamaedge.com) ay nagbibigay-daan sa mga indibidwal na user na tawagan ang iba't ibang quantized models:

#### Ollama

Maaari mong direktang patakbuhin ang `ollama run Phi-3` o i-configure ito offline sa pamamagitan ng paggawa ng isang `Modelfile` na may path patungo sa iyong `.gguf` file.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Kung nais mong gamitin ang mga `.gguf` file sa cloud at sa edge devices nang sabay, ang LlamaEdge ay isang mahusay na pagpipilian. Maaari kang tumingin sa [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) upang magsimula.

### Pag-install at Pagpapatakbo sa Android Phones

1. **I-download ang MLC Chat app** (Libre) para sa mga Android phone.
2. I-download ang APK file (148MB) at i-install ito sa iyong device.
3. I-launch ang MLC Chat app. Makikita mo ang listahan ng mga AI models, kabilang ang Phi-3-mini.

Sa kabuuan, ang Phi-3-mini ay nagbibigay ng kapanapanabik na mga posibilidad para sa generative AI sa mga edge device, at maaari mong simulang tuklasin ang mga kakayahan nito sa Android.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.