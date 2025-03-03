# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU සහ RAG ආකෘතිය ප්‍රදර්ශනය කිරීම සඳහා ඩෙමෝව

Phi-3.5 Onnx Hosted ආකෘතිය සමඟ RAG ආකෘතිය Retrieval-Augmented Generation ක්‍රමවේදය යොදා ගනිමින්, ONNX සත්කාරකය මගින් කාර්යක්ෂම AI යෙදුම් සඳහා Phi-3.5 ආකෘතිවල ශක්තිය එකතු කරයි. මෙම ආකෘතිය විශේෂිත ක්ෂේත්‍ර කාර්යයන් සඳහා ආකෘති සන්සුන් කිරීමේදී ප්‍රයෝජනවත් වන අතර, ගුණාත්මකභාවය, පිරිවැය කාර්යක්ෂමතාවය, සහ දිගු-පරිපාලන අවබෝධය අතර මධ්‍යස්ථිතියක් ලබා දේ. මෙය Azure AI සූට් එකේ කොටසක් වන අතර, විවිධ කර්මාන්ත අවශ්‍යතා සඳහා අභිරුචි කිරීමට පහසු ලෙස ආකෘති විශාලතම එකතුවක් සපයයි.

## WebGPU කියන්නේ කුමක්ද?  
WebGPU යනු නවීන වෙබ් ග්‍රැෆික්ස් API එකක් වන අතර, වෙබ් බ්‍රව්සර වලින් සෘජුවම උපාංගයක ග්‍රැෆික්ස් සැකසුම් ඒකකය (GPU) වෙත කාර්යක්ෂම ප්‍රවේශයක් ලබා දීම සඳහා නිර්මාණය කර ඇත. මෙය WebGL හි අනුප්‍රාප්තිකය ලෙස සැලකෙන අතර, මූලික වාසි කිහිපයක් ලබා දේ:

1. **නවීන GPU සමඟ සන්සුන්තාවය**: WebGPU නවීන GPU ව්‍යුහයන් සමඟ නිරවුල්ව ක්‍රියා කිරීමට නිර්මාණය කර ඇති අතර, Vulkan, Metal, සහ Direct3D 12 වැනි පද්ධති API භාවිතා කරයි.
2. **කාර්ය සාධනය වැඩි කිරීම**: මෙය පොදු-අරමුණු GPU ගණනය කිරීම් සහ වේගවත් මෙහෙයුම් සඳහා සහය දක්වයි, ග්‍රැෆික්ස් රෙන්ඩරින් සහ යන්ත්‍රය අධ්‍යයන කාර්යයන් සඳහා සුදුසු වේ.
3. **උසස් විශේෂාංග**: WebGPU නවීන GPU හැකියාවන් වෙත ප්‍රවේශය ලබා දෙන අතර, සංකීර්ණ සහ ගතික ග්‍රැෆික්ස් සහ ගණනික කාර්යබහුලතාවයන් සඳහා ඉඩ සලසයි.
4. **JavaScript වැඩබර අඩු කිරීම**: වැඩි වැඩක් GPU වෙත පැවරීම මගින්, WebGPU JavaScript හි වැඩබරය සීග්‍රයෙන් අඩු කරයි, වැඩි කාර්ය සාධනයක් සහ මෘදු අත්දැකීම් ලබා දේ.

WebGPU දැනට Google Chrome වැනි බ්‍රව්සරවල සහය ලබන අතර, අනෙකුත් වේදිකාවන් වෙත සහය පුළුල් කිරීමේ වැඩ කටයුතු සිදු වෙමින් පවතී.

### 03.WebGPU  
අවශ්‍ය පරිසරය:

**සහාය ලැබෙන බ්‍රව්සර:**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU සක්‍රිය කිරීම:

- Chrome/Microsoft Edge තුළ  

`chrome://flags/#enable-unsafe-webgpu` ප්‍රධානය සක්‍රිය කරන්න.

#### ඔබේ බ්‍රව්සරය විවෘත කරන්න:  
Google Chrome හෝ Microsoft Edge ආරම්භ කරන්න.

#### ප්‍රධාන පිටුවට ප්‍රවේශ වන්න:  
ලිපින තීරුවේ `chrome://flags` ටයිප් කර Enter ඔබන්න.

#### ප්‍රධානය සෙවීම:  
පිටුවේ ඉහළ ඇති සෙවුම් කොටුවේ 'enable-unsafe-webgpu' ටයිප් කරන්න.

#### ප්‍රධානය සක්‍රිය කරන්න:  
ප්‍රතිඵල ලැයිස්තුවේ #enable-unsafe-webgpu ප්‍රධානය සොයාගන්න.

ඊට අසල ඇති ඩ්‍රොප්ඩවුන් මෙනුව ක්ලික් කර Enabled තෝරන්න.

#### ඔබේ බ්‍රව්සරය නැවත ආරම්භ කරන්න:  

ප්‍රධානය සක්‍රිය කිරීමෙන් පසු, වෙනස්කම් බලපැවැත්වීම සඳහා ඔබේ බ්‍රව්සරය නැවත ආරම්භ කළ යුතුය. පිටුගැටුම් බොත්තම ක්ලික් කරන්න.

- Linux සඳහා, `--enable-features=Vulkan` සමඟ බ්‍රව්සරය ආරම්භ කරන්න.
- Safari 18 (macOS 15) හි WebGPU පෙරනිමියෙන්ම සක්‍රිය කර ඇත.
- Firefox Nightly හි, ලිපින තීරුවේ about:config ටයිප් කර `set dom.webgpu.enabled to true` කරන්න.

### Microsoft Edge සඳහා GPU සැකසීම

Microsoft Edge සඳහා Windows මත ඉහළ කාර්ය සාධනයේ GPU සකසන ක්‍රමවේද මෙන්න:

- **සැකසුම් විවෘත කරන්න:** Start මෙනුව ක්ලික් කර Settings තෝරන්න.
- **පද්ධති සැකසුම්:** System වෙත ගොස් Display තෝරන්න.
- **Graphics සැකසුම්:** පහළට ගොස් Graphics settings ක්ලික් කරන්න.
- **යෙදුම තෝරන්න:** “Choose an app to set preference” යටතේ Desktop app තෝරන්න සහ පසුව Browse.
- **Edge තෝරන්න:** Edge ස්ථාපන ෆෝල්ඩරය (සාමාන්‍යයෙන් `C:\Program Files (x86)\Microsoft\Edge\Application`) වෙත ගොස් `msedge.exe` තෝරන්න.
- **අභිරුචි සකසන්න:** Options ක්ලික් කර, High performance තෝරන්න, පසුව Save ක්ලික් කරන්න.  
මෙම ක්‍රියා මගින් Microsoft Edge ඔබේ ඉහළ කාර්ය සාධන GPU භාවිතා කරයි.  
- **Restart** කරන්න ඔබේ පරිගණකය, මෙම සැකසුම් බලපැවැත්වීම සඳහා.

### උදාහරණ: කරුණාකර [මෙම සබැඳිය ක්ලික් කරන්න](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

It seems you've requested a translation to "mo," but it's unclear what specific language or dialect "mo" refers to. Could you clarify the language you're referring to so I can assist you properly? For example, are you referring to Maori, Mongolian, or another language?