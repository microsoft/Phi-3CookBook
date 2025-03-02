# Korištenje Windows GPU-a za stvaranje Prompt Flow rješenja s Phi-3.5-Instruct ONNX

Sljedeći dokument je primjer kako koristiti PromptFlow s ONNX-om (Open Neural Network Exchange) za razvoj AI aplikacija temeljenih na Phi-3 modelima.

PromptFlow je skup alata za razvoj koji olakšava cjelokupni razvojni ciklus AI aplikacija temeljenih na velikim jezičnim modelima (LLM), od ideje i prototipiranja do testiranja i evaluacije.

Integracijom PromptFlow-a s ONNX-om, programeri mogu:

- Optimizirati performanse modela: Iskoristiti ONNX za učinkovitu inferenciju i implementaciju modela.
- Pojednostaviti razvoj: Koristiti PromptFlow za upravljanje radnim procesom i automatizaciju repetitivnih zadataka.
- Poboljšati suradnju: Olakšati bolju suradnju među članovima tima pružanjem jedinstvenog razvojnog okruženja.

**Prompt flow** je skup alata za razvoj koji olakšava cjelokupni razvojni ciklus AI aplikacija temeljenih na LLM-ovima, od ideje, prototipa, testiranja, evaluacije do implementacije u produkciju i praćenja. Omogućuje jednostavnije kreiranje promptova i razvoj LLM aplikacija produkcijske kvalitete.

Prompt flow može se povezati s OpenAI, Azure OpenAI Service i prilagodljivim modelima (Huggingface, lokalni LLM/SLM). Naš cilj je implementirati kvantizirani ONNX model Phi-3.5 u lokalne aplikacije. Prompt flow nam može pomoći bolje planirati poslovanje i dovršiti lokalna rješenja temeljena na Phi-3.5. U ovom primjeru, kombinirat ćemo ONNX Runtime GenAI biblioteku kako bismo dovršili Prompt Flow rješenje temeljeno na Windows GPU-u.

## **Instalacija**

### **ONNX Runtime GenAI za Windows GPU**

Pročitajte ovaj vodič za postavljanje ONNX Runtime GenAI za Windows GPU [kliknite ovdje](./ORTWindowGPUGuideline.md)

### **Postavljanje Prompt flow-a u VSCode**

1. Instalirajte Prompt flow proširenje za VS Code

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.hr.png)

2. Nakon instalacije Prompt flow proširenja za VS Code, kliknite na proširenje i odaberite **Installation dependencies** te slijedite ovaj vodič za instalaciju Prompt flow SDK-a u svoje okruženje.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.hr.png)

3. Preuzmite [Primjer koda](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) i otvorite ga u VS Code-u.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.hr.png)

4. Otvorite **flow.dag.yaml** kako biste odabrali svoje Python okruženje.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.hr.png)

   Otvorite **chat_phi3_ort.py** kako biste promijenili lokaciju svog Phi-3.5-instruct ONNX modela.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.hr.png)

5. Pokrenite svoj Prompt flow za testiranje.

Otvorite **flow.dag.yaml** i kliknite na vizualni uređivač.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.hr.png)

Nakon što kliknete, pokrenite ga za testiranje.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.hr.png)

1. Možete pokrenuti batch u terminalu kako biste provjerili više rezultata.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Rezultate možete provjeriti u svom zadano postavljenom pregledniku.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojnog prevođenja temeljenih na umjetnoj inteligenciji. Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane stručnjaka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.