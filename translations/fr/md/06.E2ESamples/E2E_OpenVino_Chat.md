[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ce code exporte un modèle au format OpenVINO, le charge et l'utilise pour générer une réponse à une invite donnée.

1. **Exportation du modèle** :
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Cette commande utilise `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`.

2. **Importation des bibliothèques nécessaires** :
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ces lignes importent des classes du module `transformers` library and the `optimum.intel.openvino`, nécessaires pour charger et utiliser le modèle.

3. **Configuration du répertoire et des paramètres du modèle** :
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` est un dictionnaire qui configure le modèle OpenVINO pour prioriser une faible latence, utiliser un seul flux d'inférence et ne pas utiliser de répertoire de cache.

4. **Chargement du modèle** :
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Cette ligne charge le modèle depuis le répertoire spécifié, en utilisant les paramètres de configuration définis précédemment. Elle permet également l'exécution de code à distance si nécessaire.

5. **Chargement du tokenizer** :
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Cette ligne charge le tokenizer, qui est responsable de convertir le texte en tokens compréhensibles par le modèle.

6. **Configuration des arguments du tokenizer** :
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ce dictionnaire spécifie que les tokens spéciaux ne doivent pas être ajoutés à la sortie tokenisée.

7. **Définition de l'invite** :
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Cette chaîne de caractères configure une invite de conversation où l'utilisateur demande à l'assistant IA de se présenter.

8. **Tokenisation de l'invite** :
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Cette ligne convertit l'invite en tokens que le modèle peut traiter, retournant le résultat sous forme de tenseurs PyTorch.

9. **Génération d'une réponse** :
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Cette ligne utilise le modèle pour générer une réponse basée sur les tokens d'entrée, avec un maximum de 1024 nouveaux tokens.

10. **Décodage de la réponse** :
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Cette ligne convertit les tokens générés en une chaîne de caractères lisible par un humain, en ignorant les tokens spéciaux, et récupère le premier résultat.

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.