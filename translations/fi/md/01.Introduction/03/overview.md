Phi-3-mini-mallin tapauksessa päättely tarkoittaa prosessia, jossa mallia käytetään ennusteiden tekemiseen tai tulosten tuottamiseen syöteaineiston perusteella. Tässä lisätietoa Phi-3-mini-mallista ja sen päättelyominaisuuksista.

Phi-3-mini kuuluu Microsoftin julkaisemaan Phi-3-mallisarjaan. Nämä mallit on suunniteltu uudistamaan pienten kielimallien (SLM) mahdollisuuksia.

Tässä keskeisiä kohtia Phi-3-mini-mallista ja sen päättelyominaisuuksista:

## **Phi-3-mini Yleiskatsaus:**
- Phi-3-mini sisältää 3,8 miljardia parametria.
- Se voi toimia paitsi perinteisillä laskentalaitteilla myös reuna-alustoilla, kuten mobiililaitteilla ja IoT-laitteilla.
- Phi-3-mini:n julkaisu mahdollistaa yksityishenkilöiden ja yritysten käyttöönoton erilaisilla laitteilla, erityisesti ympäristöissä, joissa resurssit ovat rajalliset.
- Se tukee useita malliformaatteja, kuten perinteistä PyTorch-muotoa, kvantisoitua gguf-muotoa ja ONNX-pohjaista kvantisoitua versiota.

## **Phi-3-mini:n Käyttöönotto:**
Phi-3-mini-mallin käyttöön voit hyödyntää [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) -työkalua Copilot-sovelluksessa. Semantic Kernel on yhteensopiva Azure OpenAI Servicen, Hugging Facen avoimen lähdekoodin mallien ja paikallisten mallien kanssa.
Voit myös käyttää [Ollama](https://ollama.com) tai [LlamaEdge](https://llamaedge.com) -palveluita kvantisoitujen mallien hyödyntämiseen. Ollama mahdollistaa yksittäisten käyttäjien kutsua eri kvantisoituja malleja, kun taas LlamaEdge tarjoaa GGUF-malleille alustojen välisen tuen.

## **Kvantisoidut Mallit:**
Monet käyttäjät suosivat kvantisoituja malleja paikallista päättelyä varten. Esimerkiksi voit suoraan ajaa Ollama run Phi-3 -komennolla tai konfiguroida sen offline-tilassa Modelfile-tiedoston avulla. Modelfile määrittää GGUF-tiedoston polun ja kehotteen muodon.

## **Generatiivisen AI:n Mahdollisuudet:**
SLM-mallien, kuten Phi-3-mini, yhdistäminen avaa uusia mahdollisuuksia generatiiviselle tekoälylle. Päättely on vasta ensimmäinen askel; näitä malleja voidaan hyödyntää monenlaisissa tehtävissä ympäristöissä, joissa resurssit, viive ja kustannukset ovat kriittisiä tekijöitä.

## **Generatiivisen AI:n Hyödyntäminen Phi-3-mini-mallilla: Opas Päättelyyn ja Käyttöönottoon** 
Opi käyttämään Semantic Kernel -työkalua, Ollama/LlamaEdge-palveluita ja ONNX Runtime -ympäristöä Phi-3-mini-mallien käyttöön ja päättelyyn, ja tutustu generatiivisen tekoälyn mahdollisuuksiin eri sovellustilanteissa.

**Ominaisuudet**
Päättely Phi-3-mini-mallilla seuraavissa:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Yhteenvetona, Phi-3-mini antaa kehittäjille mahdollisuuden tutkia erilaisia malliformaatteja ja hyödyntää generatiivista tekoälyä monissa sovellustilanteissa.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkinnoista.