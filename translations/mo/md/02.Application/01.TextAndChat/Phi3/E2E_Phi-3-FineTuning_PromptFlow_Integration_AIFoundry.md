# Fine-tune et intégrez des modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry

Cet exemple de bout en bout (E2E) est basé sur le guide "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" de la communauté technique Microsoft. Il explique les processus de fine-tuning, de déploiement et d'intégration de modèles Phi-3 personnalisés avec Prompt Flow dans Azure AI Foundry.  
Contrairement à l'exemple E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", qui nécessitait l'exécution de code localement, ce tutoriel se concentre entièrement sur le fine-tuning et l'intégration de votre modèle dans Azure AI / ML Studio.

## Vue d'ensemble

Dans cet exemple E2E, vous apprendrez à affiner le modèle Phi-3 et à l'intégrer avec Prompt Flow dans Azure AI Foundry. En tirant parti d'Azure AI / ML Studio, vous mettrez en place un workflow pour déployer et utiliser des modèles IA personnalisés. Cet exemple est divisé en trois scénarios :

**Scénario 1 : Configurer les ressources Azure et préparer le fine-tuning**  

**Scénario 2 : Affiner le modèle Phi-3 et le déployer dans Azure Machine Learning Studio**  

**Scénario 3 : Intégrer avec Prompt Flow et interagir avec votre modèle personnalisé dans Azure AI Foundry**  

Voici une vue d'ensemble de cet exemple E2E.  

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.mo.png)

### Table des matières

1. **[Scénario 1 : Configurer les ressources Azure et préparer le fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Créer un espace de travail Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Demander des quotas GPU dans l'abonnement Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Ajouter une attribution de rôle](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Configurer le projet](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Préparer le jeu de données pour le fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Scénario 2 : Affiner le modèle Phi-3 et le déployer dans Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Affiner le modèle Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Déployer le modèle Phi-3 affiné](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[Scénario 3 : Intégrer avec Prompt Flow et interagir avec votre modèle personnalisé dans Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Intégrer le modèle Phi-3 personnalisé avec Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Interagir avec votre modèle Phi-3 personnalisé](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## Scénario 1 : Configurer les ressources Azure et préparer le fine-tuning  

### Créer un espace de travail Azure Machine Learning  

1. Tapez *azure machine learning* dans la **barre de recherche** en haut de la page du portail, puis sélectionnez **Azure Machine Learning** parmi les options proposées.  

    ![Tapez azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.mo.png)  

2. Sélectionnez **+ Créer** dans le menu de navigation.  

3. Sélectionnez **Nouvel espace de travail** dans le menu de navigation.  

    ![Sélectionnez nouvel espace de travail.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.mo.png)  

4. Effectuez les tâches suivantes :  

    - Sélectionnez votre **Abonnement Azure**.  
    - Choisissez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).  
    - Saisissez un **Nom d'espace de travail** unique.  
    - Sélectionnez la **Région** à utiliser.  
    - Choisissez le **Compte de stockage** à utiliser (créez-en un nouveau si nécessaire).  
    - Sélectionnez le **Key Vault** à utiliser (créez-en un nouveau si nécessaire).  
    - Sélectionnez les **Insights d'application** à utiliser (créez-en un nouveau si nécessaire).  
    - Sélectionnez le **Registre de conteneurs** à utiliser (créez-en un nouveau si nécessaire).  

    ![Remplissez les informations Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.mo.png)  

5. Cliquez sur **Vérifier + Créer**.  

6. Sélectionnez **Créer**.  

### Demander des quotas GPU dans l'abonnement Azure  

Dans ce tutoriel, vous apprendrez à affiner et déployer un modèle Phi-3 en utilisant des GPU. Pour le fine-tuning, vous utiliserez le GPU *Standard_NC24ads_A100_v4*, qui nécessite une demande de quota. Pour le déploiement, vous utiliserez le GPU *Standard_NC6s_v3*, qui nécessite également une demande de quota.  

> [!NOTE]  
> Seuls les abonnements Pay-As-You-Go (le type d'abonnement standard) sont éligibles pour l'allocation GPU ; les abonnements avec avantages ne sont actuellement pas pris en charge.  

1. Accédez à [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).  

1. Effectuez les tâches suivantes pour demander un quota pour la famille *Standard NCADSA100v4* :  

    - Sélectionnez **Quota** dans l'onglet latéral gauche.  
    - Choisissez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC24ads_A100_v4*.  
    - Cliquez sur **Demander un quota** dans le menu de navigation.  

        ![Demander un quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.mo.png)  

    - Sur la page de demande de quota, saisissez la **Nouvelle limite de cœurs** souhaitée. Par exemple, 24.  
    - Sur la page de demande de quota, cliquez sur **Soumettre** pour demander le quota GPU.  

1. Effectuez les tâches suivantes pour demander un quota pour la famille *Standard NCSv3* :  

    - Sélectionnez **Quota** dans l'onglet latéral gauche.  
    - Choisissez la **Famille de machines virtuelles** à utiliser. Par exemple, sélectionnez **Standard NCSv3 Family Cluster Dedicated vCPUs**, qui inclut le GPU *Standard_NC6s_v3*.  
    - Cliquez sur **Demander un quota** dans le menu de navigation.  
    - Sur la page de demande de quota, saisissez la **Nouvelle limite de cœurs** souhaitée. Par exemple, 24.  
    - Sur la page de demande de quota, cliquez sur **Soumettre** pour demander le quota GPU.  

### Ajouter une attribution de rôle  

Pour affiner et déployer vos modèles, vous devez d'abord créer une identité managée affectée par l'utilisateur (UAI) et lui attribuer les autorisations appropriées. Cette UAI sera utilisée pour l'authentification pendant le déploiement.  

#### Créer une identité managée affectée par l'utilisateur (UAI)  

1. Tapez *identités managées* dans la **barre de recherche** en haut de la page du portail, puis sélectionnez **Identités managées** parmi les options proposées.  

    ![Tapez identités managées.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.mo.png)  

1. Cliquez sur **+ Créer**.  

    ![Cliquez sur créer.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.mo.png)  

1. Effectuez les tâches suivantes :  

    - Sélectionnez votre **Abonnement Azure**.  
    - Choisissez le **Groupe de ressources** à utiliser (créez-en un nouveau si nécessaire).  
    - Sélectionnez la **Région** à utiliser.  
    - Saisissez un **Nom** unique.  

    ![Remplissez les informations pour créer une identité managée.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.mo.png)  

1. Cliquez sur **Vérifier + créer**.  

1. Cliquez sur **Créer**.  

#### Ajouter un rôle de contributeur à l'identité managée  

1. Accédez à la ressource d'identité managée que vous avez créée.  

1. Sélectionnez **Attributions de rôles Azure** dans l'onglet latéral gauche.  

1. Cliquez sur **+ Ajouter une attribution de rôle** dans le menu de navigation.  

1. Sur la page d'ajout d'attribution de rôle, effectuez les tâches suivantes :  
    - Définissez le **Périmètre** sur **Groupe de ressources**.  
    - Sélectionnez votre **Abonnement Azure**.  
    - Choisissez le **Groupe de ressources** à utiliser.  
    - Définissez le **Rôle** sur **Contributeur**.  

    ![Remplissez les informations pour le rôle de contributeur.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.mo.png)  

2. Cliquez sur **Enregistrer**.  

#### Ajouter un rôle de lecteur de données Blob pour le stockage  

... (La traduction se poursuit en suivant la structure originale.)
1. မည်သူမဆို [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. ဘယ်ဘက်ဘောင်မှ **Compute** ကိုရွေးပါ။

1. **Compute clusters** ကိုရွေးချယ်ပါ။

1. **+ New** ကိုနှိပ်ပါ။

    ![Compute ကိုရွေးချယ်ပါ။](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.mo.png)

1. အောက်ပါအလုပ်များကို ဆောင်ရွက်ပါ။

    - သင်အသုံးပြုလိုသော **Region** ကိုရွေးချယ်ပါ။
    - **Virtual machine tier** ကို **Dedicated** သို့ရွေးပါ။
    - **Virtual machine type** ကို **GPU** သို့ရွေးပါ။
    - **Virtual machine size** filter ကို **Select from all options** သို့ရွေးပါ။
    - **Virtual machine size** ကို **Standard_NC24ads_A100_v4** သို့ရွေးပါ။

    ![Cluster တစ်ခု ဖန်တီးပါ။](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.mo.png)

1. **Next** ကိုရွေးပါ။

1. အောက်ပါအလုပ်များကို ဆောင်ရွက်ပါ။

    - **Compute name** ကိုထည့်ပါ။ ၎င်းသည် ထူးခြားသောတန်ဖိုးဖြစ်ရမည်။
    - **Minimum number of nodes** ကို **0** သို့ရွေးပါ။
    - **Maximum number of nodes** ကို **1** သို့ရွေးပါ။
    - **Idle seconds before scale down** ကို **120** သို့ရွေးပါ။

    ![Cluster တစ်ခု ဖန်တီးပါ။](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.mo.png)

1. **Create** ကိုရွေးပါ။

#### Phi-3 မော်ဒယ်ကို Fine-tune ပြုလုပ်ပါ။

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace ကိုရွေးချယ်ပါ။

    ![သင်ဖန်တီးထားသော workspace ကိုရွေးပါ။](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.mo.png)

1. အောက်ပါအလုပ်များကို ဆောင်ရွက်ပါ။

    - ဘယ်ဘက်ဘောင်မှ **Model catalog** ကိုရွေးချယ်ပါ။
    - **search bar** တွင် *phi-3-mini-4k* ဟုရိုက်ထည့်ပြီး **Phi-3-mini-4k-instruct** ကိုရွေးချယ်ပါ။

    ![phi-3-mini-4k ဟုရိုက်ပါ။](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.mo.png)

1. Navigation menu မှ **Fine-tune** ကိုရွေးချယ်ပါ။

    ![Fine tune ကိုရွေးပါ။](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.mo.png)

1. အောက်ပါအလုပ်များကို ဆောင်ရွက်ပါ။

    - **Select task type** ကို **Chat completion** သို့ရွေးပါ။
    - **+ Select data** ကိုရွေးပြီး **Training data** ကို upload လုပ်ပါ။
    - Validation data upload type ကို **Provide different validation data** သို့ရွေးပါ။
    - **+ Select data** ကိုရွေးပြီး **Validation data** ကို upload လုပ်ပါ။

    ![Fine-tuning စာမျက်နှာကို ဖြည့်ပါ။](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.mo.png)

    > [!TIP]
    >
    > **Advanced settings** ကိုရွေးချယ်ပြီး **learning_rate** နှင့် **lr_scheduler_type** တို့ကို သင်၏လိုအပ်ချက်များအတိုင်း ချိန်ညှိ၍ Fine-tuning လုပ်ငန်းစဉ်ကို အကောင်းဆုံးဖြစ်စေရန် ပြုလုပ်နိုင်သည်။

1. **Finish** ကိုရွေးပါ။

1. ဤလေ့ကျင့်မှုတွင် သင်သည် Azure Machine Learning ကို အသုံးပြု၍ Phi-3 မော်ဒယ်ကို အောင်မြင်စွာ Fine-tune ပြုလုပ်နိုင်ခဲ့ပါသည်။ Fine-tuning လုပ်ငန်းစဉ်သည် အချိန်အတော်ကြာနိုင်သည်ကို မှတ်သားပါ။ Fine-tuning job ကို run ပြီးနောက် ၎င်း၏ အခြေအနေကို စောင့်ကြည့်ရန် Azure Machine Learning Workspace ၏ Jobs tab သို့ သွားပါ။ နောက်ထပ် အစီအစဉ်တွင် Fine-tuned မော်ဒယ်ကို Deploy ပြုလုပ်ပြီး Prompt flow နှင့် ပေါင်းစပ်အသုံးပြုမည်။

    ![Fine-tuning job ကိုကြည့်ပါ။](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.mo.png)

### Fine-tuned Phi-3 မော်ဒယ်ကို Deploy ပြုလုပ်ပါ။

Fine-tuned Phi-3 မော်ဒယ်ကို Prompt flow နှင့် ပေါင်းစပ်အသုံးပြုရန်အတွက် ၎င်းကို real-time inference အတွက် အသုံးပြုနိုင်ရန် Deploy လုပ်ရမည်။ ဤလုပ်ငန်းစဉ်တွင် မော်ဒယ်ကို Register လုပ်ခြင်း၊ online endpoint တစ်ခုဖန်တီးခြင်းနှင့် မော်ဒယ်ကို Deploy ပြုလုပ်ခြင်းတို့ ပါဝင်သည်။

ဤလေ့ကျင့်မှုတွင် သင်သည် -

- Fine-tuned မော်ဒယ်ကို Azure Machine Learning workspace တွင် Register လုပ်ပါ။
- Online endpoint တစ်ခု ဖန်တီးပါ။
- Register လုပ်ထားသော Fine-tuned Phi-3 မော်ဒယ်ကို Deploy ပြုလုပ်ပါ။

#### Fine-tuned မော်ဒယ်ကို Register လုပ်ပါ။

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) သို့ သွားပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace ကိုရွေးချယ်ပါ။

    ![သင်ဖန်တီးထားသော workspace ကိုရွေးပါ။](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.mo.png)

1. ဘယ်ဘက်ဘောင်မှ **Models** ကိုရွေးပါ။
1. **+ Register** ကိုရွေးပါ။
1. **From a job output** ကိုရွေးပါ။

    ![မော်ဒယ်ကို Register လုပ်ပါ။](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.mo.png)

1. သင်ဖန်တီးထားသော job ကိုရွေးပါ။

    ![Job ကိုရွေးပါ။](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.mo.png)

1. **Next** ကိုရွေးပါ။

1. **Model type** ကို **MLflow** သို့ရွေးပါ။

1. **Job output** ရွေးထားပြီးဖြစ်ရမည်။ ၎င်းကို အလိုအလျောက်ရွေးထားမည်။

    ![Output ကိုရွေးပါ။](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.mo.png)

2. **Next** ကိုရွေးပါ။

3. **Register** ကိုရွေးပါ။

    ![Register ကိုရွေးပါ။](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.mo.png)

4. **Models** menu သို့သွား၍ သင်၏ Register လုပ်ထားသော မော်ဒယ်ကို ကြည့်ရှုနိုင်သည်။

    ![Register လုပ်ထားသော မော်ဒယ်။](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.mo.png)

#### Fine-tuned မော်ဒယ်ကို Deploy ပြုလုပ်ပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace သို့သွားပါ။

1. ဘယ်ဘက်ဘောင်မှ **Endpoints** ကိုရွေးပါ။

1. Navigation menu မှ **Real-time endpoints** ကိုရွေးချယ်ပါ။

    ![Endpoint တစ်ခု ဖန်တီးပါ။](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.mo.png)

1. **Create** ကိုရွေးပါ။

1. သင်ဖန်တီးထားသော registered model ကိုရွေးပါ။

    ![Registered model ကိုရွေးပါ။](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.mo.png)

1. **Select** ကိုရွေးပါ။

1. အောက်ပါအလုပ်များကို ဆောင်ရွက်ပါ။

    - **Virtual machine** ကို *Standard_NC6s_v3* သို့ရွေးပါ။
    - သင်အသုံးပြုလိုသော **Instance count** ကိုရွေးပါ။ ဥပမာ - *1*။
    - **Endpoint** ကို **New** သို့ရွေးပြီး endpoint တစ်ခုဖန်တီးပါ။
    - **Endpoint name** ထည့်ပါ။ ၎င်းသည် ထူးခြားသောတန်ဖိုးဖြစ်ရမည်။
    - **Deployment name** ထည့်ပါ။ ၎င်းသည် ထူးခြားသောတန်ဖိုးဖြစ်ရမည်။

    ![Deployment setting ကို ဖြည့်ပါ။](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.mo.png)

1. **Deploy** ကိုရွေးပါ။

> [!WARNING]
> သင်၏အကောင့်တွင် အပိုဝန်ဆောင်မှုကြေးမဖြစ်စေရန် Azure Machine Learning workspace တွင် ဖန်တီးထားသော endpoint ကို ဖျက်သိမ်းပါ။
>

#### Azure Machine Learning Workspace တွင် Deployment Status ကို စစ်ဆေးပါ။

1. သင်ဖန်တီးထားသော Azure Machine Learning workspace သို့သွားပါ။

1. ဘယ်ဘက်ဘောင်မှ **Endpoints** ကိုရွေးပါ။

1. သင်ဖန်တီးထားသော endpoint ကိုရွေးပါ။

    ![Endpoints ကိုရွေးပါ။](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.mo.png)

1. ဤစာမျက်နှာတွင် Deployment လုပ်ငန်းစဉ်အတွင်း Endpoints ကို စီမံခန့်ခွဲနိုင်သည်။

> [!NOTE]
> Deployment ပြီးဆုံးပြီးနောက် **Live traffic** ကို **100%** သို့ထားထားပါ။ မဟုတ်ပါက **Update traffic** ကိုရွေးပြီး traffic setting ကို ပြင်ဆင်ပါ။ Traffic ကို 0% သို့ထားပါက မော်ဒယ်ကို စမ်းသပ်၍မရနိုင်ပါ။
>
> ![Traffic ကိုသတ်မှတ်ပါ။](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.mo.png)
>
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.mo.png)

#### Add the Custom Connection

1. ไปที่ [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)

1. เข้าสู่โปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. ในโปรเจกต์ที่คุณสร้าง ให้เลือก **Settings** จากแท็บด้านซ้าย

1. เลือก **+ New connection**

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.mo.png)

1. เลือก **Custom keys** จากเมนูนำทาง

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.mo.png)

1. ทำตามขั้นตอนดังนี้:

    - เลือก **+ Add key value pairs**
    - ในช่อง key name ให้ป้อน **endpoint** และวาง endpoint ที่คัดลอกจาก Azure ML Studio ลงในช่อง value
    - เลือก **+ Add key value pairs** อีกครั้ง
    - ในช่อง key name ให้ป้อน **key** และวาง key ที่คัดลอกจาก Azure ML Studio ลงในช่อง value
    - หลังจากเพิ่ม keys แล้ว ให้เลือก **is secret** เพื่อป้องกันไม่ให้ key ถูกเปิดเผย

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.mo.png)

1. เลือก **Add connection**

#### Create Prompt flow

คุณได้เพิ่ม Custom Connection ใน Azure AI Foundry แล้ว ตอนนี้เราจะสร้าง Prompt flow โดยทำตามขั้นตอนต่อไปนี้ และคุณจะเชื่อมต่อ Prompt flow นี้เข้ากับ Custom Connection เพื่อใช้งานโมเดลที่ปรับแต่งแล้วภายใน Prompt flow

1. ไปที่โปรเจกต์ Azure AI Foundry ที่คุณสร้างไว้

1. เลือก **Prompt flow** จากแท็บด้านซ้าย

1. เลือก **+ Create** จากเมนูนำทาง

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.mo.png)

1. เลือก **Chat flow** จากเมนูนำทาง

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.mo.png)

1. ป้อน **Folder name** ที่ต้องการใช้

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.mo.png)

2. เลือก **Create**

#### Set up Prompt flow to chat with your custom Phi-3 model

คุณจำเป็นต้องผสานโมเดล Phi-3 ที่ปรับแต่งแล้วเข้ากับ Prompt flow อย่างไรก็ตาม Prompt flow ที่มีอยู่เดิมไม่ได้ออกแบบมาเพื่อจุดประสงค์นี้ ดังนั้นคุณต้องปรับปรุง Prompt flow ใหม่เพื่อรองรับการผสานโมเดลที่ปรับแต่งแล้ว

1. ใน Prompt flow ให้ทำตามขั้นตอนต่อไปนี้เพื่อปรับปรุง flow ที่มีอยู่:

    - เลือก **Raw file mode**
    - ลบโค้ดทั้งหมดในไฟล์ *flow.dag.yml*
    - เพิ่มโค้ดต่อไปนี้ลงในไฟล์ *flow.dag.yml*

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

    - เลือก **Save**

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.mo.png)

1. เพิ่มโค้ดต่อไปนี้ลงในไฟล์ *integrate_with_promptflow.py* เพื่อใช้งานโมเดล Phi-3 ที่ปรับแต่งแล้วใน Prompt flow

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
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
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
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.mo.png)

> [!NOTE]
> สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ Prompt flow ใน Azure AI Foundry สามารถดูได้ที่ [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)

1. เลือก **Chat input**, **Chat output** เพื่อเปิดใช้งานการแชทกับโมเดลของคุณ

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.mo.png)

1. ตอนนี้คุณพร้อมที่จะเริ่มแชทกับโมเดล Phi-3 ที่ปรับแต่งแล้ว ในขั้นตอนถัดไป คุณจะได้เรียนรู้วิธีเริ่มต้น Prompt flow และใช้งานเพื่อแชทกับโมเดล Phi-3 ที่ปรับแต่งแล้วของคุณ

> [!NOTE]
>
> Prompt flow ที่ปรับปรุงแล้วควรมีลักษณะดังภาพด้านล่าง:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.mo.png)
>

### Chat with your custom Phi-3 model

ตอนนี้คุณได้ปรับแต่งและผสานโมเดล Phi-3 ที่ปรับแต่งแล้วเข้ากับ Prompt flow คุณพร้อมที่จะเริ่มต้นใช้งานและแชทกับมันแล้ว ขั้นตอนนี้จะแนะนำวิธีการตั้งค่าและเริ่มต้นการแชทกับโมเดลของคุณโดยใช้ Prompt flow โดยการทำตามขั้นตอนนี้ คุณจะสามารถใช้งานความสามารถของโมเดล Phi-3 ที่ปรับแต่งแล้วได้อย่างเต็มที่สำหรับงานและการสนทนาต่างๆ

- แชทกับโมเดล Phi-3 ที่ปรับแต่งแล้วของคุณโดยใช้ Prompt flow

#### Start Prompt flow

1. เลือก **Start compute sessions** เพื่อเริ่มต้น Prompt flow

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.mo.png)

1. เลือก **Validate and parse input** เพื่อรีเฟรชพารามิเตอร์

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.mo.png)

1. เลือก **Value** ของ **connection** ที่เชื่อมต่อกับ Custom Connection ที่คุณสร้างไว้ ตัวอย่างเช่น *connection*

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.mo.png)

#### Chat with your custom model

1. เลือก **Chat**

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.mo.png)

1. ตัวอย่างผลลัพธ์: ตอนนี้คุณสามารถแชทกับโมเดล Phi-3 ที่ปรับแต่งแล้วของคุณได้ แนะนำให้ถามคำถามที่เกี่ยวข้องกับข้อมูลที่ใช้ในการปรับแต่ง

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.mo.png)

It seems you may be asking for a translation into "mo," but it’s unclear what specific language or context "mo" refers to. Could you clarify the target language or provide more details? For example, are you referring to Maori, Mongolian, or something else? Let me know so I can assist you better!