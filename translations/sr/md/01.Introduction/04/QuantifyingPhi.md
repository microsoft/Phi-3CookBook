# **Kvantifikacija Phi porodice**

Kvantizacija modela odnosi se na proces mapiranja parametara (kao što su težine i vrednosti aktivacija) u modelu neuronske mreže sa velikog opsega vrednosti (obično kontinuiranog opsega) na manji, konačan opseg vrednosti. Ova tehnologija može smanjiti veličinu i računsku složenost modela i poboljšati efikasnost rada modela u okruženjima sa ograničenim resursima, kao što su mobilni uređaji ili ugrađeni sistemi. Kvantizacija modela postiže kompresiju smanjenjem preciznosti parametara, ali takođe uvodi određeni gubitak preciznosti. Stoga je tokom procesa kvantizacije potrebno balansirati veličinu modela, računsku složenost i preciznost. Uobičajene metode kvantizacije uključuju kvantizaciju sa fiksnom tačkom, kvantizaciju sa pokretnom tačkom itd. Možete odabrati odgovarajuću strategiju kvantizacije u zavisnosti od konkretne situacije i potreba.

Naš cilj je da GenAI modele implementiramo na uređaje na ivici mreže i omogućimo većem broju uređaja da učestvuju u GenAI scenarijima, poput mobilnih uređaja, AI PC/Copilot+PC i tradicionalnih IoT uređaja. Kroz kvantizovane modele možemo ih prilagoditi različitim uređajima na ivici mreže. Kombinovanjem sa okvirima za ubrzanje modela i kvantizovanim modelima koje pružaju proizvođači hardvera, možemo izgraditi bolje SLM aplikacione scenarije.

U kvantizacionim scenarijima imamo različite nivoe preciznosti (INT4, INT8, FP16, FP32). Slede objašnjenja najčešće korišćenih nivoa kvantizacije:

### **INT4**

INT4 kvantizacija je radikalna metoda kvantizacije koja kvantizuje težine i vrednosti aktivacija modela u 4-bitne celobrojne vrednosti. INT4 kvantizacija obično dovodi do većeg gubitka preciznosti zbog manjeg opsega reprezentacije i niže preciznosti. Međutim, u poređenju sa INT8 kvantizacijom, INT4 kvantizacija može dodatno smanjiti zahteve za skladištenjem i računsku složenost modela. Treba napomenuti da je INT4 kvantizacija relativno retka u praktičnim primenama, jer preniska preciznost može izazvati značajno pogoršanje performansi modela. Pored toga, nisu svi hardverski uređaji kompatibilni sa INT4 operacijama, pa treba uzeti u obzir kompatibilnost hardvera prilikom izbora metode kvantizacije.

### **INT8**

INT8 kvantizacija je proces pretvaranja težina i aktivacija modela iz brojeva sa pokretnom tačkom u 8-bitne celobrojne vrednosti. Iako je opseg vrednosti koje predstavljaju INT8 celobrojne vrednosti manji i manje precizan, može značajno smanjiti zahteve za skladištenjem i računanjem. Kod INT8 kvantizacije, težine i vrednosti aktivacija modela prolaze kroz proces kvantizacije, uključujući skaliranje i pomeranje, kako bi se što je moguće više sačuvale originalne informacije sa pokretnom tačkom. Tokom inferencije, ove kvantizovane vrednosti se dekvantizuju nazad u brojeve sa pokretnom tačkom za računanje, a zatim ponovo kvantizuju u INT8 za sledeći korak. Ova metoda može pružiti dovoljnu preciznost u većini aplikacija, uz održavanje visoke računske efikasnosti.

### **FP16**

FP16 format, tj. 16-bitni brojevi sa pokretnom tačkom (float16), smanjuje memorijski otisak za polovinu u poređenju sa 32-bitnim brojevima sa pokretnom tačkom (float32), što ima značajne prednosti u aplikacijama za duboko učenje velikih razmera. FP16 format omogućava učitavanje većih modela ili obradu više podataka unutar istih ograničenja GPU memorije. Kako savremeni GPU uređaji sve više podržavaju FP16 operacije, korišćenje FP16 formata može doneti i poboljšanja u brzini obrade. Međutim, FP16 format ima i svoje inherentne nedostatke, poput niže preciznosti, što može dovesti do numeričke nestabilnosti ili gubitka preciznosti u nekim slučajevima.

### **FP32**

FP32 format pruža viši nivo preciznosti i može tačno predstaviti širok opseg vrednosti. U scenarijima gde se izvode složene matematičke operacije ili su potrebni rezultati visoke preciznosti, FP32 format je poželjan. Međutim, visoka preciznost takođe znači veću potrošnju memorije i duže vreme računanja. Za modele dubokog učenja velikih razmera, posebno kada postoji mnogo parametara modela i ogromna količina podataka, FP32 format može izazvati nedostatak GPU memorije ili smanjenje brzine inferencije.

Na mobilnim uređajima ili IoT uređajima možemo konvertovati Phi-3.x modele u INT4, dok AI PC / Copilot PC može koristiti veću preciznost, poput INT8, FP16, FP32.

Trenutno različiti proizvođači hardvera imaju različite okvire za podršku generativnim modelima, poput Intelovog OpenVINO, Qualcommovog QNN, Appleovog MLX i Nvidia-inog CUDA. Kombinovanjem sa kvantizacijom modela možemo ostvariti lokalnu implementaciju.

Što se tiče tehnologije, nakon kvantizacije imamo podršku za različite formate, kao što su PyTorch / Tensorflow format, GGUF i ONNX. Uradio sam poređenje formata i scenarija primene između GGUF i ONNX. Ovde preporučujem ONNX format za kvantizaciju, jer ima dobru podršku od modelskog okvira do hardvera. U ovom poglavlju fokusiraćemo se na ONNX Runtime za GenAI, OpenVINO i Apple MLX za sprovođenje kvantizacije modela (ako imate bolji način, možete ga podeliti sa nama podnošenjem PR-a).

**Ovo poglavlje uključuje**

1. [Kvantizacija Phi-3.5 / 4 koristeći llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Kvantizacija Phi-3.5 / 4 koristeći ekstenzije za generativni AI u onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Kvantizacija Phi-3.5 / 4 koristeći Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Kvantizacija Phi-3.5 / 4 koristeći Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских AI услуга за превођење. Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала коришћењем овог превода.