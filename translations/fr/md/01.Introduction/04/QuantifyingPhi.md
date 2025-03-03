# **Quantification de la famille Phi**

La quantification de modèle fait référence au processus de réduction de l'échelle des paramètres (tels que les poids et les valeurs d'activation) d'un modèle de réseau neuronal, en passant d'une plage de valeurs large (généralement continue) à une plage de valeurs finie plus petite. Cette technologie permet de réduire la taille et la complexité computationnelle du modèle, tout en améliorant son efficacité dans des environnements aux ressources limitées, comme les appareils mobiles ou les systèmes embarqués. La quantification de modèle atteint une compression en réduisant la précision des paramètres, mais cela introduit également une certaine perte de précision. Par conséquent, lors du processus de quantification, il est nécessaire de trouver un équilibre entre la taille du modèle, la complexité computationnelle et la précision. Les méthodes de quantification courantes incluent la quantification en virgule fixe, la quantification en virgule flottante, etc. Vous pouvez choisir la stratégie de quantification appropriée en fonction du scénario et des besoins spécifiques.

Nous espérons déployer le modèle GenAI sur des appareils en périphérie et permettre à davantage d'appareils d'entrer dans des scénarios GenAI, tels que les appareils mobiles, les PC AI / Copilot+PC, et les appareils IoT traditionnels. Grâce au modèle quantifié, nous pouvons le déployer sur différents appareils en périphérie en fonction de leurs caractéristiques. Combiné avec le cadre d'accélération du modèle et le modèle quantifié fournis par les fabricants de matériel, nous pouvons construire de meilleurs scénarios d'application SLM.

Dans le cadre de la quantification, nous avons différentes précisions (INT4, INT8, FP16, FP32). Voici une explication des précisions de quantification couramment utilisées :

### **INT4**

La quantification INT4 est une méthode radicale qui réduit les poids et les valeurs d'activation du modèle à des entiers sur 4 bits. La quantification INT4 entraîne généralement une perte de précision plus importante en raison de la plage de représentation plus restreinte et de la précision plus faible. Cependant, par rapport à la quantification INT8, la quantification INT4 peut réduire encore davantage les exigences de stockage et la complexité computationnelle du modèle. Il convient de noter que la quantification INT4 est relativement rare dans les applications pratiques, car une précision trop faible peut entraîner une dégradation significative des performances du modèle. De plus, tous les matériels ne prennent pas en charge les opérations INT4, il est donc nécessaire de tenir compte de la compatibilité matérielle lors du choix de la méthode de quantification.

### **INT8**

La quantification INT8 consiste à convertir les poids et les activations d’un modèle, exprimés en nombres à virgule flottante, en entiers sur 8 bits. Bien que la plage numérique représentée par les entiers INT8 soit plus restreinte et moins précise, cette méthode permet de réduire considérablement les besoins en stockage et en calcul. Dans la quantification INT8, les poids et les valeurs d'activation du modèle subissent un processus de quantification, comprenant un facteur d'échelle et un décalage, afin de préserver autant que possible les informations d'origine en virgule flottante. Lors de l'inférence, ces valeurs quantifiées sont déquantifiées en nombres à virgule flottante pour le calcul, puis re-quantifiées en INT8 pour l'étape suivante. Cette méthode offre une précision suffisante dans la plupart des applications tout en maintenant une efficacité computationnelle élevée.

### **FP16**

Le format FP16, soit les nombres à virgule flottante sur 16 bits (float16), réduit de moitié l’empreinte mémoire par rapport aux nombres à virgule flottante sur 32 bits (float32), ce qui présente des avantages significatifs dans les applications d'apprentissage profond à grande échelle. Le format FP16 permet de charger des modèles plus volumineux ou de traiter davantage de données avec les mêmes limitations de mémoire GPU. Avec le support croissant des opérations FP16 par le matériel GPU moderne, l'utilisation du format FP16 peut également améliorer la vitesse de calcul. Cependant, le format FP16 a également ses inconvénients inhérents, à savoir une précision moindre, ce qui peut entraîner une instabilité numérique ou une perte de précision dans certains cas.

### **FP32**

Le format FP32 offre une précision plus élevée et peut représenter avec précision une large gamme de valeurs. Dans des scénarios nécessitant des opérations mathématiques complexes ou des résultats de haute précision, le format FP32 est privilégié. Cependant, une précision élevée signifie également une utilisation accrue de la mémoire et un temps de calcul plus long. Pour les modèles d'apprentissage profond à grande échelle, en particulier lorsqu'il y a de nombreux paramètres et une énorme quantité de données, le format FP32 peut entraîner une insuffisance de mémoire GPU ou une diminution de la vitesse d'inférence.

Sur les appareils mobiles ou les appareils IoT, nous pouvons convertir les modèles Phi-3.x en INT4, tandis que les PC AI / Copilot PC peuvent utiliser des précisions plus élevées telles que INT8, FP16 ou FP32.

Actuellement, différents fabricants de matériel proposent des cadres variés pour prendre en charge les modèles génératifs, comme OpenVINO d'Intel, QNN de Qualcomm, MLX d'Apple et CUDA de Nvidia, qui, combinés à la quantification de modèles, permettent un déploiement local.

Sur le plan technique, nous disposons de différents formats après quantification, tels que les formats PyTorch / Tensorflow, GGUF et ONNX. J'ai réalisé une comparaison des formats et des scénarios d'application entre GGUF et ONNX. Ici, je recommande le format de quantification ONNX, qui bénéficie d'un bon support allant du cadre du modèle au matériel. Dans ce chapitre, nous nous concentrerons sur ONNX Runtime pour GenAI, OpenVINO et Apple MLX pour effectuer la quantification des modèles (si vous avez une meilleure méthode, vous pouvez également nous la soumettre via un PR).

**Ce chapitre inclut**

1. [Quantification de Phi-3.5 / 4 à l'aide de llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantification de Phi-3.5 / 4 à l'aide des extensions Generative AI pour onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantification de Phi-3.5 / 4 à l'aide d'Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantification de Phi-3.5 / 4 à l'aide du cadre Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité pour les malentendus ou les interprétations erronées résultant de l'utilisation de cette traduction.