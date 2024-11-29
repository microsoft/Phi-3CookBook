# Sécurité de l'IA pour les modèles Phi-3

La famille de modèles Phi-3 a été développée conformément à la [Norme de Microsoft pour une IA Responsable](https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE5cmFl), qui est un ensemble d'exigences à l'échelle de l'entreprise basé sur les six principes suivants : responsabilité, transparence, équité, fiabilité et sécurité, confidentialité et sécurité, et inclusivité, qui forment les [principes de l'IA Responsable de Microsoft](https://www.microsoft.com/ai/responsible-ai).

Comme pour les modèles Phi-3 précédents, une évaluation de sécurité multi-facettes et une approche de sécurité après formation ont été adoptées, avec des mesures supplémentaires prises pour tenir compte des capacités multilingues de cette version. Notre approche de la formation et des évaluations de sécurité, y compris les tests dans plusieurs langues et catégories de risques, est décrite dans le [Document sur la sécurité après formation de Phi-3](https://arxiv.org/abs/2407.13833). Bien que les modèles Phi-3 bénéficient de cette approche, les développeurs doivent appliquer les meilleures pratiques de l'IA responsable, y compris la cartographie, la mesure et l'atténuation des risques associés à leur cas d'utilisation spécifique et à leur contexte culturel et linguistique.

## Meilleures Pratiques

Comme d'autres modèles, la famille de modèles Phi peut potentiellement se comporter de manière injuste, peu fiable ou offensante.

Certains des comportements limitants des SLM et LLM dont vous devez être conscient incluent :

- **Qualité de Service :** Les modèles Phi sont principalement entraînés sur des textes en anglais. Les langues autres que l'anglais auront des performances moindres. Les variétés de la langue anglaise moins représentées dans les données d'entraînement pourraient avoir des performances inférieures à l'anglais américain standard.
- **Représentation des préjudices et perpétuation des stéréotypes :** Ces modèles peuvent sur- ou sous-représenter des groupes de personnes, effacer la représentation de certains groupes ou renforcer des stéréotypes dégradants ou négatifs. Malgré la formation de sécurité postérieure, ces limitations peuvent encore être présentes en raison des niveaux de représentation différents de différents groupes ou de la prévalence d'exemples de stéréotypes négatifs dans les données d'entraînement qui reflètent les schémas du monde réel et les biais sociétaux.
- **Contenu inapproprié ou offensant :** Ces modèles peuvent produire d'autres types de contenu inapproprié ou offensant, ce qui peut les rendre inappropriés à déployer pour des contextes sensibles sans mesures d'atténuation supplémentaires spécifiques au cas d'utilisation.
- **Fiabilité de l'information :** Les modèles de langage peuvent générer du contenu insensé ou fabriquer du contenu qui peut sembler raisonnable mais qui est inexact ou obsolète.
- **Portée limitée pour le code :** La majorité des données d'entraînement de Phi-3 est basée sur Python et utilise des packages courants tels que "typing, math, random, collections, datetime, itertools". Si le modèle génère des scripts Python qui utilisent d'autres packages ou des scripts dans d'autres langues, nous recommandons fortement aux utilisateurs de vérifier manuellement toutes les utilisations des API.

Les développeurs doivent appliquer les meilleures pratiques de l'IA responsable et sont responsables de s'assurer qu'un cas d'utilisation spécifique est conforme aux lois et réglementations en vigueur (par exemple, confidentialité, commerce, etc.).

## Considérations pour une IA Responsable

Comme d'autres modèles de langage, les modèles de la série Phi peuvent potentiellement se comporter de manière injuste, peu fiable ou offensante. Certains des comportements limitants dont il faut être conscient incluent :

**Qualité de Service :** Les modèles Phi sont principalement entraînés sur des textes en anglais. Les langues autres que l'anglais auront des performances moindres. Les variétés de la langue anglaise moins représentées dans les données d'entraînement pourraient avoir des performances inférieures à l'anglais américain standard.

**Représentation des préjudices et perpétuation des stéréotypes :** Ces modèles peuvent sur- ou sous-représenter des groupes de personnes, effacer la représentation de certains groupes ou renforcer des stéréotypes dégradants ou négatifs. Malgré la formation de sécurité postérieure, ces limitations peuvent encore être présentes en raison des niveaux de représentation différents de différents groupes ou de la prévalence d'exemples de stéréotypes négatifs dans les données d'entraînement qui reflètent les schémas du monde réel et les biais sociétaux.

**Contenu inapproprié ou offensant :** Ces modèles peuvent produire d'autres types de contenu inapproprié ou offensant, ce qui peut les rendre inappropriés à déployer pour des contextes sensibles sans mesures d'atténuation supplémentaires spécifiques au cas d'utilisation. Fiabilité de l'information : Les modèles de langage peuvent générer du contenu insensé ou fabriquer du contenu qui peut sembler raisonnable mais qui est inexact ou obsolète.

**Portée limitée pour le code :** La majorité des données d'entraînement de Phi-3 est basée sur Python et utilise des packages courants tels que "typing, math, random, collections, datetime, itertools". Si le modèle génère des scripts Python qui utilisent d'autres packages ou des scripts dans d'autres langues, nous recommandons fortement aux utilisateurs de vérifier manuellement toutes les utilisations des API.

Les développeurs doivent appliquer les meilleures pratiques de l'IA responsable et sont responsables de s'assurer qu'un cas d'utilisation spécifique est conforme aux lois et réglementations en vigueur (par exemple, confidentialité, commerce, etc.). Les domaines importants à prendre en compte incluent :

**Allocation :** Les modèles peuvent ne pas convenir à des scénarios pouvant avoir un impact conséquent sur le statut juridique ou l'allocation de ressources ou d'opportunités de vie (ex : logement, emploi, crédit, etc.) sans évaluations supplémentaires et techniques de dé-biaisage.

**Scénarios à haut risque :** Les développeurs doivent évaluer l'adéquation de l'utilisation des modèles dans des scénarios à haut risque où des résultats injustes, peu fiables ou offensants pourraient être extrêmement coûteux ou causer des préjudices. Cela inclut la fourniture de conseils dans des domaines sensibles ou d'expertise où la précision et la fiabilité sont essentielles (ex : conseils juridiques ou de santé). Des mesures de protection supplémentaires doivent être mises en œuvre au niveau de l'application en fonction du contexte de déploiement.

**Désinformation :** Les modèles peuvent produire des informations inexactes. Les développeurs doivent suivre les meilleures pratiques de transparence et informer les utilisateurs finaux qu'ils interagissent avec un système d'IA. Au niveau de l'application, les développeurs peuvent construire des mécanismes de retour d'information et des pipelines pour ancrer les réponses dans des informations contextuelles spécifiques au cas d'utilisation, une technique connue sous le nom de génération augmentée par la récupération (RAG).

**Génération de contenu nuisible :** Les développeurs doivent évaluer les résultats en fonction de leur contexte et utiliser les classificateurs de sécurité disponibles ou des solutions personnalisées appropriées pour leur cas d'utilisation.

**Abus :** D'autres formes d'abus telles que la fraude, le spam ou la production de logiciels malveillants peuvent être possibles, et les développeurs doivent s'assurer que leurs applications ne violent pas les lois et réglementations applicables.

### Ajustement fin et sécurité du contenu de l'IA

Après avoir affiné un modèle, nous recommandons fortement de tirer parti des mesures [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pour surveiller le contenu généré par les modèles, identifier et bloquer les risques potentiels, les menaces et les problèmes de qualité.

![Phi3AISafety](../../../../translated_images/phi3aisafety.dc76a5bdb07ffc178e8e6d6be94d55a847ad1477d379bc28055823c777e3b06f.fr.png)

[Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) prend en charge le contenu textuel et visuel. Il peut être déployé dans le cloud, dans des conteneurs déconnectés et sur des appareils embarqués/en périphérie.

## Vue d'ensemble de la sécurité du contenu de l'IA Azure

Azure AI Content Safety n'est pas une solution universelle ; elle peut être personnalisée pour s'aligner sur les politiques spécifiques des entreprises. De plus, ses modèles multilingues lui permettent de comprendre plusieurs langues simultanément.

![AIContentSafety](../../../../translated_images/AIcontentsafety.2319fe2f8154f2594e16643d4a4696100b7bb74af96b7a82b8f3327618d81122.fr.png)

- **Sécurité du contenu de l'IA Azure**
- **Développeur Microsoft**
- **5 vidéos**

Le service Azure AI Content Safety détecte le contenu nuisible généré par les utilisateurs et l'IA dans les applications et services. Il comprend des API textuelles et visuelles qui vous permettent de détecter du matériel nuisible ou inapproprié.

[Playlist de sécurité du contenu de l'IA](https://www.youtube.com/playlist?list=PLlrxD0HtieHjaQ9bJjyp1T7FeCbmVcPkQ)

**Avertissement**:
Ce document a été traduit à l'aide de services de traduction automatisée par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations cruciales, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.