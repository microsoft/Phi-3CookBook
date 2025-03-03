Katika muktadha wa Phi-3-mini, "inference" inahusu mchakato wa kutumia mfano kufanya utabiri au kutoa matokeo kulingana na data ya pembejeo. Hebu nikueleze kwa undani zaidi kuhusu Phi-3-mini na uwezo wake wa inference.

Phi-3-mini ni sehemu ya mfululizo wa mifano ya Phi-3 iliyotolewa na Microsoft. Mifano hii imeundwa ili kufafanua upya kile kinachowezekana kwa Small Language Models (SLMs).

Hapa kuna hoja muhimu kuhusu Phi-3-mini na uwezo wake wa inference:

## **Muhtasari wa Phi-3-mini:**
- Phi-3-mini ina ukubwa wa vigezo wa bilioni 3.8.
- Inaweza kuendeshwa si tu kwenye vifaa vya kompyuta vya jadi, bali pia kwenye vifaa vya edge kama vile vifaa vya rununu na vifaa vya IoT.
- Utoaji wa Phi-3-mini unawawezesha watu binafsi na mashirika kutumia SLMs kwenye vifaa tofauti vya maunzi, hasa katika mazingira yenye rasilimali chache.
- Inashughulikia miundo mbalimbali ya mfano, ikijumuisha muundo wa jadi wa PyTorch, toleo lililopunguzwa la muundo wa gguf, na toleo la ONNX lililopunguzwa.

## **Kufikia Phi-3-mini:**
Ili kufikia Phi-3-mini, unaweza kutumia [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) katika programu ya Copilot. Semantic Kernel kwa ujumla inaoana na Azure OpenAI Service, mifano ya chanzo huria kwenye Hugging Face, na mifano ya ndani.
Unaweza pia kutumia [Ollama](https://ollama.com) au [LlamaEdge](https://llamaedge.com) kupiga mifano iliyopunguzwa. Ollama inaruhusu watumiaji binafsi kupiga mifano tofauti iliyopunguzwa, wakati LlamaEdge inatoa upatikanaji wa mifano ya GGUF kwenye majukwaa mbalimbali.

## **Mifano Iliyopunguzwa:**
Watumiaji wengi wanapendelea kutumia mifano iliyopunguzwa kwa inference ya ndani. Kwa mfano, unaweza kuendesha moja kwa moja `Ollama run Phi-3` au kuiweka nje ya mtandao ukitumia Modelfile. Modelfile inaeleza njia ya faili ya GGUF na umbizo la prompt.

## **Uwezekano wa Generative AI:**
Kuchanganya SLMs kama Phi-3-mini kunafungua uwezekano mpya kwa Generative AI. Inference ni hatua ya kwanza tu; mifano hii inaweza kutumika kwa kazi mbalimbali katika mazingira yenye vikwazo vya rasilimali, ucheleweshaji, na gharama.

## **Kufungua Generative AI na Phi-3-mini: Mwongozo wa Inference na Utekelezaji**  
Jifunze jinsi ya kutumia Semantic Kernel, Ollama/LlamaEdge, na ONNX Runtime kufikia na kufanya inference kwa mifano ya Phi-3-mini, na uchunguze uwezekano wa Generative AI katika hali mbalimbali za matumizi.

**Vipengele**
Inference ya mfano wa phi3-mini katika:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Kwa muhtasari, Phi-3-mini inawawezesha watengenezaji kuchunguza miundo tofauti ya mfano na kutumia Generative AI katika hali mbalimbali za matumizi.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotumia mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.