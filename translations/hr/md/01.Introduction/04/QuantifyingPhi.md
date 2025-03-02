# **Kvantizacija Phi obitelji**

Kvantizacija modela odnosi se na proces mapiranja parametara (poput težina i vrijednosti aktivacije) u modelu neuronske mreže iz velikog raspona vrijednosti (obično kontinuiranog raspona) u manji, konačan raspon vrijednosti. Ova tehnologija može smanjiti veličinu i računalnu složenost modela te poboljšati radnu učinkovitost modela u okruženjima s ograničenim resursima, poput mobilnih uređaja ili ugrađenih sustava. Kvantizacija modela postiže kompresiju smanjenjem preciznosti parametara, ali također uvodi određeni gubitak preciznosti. Stoga je u procesu kvantizacije potrebno uravnotežiti veličinu modela, računalnu složenost i preciznost. Uobičajene metode kvantizacije uključuju kvantizaciju s fiksnom točkom, kvantizaciju s pomičnom točkom i druge. Možete odabrati odgovarajuću strategiju kvantizacije prema specifičnom scenariju i potrebama.

Želimo implementirati GenAI model na rubne uređaje i omogućiti većem broju uređaja sudjelovanje u GenAI scenarijima, poput mobilnih uređaja, AI PC-a/Copilot+PC-a i tradicionalnih IoT uređaja. Kroz kvantizirani model možemo ga implementirati na različite rubne uređaje ovisno o tipu uređaja. U kombinaciji s okvirima za ubrzanje modela i kvantiziranim modelima koje pružaju proizvođači hardvera, možemo izgraditi bolje SLM aplikacijske scenarije.

U scenariju kvantizacije imamo različite preciznosti (INT4, INT8, FP16, FP32). Slijedi objašnjenje uobičajenih preciznosti kvantizacije.

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije koja kvantizira težine i vrijednosti aktivacije modela u 4-bitne cijele brojeve. INT4 kvantizacija obično rezultira većim gubitkom preciznosti zbog manjeg raspona vrijednosti i niže preciznosti. Međutim, u usporedbi s INT8 kvantizacijom, INT4 kvantizacija može dodatno smanjiti zahtjeve za pohranom i računalnu složenost modela. Važno je napomenuti da je INT4 kvantizacija relativno rijetka u praktičnim primjenama jer preniska preciznost može uzrokovati značajno pogoršanje performansi modela. Osim toga, nije sav hardver kompatibilan s INT4 operacijama, pa je potrebno uzeti u obzir kompatibilnost hardvera pri odabiru metode kvantizacije.

### **INT8**

INT8 kvantizacija je proces pretvaranja težina i aktivacija modela iz brojeva s pomičnom točkom u 8-bitne cijele brojeve. Iako je raspon vrijednosti predstavljenih INT8 cijelim brojevima manji i manje precizan, može značajno smanjiti zahtjeve za pohranom i računanjem. U INT8 kvantizaciji, težine i vrijednosti aktivacije modela prolaze kroz proces kvantizacije, uključujući skaliranje i pomak, kako bi se što više očuvale izvorne informacije s pomičnom točkom. Tijekom izvođenja, ove kvantizirane vrijednosti dekvantiziraju se natrag u brojeve s pomičnom točkom za izračun, a zatim ponovno kvantiziraju u INT8 za sljedeći korak. Ova metoda može pružiti dovoljnu preciznost u većini primjena uz održavanje visoke računalne učinkovitosti.

### **FP16**

FP16 format, odnosno 16-bitni brojevi s pomičnom točkom (float16), smanjuje memorijski otisak za polovicu u usporedbi s 32-bitnim brojevima s pomičnom točkom (float32), što ima značajne prednosti u aplikacijama za duboko učenje velikih razmjera. FP16 format omogućuje učitavanje većih modela ili obradu više podataka unutar istih ograničenja GPU memorije. Kako moderni GPU hardver sve više podržava FP16 operacije, korištenje FP16 formata može također donijeti poboljšanja u brzini izračuna. Međutim, FP16 format ima i svoje inherentne nedostatke, odnosno nižu preciznost, što može dovesti do numeričke nestabilnosti ili gubitka preciznosti u nekim slučajevima.

### **FP32**

FP32 format pruža višu preciznost i može točno predstaviti širok raspon vrijednosti. U scenarijima gdje se izvode složene matematičke operacije ili su potrebni visoko precizni rezultati, preferira se FP32 format. Međutim, visoka preciznost također znači veću upotrebu memorije i dulje vrijeme izračuna. Za modele dubokog učenja velikih razmjera, osobito kada postoji mnogo parametara modela i ogromna količina podataka, FP32 format može uzrokovati nedostatak GPU memorije ili smanjenje brzine izvođenja.

Na mobilnim uređajima ili IoT uređajima možemo pretvoriti Phi-3.x modele u INT4, dok AI PC / Copilot PC mogu koristiti veću preciznost poput INT8, FP16, FP32.

Trenutno različiti proizvođači hardvera imaju različite okvire za podršku generativnim modelima, poput Intelovog OpenVINO-a, Qualcommovog QNN-a, Appleovog MLX-a i Nvidia CUDA-e, itd., koji u kombinaciji s kvantizacijom modela omogućuju lokalnu implementaciju.

S tehničkog aspekta, nakon kvantizacije imamo različite formate podrške, poput PyTorch / Tensorflow formata, GGUF-a i ONNX-a. Napravio sam usporedbu formata i aplikacijskih scenarija između GGUF-a i ONNX-a. Ovdje preporučujem ONNX kvantizacijski format, koji ima dobru podršku od modelskog okvira do hardvera. U ovom poglavlju fokusirat ćemo se na ONNX Runtime za GenAI, OpenVINO i Apple MLX za provođenje kvantizacije modela (ako imate bolji način, možete nam ga predložiti podnošenjem PR-a).

**Ovo poglavlje uključuje**

1. [Kvantizacija Phi-3.5 / 4 pomoću llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizacija Phi-3.5 / 4 pomoću proširenja za generativnu umjetnu inteligenciju za onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizacija Phi-3.5 / 4 pomoću Intel OpenVINO-a](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizacija Phi-3.5 / 4 pomoću Apple MLX okvira](./UsingAppleMLXQuantifyingPhi.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću usluga strojno baziranog AI prevođenja. Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.