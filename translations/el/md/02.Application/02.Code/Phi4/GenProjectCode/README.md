## **Χρήση του Phi-4-mini-mm για δημιουργία κώδικα**

Το Phi-4-mini συνεχίζει την ισχυρή ικανότητα κωδικοποίησης της οικογένειας Phi. Μπορείτε να χρησιμοποιήσετε το Prompt για να κάνετε ερωτήσεις σχετικές με την κωδικοποίηση. Φυσικά, με την προσθήκη της ισχυρής ικανότητας λογικής, έχει ακόμη πιο ενισχυμένες δυνατότητες κωδικοποίησης, όπως η δημιουργία έργων σύμφωνα με τις απαιτήσεις. Για παράδειγμα, δημιουργήστε έργα σύμφωνα με τις απαιτήσεις, όπως:

### **Απαίτηση**

Δημιουργήστε μια εφαρμογή Καλάθι Αγορών

- Δημιουργήστε ένα API Rest με τις εξής μεθόδους:
    - Λήψη λίστας από μπύρες χρησιμοποιώντας page offset και limit.
    - Λήψη λεπτομερειών μπύρας με βάση το id.
    - Αναζήτηση μπύρας με βάση το όνομα, την περιγραφή, το tagline, τους συνδυασμούς φαγητού και την τιμή.
- Δημιουργήστε μια λίστα προϊόντων στην κύρια σελίδα.
    - Δημιουργήστε μια μπάρα αναζήτησης για φιλτράρισμα προϊόντων.
    - Μεταβείτε στη σελίδα περιγραφής όταν ο χρήστης κάνει κλικ σε ένα προϊόν.
- (Προαιρετικό) Δημιουργήστε slicer για φιλτράρισμα προϊόντων με βάση την τιμή.
- Δημιουργήστε ένα καλάθι αγορών.
    - Προσθήκη προϊόντων στο καλάθι.
    - Αφαίρεση προϊόντων από το καλάθι.
    - Υπολογισμός της συνολικής τιμής των προϊόντων στο καλάθι.

### **Δείγμα Κώδικα - Python**


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

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.