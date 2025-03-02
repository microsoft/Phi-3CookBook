**Phi-3:n hienosäätö QLoRA:n avulla**

Microsoftin Phi-3 Mini -kielimallin hienosäätö [QLoRA:n (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) avulla.

QLoRA auttaa parantamaan keskustelun ymmärtämistä ja vastausten tuottamista.

Jotta voit ladata malleja 4-bittisinä käyttäen transformers- ja bitsandbytes-kirjastoja, sinun täytyy asentaa accelerate- ja transformers-kirjastot suoraan lähdekoodista ja varmistaa, että käytössäsi on uusin versio bitsandbytes-kirjastosta.

**Esimerkit**
- [Lisätietoja tästä esimerkkivihkosta](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Esimerkki Python-hienosäätöskriptistä](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Esimerkki Hugging Face Hub -hienosäädöstä LORA:n avulla](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Esimerkki Hugging Face Hub -hienosäädöstä QLORA:n avulla](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.