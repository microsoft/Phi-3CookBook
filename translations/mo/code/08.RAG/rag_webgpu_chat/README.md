Phi-3-mini WebGPU RAG Chatbot

## Demo hanefaka WebGPU sy RAG Pattern
Ny RAG Pattern miaraka amin'ny modely Phi-3 Onnx Hosted dia mampiasa ny fomba Retrieval-Augmented Generation, izay manambatra ny herin'ny modely Phi-3 sy ny ONNX hosting ho an'ny fampiharana AI mahomby. Ity lamina ity dia tena ilaina amin'ny fanatsarana modely ho an'ny asa manokana amin'ny sehatra iray, manolotra fitambarana kalitao, fahombiazana ara-toekarena, ary fahatakarana sehatra lava kokoa. Anisan'ny tolotra Azure AI izy io, manome modely isan-karazany mora hita, andramana, ary ampiasaina, mifanaraka amin'ny filan'ny indostria maro. Ny modely Phi-3, anisan'izany ny Phi-3-mini, Phi-3-small, ary Phi-3-medium, dia hita ao amin'ny Azure AI Model Catalog ary azo fintinina sy ampiharina amin'ny fomba mahaleo tena na amin'ny alàlan'ny sehatra toy ny HuggingFace sy ONNX, manaporofo ny fanoloran-tenan'i Microsoft amin'ny famahana sy fahazoana miditra amin'ny AI.

## Inona ny WebGPU 
Ny WebGPU dia API vaovao ho an'ny sary anaty tranonkala izay natao hanomezana fidirana mahomby amin'ny unitan'ny fikarakarana sary (GPU) mivantana avy amin'ny mpitety tranonkala. Izy io dia natao ho mpandimby ny WebGL, manolotra fanatsarana lehibe:

1. **Fifanarahana amin'ny GPU maoderina**: Ny WebGPU dia natao hiasa tsy misy olana amin'ny rafitra GPU ankehitriny, mampiasa API rafitra toy ny Vulkan, Metal, ary Direct3D 12.
2. **Fampisehoana nohatsaraina**: Manohana ny kajy ankapobeny amin'ny GPU sy ny asa haingana kokoa izy io, mahatonga azy ho mety amin'ny fandikana sary sy ny asa fianarana milina.
3. **Fitaovana mandroso**: Ny WebGPU dia manome fidirana amin'ny fahaiza-manao GPU mandroso kokoa, ahafahana manao asa sarotra sy miovaova kokoa amin'ny sary sy kajy.
4. **Fihenan'ny asa JavaScript**: Amin'ny alàlan'ny fanomezana asa bebe kokoa ho an'ny GPU, ny WebGPU dia mampihena be ny enta-mavesatry ny JavaScript, ka mitarika ho amin'ny fampisehoana tsara kokoa sy traikefa malefaka kokoa.

Ny WebGPU dia tohanana amin'izao fotoana izao amin'ny mpitety tranonkala toy ny Google Chrome, ary mbola eo am-panitarana ny fanohanana amin'ny sehatra hafa.

### 03.WebGPU
Tontolo iainana takiana:

**Mpitety tranonkala tohanana:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Ampidiro ny WebGPU:

- Ao amin'ny Chrome/Microsoft Edge 

Alefaso ny `chrome://flags/#enable-unsafe-webgpu` flag.

#### Sokafy ny Mpitety Tranokalanao:
Atombohy ny Google Chrome na Microsoft Edge.

#### Midira amin'ny Pejin'ny Flags:
Ao amin'ny bara adiresy, soraty `chrome://flags` ary tsindrio Enter.

#### Tadiavo ny Flag:
Ao amin'ny boaty fikarohana eo an-tampon'ny pejy, soraty 'enable-unsafe-webgpu'

#### Alefaso ny Flag:
Tadiavo ny flag #enable-unsafe-webgpu ao amin'ny lisitry ny valiny.

Tsindrio ny menio midina eo akaikiny ary fidio Enabled.

#### Avereno ny Mpitety Tranokalanao:

Rehefa alefa ny flag, mila averinao ny mpitety tranokala mba hisy fiantraikany ny fanovana. Tsindrio ny bokotra Relaunch izay miseho eo ambanin'ny pejy.

- Ho an'ny Linux, alefaso ny mpitety tranokala miaraka amin'ny `--enable-features=Vulkan`.
- Ny Safari 18 (macOS 15) dia manana WebGPU efa alefa amin'ny alàlana default.
- Ao amin'ny Firefox Nightly, midira about:config ao amin'ny bara adiresy ary `set dom.webgpu.enabled to true`.

### Fametrahana GPU ho an'ny Microsoft Edge 

Ireto misy dingana hanamboarana GPU mahery vaika ho an'ny Microsoft Edge amin'ny Windows:

- **Sokafy ny Settings:** Tsindrio ny menio Start ary fidio Settings.
- **Settings System:** Mankanesa any amin'ny System ary avy eo Display.
- **Settings Graphics:** Milentika midina ary tsindrio Graphics settings.
- **Safidio ny App:** Eo ambanin'ny “Choose an app to set preference,” safidio Desktop app ary avy eo Browse.
- **Safidio ny Edge:** Mankanesa any amin'ny lahatahiry fametrahana Edge (matetika `C:\Program Files (x86)\Microsoft\Edge\Application`) ary safidio `msedge.exe`.
- **Apetraho ny Safidy:** Tsindrio Options, safidio High performance, ary avy eo tsindrio Save.
Izany dia hiantoka fa mampiasa ny GPU mahery vaika ho an'ny Edge ianao mba hahazoana fampisehoana tsara kokoa. 
- **Avereno** ny solosainao mba hisy fiantraikany ireo fanovana ireo.

### Sokafy ny Codespace-nao:
Mankanesa any amin'ny tahirinao ao amin'ny GitHub.
Tsindrio ny bokotra Code ary safidio Open with Codespaces.

Raha tsy manana Codespace ianao dia afaka mamorona iray amin'ny fipihana New codespace.

**Fanamarihana** Fametrahana Tontolo iainana Node ao amin'ny Codespace-nao
Ny fampandehanana demo npm avy amin'ny GitHub Codespace dia fomba tsara hanandramana sy hampivelarana ny tetikasanao. Ireto misy torolalana tsikelikely hanampy anao hanomboka:

### Amboary ny Tontolo Iainanao:
Rehefa misokatra ny Codespace-nao, ataovy azo antoka fa manana Node.js sy npm napetraka ianao. Azonao atao ny manamarina izany amin'ny fanatanterahana:
```
node -v
```
```
npm -v
```

Raha tsy napetraka izy ireo, azonao atao ny mametraka azy ireo amin'ny alàlan'ny:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Mankanesa any amin'ny Lahatahiry Tetikasanao:
Ampiasao ny terminal mba hankanesana any amin'ny lahatahiry misy ny tetikasa npm-nao:
```
cd path/to/your/project
```

### Mametraha Dependencies:
Alefaso ny baiko manaraka mba hametrahana ny dependencies rehetra voalaza ao amin'ny rakitra package.json-nao:

```
npm install
```

### Alefaso ny Demo:
Rehefa napetraka ny dependencies dia azonao atao ny mampandeha ny script demo-nao. Matetika izany dia voalaza ao amin'ny fizarana scripts ao amin'ny package.json. Ohatra, raha ny script demo-nao dia antsoina hoe start, dia azonao atao ny manatanteraka:

```
npm run build
```
```
npm run dev
```

### Midira amin'ny Demo:
Raha misy mpizara tranonkala tafiditra ao amin'ny demo-nao, ny Codespaces dia hanome URL ahafahana miditra aminy. Tadiavo ny fampandrenesana na zahao ny tabilao Ports mba hahitana ny URL.

**Fanamarihana:** Mila tehirizina ao amin'ny mpitety tranokala ny modely, ka mety haka fotoana kely ny famoahana azy. 

### RAG Demo
Ampidiro ny rakitra markdown `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Safidio ny Rakitrao:
Tsindrio ny bokotra milaza hoe “Choose File” mba hisafidianana ny rakitra tianao hampidirina.

### Ampidiro ny Rakitra:
Rehefa avy nisafidy ny rakitra ianao, tsindrio ny bokotra “Upload” mba hampidirana ny rakitrao ho an'ny RAG (Retrieval-Augmented Generation).

### Atombohy ny Resaka:
Rehefa tafiditra ny rakitra dia azonao atao ny manomboka fivoriana firesahana mampiasa RAG mifototra amin'ny votoatin'ny rakitrao.

It seems like you want the text translated to "mo," but it's unclear what language "mo" refers to. Could you clarify which language you'd like the text translated into? Some possibilities might include Māori, Mongolian, or another language. Let me know so I can assist you further!