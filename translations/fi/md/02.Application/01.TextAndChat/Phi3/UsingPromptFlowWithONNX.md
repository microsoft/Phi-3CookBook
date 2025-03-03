# Windows GPU:n käyttäminen Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:lla

Tämä dokumentti on esimerkki siitä, kuinka käyttää PromptFlow'ta yhdessä ONNX:n (Open Neural Network Exchange) kanssa Phi-3-malleihin perustuvien tekoälysovellusten kehittämisessä.

PromptFlow on kehitystyökalujen kokonaisuus, joka on suunniteltu helpottamaan LLM-pohjaisten (Large Language Model) tekoälysovellusten kehityksen koko elinkaarta ideoinnista ja prototypoinnista aina testaukseen ja arviointiin asti.

Integroimalla PromptFlow ONNX:n kanssa kehittäjät voivat:

- **Optimoida mallin suorituskykyä**: Hyödyntää ONNX:ää tehokkaaseen mallin inferenssiin ja käyttöönottoon.
- **Yksinkertaistaa kehitystyötä**: Käyttää PromptFlow'ta työnkulun hallintaan ja toistuvien tehtävien automatisointiin.
- **Parantaa yhteistyötä**: Helpottaa tiimin välistä yhteistyötä tarjoamalla yhtenäisen kehitysympäristön.

**Prompt flow** on kehitystyökalujen kokonaisuus, joka on suunniteltu virtaviivaistamaan LLM-pohjaisten tekoälysovellusten kehityksen koko elinkaarta ideoinnista, prototypoinnista, testauksesta ja arvioinnista aina tuotantoon ja valvontaan asti. Se tekee prompt-suunnittelusta huomattavasti helpompaa ja mahdollistaa tuotantovalmiiden LLM-sovellusten rakentamisen.

Prompt flow voi yhdistyä OpenAI:hin, Azure OpenAI Serviceen ja mukautettuihin malleihin (Huggingface, paikalliset LLM/SLM). Tavoitteenamme on ottaa käyttöön Phi-3.5:n kvantisoitu ONNX-malli paikallisissa sovelluksissa. Prompt flow auttaa meitä suunnittelemaan liiketoimintaamme paremmin ja toteuttamaan paikallisia ratkaisuja Phi-3.5:n pohjalta. Tässä esimerkissä yhdistämme ONNX Runtime GenAI -kirjaston Prompt flow -ratkaisun toteuttamiseen Windows GPU:lla.

## **Asennus**

### **ONNX Runtime GenAI Windows GPU:lle**

Lue tämä ohje asentaaksesi ONNX Runtime GenAI Windows GPU:lle [klikkaa tästä](./ORTWindowGPUGuideline.md)

### **Prompt flow'n asennus VSCodeen**

1. Asenna Prompt flow VS Code -laajennus

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.fi.png)

2. Kun olet asentanut Prompt flow VS Code -laajennuksen, klikkaa laajennusta ja valitse **Installation dependencies**. Seuraa tätä ohjetta asentaaksesi Prompt flow SDK ympäristöösi.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.fi.png)

3. Lataa [Esimerkkikoodi](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) ja avaa tämä esimerkki VS Codessa.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.fi.png)

4. Avaa **flow.dag.yaml** ja valitse Python-ympäristösi.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.fi.png)

   Avaa **chat_phi3_ort.py** ja vaihda Phi-3.5-instruct ONNX -mallisi sijainti.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.fi.png)

5. Suorita Prompt flow -ratkaisusi testataksesi sitä.

Avaa **flow.dag.yaml** ja klikkaa visuaalista editoria.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.fi.png)

Klikkaa tätä ja suorita testataksesi.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.fi.png)

1. Voit suorittaa eräkäsittelyn terminaalissa nähdäksesi lisää tuloksia.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Voit tarkistaa tulokset oletusselaimessasi.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluita käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.