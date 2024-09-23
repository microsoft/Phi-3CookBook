[Exemple de Chat OpenVino](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ce code exporte un modèle au format OpenVINO, le charge et l'utilise pour générer une réponse à une invite donnée.

1. **Exporter le Modèle** :
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Cette commande utilise l'outil `optimum-cli` pour exporter un modèle au format OpenVINO, optimisé pour une inférence efficace.
   - Le modèle exporté est `"microsoft/Phi-3-mini-4k-instruct"`, configuré pour la tâche de génération de texte basée sur le contexte passé.
   - Les poids du modèle sont quantifiés en entiers de 4 bits (`int4`), ce qui aide à réduire la taille du modèle et à accélérer le traitement.
   - D'autres paramètres comme `group-size`, `ratio` et `sym` sont utilisés pour affiner le processus de quantification.
   - Le modèle exporté est sauvegardé dans le répertoire `./model/phi3-instruct/int4`.

2. **Importer les Bibliothèques Nécessaires** :
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ces lignes importent des classes de la bibliothèque `transformers` et du module `optimum.intel.openvino`, nécessaires pour charger et utiliser le modèle.

3. **Configurer le Répertoire et la Configuration du Modèle** :
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` spécifie où sont stockés les fichiers du modèle.
   - `ov_config` est un dictionnaire qui configure le modèle OpenVINO pour privilégier la faible latence, utiliser un flux d'inférence et ne pas utiliser de répertoire de cache.

4. **Charger le Modèle** :
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - Cette ligne charge le modèle depuis le répertoire spécifié, en utilisant les paramètres de configuration définis précédemment. Elle permet également l'exécution de code distant si nécessaire.

5. **Charger le Tokenizer** :
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Cette ligne charge le tokenizer, responsable de convertir le texte en tokens compréhensibles par le modèle.

6. **Configurer les Arguments du Tokenizer** :
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - Ce dictionnaire spécifie que les tokens spéciaux ne doivent pas être ajoutés à la sortie tokenisée.

7. **Définir l'Invite** :
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - Cette chaîne de caractères configure une invite de conversation où l'utilisateur demande à l'assistant AI de se présenter.

8. **Tokeniser l'Invite** :
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Cette ligne convertit l'invite en tokens que le modèle peut traiter, renvoyant le résultat sous forme de tenseurs PyTorch.

9. **Générer une Réponse** :
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Cette ligne utilise le modèle pour générer une réponse basée sur les tokens d'entrée, avec un maximum de 1024 nouveaux tokens.

10. **Décoder la Réponse** :
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Cette ligne convertit les tokens générés en une chaîne de caractères lisible, en sautant les tokens spéciaux, et récupère le premier résultat.

Avertissement : La traduction a été effectuée à partir de son original par un modèle d'IA et peut ne pas être parfaite. Veuillez vérifier le résultat et apporter les corrections nécessaires.