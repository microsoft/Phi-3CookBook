# **Pagku-quantify ng Phi Family**

Ang model quantization ay tumutukoy sa proseso ng pagmamapa ng mga parameter (tulad ng weights at activation values) sa isang neural network model mula sa malawak na hanay ng mga halaga (karaniwang tuloy-tuloy na hanay ng halaga) patungo sa mas maliit na hanay ng tiyak na mga halaga. Ang teknolohiyang ito ay maaaring magpabawas ng laki at computational complexity ng modelo at mapabuti ang kahusayan nito sa mga kapaligirang may limitadong resources tulad ng mga mobile device o embedded systems. Ang model quantization ay nakakamit ang compression sa pamamagitan ng pagbabawas ng precision ng mga parameter, ngunit nagdadala rin ito ng tiyak na pagkawala ng precision. Kaya't sa proseso ng quantization, kailangang balansehin ang laki ng modelo, computational complexity, at precision. Ang mga karaniwang pamamaraan ng quantization ay kinabibilangan ng fixed-point quantization, floating-point quantization, at iba pa. Maaari kang pumili ng angkop na quantization strategy batay sa partikular na sitwasyon at pangangailangan.

Nilalayon naming i-deploy ang GenAI model sa mga edge device at bigyang-daan ang mas maraming device na makapasok sa mga GenAI scenario, tulad ng mga mobile device, AI PC/Copilot+PC, at tradisyunal na IoT devices. Sa pamamagitan ng quantization model, maaari naming i-deploy ito sa iba't ibang edge device batay sa iba't ibang hardware. Pinagsama sa model acceleration framework at quantization model na ibinibigay ng mga tagagawa ng hardware, maaari kaming bumuo ng mas mahusay na SLM application scenarios.

Sa quantization scenario, mayroon tayong iba't ibang precision (INT4, INT8, FP16, FP32). Narito ang paliwanag ng mga karaniwang ginagamit na quantization precisions:

### **INT4**

Ang INT4 quantization ay isang radikal na paraan ng quantization na nagko-convert ng weights at activation values ng modelo sa 4-bit integers. Karaniwan, ang INT4 quantization ay nagdudulot ng mas malaking pagkawala ng precision dahil sa mas maliit na saklaw ng representasyon at mas mababang precision. Gayunpaman, kumpara sa INT8 quantization, ang INT4 quantization ay maaaring higit pang magpabawas sa storage requirements at computational complexity ng modelo. Dapat tandaan na ang INT4 quantization ay bihirang gamitin sa praktikal na aplikasyon, dahil ang sobrang mababang precision ay maaaring magdulot ng malaking pagbaba sa performance ng modelo. Bukod dito, hindi lahat ng hardware ay sumusuporta sa INT4 operations, kaya't kailangang isaalang-alang ang compatibility ng hardware kapag pumipili ng paraan ng quantization.

### **INT8**

Ang INT8 quantization ay ang proseso ng pag-convert ng weights at activations ng isang modelo mula sa floating-point numbers patungo sa 8-bit integers. Bagaman mas maliit ang numerical range at precision ng INT8 integers, maaari nitong lubos na bawasan ang storage at computational requirements. Sa INT8 quantization, ang weights at activation values ng modelo ay dumadaan sa proseso ng quantization, kabilang ang scaling at offset, upang mapanatili ang orihinal na floating-point information hangga't maaari. Sa panahon ng inference, ang mga quantized values na ito ay ide-dequantize pabalik sa floating-point numbers para sa kalkulasyon, at pagkatapos ay muling iku-quantize pabalik sa INT8 para sa susunod na hakbang. Ang pamamaraang ito ay maaaring magbigay ng sapat na precision sa karamihan ng mga aplikasyon habang pinapanatili ang mataas na computational efficiency.

### **FP16**

Ang FP16 format, o 16-bit floating-point numbers (float16), ay nagbabawas ng memory footprint nang kalahati kumpara sa 32-bit floating-point numbers (float32), na may malaking bentahe sa malakihang deep learning applications. Ang FP16 format ay nagbibigay-daan sa pag-load ng mas malalaking modelo o pagproseso ng mas maraming data sa loob ng parehong GPU memory limitations. Habang patuloy na sinusuportahan ng modernong GPU hardware ang FP16 operations, ang paggamit ng FP16 format ay maaari ring magdala ng mga pagpapabuti sa bilis ng pag-compute. Gayunpaman, ang FP16 format ay may likas na mga kahinaan, kabilang ang mas mababang precision, na maaaring magresulta sa numerical instability o pagkawala ng precision sa ilang mga kaso.

### **FP32**

Ang FP32 format ay nagbibigay ng mas mataas na precision at maaaring tumpak na magrepresenta ng malawak na hanay ng mga halaga. Sa mga sitwasyong nangangailangan ng kumplikadong mathematical operations o mataas na precision na resulta, mas pinipili ang FP32 format. Gayunpaman, ang mataas na precision ay nangangahulugan din ng mas malaking memory usage at mas mahabang oras ng kalkulasyon. Para sa malakihang deep learning models, lalo na kapag maraming model parameters at napakalaking dami ng data, ang FP32 format ay maaaring magdulot ng kakulangan sa GPU memory o pagbaba sa bilis ng inference.

Sa mga mobile device o IoT devices, maaari nating i-convert ang Phi-3.x models sa INT4, habang ang AI PC / Copilot PC ay maaaring gumamit ng mas mataas na precision tulad ng INT8, FP16, at FP32.

Sa kasalukuyan, iba't ibang tagagawa ng hardware ang may kani-kaniyang framework upang suportahan ang generative models, tulad ng OpenVINO ng Intel, QNN ng Qualcomm, MLX ng Apple, at CUDA ng Nvidia. Pinagsama sa model quantization, maaaring makumpleto ang local deployment.

Sa teknikal na aspeto, mayroon tayong iba't ibang format na sinusuportahan pagkatapos ng quantization, tulad ng PyTorch / Tensorflow format, GGUF, at ONNX. Nakagawa na ako ng paghahambing ng format at application scenarios sa pagitan ng GGUF at ONNX. Dito, inirerekomenda ko ang ONNX quantization format, na may mahusay na suporta mula sa model framework patungo sa hardware. Sa kabanatang ito, magtutuon tayo sa ONNX Runtime para sa GenAI, OpenVINO, at Apple MLX upang magsagawa ng model quantization (kung mayroon kang mas mahusay na paraan, maaari mo rin itong ibigay sa amin sa pamamagitan ng pagsusumite ng PR).

**Kasama sa kabanatang ito**

1. [Pagku-quantify ng Phi-3.5 / 4 gamit ang llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Pagku-quantify ng Phi-3.5 / 4 gamit ang Generative AI extensions para sa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Pagku-quantify ng Phi-3.5 / 4 gamit ang Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Pagku-quantify ng Phi-3.5 / 4 gamit ang Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.