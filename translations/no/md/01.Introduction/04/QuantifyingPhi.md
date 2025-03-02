# **Kvantisering av Phi-familien**

Modellkvantisering refererer til prosessen med å kartlegge parameterne (som vekter og aktiveringsverdier) i en nevralt nettverksmodell fra et stort verdiområde (vanligvis et kontinuerlig verdiområde) til et mindre, begrenset verdiområde. Denne teknologien kan redusere størrelsen og den beregningsmessige kompleksiteten til modellen, samt forbedre modellens ytelse i ressursbegrensede miljøer som mobiltelefoner eller innebygde systemer. Modellkvantisering oppnår komprimering ved å redusere presisjonen til parameterne, men det introduserer også et visst presisjonstap. Derfor er det nødvendig å balansere modellstørrelse, beregningskompleksitet og presisjon i kvantiseringsprosessen. Vanlige kvantiseringsmetoder inkluderer fastpunktskvantisering, flytende punkts kvantisering, og lignende. Du kan velge en passende kvantiseringsstrategi basert på spesifikke behov og scenarier.

Vi ønsker å distribuere GenAI-modellen til kant-enheter og gjøre det mulig for flere enheter å delta i GenAI-scenarier, som mobiltelefoner, AI-PC/Copilot+PC og tradisjonelle IoT-enheter. Gjennom kvantiseringsmodellen kan vi distribuere modellen til ulike kant-enheter basert på de spesifikke egenskapene til hver enhet. Kombinert med akselerasjonsrammeverk og kvantiseringsmodeller levert av maskinvareprodusenter, kan vi bygge bedre SLM-applikasjonsscenarier.

I kvantiseringsscenarier har vi ulike presisjonsnivåer (INT4, INT8, FP16, FP32). Nedenfor følger en forklaring av de mest brukte kvantiseringspresisjonene.

### **INT4**

INT4-kvantisering er en radikal metode som kvantiserer vektene og aktiveringsverdiene til modellen til 4-bits heltall. INT4-kvantisering fører vanligvis til et større presisjonstap på grunn av det mindre representasjonsområdet og lavere presisjon. Sammenlignet med INT8-kvantisering kan INT4-kvantisering imidlertid ytterligere redusere lagringsbehovet og den beregningsmessige kompleksiteten til modellen. Det er viktig å merke seg at INT4-kvantisering er relativt sjelden i praktiske anvendelser, fordi for lav presisjon kan føre til betydelig ytelsesforringelse. I tillegg støtter ikke all maskinvare INT4-operasjoner, så maskinvarekompatibilitet må vurderes når man velger kvantiseringsmetode.

### **INT8**

INT8-kvantisering innebærer å konvertere modellens vekter og aktiveringer fra flyttall til 8-bits heltall. Selv om det numeriske området representert av INT8-heltall er mindre og mindre presist, kan det betydelig redusere lagrings- og beregningskravene. I INT8-kvantisering går modellens vekter og aktiveringsverdier gjennom en kvantiseringsprosess, inkludert skalering og offset, for å bevare så mye som mulig av den opprinnelige flyttallsinformasjonen. Under inferens vil disse kvantiserte verdiene bli dekvantisert tilbake til flyttall for beregning, og deretter kvantisert tilbake til INT8 for neste steg. Denne metoden kan gi tilstrekkelig presisjon i de fleste applikasjoner samtidig som den opprettholder høy beregningseffektivitet.

### **FP16**

FP16-formatet, altså 16-bits flyttall (float16), reduserer minneforbruket med halvparten sammenlignet med 32-bits flyttall (float32), noe som gir betydelige fordeler i storskala dyp læringsapplikasjoner. FP16-formatet tillater lasting av større modeller eller behandling av mer data innenfor de samme GPU-minnebegrensningene. Etter hvert som moderne GPU-maskinvare fortsetter å støtte FP16-operasjoner, kan bruk av FP16-formatet også føre til forbedringer i beregningshastighet. Imidlertid har FP16-formatet også sine iboende ulemper, nemlig lavere presisjon, noe som kan føre til numerisk ustabilitet eller presisjonstap i visse tilfeller.

### **FP32**

FP32-formatet gir høyere presisjon og kan nøyaktig representere et bredt spekter av verdier. I scenarier der komplekse matematiske operasjoner utføres eller høy presisjon er nødvendig, foretrekkes FP32-formatet. Høy presisjon betyr imidlertid også større minnebruk og lengre beregningstid. For storskala dype læringsmodeller, spesielt når det er mange modellparametere og store datamengder, kan FP32-formatet føre til utilstrekkelig GPU-minne eller redusert inferenshastighet.

På mobiltelefoner eller IoT-enheter kan vi konvertere Phi-3.x-modeller til INT4, mens AI-PC / Copilot-PC kan bruke høyere presisjon som INT8, FP16 eller FP32.

For øyeblikket har ulike maskinvareprodusenter forskjellige rammeverk for å støtte generative modeller, som Intels OpenVINO, Qualcomms QNN, Apples MLX og Nvidias CUDA, som kan kombineres med modellkvantisering for lokal distribusjon.

Teknologisk sett har vi støtte for ulike formater etter kvantisering, som PyTorch/Tensorflow-format, GGUF og ONNX. Jeg har gjort en sammenligning av formater og applikasjonsscenarier mellom GGUF og ONNX. Her anbefaler jeg ONNX-kvantisering, som har god støtte fra modellrammeverk til maskinvare. I dette kapittelet vil vi fokusere på ONNX Runtime for GenAI, OpenVINO og Apple MLX for å utføre modellkvantisering (hvis du har en bedre metode, kan du også sende den til oss ved å sende inn en PR).

**Dette kapittelet inkluderer**

1. [Kvantisering av Phi-3.5 / 4 ved bruk av llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantisering av Phi-3.5 / 4 ved bruk av Generative AI-utvidelser for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantisering av Phi-3.5 / 4 ved bruk av Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantisering av Phi-3.5 / 4 ved bruk av Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.