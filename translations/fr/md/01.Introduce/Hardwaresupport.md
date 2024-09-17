# Support matériel pour Phi-3

Microsoft Phi-3 a été optimisé pour ONNX Runtime et prend en charge Windows DirectML. Il fonctionne bien sur divers types de matériel, y compris les GPU, les CPU et même les appareils mobiles.

## Matériel des appareils
Plus précisément, le matériel pris en charge inclut :

- GPU SKU : RTX 4090 (DirectML)
- GPU SKU : 1 A100 80GB (CUDA)
- CPU SKU : Standard F64s v2 (64 vCPUs, 128 GiB de mémoire)

## Mobile SKU

- Android - Samsung Galaxy S21
- Apple iPhone 14 ou supérieur Processeur A16/A17

## Spécification matérielle de Phi-3

- Configuration minimale requise.
- Windows : GPU compatible DirectX 12 et un minimum de 4 Go de RAM combinée

CUDA : GPU NVIDIA avec une capacité de calcul >= 7.02

![HardwareSupport](../../../../translated_images/phi3hardware.18078f58e0564ddd43d2acce655b86f50c1b2dd9fe2be2b52d49d835bcf36fbc.fr.png)

## Exécution d'onnxruntime sur plusieurs GPU

Les modèles ONNX disponibles pour Phi-3 ne sont actuellement prévus que pour 1 GPU. Il est possible de prendre en charge plusieurs GPU pour le modèle Phi-3, mais ORT avec 2 GPU ne garantit pas qu'il offrira plus de débit par rapport à 2 instances d'ort.

Lors de [Build 2024, l'équipe GenAI ONNX](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC) a annoncé qu'elle avait activé les instances multiples au lieu du multi-GPU pour les modèles Phi.

Actuellement, cela vous permet de lancer une instance onnnxruntime ou onnxruntime-genai avec la variable d'environnement CUDA_VISIBLE_DEVICES comme ceci.

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```

N'hésitez pas à explorer davantage Phi-3 dans [Azure AI Studio](https://ai.azure.com)

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.