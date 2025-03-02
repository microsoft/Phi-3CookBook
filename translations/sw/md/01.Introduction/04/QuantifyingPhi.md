# **Kuhesabu Familia ya Phi**

Kuantisha modeli inahusu mchakato wa kubadilisha vigezo (kama vile uzito na maadili ya uanzishaji) katika modeli ya mtandao wa neva kutoka safu kubwa ya thamani (kawaida safu inayoendelea ya thamani) hadi safu ndogo ya thamani yenye upeo finiti. Teknolojia hii inaweza kupunguza ukubwa na ugumu wa kihesabu wa modeli na kuboresha ufanisi wa uendeshaji wa modeli katika mazingira yenye vikwazo vya rasilimali kama vile vifaa vya rununu au mifumo iliyopachikwa. Kuantisha modeli hufanikisha ufinyanzi kwa kupunguza usahihi wa vigezo, lakini pia huleta upotevu fulani wa usahihi. Kwa hivyo, katika mchakato wa kuantisha, ni muhimu kusawazisha kati ya ukubwa wa modeli, ugumu wa kihesabu, na usahihi. Mbinu za kawaida za kuantisha ni pamoja na kuantisha kwa pointi thabiti, kuantisha kwa pointi eleaji, n.k. Unaweza kuchagua mkakati wa kuantisha unaofaa kulingana na hali na mahitaji maalum.

Tunatarajia kuwezesha modeli za GenAI kwenye vifaa vya ukingoni na kuruhusu vifaa vingi zaidi kuingia katika hali za GenAI, kama vile vifaa vya rununu, AI PC/Copilot+PC, na vifaa vya jadi vya IoT. Kupitia modeli za kuantisha, tunaweza kuzitekeleza kwenye vifaa mbalimbali vya ukingoni kulingana na vifaa tofauti. Tukichanganya na mfumo wa kuharakisha modeli na modeli za kuantisha zinazotolewa na watengenezaji wa vifaa, tunaweza kujenga hali bora za matumizi ya SLM.

Katika hali ya kuantisha, tunayo usahihi tofauti (INT4, INT8, FP16, FP32). Hapa chini ni maelezo ya usahihi wa kawaida wa kuantisha.

### **INT4**

Kuantisha kwa INT4 ni mbinu ya kuantisha yenye ukali ambayo hubadilisha uzito na maadili ya uanzishaji wa modeli kuwa namba za integer za biti 4. Kuantisha kwa INT4 mara nyingi husababisha upotevu mkubwa wa usahihi kutokana na safu ndogo ya uwakilishi na usahihi wa chini. Hata hivyo, ikilinganishwa na kuantisha kwa INT8, INT4 inaweza kupunguza zaidi mahitaji ya uhifadhi na ugumu wa kihesabu wa modeli. Ni muhimu kutambua kuwa kuantisha kwa INT4 ni nadra katika matumizi ya vitendo, kwa sababu usahihi wa chini sana unaweza kusababisha kushuka kwa utendaji wa modeli. Aidha, si vifaa vyote vinavyounga mkono operesheni za INT4, kwa hivyo utangamano wa vifaa unahitaji kuzingatiwa wakati wa kuchagua njia ya kuantisha.

### **INT8**

Kuantisha kwa INT8 ni mchakato wa kubadilisha uzito na uanzishaji wa modeli kutoka namba za pointi eleaji hadi namba za integer za biti 8. Ingawa safu ya thamani inayowakilishwa na namba za INT8 ni ndogo na isiyo sahihi sana, inaweza kupunguza kwa kiasi kikubwa mahitaji ya uhifadhi na hesabu. Katika kuantisha kwa INT8, uzito na maadili ya uanzishaji wa modeli hupitia mchakato wa kuantisha, ikiwa ni pamoja na kiwango na mwelekeo, ili kuhifadhi maelezo ya asili ya pointi eleaji kadri inavyowezekana. Wakati wa uchanganuzi, maadili haya yaliyokuantishwa yatarejeshwa tena kuwa namba za pointi eleaji kwa ajili ya mahesabu, na kisha kuquantishwa tena hadi INT8 kwa hatua inayofuata. Njia hii inaweza kutoa usahihi wa kutosha katika matumizi mengi huku ikidumisha ufanisi wa juu wa kihesabu.

### **FP16**

Muundo wa FP16, yaani, namba za pointi eleaji za biti 16 (float16), hupunguza matumizi ya kumbukumbu kwa nusu ikilinganishwa na namba za pointi eleaji za biti 32 (float32), ambayo ina faida kubwa katika matumizi ya ujifunzaji wa kina wa kiwango kikubwa. Muundo wa FP16 huruhusu kupakia modeli kubwa zaidi au kushughulikia data zaidi ndani ya mipaka ile ile ya kumbukumbu ya GPU. Kadri vifaa vya kisasa vya GPU vinavyoendelea kuunga mkono operesheni za FP16, kutumia muundo wa FP16 kunaweza pia kuleta maboresho katika kasi ya mahesabu. Hata hivyo, muundo wa FP16 pia una hasara zake za asili, yaani usahihi wa chini, ambao unaweza kusababisha kutokuwa thabiti kwa kihesabu au upotevu wa usahihi katika baadhi ya matukio.

### **FP32**

Muundo wa FP32 hutoa usahihi wa juu zaidi na unaweza kuwakilisha kwa usahihi safu pana ya thamani. Katika hali ambapo operesheni ngumu za kihesabu hufanyika au matokeo yenye usahihi wa juu yanahitajika, muundo wa FP32 unapendelewa. Hata hivyo, usahihi wa juu pia unamaanisha matumizi zaidi ya kumbukumbu na muda mrefu wa mahesabu. Kwa modeli kubwa za ujifunzaji wa kina, hasa pale ambapo kuna vigezo vingi vya modeli na kiasi kikubwa cha data, muundo wa FP32 unaweza kusababisha ukosefu wa kumbukumbu ya GPU au kupungua kwa kasi ya uchanganuzi.

Kwenye vifaa vya rununu au vifaa vya IoT, tunaweza kubadilisha modeli za Phi-3.x kuwa INT4, wakati AI PC / Copilot PC inaweza kutumia usahihi wa juu zaidi kama INT8, FP16, FP32.

Kwa sasa, watengenezaji tofauti wa vifaa wana mifumo tofauti ya kusaidia modeli za kizazi, kama vile OpenVINO ya Intel, QNN ya Qualcomm, MLX ya Apple, na CUDA ya Nvidia, n.k., pamoja na kuantisha modeli ili kukamilisha utekelezaji wa ndani.

Kwa upande wa teknolojia, tunayo miundo tofauti ya kuunga mkono baada ya kuantisha, kama vile muundo wa PyTorch / Tensorflow, GGUF, na ONNX. Nimefanya kulinganisha miundo na hali za matumizi kati ya GGUF na ONNX. Hapa napendekeza muundo wa kuantisha wa ONNX, ambao una msaada mzuri kutoka kwa mfumo wa modeli hadi vifaa. Katika sura hii, tutaangazia ONNX Runtime kwa GenAI, OpenVINO, na Apple MLX ili kufanya kuantisha kwa modeli (ikiwa una njia bora, unaweza pia kutupatia kwa kuwasilisha PR).

**Sura hii inajumuisha**

1. [Kuantisha Phi-3.5 / 4 kwa kutumia llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kuantisha Phi-3.5 / 4 kwa kutumia viendelezi vya Generative AI kwa onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kuantisha Phi-3.5 / 4 kwa kutumia Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kuantisha Phi-3.5 / 4 kwa kutumia Mfumo wa Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za mashine zinazotumia AI. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.