## Finetuning vs RAG

## Retrieval Augmented Generation

RAG yhdistää tiedonhakua ja tekstin tuottamista. Yrityksen jäsennelty ja jäsentämätön data tallennetaan vektoritietokantaan. Kun etsitään relevanttia sisältöä, löydetään yhteenveto ja sisältö, jotka muodostavat kontekstin. Tämän jälkeen hyödynnetään LLM/SLM:n tekstin täydennyskykyä sisällön luomiseen.

## RAG-prosessi
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.fi.png)

## Fine-tuning
Fine-tuning perustuu olemassa olevan mallin parantamiseen. Se ei vaadi mallialgoritmin luomista alusta alkaen, mutta dataa on kerättävä jatkuvasti. Jos haluat tarkempaa terminologiaa ja kielellistä ilmaisua toimialasovelluksissa, fine-tuning on parempi vaihtoehto. Mutta jos datasi muuttuu usein, fine-tuning voi muuttua monimutkaiseksi.

## Miten valita
Jos vastauksemme vaatii ulkoisen datan käyttämistä, RAG on paras valinta.

Jos taas tarvitset vakaata ja tarkkaa toimialatietoa, fine-tuning on hyvä vaihtoehto. RAG painottaa relevantin sisällön hakemista, mutta ei välttämättä aina tavoita erikoistuneita vivahteita.

Fine-tuning vaatii korkealaatuisen datasarjan, ja jos data kattaa vain pienen alueen, vaikutus ei ole merkittävä. RAG on joustavampi.  
Fine-tuning on kuin musta laatikko, eräänlaista metafysiikkaa, ja sen sisäistä mekanismia on vaikea ymmärtää. Sen sijaan RAG tekee datan lähteiden löytämisestä helpompaa, mikä mahdollistaa hallusinaatioiden tai sisältövirheiden tehokkaan korjaamisen ja tarjoaa paremman läpinäkyvyyden.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälyyn perustuvia käännöspalveluja käyttäen. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.