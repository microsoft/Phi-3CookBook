# Etkileşimli Phi 3 Mini 4K Talimatlı Sohbet Botu ve Whisper

## Genel Bakış

Etkileşimli Phi 3 Mini 4K Talimatlı Sohbet Botu, kullanıcıların Microsoft Phi 3 Mini 4K talimatlı demo ile metin veya ses girişi kullanarak etkileşimde bulunmalarını sağlayan bir araçtır. Sohbet botu çeviri, hava durumu güncellemeleri ve genel bilgi toplama gibi çeşitli görevler için kullanılabilir.

### Başlarken

Bu sohbet botunu kullanmak için aşağıdaki adımları izleyin:

1. Yeni bir [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) dosyasını açın.
2. Not defterinin ana penceresinde, bir metin giriş kutusu ve "Gönder" düğmesi olan bir sohbet kutusu arayüzü göreceksiniz.
3. Metin tabanlı sohbet botunu kullanmak için mesajınızı metin giriş kutusuna yazın ve "Gönder" düğmesine tıklayın. Sohbet botu, not defterinin içinden doğrudan oynatılabilen bir ses dosyası ile yanıt verecektir.

**Not**: Bu araç bir GPU ve Microsoft Phi-3 ile OpenAI Whisper modellerine erişim gerektirir. Bu modeller, konuşma tanıma ve çeviri için kullanılır.

### GPU Gereksinimleri

Bu demoyu çalıştırmak için 12 GB GPU belleği gereklidir.

**Microsoft-Phi-3-Mini-4K talimatlı** demosunu bir GPU'da çalıştırmak için gereken bellek, giriş verilerinin (ses veya metin) boyutuna, kullanılan çeviri diline, modelin hızına ve GPU üzerindeki mevcut belleğe bağlı olacaktır.

Genel olarak, Whisper modeli GPU'larda çalışacak şekilde tasarlanmıştır. Whisper modelini çalıştırmak için önerilen minimum GPU belleği 8 GB'dir, ancak gerekirse daha büyük bellek miktarlarını da işleyebilir.

Büyük miktarda veri veya model üzerinde yüksek hacimli istekler çalıştırmanın daha fazla GPU belleği gerektirebileceğini ve/veya performans sorunlarına neden olabileceğini unutmamak önemlidir. Belirli ihtiyaçlarınız için en uygun ayarları belirlemek amacıyla farklı yapılandırmaları test etmeniz ve bellek kullanımını izlemeniz önerilir.

## Whisper ile Etkileşimli Phi 3 Mini 4K Talimatlı Sohbet Botu için Uçtan Uca Örnek

[Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) başlıklı Jupyter not defteri, Microsoft Phi 3 Mini 4K talimatlı demoyu kullanarak ses veya yazılı metin girişinden metin üretmenin nasıl yapılacağını gösterir. Not defteri birkaç fonksiyon tanımlar:

1. `tts_file_name(text)`: Bu fonksiyon, oluşturulan ses dosyasını kaydetmek için giriş metnine dayalı bir dosya adı oluşturur.
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Bu fonksiyon, Edge TTS API'sini kullanarak bir dizi metin parçasından bir ses dosyası oluşturur. Giriş parametreleri, metin parçalarının listesi, konuşma hızı, ses adı ve oluşturulan ses dosyasını kaydetmek için çıktı yoludur.
3. `talk(input_text)`: Bu fonksiyon, Edge TTS API'sini kullanarak bir ses dosyası oluşturur ve /content/audio dizininde rastgele bir dosya adına kaydeder. Giriş parametresi, konuşmaya dönüştürülecek metindir.
4. `run_text_prompt(message, chat_history)`: Bu fonksiyon, Microsoft Phi 3 Mini 4K talimatlı demoyu kullanarak bir mesaj girişinden bir ses dosyası oluşturur ve bunu sohbet geçmişine ekler.
5. `run_audio_prompt(audio, chat_history)`: Bu fonksiyon, Whisper model API'sini kullanarak bir ses dosyasını metne dönüştürür ve bunu `run_text_prompt()` fonksiyonuna iletir.
6. Kod, kullanıcıların Phi 3 Mini 4K talimatlı demo ile mesaj yazarak veya ses dosyaları yükleyerek etkileşimde bulunmalarına olanak tanıyan bir Gradio uygulaması başlatır. Çıktı, uygulama içinde bir metin mesajı olarak görüntülenir.

## Sorun Giderme

Cuda GPU sürücülerini yükleme

1. Linux uygulamalarınızın güncel olduğundan emin olun:

    ```bash
    sudo apt update
    ```

2. Cuda Sürücülerini Yükleyin:

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. Cuda sürücü konumunu kaydedin:

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. Nvidia GPU bellek boyutunu kontrol etme (12 GB GPU Belleği gerekli):

    ```bash
    nvidia-smi
    ```

5. Önbelleği Boşaltma: PyTorch kullanıyorsanız, torch.cuda.empty_cache() çağrısı yaparak kullanılmayan tüm önbellek belleğini serbest bırakabilir ve diğer GPU uygulamaları tarafından kullanılmasını sağlayabilirsiniz.

    ```python
    torch.cuda.empty_cache() 
    ```

6. Nvidia Cuda'yı kontrol etme:

    ```bash
    nvcc --version
    ```

7. Hugging Face token oluşturmak için aşağıdaki görevleri gerçekleştirin:

    - [Hugging Face Token Ayarları sayfasına](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo) gidin.
    - **Yeni token** seçeneğini seçin.
    - Kullanmak istediğiniz proje **Adını** girin.
    - **Tür** olarak **Yazma** seçeneğini seçin.

> **Not**
>
> Eğer şu hatayla karşılaşırsanız:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Bunu çözmek için terminalinize şu komutu yazın:
>
> ```bash
> sudo ldconfig
> ```

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, bağlayıcı kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.