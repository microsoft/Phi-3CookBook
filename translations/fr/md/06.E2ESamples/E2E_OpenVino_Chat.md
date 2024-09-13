[OpenVino Chat Sample](../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

Ce code exporte un modèle au format OpenVINO, le charge et l'utilise pour générer une réponse à une invite donnée.

1. **Exportation du modèle** :
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - Cette commande utilise l'outil `optimum-cli` pour exporter un modèle au format OpenVINO, qui est optimisé pour une inférence efficace.
   - Le modèle exporté est `"microsoft/Phi-3-mini-4k-instruct"`, configuré pour la tâche de génération de texte basée sur le contexte passé.
   - Les poids du modèle sont quantifiés en entiers 4 bits (`int4`), ce qui aide à réduire la taille du modèle et à accélérer le traitement.
   - D'autres paramètres comme `group-size`, `ratio`, et `sym` sont utilisés pour affiner le processus de quantification.
   - Le modèle exporté est enregistré dans le répertoire `./model/phi3-instruct/int4`.

2. **Importation des bibliothèques nécessaires** :
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - Ces lignes importent des classes de la bibliothèque `transformers` et du module `optimum.intel.openvino`, nécessaires pour charger et utiliser le modèle.

3. **Configuration du répertoire du modèle et des paramètres** :
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` spécifie où les fichiers du modèle sont stockés.
   - `ov_config` est un dictionnaire qui configure le modèle OpenVINO pour privilégier la faible latence, utiliser un flux d'inférence et ne pas utiliser de répertoire de cache.

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
   - Cette ligne charge le modèle à partir du répertoire spécifié, en utilisant les paramètres de configuration définis précédemment. Elle permet également l'exécution de code distant si nécessaire.

5. **Chargement du tokenizer** :
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - Cette ligne charge le tokenizer, qui est responsable de convertir le texte en tokens que le modèle peut comprendre.

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
   - Cette chaîne de caractères définit une invite de conversation où l'utilisateur demande à l'assistant AI de se présenter.

8. **Tokenisation de l'invite** :
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - Cette ligne convertit l'invite en tokens que le modèle peut traiter, renvoyant le résultat sous forme de tenseurs PyTorch.

9. **Génération d'une réponse** :
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - Cette ligne utilise le modèle pour générer une réponse basée sur les tokens d'entrée, avec un maximum de 1024 nouveaux tokens.

10. **Décodage de la réponse** :
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - Cette ligne convertit les tokens générés en une chaîne lisible par l'homme, en sautant les tokens spéciaux, et récupère le premier résultat.

