Phi-3-mini-гийн хувьд inference гэдэг нь оролтын өгөгдөл дээр үндэслэн таамаглал гаргах эсвэл үр дүн үүсгэх үйл явцыг хэлнэ. Танд Phi-3-mini болон түүний inference хийх боломжуудын талаар дэлгэрэнгүй тайлбарлая.

Phi-3-mini нь Microsoft-ийн гаргасан Phi-3 цуврал загваруудын нэг хэсэг юм. Эдгээр загварууд нь Жижиг Хэлний Загварууд (SLM)-ын боломжуудыг шинэ түвшинд гаргах зорилготой бүтээгдсэн.

Phi-3-mini болон түүний inference хийх боломжуудын гол онцлогуудыг энд дурдлаа:

## **Phi-3-mini Тойм:**
- Phi-3-mini нь 3.8 тэрбум параметртэй.
- Энэ нь зөвхөн уламжлалт тооцооллын төхөөрөмжүүд дээр бус, мөн гар утас болон IoT төхөөрөмжүүд гэх мэт edge төхөөрөмжүүд дээр ажиллах боломжтой.
- Phi-3-mini-ийн гарснаар хувь хүн болон байгууллагуудыг SLM-уудыг янз бүрийн техник хангамж дээр, ялангуяа нөөц хязгаарлагдмал орчинд ашиглах боломжийг олгож байна.
- Энэ нь PyTorch-ийн уламжлалт формат, gguf форматын тоон хувилбар, мөн ONNX дээр суурилсан тоон хувилбар зэрэг олон төрлийн загвар форматыг хамардаг.

## **Phi-3-mini-д хандах:**
Phi-3-mini-д хандахын тулд [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)-ийг Copilot програмд ашиглаж болно. Semantic Kernel нь Azure OpenAI Service, Hugging Face дээрх нээлттэй эх загварууд болон орон нутгийн загваруудтай нийцдэг.
Мөн [Ollama](https://ollama.com) эсвэл [LlamaEdge](https://llamaedge.com)-ийг ашиглан тоон хувиргасан загваруудыг дуудах боломжтой. Ollama нь хувь хэрэглэгчдэд янз бүрийн тоон загваруудыг дуудах боломжийг олгодог бол LlamaEdge нь GGUF загваруудыг олон платформд ашиглах боломжийг олгодог.

## **Тоон Хувиргасан Загварууд:**
Олон хэрэглэгчид орон нутгийн inference хийхдээ тоон хувиргасан загваруудыг илүүд үздэг. Жишээлбэл, та Ollama-г ашиглан шууд "Phi-3"-ийг ажиллуулж эсвэл Modelfile ашиглан оффлайн тохиргоо хийж болно. Modelfile нь GGUF файлын зам болон prompt форматыг тодорхойлдог.

## **Генератив AI Боломжууд:**
Phi-3-mini гэх мэт SLM-уудыг нэгтгэх нь генератив AI-ийн шинэ боломжуудыг нээж өгдөг. Inference нь зөвхөн эхний алхам бөгөөд эдгээр загваруудыг нөөц хязгаарлагдмал, хоцрогдол шаардлагатай, зардал хэмнэх шаардлагатай нөхцөлд янз бүрийн даалгавруудад ашиглах боломжтой.

## **Phi-3-mini ашиглан Генератив AI-ийг Нээх: Inference болон Нэвтрүүлэлтийн Гарын Авлага**  
Semantic Kernel, Ollama/LlamaEdge болон ONNX Runtime ашиглан Phi-3-mini загваруудыг хэрхэн ашиглах, inference хийх, мөн янз бүрийн хэрэглээний нөхцөлд генератив AI-ийн боломжуудыг судлах талаар суралцаарай.

**Онцлогууд**
Phi-3-mini загварын inference хийх боломжууд:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Эцэст нь, Phi-3-mini нь хөгжүүлэгчдэд янз бүрийн загвар форматыг судлах, генератив AI-г янз бүрийн хэрэглээний нөхцөлд ашиглах боломжийг олгодог.

It seems you want the text translated into a language code "mo," but "mo" is not a standard or recognized language code in the ISO 639-1 standard. Could you clarify the language you want the text translated into? For example, is it Moldovan (Romanian), Mongolian, or something else?