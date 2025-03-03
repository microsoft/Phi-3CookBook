# **Uporaba Phi-3 v Azure AI Foundry**

Z razvojem generativne umetne inteligence si prizadevamo za uporabo enotne platforme za upravljanje različnih LLM in SLM, integracijo podatkov podjetja, prilagoditve/RAG operacije ter ocenjevanje različnih poslovnih procesov podjetja po integraciji LLM in SLM. S tem omogočamo boljšo implementacijo pametnih aplikacij generativne umetne inteligence. [Azure AI Foundry](https://ai.azure.com) je platforma za aplikacije generativne umetne inteligence na ravni podjetij.

![aistudo](../../../../translated_images/aifoundry_home.ffa4fe13d11f26171097f8666a1db96ac0979ffa1adde80374c60d1136c7e1de.sl.png)

Z Azure AI Foundry lahko ocenjujete odzive velikih jezikovnih modelov (LLM) in orkestrirate komponente aplikacij s prompt flow za boljše delovanje. Platforma omogoča enostavno prehod iz prototipov v popolnoma delujoče produkcijske sisteme. Neprekinjeno spremljanje in izboljšave podpirajo dolgoročni uspeh.

Model Phi-3 lahko hitro uvedemo v Azure AI Foundry s preprostimi koraki, nato pa z njim izvedemo Phi-3 povezane aktivnosti, kot so Playground/Chat, prilagoditve, ocenjevanje in druge povezane naloge.

## **1. Priprava**

Če imate na svoji napravi že nameščen [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview?WT.mc_id=aiml-138114-kinfeylo), je uporaba te predloge enostavna kot zagon tega ukaza v novi mapi.

## Ročna ustvaritev

Ustvarjanje projekta in vozlišča (hub) v Microsoft Azure AI Foundry je odličen način za organizacijo in upravljanje vašega dela na področju umetne inteligence. Tukaj je vodnik po korakih, kako začeti:

### Ustvarjanje projekta v Azure AI Foundry

1. **Pojdite na Azure AI Foundry**: Prijavite se v portal Azure AI Foundry.
2. **Ustvarite projekt**:
   - Če ste že v projektu, izberite "Azure AI Foundry" v zgornjem levem kotu strani, da se vrnete na domačo stran.
   - Izberite "+ Create project".
   - Vnesite ime za projekt.
   - Če imate vozlišče, bo to privzeto izbrano. Če imate dostop do več vozlišč, lahko izberete drugo iz spustnega seznama. Če želite ustvariti novo vozlišče, izberite "Create new hub" in vnesite ime.
   - Izberite "Create".

### Ustvarjanje vozlišča v Azure AI Foundry

1. **Pojdite na Azure AI Foundry**: Prijavite se s svojim Azure računom.
2. **Ustvarite vozlišče**:
   - V levem meniju izberite Management center.
   - Izberite "All resources", nato puščico poleg "+ New project" in izberite "+ New hub".
   - V pogovornem oknu "Create a new hub" vnesite ime za svoje vozlišče (npr. contoso-hub) in po želji prilagodite ostala polja.
   - Izberite "Next", preverite informacije in nato izberite "Create".

Za bolj podrobna navodila si lahko ogledate uradno [dokumentacijo Microsofta](https://learn.microsoft.com/azure/ai-studio/how-to/create-projects).

Po uspešni ustvaritvi lahko dostopate do ustvarjenega studia prek [ai.azure.com](https://ai.azure.com/).

Na enem AI Foundry lahko obstaja več projektov. Ustvarite projekt v AI Foundry za pripravo.

Ustvarite Azure AI Foundry [QuickStarts](https://learn.microsoft.com/azure/ai-studio/quickstarts/get-started-code)

## **2. Uvedba modela Phi v Azure AI Foundry**

Kliknite možnost Explore projekta, da vstopite v Model Catalog in izberete Phi-3.

Izberite Phi-3-mini-4k-instruct.

Kliknite 'Deploy', da uvedete model Phi-3-mini-4k-instruct.

> [!NOTE]
>
> Pri uvedbi lahko izberete računalniško moč.

## **3. Playground Chat Phi v Azure AI Foundry**

Pojdite na stran za uvedbo, izberite Playground in komunicirajte s Phi-3 na Azure AI Foundry.

## **4. Uvedba modela iz Azure AI Foundry**

Za uvedbo modela iz Azure Model Catalog sledite tem korakom:

- Prijavite se v Azure AI Foundry.
- Izberite model, ki ga želite uvesti, iz kataloga modelov Azure AI Foundry.
- Na strani s podrobnostmi modela izberite Deploy in nato Serverless API z Azure AI Content Safety.
- Izberite projekt, v katerem želite uvesti svoje modele. Če želite uporabiti možnost Serverless API, mora vaša delovna okolica pripadati regiji East US 2 ali Sweden Central. Ime uvedbe lahko prilagodite.
- V čarovniku za uvedbo izberite Pricing and terms, da izveste več o cenah in pogojih uporabe.
- Izberite Deploy. Počakajte, da je uvedba pripravljena, in boste preusmerjeni na stran Deployments.
- Izberite Open in playground, da začnete komunicirati z modelom.
- Vedno se lahko vrnete na stran Deployments, izberete uvedbo in si ogledate ciljni URL in Secret Key, ki ju lahko uporabite za klic uvedbe in generiranje odgovorov.
- Podrobnosti o ciljnem URL-ju in dostopnih ključih lahko vedno najdete tako, da se pomaknete na zavihek Build in izberete Deployments v razdelku Components.

> [!NOTE]
> Upoštevajte, da mora imeti vaš račun dovoljenja vloge Azure AI Developer na skupini virov za izvedbo teh korakov.

## **5. Uporaba Phi API v Azure AI Foundry**

Do https://{Ime vašega projekta}.region.inference.ml.azure.com/swagger.json lahko dostopate prek Postman GET in v kombinaciji s ključem spoznate razpoložljive vmesnike.

Zelo enostavno lahko pridobite parametre zahtevka in tudi parametre odgovora.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.