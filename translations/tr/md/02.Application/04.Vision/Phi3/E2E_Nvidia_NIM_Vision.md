### Örnek Senaryo

Bir resminiz olduğunu (`demo.png`) ve bu resmi işleyip yeni bir versiyonunu kaydeden Python kodu oluşturmak istediğinizi hayal edin (`phi-3-vision.jpg`). 

Yukarıdaki kod, bu süreci otomatikleştirir ve şu adımları gerçekleştirir:

1. Ortamı ve gerekli yapılandırmaları ayarlar.
2. Modelin ihtiyaç duyulan Python kodunu oluşturmasını sağlayan bir talimat oluşturur.
3. Talimatı modele gönderir ve oluşturulan kodu toplar.
4. Oluşturulan kodu çıkarır ve çalıştırır.
5. Orijinal ve işlenmiş resimleri görüntüler.

Bu yaklaşım, görüntü işleme görevlerini otomatikleştirmek için yapay zekanın gücünden faydalanır ve hedeflerinize daha hızlı ve kolay ulaşmanızı sağlar.

[Örnek Kod Çözümü](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

Kodun tamamının adım adım ne yaptığını inceleyelim:

1. **Gerekli Paketi Yükleyin**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    Bu komut, `langchain_nvidia_ai_endpoints` paketini yükler ve en son sürümünün kurulu olmasını sağlar.

2. **Gerekli Modülleri İçe Aktarın**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    Bu importlar, NVIDIA AI uç noktalarıyla etkileşim, şifreleri güvenli bir şekilde yönetme, işletim sistemi ile etkileşim ve base64 formatında veri kodlama/çözme için gerekli modülleri getirir.

3. **API Anahtarını Ayarlayın**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    Bu kod, `NVIDIA_API_KEY` ortam değişkeninin ayarlanıp ayarlanmadığını kontrol eder. Eğer ayarlanmamışsa, kullanıcıdan API anahtarını güvenli bir şekilde girmesini ister.

4. **Model ve Resim Yolunu Tanımlayın**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    Bu, kullanılacak modeli belirler, belirtilen model ile bir `ChatNVIDIA` örneği oluşturur ve resim dosyasının yolunu tanımlar.

5. **Metin Talimatını Oluşturun**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    Bu, modelin bir resmi işlemek için Python kodu oluşturmasını talep eden bir metin talimatı tanımlar.

6. **Resmi Base64 Formatında Kodlayın**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    Bu kod, resim dosyasını okur, base64 formatında kodlar ve kodlanmış verilerle bir HTML resim etiketi oluşturur.

7. **Metin ve Resmi Talimatta Birleştirin**:
    ```python
    prompt = f"{text} {image}"
    ```
    Bu, metin talimatını ve HTML resim etiketini tek bir string içinde birleştirir.

8. **ChatNVIDIA Kullanarak Kod Üretin**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    Bu kod, talimatı `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` stringine gönderir.

9. **Oluşturulan İçerikten Python Kodunu Çıkarın**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    Bu, markdown formatını kaldırarak oluşturulan içerikten gerçek Python kodunu çıkarır.

10. **Oluşturulan Kodu Çalıştırın**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    Bu, çıkarılan Python kodunu bir alt işlem olarak çalıştırır ve çıktısını yakalar.

11. **Resimleri Görüntüleyin**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    Bu satırlar, `IPython.display` modülünü kullanarak resimleri görüntüler.

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yorumlamalardan sorumlu değiliz.