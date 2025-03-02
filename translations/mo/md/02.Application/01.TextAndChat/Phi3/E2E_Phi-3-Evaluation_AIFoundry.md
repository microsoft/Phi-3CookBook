# သက်ဆိုင်ရာ Microsoft ရဲ့ တာဝန်ရှိသော AI မူဝါဒများအပေါ်အခြေခံပြီး Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ပါ။

ဒီအဆုံးစွန် နမူနာ (E2E) ကို Microsoft Tech Community မှ "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" လမ်းညွှန်ချက်အပေါ် အခြေခံထားသည်။

## အကျဉ်းချုပ်

### Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်၏ လုံခြုံမှုနှင့် စွမ်းဆောင်ရည်ကို ဘယ်လို သုံးသပ်နိုင်မလဲ?

မော်ဒယ်တစ်ခုကို Fine-tune လုပ်ခြင်းက အတော်ကြီးမျှော်မှန်းမထားသော သို့မဟုတ် မလိုလားသော ပြန်ကြားချက်များကို ဖြစ်စေတတ်သည်။ မော်ဒယ်သည် လုံခြုံပြီး ထိရောက်မှုရှိနေသေးကြောင်း သေချာစေရန်အတွက်၊ ၎င်း၏ အန္တရာယ်ရှိစေမည့် အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုနှင့် တိကျမှု၊ သက်ဆိုင်မှုနှင့် သာမန် သဘာဝဖြစ်မှုတို့ကို သုံးသပ်ရန် လိုအပ်သည်။ ဒီသင်ခန်းစာမှာ Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို Azure AI Foundry တွင် Prompt flow နှင့် ပေါင်းစပ်ပြီး လုံခြုံမှုနှင့် စွမ်းဆောင်ရည်ကို ဘယ်လို သုံးသပ်ရမယ်ဆိုတာ သင်လေ့လာရမည်။

ဒါက Azure AI Foundry ရဲ့ သုံးသပ်မှုလုပ်ငန်းစဉ်ဖြစ်ပါတယ်။

![သင်ခန်းစာ၏ ဖွဲ့စည်းမှု](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.mo.png)

*ရုပ်ပုံရင်းမြစ်: [Generative AI အက်ပလီကေးရှင်းများ၏ သုံးသပ်မှု](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 အကြောင်း ပိုမိုအသေးစိတ် သိရှိလိုပါက [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) ကို ကြည့်ရှုပါ။

### လိုအပ်ချက်များ

- [Python](https://www.python.org/downloads)
- [Azure subscription](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်

### အကြောင်းအရာများ

1. [**အခန်း ၁: Azure AI Foundry ၏ Prompt flow သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [လုံခြုံမှု သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [စွမ်းဆောင်ရည် သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**အခန်း ၂: Azure AI Foundry တွင် Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ခြင်း**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [စတင်မတိုင်မှီ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ရန် Azure OpenAI ကို တင်သွင်းခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure AI Foundry ၏ Prompt flow သုံးသပ်မှုကို အသုံးပြု၍ Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ခြင်း](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [ဂုဏ်ယူပါတယ်!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **အခန်း ၁: Azure AI Foundry ၏ Prompt flow သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း**

### လုံခြုံမှု သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း

သင့် AI မော်ဒယ်သည် တာဝန်ရှိသော AI မူဝါဒများနှင့် ကိုက်ညီနေကြောင်း သေချာစေရန် Microsoft ရဲ့ Responsible AI Principles အတိုင်း သုံးသပ်ရမည်။ Azure AI Foundry တွင် လုံခြုံမှု သုံးသပ်မှုများက မော်ဒယ်၏ jailbreak တိုက်ခိုက်မှုများအပေါ် အခွင့်ထိခိုက်မှုနှင့် အန္တရာယ်ရှိစေမည့် အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုကို သုံးသပ်ရန် ခွင့်ပြုသည်။

![လုံခြုံမှု သုံးသပ်မှု](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.mo.png)

*ရုပ်ပုံရင်းမြစ်: [Generative AI အက်ပလီကေးရှင်းများ၏ သုံးသပ်မှု](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft ၏ တာဝန်ရှိသော AI မူဝါဒများ

နည်းပညာဆိုင်ရာ အဆင့်ဆင့်စတင်မတိုင်မှီ Microsoft ၏ တာဝန်ရှိသော AI မူဝါဒများကို နားလည်ထားရမည်။ ၎င်းသည် AI စနစ်များကို တာဝန်ရှိစွာ ဖန်တီး၊ တင်သွင်းနှင့် လည်ပတ်စေခြင်းအတွက် လမ်းညွှန်သော ကျင့်ဝတ်စည်းမျဉ်းများဖြစ်သည်။ AI နည်းပညာများကို တရားမျှတမှု၊ ဖြင့်ဖြိုးမှုနှင့် ထင်ရှားမှုရှိစေရန် ၎င်းတို့ကို သေချာစေရန် ၎င်းတို့ကို လမ်းညွှန်သည်။

Microsoft ၏ တာဝန်ရှိသော AI မူဝါဒများတွင် ပါဝင်သည်-

- **တရားမျှတမှုနှင့် ဖွံ့ဖြိုးမှု**: AI စနစ်များသည် လူတိုင်းကို တရားမျှတစွာ ဆက်ဆံရမည်။ ဥပမာအားဖြင့် ဆေးဘက်ဆိုင်ရာ အကြံဉာဏ်၊ ချေးငွေ လျှောက်လွှာများ သို့မဟုတ် အလုပ်အကိုင် အကြံပြုချက်များပေးသော AI စနစ်များသည် တူညီသော ရောဂါလက္ခဏာများ၊ ဘဏ္ဍာရေးအခြေအနေများ သို့မဟုတ် ပညာအရည်အချင်းများရှိသော လူတိုင်းကို တူညီသော အကြံပြုချက်များ ပေးရမည်။

- **ယုံကြည်မှုနှင့် လုံခြုံမှု**: ယုံကြည်မှုတည်ဆောက်ရန် AI စနစ်များသည် ယုံကြည်စိတ်ချရပြီး လုံခြုံမှုရှိရမည်။

- **ထင်ရှားမှု**: AI စနစ်များသည် လူသားများအပေါ် အရေးကြီးသော ဆုံးဖြတ်ချက်များကို အခြေခံသောအခါ၊ ၎င်းဆုံးဖြတ်ချက်များ၏ ဘယ်လိုဖြစ်ပေါ်လာသည်ကို လူသားများ နားလည်နိုင်ရမည်။

- **ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံမှု**: AI စနစ်များသည် သီးသန့်အချက်အလက်များနှင့် စီးပွားရေးအချက်အလက်များကို ထိရောက်စွာ ကာကွယ်ရမည်။

- **တာဝန်ယူမှု**: AI စနစ်များကို ဒီဇိုင်းဆွဲသူများနှင့် တင်သွင်းသူများသည် ၎င်းတို့၏ လုပ်ဆောင်မှုအပေါ် တာဝန်ရှိရမည်။

![Fill hub](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.mo.png)

*ရုပ်ပုံရင်းမြစ်: [Responsible AI ဆိုတာဘာလဲ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft ၏ တာဝန်ရှိသော AI မူဝါဒများအကြောင်း ပိုမိုသိရှိလိုပါက [Responsible AI ဆိုတာဘာလဲ?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) ကို ကြည့်ရှုပါ။

#### လုံခြုံမှု အတိုင်းအတာများ

ဒီသင်ခန်းစာမှာ Fine-tuned Phi-3 မော်ဒယ်ကို Azure AI Foundry ၏ လုံခြုံမှု အတိုင်းအတာများကို အသုံးပြု၍ သုံးသပ်မည်။ ၎င်းအတိုင်းအတာများက မော်ဒယ်၏ အန္တရာယ်ရှိစေမည့် အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုနှင့် jailbreak တိုက်ခိုက်မှုများအပေါ် အခွင့်ထိခိုက်မှုကို တိုင်းတာရန် ကူညီသည်။ လုံခြုံမှု အတိုင်းအတာများတွင် ပါဝင်သည်-

- **ကိုယ့်ကိုယ်ကို ထိခိုက်စေမည့် အကြောင်းအရာများ**: မော်ဒယ်သည် ကိုယ့်ကိုယ်ကို ထိခိုက်စေမည့် အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုရှိမရှိ သုံးသပ်သည်။
- **မုန်းတီးမှုနှင့် မတရားမှုရှိသော အကြောင်းအရာများ**: မော်ဒယ်သည် မုန်းတီးမှု သို့မဟုတ် မတရားမှုရှိသော အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုရှိမရှိ သုံးသပ်သည်။
- **အကြမ်းဖက်မှုဆိုင်ရာ အကြောင်းအရာများ**: မော်ဒယ်သည် အကြမ်းဖက်မှုဆိုင်ရာ အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုရှိမရှိ သုံးသပ်သည်။
- **လိင်ပိုင်းဆိုင်ရာ အကြောင်းအရာများ**: မော်ဒယ်သည် သင့်တော်မဟုတ်သော လိင်ပိုင်းဆိုင်ရာ အကြောင်းအရာများ ထုတ်ပေးနိုင်မှုရှိမရှိ သုံးသပ်သည်။

ဒီအချက်များကို သုံးသပ်ခြင်းဖြင့် AI မော်ဒယ်သည် လူ့အသိုင်းအဝိုင်း၏ တန်ဖိုးများနှင့် စည်းမျဉ်းစည်းကမ်းများနှင့် ကိုက်ညီကြောင်း သေချာစေသည်။

![လုံခြုံမှုအပေါ် အခြေခံ၍ သုံးသပ်ခြင်း](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.mo.png)

### စွမ်းဆောင်ရည် သုံးသပ်မှုကိုမိတ်ဆက်ခြင်း

AI မော်ဒယ်သည် မျှော်မှန်းထားသည့်အတိုင်း စွမ်းဆောင်နိုင်ကြောင်း သေချာစေရန်၊ စွမ်းဆောင်ရည် အတိုင်းအတာများအပေါ် အခြေခံ၍ သုံးသပ်ရမည်။ Azure AI Foundry တွင် စွမ်းဆောင်ရည် သုံးသပ်မှုများက မော်ဒယ်၏ တိကျမှု၊ သက်ဆိုင်မှုနှင့် သဘာဝဖြစ်မှုတို့ကို တိုင်းတာရန် ခွင့်ပြုသည်။

![စွမ်းဆောင်ရည် သုံးသပ်မှု](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.mo.png)

*ရုပ်ပုံရင်းမြစ်: [Generative AI အက်ပလီကေးရှင်းများ၏ သုံးသပ်မှု](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### စွမ်းဆောင်ရည် အတိုင်းအတာများ

ဒီသင်ခန်းစာမှာ Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို Azure AI Foundry ၏ စွမ်းဆောင်ရည် အတိုင်းအတာများကို အသုံးပြု၍ သုံးသပ်မည်။ ၎င်းအတိုင်းအတာများက မော်ဒယ်၏ တိကျမှု၊ သက်ဆိုင်မှုနှင့် သဘာဝဖြစ်မှုတို့ကို တိုင်းတာရန် ကူညီသည်။ စွမ်းဆောင်ရည် အတိုင်းအတာများတွင် ပါဝင်သည်-

- **Groundedness**: ထုတ်ပေးသော အဖြေများသည် input ရင်းမြစ်မှ အချက်အလက်များနှင့် ကိုက်ညီမှုရှိကြောင်း တိုင်းတာသည်။
- **Relevance**: ထုတ်ပေးသော အဖြေများသည် ပေးသော မေးခွန်းများနှင့် သက်ဆိုင်မှုရှိကြောင်း သုံးသပ်သည်။
- **Coherence**: ထုတ်ပေးသော စာသားများသည် သဘာဝကျစွာ စီးဆင်းမှုရှိပြီး လူသားရေးသားချက်ကဲ့သို့ ဖြစ်ကြောင်း သုံးသပ်သည်။
- **Fluency**: ထုတ်ပေးသော စာသား၏ ဘာသာစကားကျွမ်းကျင်မှုကို သုံးသပ်သည်။
- **GPT Similarity**: ထုတ်ပေးသော အဖြေကို ground truth နှင့် နှိုင်းယှဉ်မှုကို တိုင်းတာသည်။
- **F1 Score**: ထုတ်ပေးသော အဖြေနှင့် ရင်းမြစ်ဒေတာအကြား မျှဝေသော စကားလုံးများ၏ အချိုးကိုတွက်ချက်သည်။

ဒီအတိုင်းအတာများက မော်ဒယ်၏ တိကျမှု၊ သက်ဆိုင်မှုနှင့် သဘာဝဖြစ်မှုတို့ကို သုံးသပ်ရန် ကူညီသည်။

![စွမ်းဆောင်ရည်အပေါ် အခြေခံ၍ သုံးသပ်ခြင်း](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.mo.png)
![Khul hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.mo.png)

1. **Agale** pe click karein.

#### Azure AI Foundry Project banayein

1. Apne banaye hue Hub mein, baaye taraf tab se **All projects** chunein.

1. Navigation menu se **+ New project** chunein.

    ![Naya project chunein.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.mo.png)

1. **Project name** daalein. Ye ek unique value honi chahiye.

    ![Project banayein.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.mo.png)

1. **Create a project** pe click karein.

#### Fine-tuned Phi-3 / Phi-3.5 model ke liye ek custom connection add karein

Apne custom Phi-3 / Phi-3.5 model ko Prompt flow ke sath integrate karne ke liye, model ka endpoint aur key ek custom connection mein save karna zaroori hai. Ye setup Prompt flow mein aapke custom Phi-3 / Phi-3.5 model tak access ensure karega.

#### Fine-tuned Phi-3 / Phi-3.5 model ka API key aur endpoint URI set karein

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) par jayein.

1. Apne banaye hue Azure Machine Learning workspace mein navigate karein.

1. Baaye taraf tab se **Endpoints** chunein.

    ![Endpoints chunein.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.mo.png)

1. Apne banaye hue endpoint ko chunein.

    ![Endpoint chunein.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.mo.png)

1. Navigation menu se **Consume** chunein.

1. Apne **REST endpoint** aur **Primary key** ko copy karein.

    ![API key aur endpoint URI copy karein.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.mo.png)

#### Custom Connection add karein

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) par jayein.

1. Apne banaye hue Azure AI Foundry project mein navigate karein.

1. Apne Project mein, baaye taraf tab se **Settings** chunein.

1. **+ New connection** chunein.

    ![Naya connection chunein.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.mo.png)

1. Navigation menu se **Custom keys** chunein.

    ![Custom keys chunein.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.mo.png)

1. Niche diye gaye tasks perform karein:

    - **+ Add key value pairs** chunein.
    - Key name ke liye **endpoint** daalein aur Azure ML Studio se copy kiya hua endpoint value field mein paste karein.
    - Phir se **+ Add key value pairs** chunein.
    - Key name ke liye **key** daalein aur Azure ML Studio se copy kiya hua key value field mein paste karein.
    - Keys add karne ke baad, **is secret** select karein taki key expose na ho.

    ![Connection add karein.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.mo.png)

1. **Add connection** chunein.

#### Prompt flow banayein

Aapne Azure AI Foundry mein ek custom connection add kiya hai. Ab, niche diye gaye steps ke zariye ek Prompt flow banayein. Iske baad, is Prompt flow ko custom connection ke sath connect karein taki fine-tuned model ko Prompt flow mein use kiya ja sake.

1. Apne banaye hue Azure AI Foundry project mein navigate karein.

1. Baaye taraf tab se **Prompt flow** chunein.

1. Navigation menu se **+ Create** chunein.

    ![Promptflow chunein.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.mo.png)

1. Navigation menu se **Chat flow** chunein.

    ![Chat flow chunein.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.mo.png)

1. Use karne ke liye **Folder name** daalein.

    ![Chat flow ka naam daalein.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.mo.png)

1. **Create** chunein.

#### Apne custom Phi-3 / Phi-3.5 model ke sath Prompt flow set karein

Aapko fine-tuned Phi-3 / Phi-3.5 model ko Prompt flow mein integrate karna hoga. Lekin, jo existing Prompt flow diya gaya hai, wo is purpose ke liye design nahi hai. Isliye, aapko Prompt flow ko redesign karna hoga taki custom model integrate ho sake.

1. Prompt flow mein, niche diye gaye tasks perform karein:

    - **Raw file mode** chunein.
    - *flow.dag.yml* file mein saara existing code delete karein.
    - *flow.dag.yml* file mein niche diya gaya code add karein:

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

    - **Save** chunein.

    ![Raw file mode chunein.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.mo.png)

1. *integrate_with_promptflow.py* file mein niche diya gaya code add karein taki custom Phi-3 / Phi-3.5 model ko Prompt flow mein use kiya ja sake:

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

    ![Prompt flow code paste karein.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.mo.png)

> [!NOTE]
> Prompt flow ka istemal karne ke liye aur zyada jaankari ke liye aap [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) ko refer kar sakte hain.

1. **Chat input**, **Chat output** chunein taki aap apne model ke sath chat kar saken.

    ![Input Output chunein.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.mo.png)

1. Ab aap apne custom Phi-3 / Phi-3.5 model ke sath chat karne ke liye tayar hain. Agle exercise mein, aap seekhenge ki Prompt flow kaise start karein aur apne fine-tuned Phi-3 / Phi-3.5 model ke sath kaise chat karein.

> [!NOTE]
>
> Rebuilt flow kuch is prakar dikhna chahiye:
>
> ![Flow example](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.mo.png)
>

#### Prompt flow shuru karein

1. **Start compute sessions** chunein taki Prompt flow shuru ho sake.

    ![Compute session shuru karein.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.mo.png)

1. **Validate and parse input** chunein taki parameters renew ho sakein.

    ![Input validate karein.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.mo.png)

1. **Connection** ka **Value** chunein jo custom connection ke liye banaya gaya tha. Jaise, *connection*.

    ![Connection chunein.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.mo.png)

#### Apne custom Phi-3 / Phi-3.5 model ke sath chat karein

1. **Chat** chunein.

    ![Chat chunein.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.mo.png)

1. Yahan ek example diya gaya hai: Ab aap apne custom Phi-3 / Phi-3.5 model ke sath chat kar sakte hain. Ye suggest kiya jata hai ki aap fine-tuning ke liye use kiye gaye data par based questions poochein.

    ![Prompt flow ke sath chat karein.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.mo.png)

### Phi-3 / Phi-3.5 model ko evaluate karne ke liye Azure OpenAI deploy karein

Azure AI Foundry mein Phi-3 / Phi-3.5 model ko evaluate karne ke liye, aapko ek Azure OpenAI model deploy karna hoga. Ye model Phi-3 / Phi-3.5 model ke performance ko evaluate karne ke liye use kiya jayega.

#### Azure OpenAI deploy karein

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) par sign in karein.

1. Apne banaye hue Azure AI Foundry project mein navigate karein.

    ![Project chunein.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.mo.png)

1. Apne Project mein, baaye taraf tab se **Deployments** chunein.

1. Navigation menu se **+ Deploy model** chunein.

1. **Deploy base model** chunein.

    ![Deployments chunein.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.mo.png)

1. Azure OpenAI model chunein jo aap use karna chahte hain. Jaise, **gpt-4o**.

    ![Azure OpenAI model chunein.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.mo.png)

1. **Confirm** chunein.

### Azure AI Foundry ke Prompt flow evaluation ka use karte hue fine-tuned Phi-3 / Phi-3.5 model evaluate karein

### Nayi evaluation shuru karein

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) par jayein.

1. Apne banaye hue Azure AI Foundry project mein navigate karein.

    ![Project chunein.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.mo.png)

1. Apne Project mein, baaye taraf tab se **Evaluation** chunein.

1. Navigation menu se **+ New evaluation** chunein.
![चयन मूल्यांकन।](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.mo.png)

1. **Prompt flow** मूल्यांकन का चयन करें।

    ![Prompt flow मूल्यांकन का चयन करें।](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.mo.png)

1. निम्नलिखित कार्य करें:

    - मूल्यांकन का नाम दर्ज करें। यह एक अद्वितीय मान होना चाहिए।
    - **सवाल और जवाब बिना संदर्भ के** कार्य प्रकार के रूप में चुनें। क्योंकि, इस ट्यूटोरियल में उपयोग किए गए **ULTRACHAT_200k** डेटासेट में संदर्भ नहीं है।
    - वह प्रॉम्प्ट फ्लो चुनें जिसे आप मूल्यांकन करना चाहते हैं।

    ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.mo.png)

1. **अगला** चुनें।

1. निम्नलिखित कार्य करें:

    - **अपना डेटासेट जोड़ें** चुनें और डेटासेट अपलोड करें। उदाहरण के लिए, आप परीक्षण डेटासेट फ़ाइल जैसे *test_data.json1* अपलोड कर सकते हैं, जो **ULTRACHAT_200k** डेटासेट डाउनलोड करने पर उपलब्ध होती है।
    - अपने डेटासेट से मेल खाने वाला **डेटासेट कॉलम** चुनें। उदाहरण के लिए, यदि आप **ULTRACHAT_200k** डेटासेट का उपयोग कर रहे हैं, तो **${data.prompt}** को डेटासेट कॉलम के रूप में चुनें।

    ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.mo.png)

1. **अगला** चुनें।

1. प्रदर्शन और गुणवत्ता मीट्रिक्स को कॉन्फ़िगर करने के लिए निम्नलिखित कार्य करें:

    - प्रदर्शन और गुणवत्ता मीट्रिक्स चुनें जिन्हें आप उपयोग करना चाहते हैं।
    - मूल्यांकन के लिए बनाए गए Azure OpenAI मॉडल का चयन करें। उदाहरण के लिए, **gpt-4o** चुनें।

    ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.mo.png)

1. जोखिम और सुरक्षा मीट्रिक्स को कॉन्फ़िगर करने के लिए निम्नलिखित कार्य करें:

    - जोखिम और सुरक्षा मीट्रिक्स चुनें जिन्हें आप उपयोग करना चाहते हैं।
    - डिफेक्ट दर की गणना के लिए थ्रेशोल्ड चुनें जिसे आप उपयोग करना चाहते हैं। उदाहरण के लिए, **मध्यम** चुनें।
    - **सवाल** के लिए, **डेटा स्रोत** को **{$data.prompt}** पर सेट करें।
    - **जवाब** के लिए, **डेटा स्रोत** को **{$run.outputs.answer}** पर सेट करें।
    - **ग्राउंड_ट्रुथ** के लिए, **डेटा स्रोत** को **{$data.message}** पर सेट करें।

    ![Prompt flow मूल्यांकन।](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.mo.png)

1. **अगला** चुनें।

1. मूल्यांकन शुरू करने के लिए **सबमिट** चुनें।

1. मूल्यांकन पूरा होने में कुछ समय लगेगा। आप प्रगति की निगरानी **मूल्यांकन** टैब में कर सकते हैं।

### मूल्यांकन परिणामों की समीक्षा करें

> [!NOTE]
> नीचे दिए गए परिणाम मूल्यांकन प्रक्रिया को समझाने के लिए प्रस्तुत किए गए हैं। इस ट्यूटोरियल में, एक अपेक्षाकृत छोटे डेटासेट पर फाइन-ट्यून किए गए मॉडल का उपयोग किया गया है, जो उप-इष्टतम परिणाम दे सकता है। वास्तविक परिणाम डेटासेट के आकार, गुणवत्ता और विविधता के साथ-साथ मॉडल की विशिष्ट कॉन्फ़िगरेशन पर निर्भर करते हुए भिन्न हो सकते हैं।

मूल्यांकन पूरा होने के बाद, आप प्रदर्शन और सुरक्षा मीट्रिक्स दोनों के लिए परिणामों की समीक्षा कर सकते हैं।

1. प्रदर्शन और गुणवत्ता मीट्रिक्स:

    - मॉडल की प्रभावशीलता का मूल्यांकन करें, जैसे कि कोहेरेंट, प्रवाहमय और प्रासंगिक प्रतिक्रियाएं उत्पन्न करना।

    ![मूल्यांकन परिणाम।](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.mo.png)

1. जोखिम और सुरक्षा मीट्रिक्स:

    - सुनिश्चित करें कि मॉडल के आउटपुट सुरक्षित हैं और जिम्मेदार AI सिद्धांतों के साथ मेल खाते हैं, जिससे किसी भी हानिकारक या आपत्तिजनक सामग्री से बचा जा सके।

    ![मूल्यांकन परिणाम।](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.mo.png)

1. **विस्तृत मीट्रिक्स परिणाम** देखने के लिए नीचे स्क्रॉल करें।

    ![मूल्यांकन परिणाम।](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.mo.png)

1. अपने कस्टम Phi-3 / Phi-3.5 मॉडल को प्रदर्शन और सुरक्षा मीट्रिक्स के खिलाफ मूल्यांकित करके, आप पुष्टि कर सकते हैं कि मॉडल न केवल प्रभावी है, बल्कि जिम्मेदार AI प्रथाओं का पालन भी करता है, जिससे यह वास्तविक दुनिया के उपयोग के लिए तैयार हो जाता है।

## बधाई हो!

### आपने यह ट्यूटोरियल पूरा कर लिया है

आपने Prompt flow के साथ एकीकृत फाइन-ट्यून किए गए Phi-3 मॉडल का सफलतापूर्वक मूल्यांकन किया है। यह सुनिश्चित करने का एक महत्वपूर्ण कदम है कि आपके AI मॉडल न केवल अच्छा प्रदर्शन करते हैं, बल्कि Microsoft के जिम्मेदार AI सिद्धांतों का भी पालन करते हैं, ताकि आप भरोसेमंद और विश्वसनीय AI एप्लिकेशन बना सकें।

![आर्किटेक्चर।](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.mo.png)

## Azure संसाधनों को साफ करें

अपने Azure खाते में अतिरिक्त शुल्क से बचने के लिए अपने Azure संसाधनों को साफ करें। Azure पोर्टल पर जाएं और निम्नलिखित संसाधनों को हटाएं:

- Azure मशीन लर्निंग संसाधन।
- Azure मशीन लर्निंग मॉडल एंडपॉइंट।
- Azure AI Foundry प्रोजेक्ट संसाधन।
- Azure AI Foundry Prompt flow संसाधन।

### अगले चरण

#### प्रलेखन

- [जिम्मेदार AI डैशबोर्ड का उपयोग करके AI सिस्टम का मूल्यांकन करें](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [जनरेटिव AI के लिए मूल्यांकन और निगरानी मीट्रिक्स](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry प्रलेखन](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow प्रलेखन](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### प्रशिक्षण सामग्री

- [Microsoft के जिम्मेदार AI दृष्टिकोण का परिचय](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry का परिचय](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### संदर्भ

- [जिम्मेदार AI क्या है?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Azure AI में नए उपकरणों की घोषणा जो अधिक सुरक्षित और भरोसेमंद जनरेटिव AI एप्लिकेशन बनाने में मदद करते हैं](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [जनरेटिव AI एप्लिकेशन का मूल्यांकन](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

It seems like "mo" might refer to a specific language or abbreviation, but it's unclear which one you're referring to. Could you clarify what "mo" stands for? For example, is it Maori, Mongolian, or something else?