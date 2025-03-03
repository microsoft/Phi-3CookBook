# Azure AI Foundry में Microsoft के उत्तरदायी AI सिद्धांतों पर ध्यान केंद्रित करते हुए Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें

यह एंड-टू-एंड (E2E) उदाहरण Microsoft टेक कम्युनिटी के गाइड "[Azure AI Foundry में Fine-tuned Phi-3 / 3.5 मॉडल का मूल्यांकन करें, Microsoft के उत्तरदायी AI पर ध्यान केंद्रित करते हुए](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" पर आधारित है।

## परिचय

### Azure AI Foundry में Fine-tuned Phi-3 / Phi-3.5 मॉडल की सुरक्षा और प्रदर्शन का मूल्यांकन कैसे करें?

कई बार मॉडल को Fine-tune करने से अनपेक्षित या अवांछित प्रतिक्रियाएं उत्पन्न हो सकती हैं। यह सुनिश्चित करने के लिए कि मॉडल सुरक्षित और प्रभावी बना रहे, यह महत्वपूर्ण है कि उसके हानिकारक सामग्री उत्पन्न करने की संभावना और सटीक, प्रासंगिक, और सुसंगत प्रतिक्रियाएं देने की क्षमता का मूल्यांकन किया जाए। इस ट्यूटोरियल में, आप Azure AI Foundry में Prompt flow के साथ इंटीग्रेट किए गए Fine-tuned Phi-3 / Phi-3.5 मॉडल की सुरक्षा और प्रदर्शन का मूल्यांकन करना सीखेंगे।

यहां Azure AI Foundry का मूल्यांकन प्रक्रिया है।

![ट्यूटोरियल की आर्किटेक्चर।](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.hi.png)

*चित्र स्रोत: [जनरेटिव AI अनुप्रयोगों का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 के बारे में अधिक जानकारी और अतिरिक्त संसाधनों को एक्सप्लोर करने के लिए, कृपया [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) पर जाएं।

### पूर्व-आवश्यकताएं

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 मॉडल

### सामग्री की तालिका

1. [**परिदृश्य 1: Azure AI Foundry के Prompt flow मूल्यांकन का परिचय**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [सुरक्षा मूल्यांकन का परिचय](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [प्रदर्शन मूल्यांकन का परिचय](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**परिदृश्य 2: Azure AI Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [शुरू करने से पहले](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए Azure OpenAI को डिप्लॉय करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry के Prompt flow मूल्यांकन का उपयोग करके Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [बधाई हो!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **परिदृश्य 1: Azure AI Foundry के Prompt flow मूल्यांकन का परिचय**

### सुरक्षा मूल्यांकन का परिचय

यह सुनिश्चित करने के लिए कि आपका AI मॉडल नैतिक और सुरक्षित है, इसे Microsoft के उत्तरदायी AI सिद्धांतों के खिलाफ मूल्यांकन करना अनिवार्य है। Azure AI Foundry में, सुरक्षा मूल्यांकन आपको यह जांचने की अनुमति देता है कि आपका मॉडल जेलब्रेक हमलों के प्रति कितना संवेदनशील है और हानिकारक सामग्री उत्पन्न करने की उसकी संभावना क्या है, जो सीधे इन सिद्धांतों के साथ संरेखित है।

![सुरक्षा मूल्यांकन।](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.hi.png)

*चित्र स्रोत: [जनरेटिव AI अनुप्रयोगों का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft के उत्तरदायी AI सिद्धांत

तकनीकी चरणों को शुरू करने से पहले, Microsoft के उत्तरदायी AI सिद्धांतों को समझना आवश्यक है। यह एक नैतिक ढांचा है जो AI सिस्टम के जिम्मेदार विकास, तैनाती, और संचालन का मार्गदर्शन करने के लिए डिज़ाइन किया गया है। ये सिद्धांत AI सिस्टम को निष्पक्ष, पारदर्शी, और समावेशी तरीके से बनाने को सुनिश्चित करते हैं। AI मॉडल की सुरक्षा का मूल्यांकन करने के लिए ये सिद्धांत आधारशिला हैं।

Microsoft के उत्तरदायी AI सिद्धांतों में शामिल हैं:

- **निष्पक्षता और समावेशिता**: AI सिस्टम को सभी के साथ निष्पक्ष व्यवहार करना चाहिए और समान परिस्थितियों वाले समूहों को अलग-अलग तरीके से प्रभावित करने से बचना चाहिए। उदाहरण के लिए, जब AI सिस्टम चिकित्सा उपचार, ऋण आवेदन, या रोजगार पर मार्गदर्शन प्रदान करता है, तो उसे समान लक्षण, वित्तीय परिस्थितियों, या पेशेवर योग्यता वाले सभी लोगों को समान सिफारिशें देनी चाहिए।

- **विश्वसनीयता और सुरक्षा**: विश्वास बनाने के लिए, यह महत्वपूर्ण है कि AI सिस्टम विश्वसनीय, सुरक्षित, और सुसंगत रूप से संचालित हो। इन सिस्टम्स को मूल रूप से डिज़ाइन किए गए तरीके से काम करने में सक्षम होना चाहिए, अप्रत्याशित परिस्थितियों का सुरक्षित तरीके से जवाब देना चाहिए, और हानिकारक हेरफेर का प्रतिरोध करना चाहिए।

- **पारदर्शिता**: जब AI सिस्टम ऐसे निर्णय लेने में मदद करता है जिनका लोगों के जीवन पर भारी प्रभाव पड़ता है, तो यह महत्वपूर्ण है कि लोग समझें कि वे निर्णय कैसे लिए गए। उदाहरण के लिए, एक बैंक AI सिस्टम का उपयोग यह तय करने के लिए कर सकता है कि कोई व्यक्ति क्रेडिट योग्य है या नहीं।

- **गोपनीयता और सुरक्षा**: जैसे-जैसे AI अधिक व्यापक हो रहा है, गोपनीयता की रक्षा करना और व्यक्तिगत और व्यावसायिक जानकारी को सुरक्षित रखना और अधिक महत्वपूर्ण और जटिल हो रहा है। AI के साथ, गोपनीयता और डेटा सुरक्षा को नज़दीकी ध्यान देने की आवश्यकता है क्योंकि AI सिस्टम को सटीक और सूचित भविष्यवाणियां और निर्णय लेने के लिए डेटा तक पहुंच आवश्यक है।

- **जवाबदेही**: जो लोग AI सिस्टम डिज़ाइन और तैनात करते हैं, उन्हें यह सुनिश्चित करने के लिए जवाबदेह होना चाहिए कि उनके सिस्टम कैसे काम करते हैं। संगठनों को जवाबदेही मानदंड विकसित करने के लिए उद्योग मानकों का उपयोग करना चाहिए। ये मानदंड यह सुनिश्चित कर सकते हैं कि AI सिस्टम किसी भी निर्णय पर अंतिम अधिकार न रखें जो लोगों के जीवन को प्रभावित करता हो।

![फिल हब।](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.hi.png)

*चित्र स्रोत: [उत्तरदायी AI क्या है?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft के उत्तरदायी AI सिद्धांतों के बारे में अधिक जानने के लिए, [उत्तरदायी AI क्या है?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) पर जाएं।

#### सुरक्षा मेट्रिक्स

इस ट्यूटोरियल में, आप Azure AI Foundry के सुरक्षा मेट्रिक्स का उपयोग करके Fine-tuned Phi-3 मॉडल की सुरक्षा का मूल्यांकन करेंगे। ये मेट्रिक्स आपको यह आकलन करने में मदद करते हैं कि मॉडल हानिकारक सामग्री उत्पन्न करने की कितनी संभावना रखता है और वह जेलब्रेक हमलों के प्रति कितना संवेदनशील है। सुरक्षा मेट्रिक्स में शामिल हैं:

- **स्वयं को नुकसान पहुंचाने वाली सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में स्वयं को नुकसान पहुंचाने वाली सामग्री उत्पन्न करने की प्रवृत्ति है।
- **घृणास्पद और अन्यायपूर्ण सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में घृणास्पद या अन्यायपूर्ण सामग्री उत्पन्न करने की प्रवृत्ति है।
- **हिंसक सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में हिंसक सामग्री उत्पन्न करने की प्रवृत्ति है।
- **यौन सामग्री**: यह मूल्यांकन करता है कि क्या मॉडल में अनुचित यौन सामग्री उत्पन्न करने की प्रवृत्ति है।

इन पहलुओं का मूल्यांकन यह सुनिश्चित करता है कि AI मॉडल हानिकारक या आपत्तिजनक सामग्री उत्पन्न नहीं करता है और यह सामाजिक मूल्यों और नियामक मानकों के साथ संरेखित है।

![सुरक्षा के आधार पर मूल्यांकन करें।](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.hi.png)

### प्रदर्शन मूल्यांकन का परिचय

यह सुनिश्चित करने के लिए कि आपका AI मॉडल अपेक्षित प्रदर्शन कर रहा है, इसे प्रदर्शन मेट्रिक्स के खिलाफ मूल्यांकन करना महत्वपूर्ण है। Azure AI Foundry में, प्रदर्शन मूल्यांकन आपको यह जांचने की अनुमति देता है कि आपका मॉडल सटीक, प्रासंगिक, और सुसंगत प्रतिक्रियाएं उत्पन्न करने में कितना प्रभावी है।

![सुरक्षा मूल्यांकन।](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.hi.png)

*चित्र स्रोत: [जनरेटिव AI अनुप्रयोगों का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### प्रदर्शन मेट्रिक्स

इस ट्यूटोरियल में, आप Azure AI Foundry के प्रदर्शन मेट्रिक्स का उपयोग करके Fine-tuned Phi-3 / Phi-3.5 मॉडल का प्रदर्शन मूल्यांकन करेंगे। ये मेट्रिक्स आपको सटीक, प्रासंगिक, और सुसंगत प्रतिक्रियाएं उत्पन्न करने में मॉडल की प्रभावशीलता का आकलन करने में मदद करते हैं। प्रदर्शन मेट्रिक्स में शामिल हैं:

- **ग्राउंडेडनेस**: यह मूल्यांकन करता है कि उत्पन्न उत्तर इनपुट स्रोत से कितनी अच्छी तरह मेल खाते हैं।
- **प्रासंगिकता**: यह दिए गए प्रश्नों के प्रति उत्पन्न प्रतिक्रियाओं की उपयुक्तता का मूल्यांकन करता है।
- **सुसंगतता**: यह मूल्यांकन करता है कि उत्पन्न टेक्स्ट कितना स्वाभाविक रूप से पढ़ा जाता है और मानव जैसी भाषा के समान है।
- **प्रवाह**: यह उत्पन्न टेक्स्ट की भाषा दक्षता का मूल्यांकन करता है।
- **GPT समानता**: यह उत्पन्न प्रतिक्रिया को ग्राउंड ट्रुथ के साथ समानता के लिए तुलना करता है।
- **F1 स्कोर**: यह उत्पन्न प्रतिक्रिया और स्रोत डेटा के बीच साझा शब्दों के अनुपात की गणना करता है।

ये मेट्रिक्स आपको सटीक, प्रासंगिक, और सुसंगत प्रतिक्रियाएं उत्पन्न करने में मॉडल की प्रभावशीलता का मूल्यांकन करने में मदद करते हैं।

![प्रदर्शन के आधार पर मूल्यांकन करें।](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.hi.png) 

## **परिदृश्य 2: Azure AI Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन**

### शुरू करने से पहले

यह ट्यूटोरियल पिछले ब्लॉग पोस्ट्स का फॉलो-अप है, "[Fine-Tune और Custom Phi-3 मॉडल को Prompt Flow के साथ इंटीग्रेट करें: चरण-दर-चरण गाइड](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" और "[Azure AI Foundry में Prompt Flow के साथ Custom Phi-3 मॉडल को Fine-Tune और इंटीग्रेट करें](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)।" इन पोस्ट्स में, हमने Azure AI Foundry में Phi-3 / Phi-3.5 मॉडल को Fine-tune करने और इसे Prompt flow के साथ इंटीग्रेट करने की प्रक्रिया पर चर्चा की थी।

इस ट्यूटोरियल में, आप Azure AI Foundry में एक मूल्यांकनकर्ता के रूप में Azure OpenAI मॉडल को डिप्लॉय करेंगे और इसका उपयोग अपने Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए करेंगे।

इस ट्यूटोरियल को शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित पूर्व-आवश्यकताएं हैं, जैसा कि पिछले ट्यूटोरियल्स में वर्णित है:

1. Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए तैयार किया गया डेटा सेट।
1. Azure Machine Learning में Fine-tuned और डिप्लॉय किया गया Phi-3 / Phi-3.5 मॉडल।
1. Azure AI Foundry में आपके Fine-tuned Phi-3 / Phi-3.5 मॉडल के साथ इंटीग्रेटेड Prompt flow।

> [!NOTE]
> आप *test_data.jsonl* फ़ाइल का उपयोग करेंगे, जो कि पिछले ब्लॉग पोस्ट्स में डाउनलोड किए गए **ULTRACHAT_200k** डेटा सेट के डेटा फोल्डर में स्थित है, Fine-tuned Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए।

#### Azure AI Foundry में Prompt flow के साथ Custom Phi-3 / Phi-3.5 मॉडल को इंटीग्रेट करें (कोड-फर्स्ट अप्रोच)

> [!NOTE]
> यदि आपने "[Azure AI Foundry में Prompt Flow के साथ Custom Phi-3 मॉडल को Fine-Tune और इंटीग्रेट करें](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" में वर्णित लो-कोड अप्रोच का पालन किया है, तो आप इस अभ्यास को छोड़ सकते हैं और अगले पर जा सकते हैं।
> हालाँकि, यदि आपने "[Fine-Tune और Custom Phi-3 मॉडल को Prompt Flow के साथ इंटीग्रेट करें: चरण-दर-चरण गाइड](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" में वर्णित कोड-फर्स्ट अप्रोच का पालन किया है, तो Prompt flow से अपने मॉडल को कनेक्ट करने की प्रक्रिया थोड़ी अलग है। आप इस अभ्यास में इस प्रक्रिया को सीखेंगे।

आगे बढ़ने के लिए, आपको अपने Fine-tuned Phi-3 / Phi-3.5 मॉडल को Azure AI Foundry में Prompt flow के साथ इंटीग्रेट करना होगा।

#### Azure AI Foundry हब बनाएं

आपको प्रोजेक्ट बनाने से पहले एक हब बनाना होगा। हब एक रिसोर्स ग्रुप की तरह कार्य करता है, जिससे आप Azure AI Foundry के भीतर कई प्रोजेक्ट्स को व्यवस्थित और प्रबंधित कर सकते हैं।

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) पर साइन इन करें।

1. बाईं ओर के टैब से **All hubs** चुनें।

1. नेविगेशन मेनू से **+ New hub** चुनें।

    ![हब बनाएं।](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.hi.png)

1. निम्नलिखित कार्य करें:

    - **Hub name** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - अपना Azure **Subscription** चुनें।
    - उपयोग करने के लिए **Resource group** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - उपयोग करने के लिए **Location** चुनें।
    - उपयोग करने के लिए **Connect Azure AI Services** चुनें (यदि आवश्यक हो तो नया बनाएं)।
    - **Connect Azure AI Search** को **Skip connecting** पर सेट करें।
![Fill hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.hi.png)

1. **अगला** चुनें।

#### Azure AI Foundry प्रोजेक्ट बनाएं

1. बनाए गए हब में, बाईं ओर के टैब से **सभी प्रोजेक्ट्स** चुनें।

1. नेविगेशन मेनू से **+ नया प्रोजेक्ट** चुनें।

    ![नया प्रोजेक्ट चुनें।](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.hi.png)

1. **प्रोजेक्ट नाम** दर्ज करें। यह एक अद्वितीय मान होना चाहिए।

    ![प्रोजेक्ट बनाएं।](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.hi.png)

1. **प्रोजेक्ट बनाएं** चुनें।

#### कस्टम कनेक्शन जोड़ें फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल के लिए

अपने कस्टम Phi-3 / Phi-3.5 मॉडल को Prompt flow के साथ एकीकृत करने के लिए, आपको मॉडल के एंडपॉइंट और कुंजी को कस्टम कनेक्शन में सहेजना होगा। यह सेटअप Prompt flow में आपके कस्टम Phi-3 / Phi-3.5 मॉडल तक पहुंच सुनिश्चित करता है।

#### फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल के लिए API कुंजी और एंडपॉइंट URI सेट करें

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) पर जाएं।

1. बनाए गए Azure Machine Learning वर्कस्पेस पर नेविगेट करें।

1. बाईं ओर के टैब से **एंडपॉइंट्स** चुनें।

    ![एंडपॉइंट्स चुनें।](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.hi.png)

1. बनाए गए एंडपॉइंट को चुनें।

    ![बनाए गए एंडपॉइंट्स चुनें।](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.hi.png)

1. नेविगेशन मेनू से **कंज्यूम** चुनें।

1. अपना **REST एंडपॉइंट** और **प्राइमरी कुंजी** कॉपी करें।

    ![API कुंजी और एंडपॉइंट URI कॉपी करें।](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.hi.png)

#### कस्टम कनेक्शन जोड़ें

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) पर जाएं।

1. बनाए गए Azure AI Foundry प्रोजेक्ट पर नेविगेट करें।

1. बनाए गए प्रोजेक्ट में, बाईं ओर के टैब से **सेटिंग्स** चुनें।

1. **+ नया कनेक्शन** चुनें।

    ![नया कनेक्शन चुनें।](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.hi.png)

1. नेविगेशन मेनू से **कस्टम कुंजियां** चुनें।

    ![कस्टम कुंजियां चुनें।](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.hi.png)

1. निम्नलिखित कार्य करें:

    - **+ कुंजी-मूल्य जोड़े जोड़ें** चुनें।
    - कुंजी नाम के लिए, **एंडपॉइंट** दर्ज करें और Azure ML Studio से कॉपी किए गए एंडपॉइंट को मूल्य फ़ील्ड में पेस्ट करें।
    - **+ कुंजी-मूल्य जोड़े जोड़ें** फिर से चुनें।
    - कुंजी नाम के लिए, **कुंजी** दर्ज करें और Azure ML Studio से कॉपी की गई कुंजी को मूल्य फ़ील्ड में पेस्ट करें।
    - कुंजियां जोड़ने के बाद, **गुप्त है** चुनें ताकि कुंजी उजागर न हो।

    ![कनेक्शन जोड़ें।](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.hi.png)

1. **कनेक्शन जोड़ें** चुनें।

#### Prompt flow बनाएं

आपने Azure AI Foundry में एक कस्टम कनेक्शन जोड़ा है। अब, निम्नलिखित चरणों का उपयोग करके एक Prompt flow बनाएं। फिर, आप इस Prompt flow को कस्टम कनेक्शन से जोड़ेंगे ताकि Prompt flow में फाइन-ट्यून किए गए मॉडल का उपयोग कर सकें।

1. बनाए गए Azure AI Foundry प्रोजेक्ट पर नेविगेट करें।

1. बाईं ओर के टैब से **Prompt flow** चुनें।

1. नेविगेशन मेनू से **+ बनाएं** चुनें।

    ![Promptflow चुनें।](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.hi.png)

1. नेविगेशन मेनू से **चैट फ्लो** चुनें।

    ![चैट फ्लो चुनें।](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.hi.png)

1. उपयोग के लिए **फोल्डर नाम** दर्ज करें।

    ![चैट फ्लो चुनें।](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.hi.png)

1. **बनाएं** चुनें।

#### Prompt flow को अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करने के लिए सेट करें

आपको फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल को Prompt flow में एकीकृत करना होगा। हालांकि, मौजूदा Prompt flow इस उद्देश्य के लिए डिज़ाइन नहीं किया गया है। इसलिए, आपको कस्टम मॉडल के एकीकरण को सक्षम करने के लिए Prompt flow को फिर से डिज़ाइन करना होगा।

1. Prompt flow में, मौजूदा फ्लो को पुनर्निर्मित करने के लिए निम्नलिखित कार्य करें:

    - **रॉ फाइल मोड** चुनें।
    - *flow.dag.yml* फ़ाइल में सभी मौजूदा कोड हटा दें।
    - *flow.dag.yml* में निम्नलिखित कोड जोड़ें:

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **सहेजें** चुनें।

    ![रॉ फाइल मोड चुनें।](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.hi.png)

1. कस्टम Phi-3 / Phi-3.5 मॉडल को Prompt flow में उपयोग करने के लिए *integrate_with_promptflow.py* में निम्नलिखित कोड जोड़ें:

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flow कोड पेस्ट करें।](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.hi.png)

> [!NOTE]
> Azure AI Foundry में Prompt flow का उपयोग करने के बारे में अधिक विस्तृत जानकारी के लिए, आप [Azure AI Foundry में Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) देख सकते हैं।

1. अपने मॉडल के साथ चैट करने के लिए **चैट इनपुट**, **चैट आउटपुट** चुनें।

    ![इनपुट आउटपुट चुनें।](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.hi.png)

1. अब आप अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करने के लिए तैयार हैं। अगले अभ्यास में, आप सीखेंगे कि Prompt flow को शुरू कैसे करें और इसे अपने फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल के साथ चैट करने के लिए कैसे उपयोग करें।

> [!NOTE]
>
> पुनर्निर्मित फ्लो निम्नलिखित छवि जैसा दिखना चाहिए:
>
> ![फ्लो उदाहरण](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.hi.png)
>

#### Prompt flow शुरू करें

1. Prompt flow शुरू करने के लिए **कंप्यूट सत्र शुरू करें** चुनें।

    ![कंप्यूट सत्र शुरू करें।](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.hi.png)

1. पैरामीटर को नवीनीकृत करने के लिए **इनपुट को मान्य करें और पार्स करें** चुनें।

    ![इनपुट को मान्य करें।](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.hi.png)

1. कस्टम कनेक्शन के **कनेक्शन** के **मूल्य** का चयन करें जिसे आपने बनाया है। उदाहरण के लिए, *connection*।

    ![कनेक्शन।](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.hi.png)

#### अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट करें

1. **चैट** चुनें।

    ![चैट चुनें।](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.hi.png)

1. यहां परिणाम का एक उदाहरण है: अब आप अपने कस्टम Phi-3 / Phi-3.5 मॉडल के साथ चैट कर सकते हैं। यह अनुशंसा की जाती है कि आप फाइन-ट्यूनिंग के लिए उपयोग किए गए डेटा के आधार पर प्रश्न पूछें।

    ![Prompt flow के साथ चैट करें।](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.hi.png)

### Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए Azure OpenAI तैनात करें

Azure AI Foundry में Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करने के लिए, आपको Azure OpenAI मॉडल तैनात करना होगा। इस मॉडल का उपयोग Phi-3 / Phi-3.5 मॉडल के प्रदर्शन का मूल्यांकन करने के लिए किया जाएगा।

#### Azure OpenAI तैनात करें

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) में साइन इन करें।

1. बनाए गए Azure AI Foundry प्रोजेक्ट पर नेविगेट करें।

    ![प्रोजेक्ट चुनें।](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.hi.png)

1. बनाए गए प्रोजेक्ट में, बाईं ओर के टैब से **डिप्लॉयमेंट्स** चुनें।

1. नेविगेशन मेनू से **+ मॉडल तैनात करें** चुनें।

1. **मूल मॉडल तैनात करें** चुनें।

    ![डिप्लॉयमेंट्स चुनें।](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.hi.png)

1. वह Azure OpenAI मॉडल चुनें जिसे आप उपयोग करना चाहते हैं। उदाहरण के लिए, **gpt-4o**।

    ![आप जिस Azure OpenAI मॉडल का उपयोग करना चाहते हैं उसे चुनें।](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.hi.png)

1. **पुष्टि करें** चुनें।

### Azure AI Foundry के Prompt flow मूल्यांकन का उपयोग करके फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें

### एक नया मूल्यांकन शुरू करें

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) पर जाएं।

1. बनाए गए Azure AI Foundry प्रोजेक्ट पर नेविगेट करें।

    ![प्रोजेक्ट चुनें।](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.hi.png)

1. बनाए गए प्रोजेक्ट में, बाईं ओर के टैब से **मूल्यांकन** चुनें।

1. नेविगेशन मेनू से **+ नया मूल्यांकन** चुनें।
![मूल्यांकन चुनें।](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.hi.png)

1. **Prompt flow** मूल्यांकन चुनें।

   ![Prompt flow मूल्यांकन चुनें।](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.hi.png)

1. निम्नलिखित कार्य करें:

   - मूल्यांकन का नाम दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
   - कार्य प्रकार के रूप में **संदर्भ के बिना प्रश्न और उत्तर** चुनें। क्योंकि, इस ट्यूटोरियल में उपयोग किया गया **ULTRACHAT_200k** डेटा सेट संदर्भ शामिल नहीं करता है।
   - वह Prompt flow चुनें जिसे आप मूल्यांकन करना चाहते हैं।

   ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.hi.png)

1. **अगला** चुनें।

1. निम्नलिखित कार्य करें:

   - डेटा सेट अपलोड करने के लिए **Add your dataset** चुनें। उदाहरण के लिए, आप परीक्षण डेटा सेट फ़ाइल जैसे *test_data.json1* अपलोड कर सकते हैं, जो **ULTRACHAT_200k** डेटा सेट डाउनलोड करते समय शामिल होती है।
   - अपने डेटा सेट से मेल खाने वाले उपयुक्त **Dataset column** का चयन करें। उदाहरण के लिए, यदि आप **ULTRACHAT_200k** डेटा सेट का उपयोग कर रहे हैं, तो **${data.prompt}** को डेटा सेट कॉलम के रूप में चुनें।

   ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.hi.png)

1. **अगला** चुनें।

1. प्रदर्शन और गुणवत्ता मेट्रिक्स को कॉन्फ़िगर करने के लिए निम्नलिखित कार्य करें:

   - प्रदर्शन और गुणवत्ता मेट्रिक्स का चयन करें जिन्हें आप उपयोग करना चाहते हैं।
   - मूल्यांकन के लिए आपने जो Azure OpenAI मॉडल बनाया है, उसे चुनें। उदाहरण के लिए, **gpt-4o** चुनें।

   ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.hi.png)

1. जोखिम और सुरक्षा मेट्रिक्स को कॉन्फ़िगर करने के लिए निम्नलिखित कार्य करें:

   - जोखिम और सुरक्षा मेट्रिक्स का चयन करें जिन्हें आप उपयोग करना चाहते हैं।
   - उस डिफेक्ट रेट की गणना के लिए थ्रेशोल्ड चुनें जिसे आप उपयोग करना चाहते हैं। उदाहरण के लिए, **मध्यम** चुनें।
   - **प्रश्न** के लिए, **Data source** को **{$data.prompt}** पर सेट करें।
   - **उत्तर** के लिए, **Data source** को **{$run.outputs.answer}** पर सेट करें।
   - **ground_truth** के लिए, **Data source** को **{$data.message}** पर सेट करें।

   ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.hi.png)

1. **अगला** चुनें।

1. मूल्यांकन शुरू करने के लिए **Submit** चुनें।

1. मूल्यांकन पूरा होने में कुछ समय लगेगा। आप **Evaluation** टैब में प्रगति की निगरानी कर सकते हैं।

### मूल्यांकन परिणामों की समीक्षा करें

> [!NOTE]  
> नीचे प्रस्तुत परिणाम मूल्यांकन प्रक्रिया को दर्शाने के लिए हैं। इस ट्यूटोरियल में, हमने अपेक्षाकृत छोटे डेटा सेट पर फाइन-ट्यून किए गए मॉडल का उपयोग किया है, जिससे परिणाम अनुकूल न हो सकते हैं। वास्तविक परिणाम डेटा सेट के आकार, गुणवत्ता और विविधता के साथ-साथ मॉडल के विशिष्ट कॉन्फ़िगरेशन के आधार पर भिन्न हो सकते हैं।

मूल्यांकन पूरा होने के बाद, आप प्रदर्शन और सुरक्षा मेट्रिक्स दोनों के लिए परिणामों की समीक्षा कर सकते हैं।

1. प्रदर्शन और गुणवत्ता मेट्रिक्स:

   - मॉडल की प्रभावशीलता का मूल्यांकन करें कि यह सुसंगत, प्रवाहपूर्ण, और प्रासंगिक उत्तर उत्पन्न करने में कितना सक्षम है।

   ![मूल्यांकन परिणाम।](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.hi.png)

1. जोखिम और सुरक्षा मेट्रिक्स:

   - सुनिश्चित करें कि मॉडल के आउटपुट सुरक्षित हैं और जिम्मेदार AI सिद्धांतों के अनुरूप हैं, किसी भी हानिकारक या आपत्तिजनक सामग्री से बचते हुए।

   ![मूल्यांकन परिणाम।](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.hi.png)

1. आप **विस्तृत मेट्रिक्स परिणाम** देखने के लिए नीचे स्क्रॉल कर सकते हैं।

   ![मूल्यांकन परिणाम।](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.hi.png)

1. अपने कस्टम Phi-3 / Phi-3.5 मॉडल का प्रदर्शन और सुरक्षा मेट्रिक्स के खिलाफ मूल्यांकन करके, आप यह सुनिश्चित कर सकते हैं कि मॉडल न केवल प्रभावी है, बल्कि जिम्मेदार AI प्रथाओं का पालन भी करता है, जिससे यह वास्तविक दुनिया में उपयोग के लिए तैयार है।

## बधाई हो!

### आपने यह ट्यूटोरियल पूरा कर लिया है

आपने Azure AI Foundry में Prompt flow के साथ एकीकृत फाइन-ट्यून किए गए Phi-3 मॉडल का सफलतापूर्वक मूल्यांकन किया है। यह सुनिश्चित करने के लिए एक महत्वपूर्ण कदम है कि आपके AI मॉडल न केवल अच्छा प्रदर्शन करते हैं, बल्कि Microsoft के जिम्मेदार AI सिद्धांतों का भी पालन करते हैं, जिससे आप भरोसेमंद और विश्वसनीय AI एप्लिकेशन बना सकें।

![आर्किटेक्चर।](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.hi.png)

## Azure संसाधनों को साफ करें

अपने खाते पर अतिरिक्त शुल्क से बचने के लिए अपने Azure संसाधनों को साफ करें। Azure पोर्टल पर जाएं और निम्नलिखित संसाधनों को हटाएं:

- Azure Machine Learning संसाधन।
- Azure Machine Learning मॉडल एंडपॉइंट।
- Azure AI Foundry प्रोजेक्ट संसाधन।
- Azure AI Foundry Prompt flow संसाधन।

### अगले चरण

#### दस्तावेज़ीकरण

- [जिम्मेदार AI डैशबोर्ड का उपयोग करके AI सिस्टम का आकलन करें](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)  
- [जनरेटिव AI के लिए मूल्यांकन और निगरानी मेट्रिक्स](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)  
- [Azure AI Foundry दस्तावेज़ीकरण](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)  
- [Prompt flow दस्तावेज़ीकरण](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)  

#### प्रशिक्षण सामग्री

- [Microsoft के जिम्मेदार AI दृष्टिकोण का परिचय](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)  
- [Azure AI Foundry का परिचय](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)  

### संदर्भ

- [जिम्मेदार AI क्या है?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)  
- [Azure AI में सुरक्षित और भरोसेमंद जनरेटिव AI एप्लिकेशन बनाने के लिए नए टूल की घोषणा](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)  
- [जनरेटिव AI एप्लिकेशन का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)  

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।