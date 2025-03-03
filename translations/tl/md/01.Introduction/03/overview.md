Sa konteksto ng Phi-3-mini, ang inference ay tumutukoy sa proseso ng paggamit ng modelo upang gumawa ng prediksyon o lumikha ng output batay sa input na datos. Narito ang higit pang detalye tungkol sa Phi-3-mini at ang mga kakayahan nito sa inference.

Ang Phi-3-mini ay bahagi ng serye ng Phi-3 na mga modelo na inilabas ng Microsoft. Ang mga modelong ito ay idinisenyo upang muling tukuyin ang mga kakayahan ng Small Language Models (SLMs).

Narito ang ilang mahahalagang punto tungkol sa Phi-3-mini at ang kakayahan nitong mag-inference:

## **Pangkalahatang-ideya ng Phi-3-mini:**
- Ang Phi-3-mini ay may laki ng parameter na 3.8 bilyon.
- Maaari itong tumakbo hindi lamang sa mga tradisyunal na computing device kundi pati na rin sa mga edge device tulad ng mga mobile device at IoT device.
- Ang paglabas ng Phi-3-mini ay nagbibigay-daan sa mga indibidwal at negosyo na mag-deploy ng SLMs sa iba’t ibang hardware device, lalo na sa mga kapaligirang limitado ang mapagkukunan.
- Sinasaklaw nito ang iba’t ibang format ng modelo, kabilang ang tradisyunal na PyTorch format, ang quantized na bersyon ng gguf format, at ang ONNX-based na quantized na bersyon.

## **Pag-access sa Phi-3-mini:**
Upang ma-access ang Phi-3-mini, maaari mong gamitin ang [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) sa isang Copilot application. Ang Semantic Kernel ay karaniwang compatible sa Azure OpenAI Service, mga open-source na modelo sa Hugging Face, at mga lokal na modelo.  
Maaari mo ring gamitin ang [Ollama](https://ollama.com) o [LlamaEdge](https://llamaedge.com) upang tawagan ang mga quantized na modelo. Ang Ollama ay nagbibigay-daan sa mga indibidwal na user na gumamit ng iba’t ibang quantized na modelo, habang ang LlamaEdge ay nagbibigay ng cross-platform availability para sa GGUF models.

## **Quantized na Mga Modelo:**
Maraming user ang mas pinipili ang paggamit ng quantized na mga modelo para sa lokal na inference. Halimbawa, maaari kang direktang magpatakbo ng Ollama run Phi-3 o i-configure ito offline gamit ang isang Modelfile. Ang Modelfile ay nagtatakda ng GGUF file path at ang prompt format.

## **Mga Posibilidad ng Generative AI:**
Ang pagsasama ng mga SLM tulad ng Phi-3-mini ay nagbubukas ng mga bagong posibilidad para sa generative AI. Ang inference ay unang hakbang lamang; ang mga modelong ito ay maaaring gamitin para sa iba’t ibang gawain sa mga kapaligirang limitado ang mapagkukunan, sensitibo sa latency, at limitado ang badyet.

## **Pag-unlock ng Generative AI gamit ang Phi-3-mini: Isang Gabay sa Inference at Deployment**  
Alamin kung paano gamitin ang Semantic Kernel, Ollama/LlamaEdge, at ONNX Runtime upang ma-access at mag-inference gamit ang mga Phi-3-mini model, at tuklasin ang mga posibilidad ng generative AI sa iba’t ibang mga senaryo ng aplikasyon.

**Mga Tampok**  
Inference ng Phi-3-mini model sa:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Sa kabuuan, ang Phi-3-mini ay nagbibigay-daan sa mga developer na galugarin ang iba’t ibang format ng modelo at gamitin ang generative AI sa iba’t ibang mga senaryo ng aplikasyon.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong pang-translate na nakabatay sa AI. Bagama't sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkaunawa o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.