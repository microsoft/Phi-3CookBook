# Technologies clés mentionnées incluent

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - une API de bas niveau pour l'apprentissage automatique accéléré par le matériel, construite sur DirectX 12.
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - une plateforme de calcul parallèle et un modèle d'interface de programmation d'applications (API) développé par Nvidia, permettant le traitement général sur les unités de traitement graphique (GPU).
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - un format ouvert conçu pour représenter les modèles d'apprentissage automatique qui fournit l'interopérabilité entre différents cadres ML.
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique, particulièrement utile pour les petits modèles de langage qui peuvent fonctionner efficacement sur des CPU avec une quantification de 4-8 bits.

## DirectML

DirectML est une API de bas niveau qui permet l'apprentissage automatique accéléré par le matériel. Elle est construite sur DirectX 12 pour utiliser l'accélération GPU et est indépendante des fournisseurs, ce qui signifie qu'elle ne nécessite pas de modifications de code pour fonctionner avec différents fournisseurs de GPU. Elle est principalement utilisée pour les charges de travail d'entraînement et d'inférence de modèles sur les GPU.

En ce qui concerne le support matériel, DirectML est conçu pour fonctionner avec une large gamme de GPU, y compris les GPU intégrés et discrets d'AMD, les GPU intégrés d'Intel et les GPU discrets de NVIDIA. Elle fait partie de la plateforme Windows AI et est supportée sur Windows 10 & 11, permettant l'entraînement et l'inférence de modèles sur n'importe quel appareil Windows.

Il y a eu des mises à jour et des opportunités liées à DirectML, comme le support de jusqu'à 150 opérateurs ONNX et son utilisation par les runtime ONNX et WinML. Elle est soutenue par des grands fournisseurs de matériel intégré (IHVs), chacun implémentant divers méta-commandes.

## CUDA

CUDA, qui signifie Compute Unified Device Architecture, est une plateforme de calcul parallèle et un modèle d'interface de programmation d'applications (API) créé par Nvidia. Elle permet aux développeurs de logiciels d'utiliser une unité de traitement graphique (GPU) compatible CUDA pour le traitement général – une approche appelée GPGPU (General-Purpose computing on Graphics Processing Units). CUDA est un élément clé de l'accélération GPU de Nvidia et est largement utilisée dans divers domaines, y compris l'apprentissage automatique, le calcul scientifique et le traitement vidéo.

Le support matériel pour CUDA est spécifique aux GPU de Nvidia, car c'est une technologie propriétaire développée par Nvidia. Chaque architecture supporte des versions spécifiques de l'outilkit CUDA, qui fournit les bibliothèques et outils nécessaires aux développeurs pour construire et exécuter des applications CUDA.

## ONNX

ONNX (Open Neural Network Exchange) est un format ouvert conçu pour représenter les modèles d'apprentissage automatique. Il fournit une définition d'un modèle de graphe de calcul extensible, ainsi que des définitions d'opérateurs intégrés et de types de données standard. ONNX permet aux développeurs de déplacer des modèles entre différents cadres ML, facilitant l'interopérabilité et rendant plus facile la création et le déploiement d'applications IA.

Phi3 mini peut fonctionner avec ONNX Runtime sur CPU et GPU à travers divers appareils, y compris les plateformes serveur, les desktops Windows, Linux et Mac, et les CPU mobiles.
Les configurations optimisées que nous avons ajoutées sont :

- Modèles ONNX pour int4 DML : Quantifié en int4 via AWQ
- Modèle ONNX pour fp16 CUDA
- Modèle ONNX pour int4 CUDA : Quantifié en int4 via RTN
- Modèle ONNX pour int4 CPU et Mobile : Quantifié en int4 via RTN

## Llama.cpp

Llama.cpp est une bibliothèque logicielle open-source écrite en C++. Elle effectue l'inférence sur divers modèles de langage de grande taille (LLMs), y compris Llama. Développée en parallèle avec la bibliothèque ggml (une bibliothèque de tenseurs à usage général), llama.cpp vise à fournir une inférence plus rapide et une utilisation de mémoire réduite par rapport à l'implémentation originale en Python. Elle supporte l'optimisation matérielle, la quantification, et offre une API simple et des exemples. Si vous êtes intéressé par une inférence LLM efficace, llama.cpp vaut la peine d'être explorée car Phi3 peut exécuter Llama.cpp.

## GGUF

GGUF (Generic Graph Update Format) est un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique. Il est particulièrement utile pour les petits modèles de langage (SLMs) qui peuvent fonctionner efficacement sur des CPU avec une quantification de 4-8 bits. GGUF est bénéfique pour le prototypage rapide et l'exécution de modèles sur des appareils de périphérie ou dans des tâches par lots comme les pipelines CI/CD.

