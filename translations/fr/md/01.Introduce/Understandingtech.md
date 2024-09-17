# Technologies clés mentionnées

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - une API de bas niveau pour l'apprentissage automatique accéléré par le matériel, construite sur DirectX 12.
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - une plateforme de calcul parallèle et un modèle d'interface de programmation d'application (API) développé par Nvidia, permettant le traitement à usage général sur les unités de traitement graphique (GPU).
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - un format ouvert conçu pour représenter les modèles d'apprentissage automatique qui offre une interopérabilité entre différents cadres ML.
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique, particulièrement utile pour les petits modèles de langage qui peuvent fonctionner efficacement sur des CPU avec une quantification en 4-8 bits.

## DirectML

DirectML est une API de bas niveau qui permet l'apprentissage automatique accéléré par le matériel. Elle est construite sur DirectX 12 pour utiliser l'accélération GPU et est indépendante du fournisseur, ce qui signifie qu'elle ne nécessite pas de modifications de code pour fonctionner avec différents fournisseurs de GPU. Elle est principalement utilisée pour l'entraînement et l'inférence de modèles sur les GPU.

En ce qui concerne le support matériel, DirectML est conçu pour fonctionner avec une large gamme de GPU, y compris les GPU intégrés et discrets d'AMD, les GPU intégrés d'Intel et les GPU discrets de NVIDIA. Elle fait partie de la plateforme Windows AI et est supportée sur Windows 10 & 11, permettant l'entraînement et l'inférence de modèles sur tout appareil Windows.

Il y a eu des mises à jour et des opportunités liées à DirectML, comme le support de jusqu'à 150 opérateurs ONNX et son utilisation par le runtime ONNX et WinML. Elle est soutenue par des grands fournisseurs de matériel intégré (IHV), chacun implémentant divers méta-commandes.

## CUDA

CUDA, qui signifie Compute Unified Device Architecture, est une plateforme de calcul parallèle et un modèle d'interface de programmation d'application (API) créé par Nvidia. Elle permet aux développeurs de logiciels d'utiliser une unité de traitement graphique (GPU) compatible CUDA pour un traitement à usage général – une approche appelée GPGPU (General-Purpose computing on Graphics Processing Units). CUDA est un élément clé de l'accélération GPU de Nvidia et est largement utilisé dans divers domaines, y compris l'apprentissage automatique, le calcul scientifique et le traitement vidéo.

Le support matériel pour CUDA est spécifique aux GPU de Nvidia, car il s'agit d'une technologie propriétaire développée par Nvidia. Chaque architecture prend en charge des versions spécifiques du kit d'outils CUDA, qui fournit les bibliothèques et outils nécessaires aux développeurs pour créer et exécuter des applications CUDA.

## ONNX

ONNX (Open Neural Network Exchange) est un format ouvert conçu pour représenter les modèles d'apprentissage automatique. Il fournit une définition d'un modèle de graphe de calcul extensible, ainsi que des définitions d'opérateurs intégrés et de types de données standard. ONNX permet aux développeurs de déplacer des modèles entre différents cadres ML, facilitant ainsi l'interopérabilité et simplifiant la création et le déploiement d'applications d'IA.

Phi3 mini peut fonctionner avec ONNX Runtime sur CPU et GPU à travers différents appareils, y compris les plateformes serveur, les ordinateurs de bureau Windows, Linux et Mac, et les CPU mobiles.
Les configurations optimisées que nous avons ajoutées sont

- Modèles ONNX pour int4 DML : Quantifiés en int4 via AWQ
- Modèle ONNX pour fp16 CUDA
- Modèle ONNX pour int4 CUDA : Quantifiés en int4 via RTN
- Modèle ONNX pour int4 CPU et Mobile : Quantifiés en int4 via RTN

## Llama.cpp

Llama.cpp est une bibliothèque logicielle open-source écrite en C++. Elle effectue des inférences sur divers grands modèles de langage (LLM), y compris Llama. Développé en parallèle avec la bibliothèque ggml (une bibliothèque de tenseurs à usage général), llama.cpp vise à fournir une inférence plus rapide et une utilisation de mémoire réduite par rapport à l'implémentation originale en Python. Elle prend en charge l'optimisation matérielle, la quantification et offre une API simple et des exemples. Si vous êtes intéressé par une inférence LLM efficace, llama.cpp vaut la peine d'être explorée car Phi3 peut exécuter Llama.cpp.

## GGUF

GGUF (Generic Graph Update Format) est un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique. Il est particulièrement utile pour les petits modèles de langage (SLM) qui peuvent fonctionner efficacement sur des CPU avec une quantification en 4-8 bits. GGUF est bénéfique pour le prototypage rapide et l'exécution de modèles sur des appareils périphériques ou dans des tâches par lots comme les pipelines CI/CD.

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.