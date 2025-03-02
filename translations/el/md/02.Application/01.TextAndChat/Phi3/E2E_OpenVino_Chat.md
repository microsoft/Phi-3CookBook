[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Αυτός ο κώδικας εξάγει ένα μοντέλο στη μορφή OpenVINO, το φορτώνει και το χρησιμοποιεί για να δημιουργήσει μια απάντηση σε μια δεδομένη προτροπή.

1. **Εξαγωγή του Μοντέλου**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Αυτή η εντολή χρησιμοποιεί το `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Εισαγωγή Απαραίτητων Βιβλιοθηκών**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Αυτές οι γραμμές εισάγουν κλάσεις από το `transformers` library and the `optimum.intel.openvino` module, οι οποίες είναι απαραίτητες για τη φόρτωση και τη χρήση του μοντέλου.

3. **Ορισμός του Φακέλου του Μοντέλου και της Διαμόρφωσης**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - Το `model_dir` specifies where the model files are stored.
   - `ov_config` είναι ένα λεξικό που ρυθμίζει το μοντέλο OpenVINO ώστε να δίνει προτεραιότητα στη χαμηλή καθυστέρηση, να χρησιμοποιεί ένα ρεύμα επεξεργασίας και να μην χρησιμοποιεί φάκελο προσωρινής αποθήκευσης.

4. **Φόρτωση του Μοντέλου**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Αυτή η γραμμή φορτώνει το μοντέλο από τον καθορισμένο φάκελο, χρησιμοποιώντας τις ρυθμίσεις διαμόρφωσης που ορίστηκαν προηγουμένως. Επίσης, επιτρέπει την απομακρυσμένη εκτέλεση κώδικα, αν χρειαστεί.

5. **Φόρτωση του Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Αυτή η γραμμή φορτώνει το tokenizer, το οποίο είναι υπεύθυνο για τη μετατροπή του κειμένου σε tokens που μπορεί να επεξεργαστεί το μοντέλο.

6. **Ορισμός Παραμέτρων για το Tokenizer**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Αυτό το λεξικό καθορίζει ότι δεν πρέπει να προστεθούν ειδικά tokens στην έξοδο που έχει γίνει tokenize.

7. **Ορισμός της Προτροπής**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Αυτή η συμβολοσειρά δημιουργεί μια προτροπή συνομιλίας, όπου ο χρήστης ζητά από τον AI βοηθό να συστηθεί.

8. **Μετατροπή της Προτροπής σε Tokens**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Αυτή η γραμμή μετατρέπει την προτροπή σε tokens που μπορεί να επεξεργαστεί το μοντέλο, επιστρέφοντας το αποτέλεσμα ως PyTorch tensors.

9. **Δημιουργία Απάντησης**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Αυτή η γραμμή χρησιμοποιεί το μοντέλο για να δημιουργήσει μια απάντηση βασισμένη στα tokens εισόδου, με μέγιστο αριθμό 1024 νέων tokens.

10. **Αποκωδικοποίηση της Απάντησης**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Αυτή η γραμμή μετατρέπει τα παραγόμενα tokens πίσω σε μια αναγνώσιμη από τον άνθρωπο συμβολοσειρά, παραλείποντας οποιαδήποτε ειδικά tokens, και επιστρέφει το πρώτο αποτέλεσμα.

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.