# **Kvantifiering av Phi-familjen**

Modellkvantisering avser processen att mappa parametrarna (såsom vikter och aktiveringsvärden) i en neuralt nätverksmodell från ett stort värdeintervall (vanligtvis ett kontinuerligt värdeintervall) till ett mindre, ändligt värdeintervall. Denna teknik kan minska modellens storlek och beräkningskomplexitet samt förbättra modellens driftseffektivitet i resursbegränsade miljöer, såsom mobila enheter eller inbyggda system. Modellkvantisering uppnår kompression genom att minska precisionen på parametrarna, men det introducerar också en viss förlust av noggrannhet. Därför är det viktigt att balansera modellens storlek, beräkningskomplexitet och precision under kvantiseringsprocessen. Vanliga kvantiseringsmetoder inkluderar fastpunktskvantisering, flyttalskvantisering, med mera. Du kan välja en lämplig kvantiseringsstrategi beroende på det specifika scenariot och behoven.

Vi hoppas kunna distribuera GenAI-modellen till edge-enheter och möjliggöra att fler enheter kan delta i GenAI-scenarier, såsom mobila enheter, AI-PC/Copilot+PC och traditionella IoT-enheter. Genom att använda en kvantiserad modell kan vi distribuera den till olika edge-enheter baserat på deras specifikationer. I kombination med accelerationsramverk och kvantiseringsmodeller som tillhandahålls av hårdvarutillverkare kan vi skapa bättre SLM-applikationsscenarier.

I kvantiseringsscenarier har vi olika precisionsnivåer (INT4, INT8, FP16, FP32). Nedan följer en förklaring av de vanligaste kvantiseringsprecisionsnivåerna.

### **INT4**

INT4-kvantisering är en radikal kvantiseringsmetod som kvantiserar modellens vikter och aktiveringsvärden till 4-bitars heltal. INT4-kvantisering leder vanligtvis till en större förlust av noggrannhet på grund av det mindre representationsintervallet och den lägre precisionen. Dock kan INT4-kvantisering, jämfört med INT8, ytterligare minska modellens lagringskrav och beräkningskomplexitet. Det är viktigt att notera att INT4-kvantisering är relativt ovanlig i praktiska tillämpningar eftersom den låga noggrannheten kan orsaka betydande försämring av modellens prestanda. Dessutom stöds inte INT4-operationer av all hårdvara, så hårdvarukompatibilitet måste beaktas när man väljer kvantiseringsmetod.

### **INT8**

INT8-kvantisering innebär att modellens vikter och aktiveringar konverteras från flyttal till 8-bitars heltal. Även om det numeriska intervallet som representeras av INT8-heltal är mindre och mindre precist, kan det avsevärt minska lagrings- och beräkningskraven. Vid INT8-kvantisering genomgår modellens vikter och aktiveringsvärden en kvantiseringsprocess, inklusive skalning och offset, för att bevara så mycket som möjligt av den ursprungliga flyttalsinformationen. Under inferens dekvantiseras dessa kvantiserade värden tillbaka till flyttal för beräkning och kvantiseras sedan tillbaka till INT8 för nästa steg. Denna metod kan ge tillräcklig noggrannhet i de flesta tillämpningar samtidigt som den bibehåller hög beräkningseffektivitet.

### **FP16**

FP16-formatet, det vill säga 16-bitars flyttal (float16), halverar minnesanvändningen jämfört med 32-bitars flyttal (float32), vilket har betydande fördelar i storskaliga djupinlärningsapplikationer. FP16-formatet möjliggör laddning av större modeller eller bearbetning av mer data inom samma GPU-minnesbegränsningar. I takt med att modern GPU-hårdvara fortsätter att stödja FP16-operationer kan användning av FP16-formatet också medföra förbättringar i beräkningshastighet. Dock har FP16-formatet också sina inneboende nackdelar, nämligen lägre precision, vilket kan leda till numerisk instabilitet eller förlust av noggrannhet i vissa fall.

### **FP32**

FP32-formatet erbjuder högre precision och kan noggrant representera ett brett spektrum av värden. I scenarier där komplexa matematiska operationer utförs eller högprecisionsresultat krävs, föredras FP32-formatet. Dock innebär hög precision också högre minnesanvändning och längre beräkningstid. För storskaliga djupinlärningsmodeller, särskilt när det finns många modellparametrar och en enorm mängd data, kan FP32-formatet orsaka otillräckligt GPU-minne eller minskad inferenshastighet.

På mobila enheter eller IoT-enheter kan vi konvertera Phi-3.x-modeller till INT4, medan AI-PC/Copilot-PC kan använda högre precision, såsom INT8, FP16, FP32.

För närvarande har olika hårdvarutillverkare olika ramverk för att stödja generativa modeller, såsom Intels OpenVINO, Qualcomms QNN, Apples MLX och Nvidias CUDA, med stöd av modellkvantisering för lokal distribution.

Tekniskt sett har vi olika formatstöd efter kvantisering, såsom PyTorch/Tensorflow-format, GGUF och ONNX. Jag har gjort en jämförelse av format och applikationsscenarier mellan GGUF och ONNX. Här rekommenderar jag ONNX-kvantisering, som har bra stöd från modellramverk till hårdvara. I detta kapitel kommer vi att fokusera på ONNX Runtime för GenAI, OpenVINO och Apple MLX för att utföra modellkvantisering (om du har ett bättre sätt kan du också bidra genom att skicka in en PR).

**Detta kapitel inkluderar**

1. [Kvantisering av Phi-3.5/4 med llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantisering av Phi-3.5/4 med generativa AI-tillägg för onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantisering av Phi-3.5/4 med Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantisering av Phi-3.5/4 med Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt ursprungsspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.