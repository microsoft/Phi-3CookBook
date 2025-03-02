# Buku Resep Phi: Contoh Praktis dengan Model Phi dari Microsoft

[![Buka dan gunakan sampel di GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Buka di Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Kontributor GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Masalah GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Permintaan Gabungan GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Pengamat GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Fork GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Bintang GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi adalah serangkaian model AI open-source yang dikembangkan oleh Microsoft.

Phi saat ini merupakan model bahasa kecil (SLM) yang paling kuat dan hemat biaya, dengan performa yang sangat baik dalam berbagai bahasa, penalaran, pembuatan teks/chat, pemrograman, gambar, audio, dan skenario lainnya.

Anda dapat menerapkan Phi di cloud atau perangkat edge, serta dengan mudah membangun aplikasi AI generatif dengan daya komputasi yang terbatas.

Ikuti langkah-langkah ini untuk mulai menggunakan sumber daya ini:
1. **Fork Repositori**: Klik [![Fork GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone Repositori**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Bergabung dengan Komunitas Discord AI Microsoft dan temui para ahli serta pengembang lainnya**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.id.png)

## Daftar Isi

- Pengantar
  - [Selamat Datang di Keluarga Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Menyiapkan Lingkungan Anda](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Memahami Teknologi Utama](./md/01.Introduction/01/01.Understandingtech.md)
  - [Keamanan AI untuk Model Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Dukungan Perangkat Keras untuk Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Model Phi & Ketersediaannya di Berbagai Platform](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Menggunakan Guidance-ai dan Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Model di Marketplace GitHub](https://github.com/marketplace/models)
  - [Katalog Model Azure AI](https://ai.azure.com)

- Inferensi Phi di Berbagai Lingkungan
    - [Hugging Face](./md/01.Introduction/02/01.HF.md)
    - [Model GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Katalog Model Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inferensi Keluarga Phi
    - [Inferensi Phi di iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferensi Phi di Android](./md/01.Introduction/03/Android_Inference.md)
- [Inference Phi di Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inference Phi di AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inference Phi dengan Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inference Phi di Server Lokal](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inference Phi di Server Jarak Jauh menggunakan AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inference Phi dengan Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inference Phi--Vision di Lokal](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inference Phi dengan Kaito AKS, Azure Containers (dukungan resmi)](./md/01.Introduction/03/Kaito_Inference.md)  

- [Mengkuantisasi Keluarga Phi](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Kuantisasi Phi-3.5 / 4 menggunakan llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Kuantisasi Phi-3.5 / 4 menggunakan ekstensi Generative AI untuk onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Kuantisasi Phi-3.5 / 4 menggunakan Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Kuantisasi Phi-3.5 / 4 menggunakan Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)  

- Evaluasi Phi  
    - [AI yang Bertanggung Jawab](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry untuk Evaluasi](./md/01.Introduction/05/AIFoundry.md)  
    - [Menggunakan Promptflow untuk Evaluasi](./md/01.Introduction/05/Promptflow.md)  

- RAG dengan Azure AI Search  
    - [Cara menggunakan Phi-4-mini dan Phi-4-multimodal (RAG) dengan Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)  

- Contoh pengembangan aplikasi Phi  
  - Aplikasi Teks & Chat  
    - Contoh Phi-4 🆕  
      - [📓] [Chat dengan Model Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat dengan Model Lokal Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Aplikasi Konsol Chat .NET dengan Phi-4 ONNX menggunakan Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Contoh Phi-3 / 3.5  
      - [Chatbot Lokal di browser menggunakan Phi3, ONNX Runtime Web, dan WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi Model - Interaktif Phi-3-mini dan OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Membangun wrapper dan menggunakan Phi-3 dengan MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Optimisasi Model - Cara mengoptimalkan model Phi-3-min untuk ONNX Runtime Web dengan Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Aplikasi WinUI3 dengan Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Contoh Aplikasi Catatan AI Multi Model di WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)  
      - [Fine-tune dan Integrasi model Phi-3 kustom dengan Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
      - [Fine-tune dan Integrasi model Phi-3 kustom dengan Prompt flow di Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
      - [Evaluasi Model Phi-3 / Phi-3.5 yang telah di-Fine-tune di Azure AI Foundry dengan Fokus pada Prinsip AI Bertanggung Jawab Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Contoh prediksi bahasa Phi-3.5-mini-instruct (China/Inggris)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Chatbot RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Menggunakan GPU Windows untuk membuat solusi Prompt Flow dengan Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Menggunakan Microsoft Phi-3.5 tflite untuk membuat aplikasi Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Contoh Q&A .NET menggunakan model lokal ONNX Phi-3 dengan Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Aplikasi chat konsol .NET dengan Semantic Kernel dan Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Contoh Berbasis Kode Azure AI Inference SDK
    - Contoh Phi-4 🆕
      - [📓] [Menghasilkan kode proyek menggunakan Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Contoh Phi-3 / 3.5
      - [Bangun GitHub Copilot Chat Visual Studio Code Anda sendiri dengan Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Buat Agen Chat Copilot Visual Studio Code Anda sendiri dengan Phi-3.5 oleh Model GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Contoh Penalaran Lanjutan
    - Contoh Phi-4 🆕
      - [📓] [Contoh Penalaran Phi-4-mini](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - Demo
      - [Demo Phi-4-mini yang dihosting di Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Demo Phi-4-multimodal yang dihosting di Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Contoh Vision
    - Contoh Phi-4 🆕
      - [📓] [Menggunakan Phi-4-multimodal untuk membaca gambar dan menghasilkan kode](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Contoh Phi-3 / 3.5
      - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Daur Ulang](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Asisten bahasa visual - dengan Phi3-Vision dan OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision contoh multi-frame atau multi-image](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Model ONNX Lokal Phi-3 Vision menggunakan Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Model ONNX Lokal Phi-3 Vision berbasis Menu menggunakan Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Contoh Audio
    - Contoh Phi-4 🆕
      - [📓] [Mengekstrak transkrip audio menggunakan Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Contoh Audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Contoh Terjemahan Ucapan Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Aplikasi konsol .NET menggunakan Phi-4-multimodal Audio untuk menganalisis file audio dan menghasilkan transkrip](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Contoh MOE
    - Contoh Phi-3 / 3.5
      - [📓] [Model Mixture of Experts (MoEs) Phi-3.5 Contoh Media Sosial](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Membangun Pipeline Retrieval-Augmented Generation (RAG) dengan NVIDIA NIM Phi-3 MOE, Azure AI Search, dan LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Contoh Function Calling
    - Contoh Phi-4 🆕
      - [📓] [Menggunakan Function Calling Dengan Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
  - Contoh Pencampuran Multimodal
    - Contoh Phi-4 🆕
-  [📓] [Menggunakan Phi-4-multimodal sebagai Jurnalis Teknologi](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [Aplikasi konsol .NET menggunakan Phi-4-multimodal untuk menganalisis gambar](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Contoh Phi
  - [Skenario Fine-tuning](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning Membuat Phi-3 menjadi Ahli Industri](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fine-tuning Phi-3 dengan AI Toolkit untuk VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fine-tuning Phi-3 dengan Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Fine-tuning Phi-3 dengan Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fine-tuning Phi-3 dengan QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fine-tuning Phi-3 dengan Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fine-tuning Phi-3 dengan Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fine-tuning dengan Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fine-tuning dengan Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fine-tuning Phi-3-vision dengan Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fine-tuning Phi-3 dengan Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fine-tuning Phi-3-vision (dukungan resmi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fine-Tuning Phi-3 dengan Kaito AKS, Azure Containers (dukungan resmi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fine-Tuning Phi-3 dan 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [Mengeksplorasi model terbaru: LLMs, SLMs, pengembangan lokal, dan lainnya](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Mengungkap Potensi NLP: Fine-Tuning dengan Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Makalah Penelitian Akademik dan Publikasi
  - [Textbooks Are All You Need II: laporan teknis phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Laporan Teknis Phi-3: Model Bahasa yang Sangat Mampu Secara Lokal di Ponsel Anda](https://arxiv.org/abs/2404.14219)
  - [Laporan Teknis Phi-4](https://arxiv.org/abs/2412.08905)
  - [Mengoptimalkan Model Bahasa Kecil untuk Pemanggilan Fungsi di Kendaraan](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning PHI-3 untuk Menjawab Pertanyaan Pilihan Ganda: Metodologi, Hasil, dan Tantangan](https://arxiv.org/abs/2501.01588)

## Menggunakan Model Phi

### Phi di Azure AI Foundry

Anda dapat mempelajari cara menggunakan Microsoft Phi dan cara membangun solusi E2E di berbagai perangkat keras Anda. Untuk mencoba Phi sendiri, mulailah dengan menjelajahi model dan menyesuaikan Phi untuk skenario Anda menggunakan [Katalog Model Azure AI Foundry](https://aka.ms/phi3-azure-ai). Anda dapat mempelajari lebih lanjut di Panduan Memulai dengan [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Setiap model memiliki playground khusus untuk menguji model [Azure AI Playground](https://aka.ms/try-phi3).

### Phi di Model GitHub

Anda dapat mempelajari cara menggunakan Microsoft Phi dan cara membangun solusi E2E di berbagai perangkat keras Anda. Untuk mencoba Phi sendiri, mulailah dengan menjelajahi model dan menyesuaikan Phi untuk skenario Anda menggunakan [Katalog Model GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Anda dapat mempelajari lebih lanjut di Panduan Memulai dengan [Katalog Model GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Setiap model memiliki [playground khusus untuk menguji model](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi di Hugging Face

Anda juga dapat menemukan model ini di [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## AI yang Bertanggung Jawab

Microsoft berkomitmen untuk membantu pelanggan menggunakan produk AI kami secara bertanggung jawab, berbagi pembelajaran kami, dan membangun kemitraan berbasis kepercayaan melalui alat seperti Transparency Notes dan Impact Assessments. Banyak dari sumber daya ini dapat ditemukan di [https://aka.ms/RAI](https://aka.ms/RAI).  
Pendekatan Microsoft terhadap AI yang bertanggung jawab didasarkan pada prinsip AI kami, yaitu keadilan, keandalan dan keselamatan, privasi dan keamanan, inklusivitas, transparansi, dan akuntabilitas.

Model bahasa alami, gambar, dan suara berskala besar - seperti yang digunakan dalam sampel ini - berpotensi berperilaku dengan cara yang tidak adil, tidak dapat diandalkan, atau menyinggung, yang pada akhirnya dapat menyebabkan kerugian. Silakan konsultasikan [catatan transparansi layanan Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) untuk memahami risiko dan keterbatasannya.

Pendekatan yang direkomendasikan untuk mengurangi risiko ini adalah dengan memasukkan sistem keamanan dalam arsitektur Anda yang dapat mendeteksi dan mencegah perilaku berbahaya. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) menyediakan lapisan perlindungan independen, yang mampu mendeteksi konten berbahaya yang dihasilkan pengguna atau AI dalam aplikasi dan layanan. Azure AI Content Safety mencakup API teks dan gambar yang memungkinkan Anda mendeteksi materi yang berbahaya. Di dalam Azure AI Foundry, layanan Content Safety memungkinkan Anda melihat, mengeksplorasi, dan mencoba kode sampel untuk mendeteksi konten berbahaya di berbagai modalitas. [Dokumentasi quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) berikut ini memandu Anda dalam membuat permintaan ke layanan tersebut.

Aspek lain yang perlu diperhatikan adalah kinerja aplikasi secara keseluruhan. Dalam aplikasi multi-modal dan multi-model, kami menganggap kinerja berarti sistem bekerja sesuai dengan harapan Anda dan pengguna Anda, termasuk tidak menghasilkan output yang berbahaya. Penting untuk menilai kinerja aplikasi Anda secara keseluruhan menggunakan [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Anda juga memiliki kemampuan untuk membuat dan mengevaluasi dengan [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Anda dapat mengevaluasi aplikasi AI Anda di lingkungan pengembangan menggunakan [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dengan dataset uji atau target tertentu, generasi aplikasi AI generatif Anda diukur secara kuantitatif menggunakan evaluators bawaan atau evaluators kustom pilihan Anda. Untuk memulai dengan Azure AI Evaluation SDK untuk mengevaluasi sistem Anda, Anda dapat mengikuti [panduan quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Setelah Anda menjalankan evaluasi, Anda dapat [memvisualisasikan hasilnya di Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Merek Dagang

Proyek ini mungkin mengandung merek dagang atau logo untuk proyek, produk, atau layanan. Penggunaan merek dagang atau logo Microsoft yang diizinkan harus sesuai dan mematuhi [Panduan Merek & Merek Dagang Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Penggunaan merek dagang atau logo Microsoft dalam versi modifikasi dari proyek ini tidak boleh menyebabkan kebingungan atau menyiratkan sponsor dari Microsoft. Setiap penggunaan merek dagang atau logo pihak ketiga tunduk pada kebijakan pihak ketiga tersebut.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.