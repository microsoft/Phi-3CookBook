# Technologies clés mentionnées incluent

1. [DirectML](https://learn.microsoft.com/windows/ai/directml/dml?WT.mc_id=aiml-138114-kinfeylo) - une API de bas niveau pour l'apprentissage automatique accéléré par le matériel, construite sur DirectX 12.
2. [CUDA](https://blogs.nvidia.com/blog/what-is-cuda-2/) - une plateforme de calcul parallèle et un modèle d'interface de programmation d'applications (API) développé par Nvidia, permettant le traitement à usage général sur des unités de traitement graphique (GPU).
3. [ONNX](https://onnx.ai/) (Open Neural Network Exchange) - un format ouvert conçu pour représenter les modèles d'apprentissage automatique qui fournit l'interopérabilité entre différents frameworks ML.
4. [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) (Generic Graph Update Format) - un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique, particulièrement utile pour les modèles de langue plus petits qui peuvent fonctionner efficacement sur des CPU avec une quantification de 4-8 bits.

## DirectML

DirectML est une API de bas niveau qui permet l'apprentissage automatique accéléré par le matériel. Elle est construite sur DirectX 12 pour utiliser l'accélération GPU et est indépendante du fournisseur, ce qui signifie qu'elle ne nécessite pas de modifications de code pour fonctionner avec différents fournisseurs de GPU. Elle est principalement utilisée pour les charges de travail d'entraînement et d'inférence de modèles sur les GPU.

En ce qui concerne le support matériel, DirectML est conçu pour fonctionner avec une large gamme de GPU, y compris les GPU intégrés et discrets d'AMD, les GPU intégrés d'Intel et les GPU discrets de NVIDIA. Elle fait partie de la plateforme Windows AI et est supportée sur Windows 10 et 11, permettant l'entraînement et l'inférence de modèles sur tout appareil Windows.

Il y a eu des mises à jour et des opportunités liées à DirectML, comme le support de jusqu'à 150 opérateurs ONNX et son utilisation par l'exécution ONNX et WinML. Elle est soutenue par les principaux fournisseurs de matériel intégré (IHV), chacun implémentant divers métacommandes.

## CUDA

CUDA, qui signifie Compute Unified Device Architecture, est une plateforme de calcul parallèle et un modèle d'interface de programmation d'applications (API) créé par Nvidia. Elle permet aux développeurs de logiciels d'utiliser une unité de traitement graphique (GPU) compatible CUDA pour le traitement à usage général – une approche appelée GPGPU (General-Purpose computing on Graphics Processing Units). CUDA est un élément clé de l'accélération GPU de Nvidia et est largement utilisé dans divers domaines, y compris l'apprentissage automatique, le calcul scientifique et le traitement vidéo.

Le support matériel pour CUDA est spécifique aux GPU de Nvidia, car il s'agit d'une technologie propriétaire développée par Nvidia. Chaque architecture prend en charge des versions spécifiques du kit d'outils CUDA, qui fournit les bibliothèques et outils nécessaires aux développeurs pour créer et exécuter des applications CUDA.

## ONNX

ONNX (Open Neural Network Exchange) est un format ouvert conçu pour représenter les modèles d'apprentissage automatique. Il fournit une définition d'un modèle de graphe de calcul extensible, ainsi que des définitions d'opérateurs intégrés et de types de données standard. ONNX permet aux développeurs de déplacer des modèles entre différents frameworks ML, permettant l'interopérabilité et facilitant la création et le déploiement d'applications IA.

Phi3 mini peut fonctionner avec ONNX Runtime sur CPU et GPU sur différents appareils, y compris les plateformes serveur, les ordinateurs de bureau Windows, Linux et Mac, et les CPU mobiles.
Les configurations optimisées que nous avons ajoutées sont

- Modèles ONNX pour int4 DML : Quantifiés en int4 via AWQ
- Modèle ONNX pour fp16 CUDA
- Modèle ONNX pour int4 CUDA : Quantifié en int4 via RTN
- Modèle ONNX pour int4 CPU et Mobile : Quantifié en int4 via RTN

## Llama.cpp

Llama.cpp est une bibliothèque logicielle open-source écrite en C++. Elle effectue l'inférence sur divers modèles de langue de grande taille (LLM), y compris Llama. Développée en parallèle avec la bibliothèque ggml (une bibliothèque tensorielle à usage général), llama.cpp vise à fournir une inférence plus rapide et une utilisation de la mémoire inférieure par rapport à l'implémentation originale en Python. Elle prend en charge l'optimisation matérielle, la quantification, et offre une API simple et des exemples. Si vous êtes intéressé par une inférence efficace des LLM, llama.cpp vaut la peine d'être explorée car Phi3 peut exécuter Llama.cpp.

## GGUF

GGUF (Generic Graph Update Format) est un format utilisé pour représenter et mettre à jour les modèles d'apprentissage automatique. Il est particulièrement utile pour les modèles de langue plus petits (SLM) qui peuvent fonctionner efficacement sur des CPU avec une quantification de 4-8 bits. GGUF est bénéfique pour le prototypage rapide et l'exécution de modèles sur des appareils en périphérie ou dans des tâches par lots comme les pipelines CI/CD.

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.