# **Inference Phi-3 Android-laitteilla**

Tutustutaan siihen, kuinka voit suorittaa inferenssin Phi-3-mini-mallilla Android-laitteilla. Phi-3-mini on Microsoftin uusi mallisarja, joka mahdollistaa suurten kielimallien (LLM) käytön reunalaitteilla ja IoT-laitteilla.

## Semantic Kernel ja inferenssi

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) on sovelluskehys, jonka avulla voit luoda sovelluksia, jotka ovat yhteensopivia Azure OpenAI Servicen, OpenAI-mallien ja myös paikallisten mallien kanssa. Jos Semantic Kernel on sinulle uusi, suosittelemme tutustumaan [Semantic Kernel Cookbookiin](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Phi-3-minin käyttö Semantic Kernelin avulla

Voit yhdistää sen Semantic Kernelissä Hugging Face Connectoriin. Katso [esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Oletuksena se vastaa Hugging Facen mallin tunnistetta. Voit kuitenkin myös yhdistää paikallisesti rakennettuun Phi-3-mini-mallipalvelimeen.

### Kvantisoitujen mallien kutsuminen Ollaman tai LlamaEdgen avulla

Monet käyttäjät suosivat kvantisoituja malleja mallien paikalliseen suorittamiseen. [Ollama](https://ollama.com/) ja [LlamaEdge](https://llamaedge.com) tarjoavat mahdollisuuden käyttää erilaisia kvantisoituja malleja:

#### Ollama

Voit suorittaa `ollama run Phi-3` suoraan tai määrittää sen offline-tilassa luomalla `Modelfile`, jossa on polku `.gguf`-tiedostoon.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Esimerkkikoodi](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Jos haluat käyttää `.gguf`-tiedostoja pilvessä ja reunalaitteilla samanaikaisesti, LlamaEdge on erinomainen valinta. Voit aloittaa tutustumalla tähän [esimerkkikoodiin](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Asennus ja käyttö Android-puhelimilla

1. **Lataa MLC Chat -sovellus** (ilmainen) Android-puhelimille.
2. Lataa APK-tiedosto (148 Mt) ja asenna se laitteellesi.
3. Käynnistä MLC Chat -sovellus. Näet luettelon AI-malleista, mukaan lukien Phi-3-mini.

Yhteenvetona voidaan todeta, että Phi-3-mini tarjoaa jännittäviä mahdollisuuksia generatiivisen tekoälyn käyttöön reunalaitteilla, ja voit alkaa tutkia sen ominaisuuksia Android-laitteilla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisten tekoälyyn perustuvien käännöspalveluiden avulla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista, ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.