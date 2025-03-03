# **Quantification de Phi-3.5 avec Intel OpenVINO**

Intel est le fabricant de processeurs le plus traditionnel, comptant de nombreux utilisateurs. Avec l'essor de l'apprentissage automatique et du deep learning, Intel s'est également lancé dans la compétition pour l'accélération de l'IA. Pour l'inférence des modèles, Intel utilise non seulement des GPU et des CPU, mais aussi des NPU.

Nous espérons déployer la famille Phi-3.x sur les dispositifs finaux, dans l'espoir de devenir une partie essentielle des PC d'IA et des PC Copilot. Le chargement du modèle sur les dispositifs finaux dépend de la collaboration entre différents fabricants de matériel. Ce chapitre se concentre principalement sur le scénario d'application d'Intel OpenVINO en tant que modèle quantitatif.

## **Qu'est-ce qu'OpenVINO**

OpenVINO est un kit d'outils open source conçu pour optimiser et déployer des modèles de deep learning, du cloud jusqu'à la périphérie. Il accélère l'inférence de deep learning dans divers cas d'utilisation, tels que l'IA générative, la vidéo, l'audio et le langage, avec des modèles provenant de frameworks populaires comme PyTorch, TensorFlow, ONNX, et bien d'autres. Convertissez et optimisez des modèles, puis déployez-les sur un mélange de matériel et d'environnements Intel®, que ce soit sur site ou sur dispositif, dans le navigateur ou dans le cloud.

Avec OpenVINO, vous pouvez désormais quantifier rapidement le modèle GenAI sur le matériel Intel et accélérer l'inférence du modèle.

OpenVINO prend désormais en charge la conversion quantifiée de Phi-3.5-Vision et Phi-3.5-Instruct.

### **Configuration de l'environnement**

Veuillez vous assurer que les dépendances suivantes sont installées. Voici le fichier requirements.txt : 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantification de Phi-3.5-Instruct avec OpenVINO**

Dans le terminal, exécutez ce script :

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantification de Phi-3.5-Vision avec OpenVINO**

Exécutez ce script dans Python ou Jupyter Lab :

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Exemples pour Phi-3.5 avec Intel OpenVINO**

| Laboratoires | Présentation | Accéder |
| ------------ | ------------ | ------- |
| 🚀 Lab-Présentation de Phi-3.5 Instruct  | Apprenez à utiliser Phi-3.5 Instruct sur votre PC d'IA | [Accéder](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb) |
| 🚀 Lab-Présentation de Phi-3.5 Vision (image) | Apprenez à utiliser Phi-3.5 Vision pour analyser des images sur votre PC d'IA | [Accéder](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb) |
| 🚀 Lab-Présentation de Phi-3.5 Vision (vidéo) | Apprenez à utiliser Phi-3.5 Vision pour analyser des vidéos sur votre PC d'IA | [Accéder](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb) |

## **Ressources**

1. En savoir plus sur Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Répertoire GitHub d'Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.