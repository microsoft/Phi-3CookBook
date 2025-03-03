## **Phi-4-mini-mm kullanarak kod oluşturma**

Phi-4-mini, Phi Ailesi'nin güçlü kodlama yeteneklerini devam ettiriyor. Kodlama ile ilgili sorular sormak için Prompt'u kullanabilirsiniz. Tabii ki, güçlü akıl yürütme yeteneği eklendikten sonra, gereksinimlere göre projeler oluşturmak gibi daha güçlü kodlama yeteneklerine sahip olmuştur. Örneğin, gereksinimlere göre projeler oluşturabilirsiniz, örneğin:

### **Gereksinim**

Bir Alışveriş Sepeti Uygulaması Oluşturun

- Aşağıdaki yöntemlere sahip bir API Rest oluşturun:
    - Sayfa kaydırma ve limit kullanarak bira listesini alın.
    - Kimliğe göre bira detaylarını alın.
    - Ad, açıklama, slogan, yemek eşleşmeleri ve fiyata göre bira arayın.
- Ana sayfada bir ürün listesi oluşturun.
    - Ürünleri filtrelemek için bir arama çubuğu oluşturun.
    - Kullanıcı bir ürüne tıkladığında açıklama sayfasına yönlendirin.
- (İsteğe bağlı) Fiyata göre ürünleri filtrelemek için bir dilimleyici ekleyin.
- Bir alışveriş sepeti oluşturun.
    - Ürünleri sepete ekleyin.
    - Ürünleri sepetten çıkarın.
    - Sepetteki ürünlerin toplam fiyatını hesaplayın.

### **Örnek Kod - Python**


```python

import requests
import torch
from PIL import Image
import soundfile
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig,pipeline,AutoTokenizer

model_path = 'Your Phi-4-mini-mm-instruct'

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype='auto',
    _attn_implementation='flash_attention_2',
).cuda()

generation_config = GenerationConfig.from_pretrained(model_path, 'generation_config.json')

user_prompt = '<|user|>'
assistant_prompt = '<|assistant|>'
prompt_suffix = '<|end|>'

requirement = """

Create a Shopping Cart App

- Create an API Rest with the following methods:
    - Get a list of beers using page offset and limit.
    - Get beer details by id.
    - Search for beer by name, description, tagline, food pairings, and price.
- Create a list of products on the main page.
    - Create a search bar to filter products.
    - Navigate to the description page when the user clicks on a product.
- (Optional) Slicer to filter products by price.
- Create a shopping cart.
    - Add products to the cart.
    - Remove products from the cart.
    - Calculate the total price of the products in the cart."""

note = """ 

            Note:

            1. Use Python Flask to create a Repository pattern based on the following structure to generate the files

            ｜- models
            ｜- controllers
            ｜- repositories
            ｜- views

            2. For the view page, please use SPA + VueJS + TypeScript to build

            3. Firstly use markdown to output the generated project structure (including directories and files), and then generate the  file names and corresponding codes step by step, output like this 

               ## Project Structure

                    ｜- models
                        | - user.py
                    ｜- controllers
                        | - user_controller.py
                    ｜- repositories
                        | - user_repository.py
                    ｜- templates
                        | - index.html

               ## Backend
                 
                   #### `models/user.py`
                   ```python

                   ```
                   .......
               

               ## Frontend
                 
                   #### `templates/index.html`
                   ```html

                   ```
                   ......."""

prompt = f'{user_prompt}Please create a project with Python and Flask according to the following requirements：\n{requirement}{note}{prompt_suffix}{assistant_prompt}'

inputs = processor(prompt, images=None, return_tensors='pt').to('cuda:0')

generate_ids = model.generate(
    **inputs,
    max_new_tokens=2048,
    generation_config=generation_config,
)

generate_ids = generate_ids[:, inputs['input_ids'].shape[1] :]

response = processor.batch_decode(
    generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
)[0]

print(response)

```

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanabilecek yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.