Phi-3-mini को सन्दर्भमा, "inference" भनेको मोडेललाई इनपुट डाटाको आधारमा भविष्यवाणी गर्न वा आउटपुट उत्पादन गर्न प्रयोग गर्ने प्रक्रिया हो। अब म तपाईंलाई Phi-3-mini र यसको inference क्षमताका बारेमा थप विवरण दिन्छु।

Phi-3-mini, Microsoft द्वारा जारी गरिएको Phi-3 श्रृंखलाको हिस्सा हो। यी मोडेलहरू साना भाषा मोडेलहरू (SLMs) का साथ सम्भव हुने कुराहरूलाई पुनः परिभाषित गर्न डिजाइन गरिएका छन्।

यहाँ Phi-3-mini र यसको inference क्षमताका केही मुख्य बुँदाहरू छन्:

## **Phi-3-mini को अवलोकन:**
- Phi-3-mini को parameter आकार ३.८ अर्ब छ।
- यसले परम्परागत कम्प्युटिङ उपकरणहरू मात्र नभई मोबाइल उपकरणहरू र IoT उपकरणहरू जस्ता edge उपकरणहरूमा पनि चलाउन सक्छ।
- Phi-3-mini को रिलिजले व्यक्तिहरू र उद्यमहरूलाई resource-constrained वातावरणहरूमा विभिन्न हार्डवेयर उपकरणहरूमा SLMs तैनाथ गर्न सक्षम बनाउँछ।
- यसले विभिन्न मोडेल ढाँचाहरू समेट्छ, जस्तै परम्परागत PyTorch ढाँचा, gguf ढाँचाको quantized संस्करण, र ONNX-आधारित quantized संस्करण।

## **Phi-3-mini पहुँच गर्ने तरिका:**
Phi-3-mini पहुँच गर्न, तपाईं [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) लाई Copilot एप्लिकेसनमा प्रयोग गर्न सक्नुहुन्छ। Semantic Kernel सामान्यतया Azure OpenAI Service, Hugging Face मा रहेका open-source मोडेलहरू, र स्थानीय मोडेलहरूसँग उपयुक्त छ।
तपाईं [Ollama](https://ollama.com) वा [LlamaEdge](https://llamaedge.com) प्रयोग गरेर पनि quantized मोडेलहरूलाई कल गर्न सक्नुहुन्छ। Ollama ले व्यक्तिगत प्रयोगकर्ताहरूलाई विभिन्न quantized मोडेलहरू कल गर्न अनुमति दिन्छ, जबकि LlamaEdge ले GGUF मोडेलहरूको लागि cross-platform उपलब्धता प्रदान गर्छ।

## **Quantized मोडेलहरू:**
धेरै प्रयोगकर्ताहरू स्थानीय inference को लागि quantized मोडेलहरू प्रयोग गर्न रुचाउँछन्। उदाहरणका लागि, तपाईं सिधै "Ollama run Phi-3" चलाउन सक्नुहुन्छ वा Modelfile प्रयोग गरेर यसलाई अफलाइन कन्फिगर गर्न सक्नुहुन्छ। Modelfile ले GGUF फाइल पथ र prompt ढाँचालाई निर्दिष्ट गर्छ।

## **Generative AI का सम्भावनाहरू:**
Phi-3-mini जस्ता SLMs को संयोजनले Generative AI को नयाँ सम्भावनाहरू खोल्छ। Inference त पहिलो कदम मात्र हो; यी मोडेलहरू resource-constrained, latency-bound, र cost-constrained परिदृश्यहरूमा विभिन्न कार्यहरूको लागि प्रयोग गर्न सकिन्छ।

## **Phi-3-mini सँग Generative AI अनलक गर्ने: Inference र Deployment को मार्गदर्शन**  
Semantic Kernel, Ollama/LlamaEdge, र ONNX Runtime प्रयोग गरेर Phi-3-mini मोडेलहरू पहुँच गर्न र infer गर्न सिक्नुहोस्, र विभिन्न एप्लिकेसन परिदृश्यहरूमा Generative AI को सम्भावनाहरू पत्ता लगाउनुहोस्।

**विशेषताहरू**
Phi-3-mini मोडेललाई निम्नमा infer गर्नुहोस्:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

सारांशमा, Phi-3-mini ले विकासकर्ताहरूलाई विभिन्न मोडेल ढाँचाहरू अन्वेषण गर्न र Generative AI लाई विभिन्न एप्लिकेसन परिदृश्यहरूमा प्रयोग गर्न सक्षम बनाउँछ।

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको छ। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया सचेत रहनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल भाषामा रहेको मूल दस्तावेजलाई प्रामाणिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।