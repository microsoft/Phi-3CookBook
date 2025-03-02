# **ဆယ်ကျော်သက်များအတွက် Visual Studio Code GitHub Copilot Chat ကို Microsoft Phi-3 မျိုးဆက်နှင့်အတူ တည်ဆောက်ပါ**

GitHub Copilot Chat တွင် workspace agent ကိုအသုံးပြုဖူးပါသလား။ သင့်အဖွဲ့အစည်းအတွက် ကိုယ်ပိုင် code agent တစ်ခု တည်ဆောက်လိုပါသလား။ ဒီလက်တွေ့လေ့လာမှုမှာ ဖွင့်လှစ်မော်ဒယ်နှင့် ပေါင်းစပ်ပြီး လုပ်ငန်းအဆင့် code အကျိုးပြု agent တစ်ခု တည်ဆောက်ရန် ရည်ရွယ်ထားသည်။

## **အခြေခံအချက်များ**

### **Microsoft Phi-3 ကို ရွေးချယ်ရသည့် အကြောင်း**

Phi-3 သည် မျိုးဆက်တစ်ခုဖြစ်ပြီး, phi-3-mini, phi-3-small, နှင့် phi-3-medium အပါအဝင် စာသားထုတ်လုပ်ခြင်း၊ စကားပြောဖြည့်စွက်ခြင်း၊ နှင့် ကုဒ်ထုတ်လုပ်ခြင်းအတွက် ကွဲပြားသော သင်ကြားမှု parameters များအပေါ်မူတည်သည်။ Vision အပေါ်မူတည်သော phi-3-vision လည်း ပါဝင်သည်။ ၎င်းသည် လုပ်ငန်းများ သို့မဟုတ် အဖွဲ့အစည်းအမျိုးမျိုးအတွက် အော့ဖ်လိုင်း AI ဖြေရှင်းချက်များ ဖန်တီးရန် သင့်တော်သည်။

ဤလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုပါ [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat extension သည် chat interface တစ်ခုကို ပံ့ပိုးပေးပြီး, သင့်အား GitHub Copilot နှင့် ဆက်သွယ်ရန်နှင့် coding ဆိုင်ရာမေးခွန်းများအတွက် ဖြေကြားချက်များကို VS Code အတွင်းမှ တိုက်ရိုက် ရရှိစေသည်။ ဒါကြောင့် documentation သို့မဟုတ် အွန်လိုင်းဖိုရမ်များတွင် ရှာဖွေရန် မလိုအပ်တော့ပါ။

Copilot Chat သည် syntax highlighting, indentation, နှင့် အခြား formatting အင်္ဂါရပ်များကို အသုံးပြု၍ ထုတ်လုပ်သော ဖြေကြားချက်ကို ပိုမိုရှင်းလင်းစေပါသည်။ အသုံးပြုသူ၏ မေးခွန်းအမျိုးအစားအပေါ်မူတည်ပြီး, ဖြေကြားချက်တွင် Copilot သုံးစွဲထားသည့် context များကို ရှင်းလင်းစေသည့် links, source code files, သို့မဟုတ် documentation တို့ ပါဝင်နိုင်ပါသည်။ 

- Copilot Chat သည် သင့် developer flow အတွင်း ပေါင်းစည်းထားပြီး, သင့်လိုအပ်သောနေရာတွင် ကူညီပေးသည်:

- Editor သို့မဟုတ် terminal မှ တိုက်ရိုက် inline chat စတင်၍ ကုဒ်ရေးစဉ် ကူညီမှုရယူပါ

- Chat view ကို အသုံးပြု၍ အချိန်မရွေး AI assistant ကို ရရှိပါ

- Quick Chat ကို ဖွင့်ပြီး, မေးခွန်းတစ်ခုကို အမြန်မေးပြီး, သင့်လုပ်ဆောင်မှုကို ပြန်လည်ဆက်လက်လုပ်ဆောင်ပါ

GitHub Copilot Chat ကို အမျိုးမျိုးသောအခြေအနေများတွင် အသုံးပြုနိုင်သည်, ဥပမာ-

- ပြဿနာကို အကောင်းဆုံးဖြေရှင်းရန် coding မေးခွန်းများကို ဖြေကြားခြင်း

- အခြားသူ၏ကုဒ်ကို ရှင်းပြပြီး တိုးတက်မှုများကို အကြံပြုခြင်း

- ကုဒ်ပြုပြင်မှုများကို အကြံပြုခြင်း

- Unit test cases များကို ထုတ်လုပ်ခြင်း

- ကုဒ် documentation များကို ထုတ်လုပ်ခြင်း

ဤလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုပါ [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


### **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat တွင် **@workspace** ကို ကိုးကားခြင်းဖြင့်, သင့်ကုဒ်အကျွမ်းထဲမှ မေးခွန်းများမေးနိုင်သည်။ မေးခွန်းအပေါ်မူတည်၍, Copilot သည် သက်ဆိုင်ရာ ဖိုင်များနှင့် symbols များကို ထုတ်ယူပြီး, ၎င်း၏ ဖြေကြားချက်တွင် links နှင့် code examples အဖြစ် ကိုးကားပေးပါသည်။

**@workspace** သည် developer တစ်ဦး VS Code တွင် codebase ကို သွားလည်စဉ် အသုံးပြုမည့် အရင်းအမြစ်များကို ရှာဖွေပြီး သင့်မေးခွန်းကို ဖြေကြားသည်-

- Workspace အတွင်းရှိ ဖိုင်အားလုံး, .gitignore ဖိုင်မှ မလွဲချော်ဘဲ

- Directory structure နှင့် folder နှင့် file names များ

- GitHub ၏ code search index, workspace သည် GitHub repository ဖြစ်ပြီး code search ဖြင့် indexed လုပ်ထားပါက

- Workspace အတွင်း symbols နှင့် definitions

- လက်ရှိရွေးချယ်ထားသောစာသား သို့မဟုတ် active editor အတွင်း မြင်နိုင်သောစာသား

မှတ်ချက်- .gitignore ကို သင့်တွင် ဖိုင်တစ်ခုဖွင့်ထားသည် သို့မဟုတ် .gitignore ဖိုင်တွင်း စာသားရွေးထားပါက, ၎င်းကို ကျော်ဖြတ်နိုင်သည်။

ဤလင့်ခ်ကို ဖတ်ရှုရန် အကြံပြုပါ [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **ဤ Lab အကြောင်းပိုမိုလေ့လာပါ**

GitHub Copilot သည် လုပ်ငန်းများ၏ programming ထိရောက်မှုကို အလွန်တိုးတက်စေပြီး, လုပ်ငန်းတိုင်းသည် GitHub Copilot ၏ဆက်စပ်လုပ်ဆောင်ချက်များကို customize လုပ်ရန် လိုလားကြသည်။ လုပ်ငန်းအများစုသည်, ၎င်းတို့၏ လုပ်ငန်းလိုအပ်ချက်များနှင့် ဖွင့်လှစ်မော်ဒယ်များအပေါ်မူတည်၍ GitHub Copilot နှင့်ဆင်တူသော Extensions များကို customize လုပ်ထားကြသည်။ 

လုပ်ငန်းများအတွက်, customize လုပ်ထားသော Extensions များသည် ထိန်းချုပ်ရန် ပိုမိုလွယ်ကူသော်လည်း, ၎င်းသည် အသုံးပြုသူအတွေ့အကြုံကို ထိခိုက်စေနိုင်သည်။ သို့သော်, GitHub Copilot သည် အထွေထွေလုပ်ငန်းများနှင့် ကျွမ်းကျင်မှုဆိုင်ရာတွင် ပိုမိုအားကောင်းသည်။ အတွေ့အကြုံကို တစ်ခုတည်းထိန်းသိမ်းနိုင်ပြီး, လုပ်ငန်းအတွက် customize လုပ်ထားသော Extension များကို အသုံးပြုနိုင်မည်ဆိုပါက, ပိုမိုကောင်းမွန်သော အသုံးပြုသူအတွေ့အကြုံ ဖြစ်နိုင်သည်။

ဤ lab သည် Phi-3 မော်ဒယ်ကို အသုံးပြု၍, local NPU နှင့် Azure hybrid တို့ကို ပေါင်းစပ်ကာ GitHub Copilot Chat တွင် ***@PHI3*** ကို အသုံးပြု၍, enterprise developers များကို code generation ***(@PHI3 /gen)*** နှင့် ပုံများပေါ်မူတည်၍ code ထုတ်လုပ်မှု ***(@PHI3 /img)*** ကို ပြီးစီးရန် ကူညီပေးရန် ရည်ရွယ်ထားသည်။

![PHI3](../../../../../../../translated_images/cover.410a18b85555fad4ca8bfb8f0b1776a96ae7f8eae1132b8f0c09d4b92b8e3365.mo.png)

### ***မှတ်ချက်:*** 

ဤ lab ကို လက်ရှိတွင် Intel CPU ၏ AIPC နှင့် Apple Silicon တွင် အကောင်အထည်ဖော်ထားပါသည်။ Qualcomm NPU ဗားရှင်းကို ဆက်လက်အပ်ဒိတ်လုပ်မည်ဖြစ်သည်။


## **Lab**


| အမည် | ဖော်ပြချက် | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | သက်ဆိုင်ရာ ပတ်ဝန်းကျင်များနှင့် installation tools များကို configure နှင့် install လုပ်ပါ | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | AIPC / Apple Silicon နှင့်ပေါင်းစပ်ပြီး, Phi-3-mini ကို အသုံးပြုကာ local NPU ဖြင့် code ထုတ်လုပ်ပါ | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | Azure Machine Learning Service ၏ Model Catalog - Phi-3-vision image ကို deploy လုပ်ကာ code ထုတ်လုပ်ပါ | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | GitHub Copilot Chat တွင် custom Phi-3 agent တစ်ခု ဖန်တီးပြီး, code generation, graph generation code, RAG, စသည်တို့ကို ပြီးစီးပါ | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| နမူနာကုဒ် (✅)  | နမူနာကုဒ်ကို ဒေါင်းလုပ်လုပ်ပါ | [Go](../../../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../../../code/07.Lab/01/Apple) |


## **ရင်းမြစ်များ**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot အကြောင်းပိုမိုလေ့လာပါ [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat အကြောင်းပိုမိုလေ့လာပါ [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API အကြောင်းပိုမိုလေ့လာပါ [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Foundry အကြောင်းပိုမိုလေ့လာပါ [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Foundry ၏ Model Catalog အကြောင်းပိုမိုလေ့လာပါ [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

It seems like you are requesting a translation into "mo." Could you clarify what "mo" refers to? For example, is it short for a specific language, such as Maori, Mongolian, or something else? Let me know, and I'd be happy to assist!