# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Muundo wa RAG

Muundo wa RAG na Phi-3.5 Onnx Hosted model unatumia mbinu ya Retrieval-Augmented Generation, ikichanganya nguvu za modeli za Phi-3.5 na ONNX hosting kwa ajili ya matumizi bora ya AI. Muundo huu ni muhimu katika kurekebisha modeli kwa kazi maalum za kikoa, ukitoa mchanganyiko wa ubora, ufanisi wa gharama, na uelewa wa muktadha mrefu. Ni sehemu ya huduma za Azure AI, ikitoa aina mbalimbali za modeli ambazo ni rahisi kupatikana, kujaribu, na kutumia, zikiwa zimeundwa kukidhi mahitaji ya ubinafsishaji wa viwanda tofauti.

## WebGPU ni nini  
WebGPU ni API ya kisasa ya michoro za wavuti iliyoundwa kutoa upatikanaji wa moja kwa moja wa GPU ya kifaa kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mrithi wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Utangamano na GPU za Kisasa**: WebGPU imejengwa kufanya kazi bila matatizo na usanifu wa kisasa wa GPU, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.
2. **Utendaji Bora**: Inasaidia mahesabu ya GPU kwa madhumuni ya jumla na operesheni za haraka, hivyo kufaa kwa michoro za picha na kazi za ujifunzaji wa mashine.
3. **Vipengele Vilivyoboreshwa**: WebGPU inatoa ufikiaji wa uwezo wa juu wa GPU, ikiwezesha kazi ngumu zaidi na za nguvu za picha na mahesabu.
4. **Kupunguza Mzigo wa JavaScript**: Kwa kuhamisha kazi nyingi zaidi kwa GPU, WebGPU inapunguza mzigo wa JavaScript kwa kiasi kikubwa, hivyo kuleta utendaji bora na uzoefu laini.

WebGPU kwa sasa inaungwa mkono na vivinjari kama Google Chrome, huku kazi ikiendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU
Mahitaji ya Mazingira:

**Vivinjari vinavyoungwa mkono:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.  

### Kuwasha WebGPU:

- Katika Chrome/Microsoft Edge  

Washa `chrome://flags/#enable-unsafe-webgpu` flag.

#### Fungua Kivinjari Chako:  
Zindua Google Chrome au Microsoft Edge.

#### Fikia Ukurasa wa Flags:  
Katika upau wa anwani, andika `chrome://flags` na bonyeza Enter.

#### Tafuta Flag:  
Katika kisanduku cha utaftaji juu ya ukurasa, andika 'enable-unsafe-webgpu'

#### Washa Flag:  
Tafuta flag ya #enable-unsafe-webgpu katika orodha ya matokeo.

Bonyeza menyu ya kushuka karibu nayo na uchague Enabled.

#### Anzisha Upya Kivinjari Chako:

Baada ya kuwasha flag, utahitaji kuanzisha upya kivinjari chako ili mabadiliko yaanze kufanya kazi. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.

- Kwa Linux, zindua kivinjari na `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU tayari imewashwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config kwenye upau wa anwani na `set dom.webgpu.enabled to true`.  

### Kuweka GPU kwa Microsoft Edge  

Hizi hapa hatua za kuweka GPU yenye utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Mipangilio:** Bonyeza kwenye menyu ya Start na uchague Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System halafu Display.  
- **Mipangilio ya Michoro:** Shuka chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app halafu Browse.  
- **Chagua Edge:** Nenda kwenye folda ya usakinishaji wa Edge (kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na uchague `msedge.exe`.  
- **Weka Upendeleo:** Bonyeza Options, chagua High performance, halafu bonyeza Save.  
Hii itahakikisha kwamba Microsoft Edge inatumia GPU yako yenye utendaji wa juu kwa utendaji bora.  
- **Anzisha Upya** kompyuta yako ili mipangilio hii ianze kufanya kazi.  

### Sampuli: Tafadhali [bonyeza kiungo hiki](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kiakili za mashine. Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.