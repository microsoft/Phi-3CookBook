Phi-3-mini WebGPU RAG Chatbot

## Demo ya kuonyesha WebGPU na Mfumo wa RAG
Mfumo wa RAG na Phi-3 Onnx Hosted model unatumia mbinu ya Retrieval-Augmented Generation, ukichanganya uwezo wa mifano ya Phi-3 na mwenyeji wa ONNX kwa ajili ya utekelezaji wa AI wenye ufanisi. Mfumo huu ni muhimu katika kurekebisha mifano kwa kazi maalum za kikoa, ukitoa mchanganyiko wa ubora, gharama nafuu, na uelewa wa muktadha mrefu. Ni sehemu ya suite ya Azure AI, inayotoa uteuzi mpana wa mifano ambayo ni rahisi kupata, kujaribu, na kutumia, ikikidhi mahitaji ya ubinafsishaji ya sekta mbalimbali. Mifano ya Phi-3, ikijumuisha Phi-3-mini, Phi-3-small, na Phi-3-medium, inapatikana kwenye Azure AI Model Catalog na inaweza kurekebishwa na kutekelezwa kwa kujitegemea au kupitia majukwaa kama HuggingFace na ONNX, ikionyesha dhamira ya Microsoft katika kutoa suluhisho za AI zinazopatikana na zenye ufanisi.

## WebGPU ni nini
WebGPU ni API ya kisasa ya michoro ya wavuti iliyoundwa ili kutoa ufikiaji wa moja kwa moja wa GPU ya kifaa kutoka kwa vivinjari vya wavuti. Inakusudiwa kuwa mrithi wa WebGL, ikitoa maboresho kadhaa muhimu:

1. **Utangamano na GPU za Kisasa**: WebGPU imejengwa kufanya kazi bila matatizo na miundo ya kisasa ya GPU, ikitumia API za mfumo kama Vulkan, Metal, na Direct3D 12.
2. **Utendaji Bora**: Inasaidia mahesabu ya GPU kwa madhumuni ya jumla na operesheni za haraka, kuifanya kufaa kwa michoro na kazi za ujifunzaji wa mashine.
3. **Vipengele vya Juu**: WebGPU inatoa ufikiaji wa uwezo wa juu wa GPU, kuwezesha kazi za michoro na mahesabu zilizo ngumu zaidi na za nguvu.
4. **Kupunguza Kazi ya JavaScript**: Kwa kupunguza kazi zaidi kwa GPU, WebGPU inapunguza sana mzigo wa JavaScript, ikileta utendaji bora na uzoefu laini.

Kwa sasa, WebGPU inasaidiwa katika vivinjari kama Google Chrome, huku kazi ikiendelea kupanua msaada kwa majukwaa mengine.

### 03.WebGPU
Mazingira Yanayohitajika:

**Vivinjari Vinavyosaidiwa:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.  

### Kuwezesha WebGPU:

- Katika Chrome/Microsoft Edge  

Washa `chrome://flags/#enable-unsafe-webgpu` flag.

#### Fungua Kivinjari Chako:
Zindua Google Chrome au Microsoft Edge.

#### Fikia Ukurasa wa Flags:
Kwenye upau wa anwani, andika `chrome://flags` na bonyeza Enter.

#### Tafuta Flag:
Kwenye kisanduku cha utaftaji juu ya ukurasa, andika 'enable-unsafe-webgpu'

#### Washa Flag:
Tafuta flag ya #enable-unsafe-webgpu kwenye orodha ya matokeo.  
Bonyeza menyu ya kushuka karibu nayo na uchague Enabled.

#### Anzisha Upya Kivinjari Chako:
Baada ya kuwasha flag, utahitaji kuanzisha upya kivinjari chako ili mabadiliko yaanze kutumika. Bonyeza kitufe cha Relaunch kinachoonekana chini ya ukurasa.  

- Kwa Linux, zindua kivinjari na `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) ina WebGPU tayari imewezeshwa kwa chaguo-msingi.  
- Katika Firefox Nightly, ingiza about:config kwenye upau wa anwani na `set dom.webgpu.enabled to true`.  

### Kuweka GPU kwa Microsoft Edge  

Hapa kuna hatua za kuweka GPU ya utendaji wa juu kwa Microsoft Edge kwenye Windows:

- **Fungua Mipangilio:** Bonyeza kwenye menyu ya Start na uchague Settings.  
- **Mipangilio ya Mfumo:** Nenda kwenye System kisha Display.  
- **Mipangilio ya Michoro:** Tembea chini na bonyeza Graphics settings.  
- **Chagua Programu:** Chini ya “Choose an app to set preference,” chagua Desktop app kisha Browse.  
- **Chagua Edge:** Nenda kwenye folda ya usakinishaji ya Edge (kawaida `C:\Program Files (x86)\Microsoft\Edge\Application`) na chagua `msedge.exe`.  
- **Weka Mapendeleo:** Bonyeza Options, chagua High performance, kisha bonyeza Save.  
Hii itahakikisha kwamba Microsoft Edge inatumia GPU yako ya utendaji wa juu kwa utendaji bora.  
- **Anzisha Upya** kompyuta yako ili mipangilio hii ianze kutumika.  

### Fungua Codespace Yako:
Nenda kwenye hazina yako kwenye GitHub.  
Bonyeza kitufe cha Code na uchague Open with Codespaces.  

Ikiwa huna Codespace bado, unaweza kuunda moja kwa kubonyeza New codespace.  

**Kumbuka** Kusakinisha Mazingira ya Node kwenye codespace yako  
Kuendesha demo ya npm kutoka Codespace ya GitHub ni njia nzuri ya kujaribu na kuendeleza mradi wako. Hapa kuna mwongozo wa hatua kwa hatua wa kukusaidia kuanza:

### Sanidi Mazingira Yako:
Mara Codespace yako inapofunguka, hakikisha una Node.js na npm vimesakinishwa. Unaweza kuangalia hili kwa kuendesha:  
```
node -v
```  
```
npm -v
```  

Ikiwa hazijasakinishwa, unaweza kuzisakinisha kwa kutumia:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```  

### Nenda kwenye Saraka ya Mradi Wako:
Tumia terminal kuingia kwenye saraka ambapo mradi wako wa npm upo:  
```
cd path/to/your/project
```  

### Sakinisha Mahitaji:
Endesha amri ifuatayo kusakinisha mahitaji yote muhimu yaliyoorodheshwa kwenye faili yako ya package.json:  

```
npm install
```  

### Endesha Demo:
Mara mahitaji yanaposakinishwa, unaweza kuendesha script yako ya demo. Hii kwa kawaida hufafanuliwa katika sehemu ya scripts ya package.json yako. Kwa mfano, ikiwa script yako ya demo inaitwa start, unaweza kuendesha:  

```
npm run build
```  
```
npm run dev
```  

### Fikia Demo:
Ikiwa demo yako inahusisha seva ya wavuti, Codespaces itatoa URL ya kuifikia. Tafuta arifa au angalia kichupo cha Ports ili kupata URL.  

**Kumbuka:** Mfano unahitaji kuhifadhiwa kwenye kivinjari, kwa hivyo inaweza kuchukua muda kupakia.  

### Demo ya RAG
Pakia faili ya markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`  

### Chagua Faili Yako:
Bonyeza kitufe kinachosema “Choose File” kuchagua hati unayotaka kupakia.  

### Pakia Hati:
Baada ya kuchagua faili yako, bonyeza kitufe cha “Upload” kupakia hati yako kwa RAG (Retrieval-Augmented Generation).  

### Anza Gumzo Lako:
Mara hati inapopakiwa, unaweza kuanza kikao cha gumzo ukitumia RAG kulingana na yaliyomo kwenye hati yako.  

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.