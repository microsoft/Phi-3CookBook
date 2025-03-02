[OpenVino Sohbet Örneği](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Bu kod, bir modeli OpenVINO formatına dönüştürür, yükler ve verilen bir isteme yanıt oluşturmak için kullanır.

1. **Modeli Dışa Aktarma**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Bu komut, `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` kullanır.

2. **Gerekli Kütüphaneleri İçe Aktarma**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Bu satırlar, modeli yüklemek ve kullanmak için gereken `transformers` library and the `optimum.intel.openvino` modülünden sınıfları içe aktarır.

3. **Model Dizini ve Yapılandırmasını Ayarlama**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config`, OpenVINO modelinin düşük gecikmeye öncelik vermesi, bir tahmin akışı kullanması ve önbellek dizini kullanmaması için bir sözlük olarak yapılandırılır.

4. **Modeli Yükleme**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Bu satır, daha önce tanımlanan yapılandırma ayarlarını kullanarak belirtilen dizinden modeli yükler. Gerekirse uzaktan kod çalıştırmaya da izin verir.

5. **Tokenizer'ı Yükleme**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Bu satır, metni modelin anlayabileceği tokenlara dönüştürmekten sorumlu olan tokenizer'ı yükler.

6. **Tokenizer Argümanlarını Ayarlama**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Bu sözlük, tokenlaştırılmış çıktıya özel tokenların eklenmemesi gerektiğini belirtir.

7. **İstem Tanımlama**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Bu dize, kullanıcıdan yapay zeka asistanına kendini tanıtmasını istemek için bir sohbet istemi oluşturur.

8. **İstemi Tokenlaştırma**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Bu satır, istemi modelin işleyebileceği tokenlara dönüştürür ve sonucu PyTorch tensörleri olarak döndürür.

9. **Yanıt Oluşturma**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Bu satır, modelin giriş tokenlarına dayanarak bir yanıt oluşturmasını sağlar ve maksimum 1024 yeni token sınırı belirler.

10. **Yanıtı Çözümleme**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Bu satır, oluşturulan tokenları insan tarafından okunabilir bir dizeye dönüştürür, özel tokenları atlar ve ilk sonucu döndürür.

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul etmiyoruz.