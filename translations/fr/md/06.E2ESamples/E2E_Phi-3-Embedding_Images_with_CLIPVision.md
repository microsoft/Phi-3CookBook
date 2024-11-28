# Utilisation du CLIPVisionModel pour traiter des images et générer des embeddings d'images avec Phi-3-vision

L'exemple python suivant fournit la fonctionnalité nécessaire pour traiter des images et générer des embeddings d'images en utilisant le CLIPVisionModel.

## Qu'est-ce que CLIP
CLIP, qui signifie Contrastive Language-Image Pre-training, est un modèle développé par OpenAI qui apprend efficacement les concepts visuels à partir de la supervision en langage naturel. C’est un modèle multimodal qui combine la compréhension des images et du texte dans un cadre unique. CLIP est entraîné sur une variété d'images provenant d'internet et le texte associé, apprenant à prédire quelles images étaient associées à quels textes, reliant ainsi efficacement les deux modalités.

Le modèle fonctionne en prenant une image et un extrait de texte en entrée, puis en prédisant la probabilité que le texte soit une description précise de l'image. Cette approche permet à CLIP de gérer une large gamme de tâches visuelles, telles que la reconnaissance d'objets, la classification, et même la génération de descriptions pour des images qu'il n'a jamais vues auparavant.

L'un des principaux avantages de CLIP est sa capacité à effectuer un apprentissage "zero-shot", où le modèle peut correctement gérer des tâches pour lesquelles il n'a pas été explicitement entraîné, simplement en lisant la description de la tâche. Cela est possible grâce à la grande quantité de données diversifiées sur lesquelles il a été entraîné, ce qui l'aide à bien se généraliser à de nouvelles tâches.

## Phi-3-vision
Phi-3-vision est un modèle multimodal de 4,2 milliards de paramètres avec des capacités de langage et de vision, capable de raisonner sur des images du monde réel et des documents numériques, d'extraire et de raisonner sur le texte des images, et de générer des insights et des réponses liées à des graphiques ou des diagrammes.

**Objectif de l'exemple :** Cet exemple démontre la génération d'embeddings d'images en utilisant CLIP et comment cela peut être appliqué à des tâches liées au modèle Phi-3. Il sert de référence pour comparer les performances et les caractéristiques de différentes techniques d'embeddings (CLIP vs. Phi-3).
**Défi d'intégration :** Intégrer un autre encodeur de vision comme CLIP directement dans Phi-3 est en effet complexe. Cette complexité provient des différences architecturales et de la nécessité d'une intégration transparente sans perte de contexte ou de performance. L'intégration n'a pas encore été entièrement évaluée ou mise en œuvre, donc cela est inclus.
**Approche de comparaison :** Le code vise à fournir une comparaison parallèle plutôt qu'une solution intégrée. Il permet aux utilisateurs de voir comment les embeddings de CLIP se comportent aux côtés des embeddings de Phi-3, fournissant des insights sur les avantages ou les inconvénients potentiels.
**Clarification :** Cet exemple du Phi-3CookBook : montre comment utiliser les embeddings de CLIP comme un outil de comparaison plutôt qu'une intégration directe dans Phi-3.
**Travail d'intégration :** L'intégration complète des embeddings de CLIP dans Phi-3 reste un défi et n'a pas été entièrement explorée mais est là pour que les clients puissent expérimenter.

## Code Exemple
Ce code définit une classe appelée Phi3ImageEmbedding qui représente un modèle d'embedding d'images. Le but de cette classe est de traiter des images et de générer des embeddings qui peuvent être utilisés pour des tâches en aval telles que la classification ou la récupération d'images.

La méthode __init__ initialise le modèle en configurant divers composants tels que le dropout des embeddings, le processeur d'images, les paramètres de transformation HD, et la projection d'images. Elle prend un objet config en entrée, qui contient les paramètres de configuration pour le modèle. Le paramètre wte est une entrée optionnelle qui représente les embeddings de tokens de mots.

La méthode get_img_features prend un tenseur d'entrée img_embeds représentant les embeddings d'images et renvoie un tenseur représentant les caractéristiques d'image extraites. Elle utilise le img_processor pour traiter les embeddings d'images et extraire les caractéristiques souhaitées en fonction des paramètres layer_idx et type_feature.

## Explication du Code
Passons en revue le code étape par étape :

Le code importe les bibliothèques et modules nécessaires, y compris math, torch, torch.nn, et divers composants de la bibliothèque transformers.

Le code définit un objet de configuration appelé CLIP_VIT_LARGE_PATCH14_336_CONFIG qui contient divers hyperparamètres pour le modèle d'embedding d'images.

La classe Phi3ImageEmbedding est définie, qui est une sous-classe de torch.nn.Module. Cette classe représente le modèle d'embedding d'images et contient des méthodes pour la propagation avant et la définition des caractéristiques d'images.

La méthode __init__ initialise l'objet Phi3ImageEmbedding. Elle prend un objet config en entrée, qui est une instance de la classe PretrainedConfig. Elle prend également un argument wte optionnel.

La méthode __init__ initialise divers attributs de l'objet Phi3ImageEmbedding en fonction de l'objet config fourni. Elle définit la taille cachée, le taux de dropout, le processeur d'images, la projection d'images, et d'autres paramètres.

La méthode set_img_features définit les caractéristiques d'images pour le modèle. Elle prend un tenseur de caractéristiques d'images en entrée et l'assigne à l'attribut img_features de l'objet.

La méthode set_img_sizes définit les tailles d'images pour le modèle. Elle prend un tenseur de tailles d'images en entrée et l'assigne à l'attribut img_sizes de l'objet.

La méthode get_img_features extrait les caractéristiques d'images des embeddings d'images d'entrée. Elle prend un tenseur d'embeddings d'images en entrée et renvoie les caractéristiques d'images extraites.

La méthode forward effectue la propagation avant à travers le modèle. Elle prend les IDs d'entrée, les valeurs de pixels, et les tailles d'images en entrée et renvoie les états cachés du modèle. Elle vérifie d'abord si les caractéristiques et tailles d'images sont déjà définies, et si ce n'est pas le cas, elle utilise l'entrée fournie pour les définir. Ensuite, elle traite les IDs d'entrée et extrait les caractéristiques d'images en fonction du processeur d'images configuré. Enfin, elle applique la projection d'images aux caractéristiques extraites et renvoie les états cachés.

Dans l'ensemble, ce code définit une classe qui représente un modèle d'embedding d'images et fournit des méthodes pour définir les caractéristiques d'images et effectuer la propagation avant.

[Code Exemple](../../../../code/06.E2E/phi3imageembedding.py)
```
import math
import torch
from transformers import CLIPVisionModel, PretrainedConfig
from transformers import CLIPVisionConfig 
from transformers.utils import logging
from datetime import datetime 

# Import necessary libraries
import torch.nn as nn

# Set up logging
logger = logging.get_logger(__name__)

# Define the configuration for the CLIPVisionModel
CLIP_VIT_LARGE_PATCH14_336_CONFIG = CLIPVisionConfig(
    attention_dropout=0.0,
    dropout=0.0,
    hidden_act="quick_gelu",
    hidden_size=1024,
    image_size=336,
    initializer_factor=1.0,
    initializer_range=0.02,
    intermediate_size=4096,
    layer_norm_eps=1e-05,
    num_attention_heads=16,
    num_channels=3,
    num_hidden_layers=24,
    patch_size=14,
    projection_dim=768 
)

# Define the Phi3ImageEmbedding class
class Phi3ImageEmbedding(nn.Module):
        """Phi3 Image embedding."""

        def __init__(self, config: PretrainedConfig, wte=None, **kwargs) -> None:
                super().__init__()

                # Set up the embedding dropout
                hidden_size = config.n_embd if hasattr(config, 'n_embd') else config.hidden_size
                if hasattr(config, 'embd_pdrop') or hasattr(config, 'embed_pdrop'):
                        embd_drop = config.embd_pdrop if hasattr(config, 'embd_pdrop') else config.embed_pdrop
                        self.drop = nn.Dropout(embd_drop)
                else:
                        self.drop = None

                self.wte = wte

                # Set up the image processor based on the configuration
                if isinstance(config.img_processor, dict) and config.img_processor.get('name', None) == 'clip_vision_model':
                        assert 'model_name' in config.img_processor, 'model_name must be provided for CLIPVisionModel'
                        assert 'image_dim_out' in config.img_processor, 'image_dim_out must be provided for CLIPVisionModel'
                        assert 'num_img_tokens' in config.img_processor, 'num_img_tokens must be provided for CLIPVisionModel'
                        assert config.img_processor['model_name'] == 'openai/clip-vit-large-patch14-336'
                        clip_config = CLIP_VIT_LARGE_PATCH14_336_CONFIG
                        self.img_processor = CLIPVisionModel(clip_config)
                        image_dim_out = config.img_processor['image_dim_out']
                        self.num_img_tokens = config.img_processor['num_img_tokens']
                else:
                        raise NotImplementedError(f'img_processor = {config.img_processor}, not implemented')

                self.image_dim_out = image_dim_out
                self.img_sizes = None

                # Set up the HD transform parameters
                self.use_hd_transform = kwargs.get('use_hd_transform', False)
                self.with_learnable_separator = kwargs.get('with_learnable_separator', False)
                self.hd_transform_order = kwargs.get('hd_transform_order', 'glb_sub')
                assert self.use_hd_transform == self.with_learnable_separator, 'use_hd_transform and with_learnable_separator should have same value'
                if self.with_learnable_separator:
                        assert self.use_hd_transform, 'learnable separator is only for hd transform'
                        self.glb_GN = nn.Parameter(torch.zeros([1, 1, self.image_dim_out * 4]))
                        self.sub_GN = nn.Parameter(torch.zeros([1, 1, 1, self.image_dim_out * 4]))
                        logger.info(f'learnable separator enabled for hd transform, hd_transform_order = {self.hd_transform_order}')

                # Set up the image projection based on the projection_cls
                projection_cls = kwargs.get('projection_cls', 'linear')
                if projection_cls == 'linear':
                        self.img_projection = nn.Linear(image_dim_out, hidden_size)
                elif projection_cls == 'mlp' and self.use_hd_transform:
                        dim_projection = hidden_size
                        depth = 2
                        layers = [nn.Linear(image_dim_out * 4, dim_projection)]
                        for _ in range(1, depth):
                                layers.extend([nn.GELU(),
                                                                nn.Linear(dim_projection, dim_projection)])
                        self.img_projection = nn.Sequential(*layers)
                elif projection_cls == 'mlp':
                        dim_projection = hidden_size
                        depth = 2
                        layers = [nn.Linear(image_dim_out, dim_projection)]
                        for _ in range(1, depth):
                                layers.extend([nn.GELU(),
                                                                nn.Linear(dim_projection, dim_projection)])
                        self.img_projection = nn.Sequential(*layers)
                else:
                        raise NotImplementedError(f'projection_cls = {projection_cls}, not implemented')

                self.vocab_size = config.vocab_size
                self.img_features = None

                # Set up the layer index and type of feature for the image processor
                if isinstance(config.img_processor, dict):
                        self.layer_idx = config.img_processor.get('layer_idx', -2)
                        self.type_feature = config.img_processor.get('type_feature', 'patch')
                else:
                        self.layer_idx = -2
                        self.type_feature = 'patch'


        def set_img_features(self, img_features: torch.FloatTensor) -> None:
                self.img_features = img_features

        def set_img_sizes(self, img_sizes: torch.LongTensor) -> None:
                self.img_sizes = img_sizes

        def get_img_features(self, img_embeds: torch.FloatTensor) -> torch.FloatTensor:
                LAYER_IDX = self.layer_idx
                TYPE_FEATURE = self.type_feature

                img_processor_output = self.img_processor(img_embeds, output_hidden_states=True)
                img_feature = img_processor_output.hidden_states[LAYER_IDX]

                if TYPE_FEATURE == "patch":
                        patch_feature = img_feature[:, 1:]
                        return patch_feature

                if TYPE_FEATURE == "cls_patch":
                        return img_feature

                raise NotImplementedError

        def forward(self, input_ids: torch.LongTensor, pixel_values: torch.FloatTensor, image_sizes=None) -> torch.FloatTensor:

                MAX_INPUT_ID = int(1e9)
                img_embeds = pixel_values
                img_sizes = image_sizes

                if self.img_features is not None:
                        img_embeds = self.img_features.clone()
                        self.img_features = None

                if self.img_sizes is not None:
                        img_sizes = self.img_sizes

                input_shape = input_ids.size()
                input_ids = input_ids.view(-1, input_shape[-1])

                with torch.no_grad():
                        positions = torch.nonzero((input_ids < 0) & (input_ids > -MAX_INPUT_ID), as_tuple=False)
                
                select = False

                if isinstance(self.img_projection, nn.Sequential):  
                        target_device = self.img_projection[0].bias.device  
                        target_dtype = self.img_projection[0].bias.dtype  
                else:  # It's a single nn.Linear layer  
                        target_device = self.img_projection.bias.device  
                        target_dtype = self.img_projection.bias.dtype  

                if len(positions.tolist()) > 0:
                        with torch.no_grad():
                                g_values = abs(input_ids[positions[:, 0], positions[:, 1]])

                        if self.use_hd_transform and img_sizes is not None and len(img_sizes):
                                hd_transform = True
                                assert img_embeds.ndim == 5, f'img_embeds size: {img_embeds.size()}, expect 5D tensor for hd transform'
                                img_features = self.get_img_features(img_embeds.flatten(0, 1))
                                base_feat_height = base_feat_width = int(img_features.shape[1] ** 0.5)
                                assert base_feat_height == 24 and base_feat_width == 24, f'base_feat_height: {base_feat_height}, base_feat_width: {base_feat_width}, expect 24x24 features for hd transform'
                                img_features = img_features.view(bs, -1, base_feat_height * base_feat_width, self.image_dim_out)
                                C = self.image_dim_out
                                H = base_feat_height

                                output_imgs = []
                                output_len = []
                                if isinstance(img_sizes, torch.Tensor):
                                        img_sizes = img_sizes.view(-1, 2)
                                for _bs in range(bs):
                                        h, w = img_sizes[_bs]
                                        h = h // 336 
                                        w = w // 336
                                        B_ = h * w

                                        global_img_feature = img_features[_bs, :1]
                                        glb_img = global_img_feature.reshape(1,H,H,C).reshape(1,H//2,2,H//2,2,C).contiguous().permute(0,1,3,2,4,5).reshape(1,H//2,H//2,4*C).contiguous()
                                        temp_glb_GN = self.sub_GN.repeat(1, H//2, 1, 1)
                                        glb_img = torch.cat([glb_img, temp_glb_GN], dim=2).reshape(1,-1,4*C)
                                        sub_img = img_features[_bs, 1:]
                                        sub_img = sub_img[:B_]
                                        sub_img = sub_img.reshape(B_,H,H,C).reshape(B_,H//2,2,H//2,2,C).contiguous().permute(0,1,3,2,4,5).reshape(B_,-1,4*C).contiguous()
                                        sub_img = sub_img.reshape(1, h, w, 12, 12, -1).permute(0,1,3,2,4,5).reshape(1,h*12,w*12,4*C)
                                        temp_sub_GN = self.sub_GN.repeat(1, h*12, 1, 1)
                                        sub_img = torch.cat([sub_img, temp_sub_GN], dim=2).reshape(1,-1,4*C)
                                        if self.hd_transform_order == 'glb_sub':
                                                output_imgs.append(torch.cat([glb_img, self.glb_GN, sub_img], dim=1))
                                        elif self.hd_transform_order == 'sub_glb':
                                                output_imgs.append(torch.cat([sub_img, self.glb_GN, glb_img], dim=1))
                                        else:
                                                raise NotImplementedError(f'hd_transform_order = {self.hd_transform_order}, not implemented')
                                        temp_len = int((h*w+1)*144 + 1 + (h+1)*12)
                                        assert temp_len == output_imgs[-1].shape[1], f'temp_len: {temp_len}, output_imgs[-1].shape[1]: {output_imgs[-1].shape[1]}'
                                        output_len.append(temp_len)
                                
                                num_img_tokens = output_len
                                img_set_tensor = []
                                for _output_img in output_imgs:
                                        img_feature_proj = self.img_projection(_output_img.to(target_device).to(target_dtype))
                                        img_set_tensor.append(img_feature_proj)
                                logger.info(f'img_embeds size: {img_embeds.size()}, image sizes: {img_sizes} loading time {datetime.now() - start_time}')
                        elif img_embeds.ndim == 4:
                                selected_g_values = g_values[::self.num_img_tokens]
                                assert len(img_embeds) == len(selected_g_values), f'img_embeds size: {img_embeds.size()}, selected_g_values size: {len(selected_g_values)}, selected_g_value {selected_g_values}'
                                start_time = datetime.now()
                                tt = (
                                        self.get_img_features(img_embeds)
                                        .to(target_device)
                                        .to(target_dtype)
                                        .reshape(-1, self.image_dim_out)
                                )
                                logger.info(f'img_embeds size: {img_embeds.size()}, loading time {datetime.now() - start_time}')
                                img_set_tensor = self.img_projection(tt)
                        elif img_embeds.ndim == 3:
                                selected_g_values = g_values[::self.num_img_tokens]
                                assert len(img_embeds) == len(selected_g_values), f'img_embeds size: {img_embeds.size()}, selected_g_values size: {len(selected_g_values)}, selected_g_value {selected_g_values}'
                                tt = (
                                        img_embeds
                                        .to(target_device)
                                        .to(target_dtype)
                                        .view(-1, self.image_dim_out)
                                )
                                img_set_tensor = self.img_projection(tt)
                        else:
                                raise NotImplementedError
                        select = True
                
                with torch.no_grad():
                        input_ids.clamp_min_(0).clamp_max_(self.vocab_size)
                
                hidden_states = self.wte(input_ids)

                if select:
                        if hd_transform:
                                idx = 0
                                for i, cnt in enumerate(num_img_tokens):
                                        hidden_states[positions[idx, 0], positions[idx, 1] : positions[idx, 1] + cnt] = (
                                                img_set_tensor[i]
                                                .to(hidden_states.dtype)
                                                .to(hidden_states.device)
                                                )
                                        idx += cnt
                        else:
                                idx = 0
                                assert len(selected_g_values) * self.num_img_tokens == len(img_set_tensor), f'len(selected_g_values) * self.num_img_tokens = {len(selected_g_values) * self.num_img_tokens}, len(img_set_tensor) = {len(img_set_tensor)}'
                                for i, g in enumerate(selected_g_values):
                                        cnt = self.num_img_tokens
                                        hidden_states[positions[idx, 0], positions[idx, 1] : positions[idx, 1] + cnt] = (
                                                img_set_tensor[i * cnt : (i + 1) * cnt]
                                                .to(hidden_states.dtype)
                                                .to(hidden_states.device)
                                                )
                                        idx += cnt

                if self.drop is not None:
                        hidden_states = self.drop(hidden_states)

                return hidden_states
```

## Construire votre Pipeline

En travaillant avec du code qui génère des embeddings, comme l'exemple ci-dessus, vous l'intégrez généralement dans votre pipeline en fonction de votre cas d'utilisation spécifique.

1. Chargement des Modèles Pré-entraînés : Si vous chargez des modèles pré-entraînés depuis Hugging Face, ces modèles sont en effet binaires. Vous pouvez les utiliser directement pour générer des embeddings sans entraînement supplémentaire. Cela est utile pour des tâches comme l'extraction de caractéristiques ou la recherche sémantique où vous avez besoin d'embeddings prêts à l'emploi.

2. Pipeline de Fine-Tuning : Si vous devez adapter le modèle à une tâche ou un jeu de données spécifique, vous intégreriez le code dans un pipeline de fine-tuning. Cela implique :
   - Chargement du Modèle Pré-entraîné : Commencez avec un modèle pré-entraîné de Hugging Face.
   - Préparation de Votre Jeu de Données : Assurez-vous que votre jeu de données est dans le format correct pour l'entraînement.
   - Fine-Tuning : Utilisez des bibliothèques comme `transformers` and `datasets` de Hugging Face pour fine-tuner le modèle sur votre jeu de données. Cette étape ajuste les poids du modèle pour mieux convenir à votre tâche spécifique.

Par exemple, dans le contexte du Phi-3 Cookbook et de CLIPVision, vous pourriez :
- Générer des Embeddings : Utiliser le modèle CLIP pré-entraîné pour générer des embeddings pour les images.
- Fine-Tuning : Si les embeddings doivent être plus spécifiques à votre application, fine-tuner le modèle CLIP sur un jeu de données pertinent pour votre cas d'utilisation.

Voici un exemple simplifié de la façon dont vous pourriez intégrer cela dans le code :

```python
from transformers import CLIPProcessor, CLIPModel
import torch
 
# Load pre-trained model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
 
# Prepare your data
images = [...]  # List of images
inputs = processor(images=images, return_tensors="pt")
 
# Generate embeddings
with torch.no_grad():
    embeddings = model.get_image_features(**inputs)
 
# Fine-tuning (if needed)
# Define your fine-tuning logic here
```

Cette approche vous permet de tirer parti de modèles pré-entraînés puissants et de les adapter à vos besoins spécifiques.

## Intégrer la Famille de Modèles Phi

Intégrer le modèle Phi-3 avec l'exemple de code fourni impliquant CLIP peut en effet être un défi, surtout en considérant différents encodeurs de vision.

Voici un aperçu de la façon dont vous pourriez aborder cela :

### Points Clés
**Traitement des Données :** Assurez-vous que les images sont traitées de manière à correspondre aux exigences d'entrée du modèle Phi-3.
**Génération d'Embeddings :** Remplacez la génération d'embeddings de CLIP par la méthode correspondante de votre modèle Phi-3.
**Fine-Tuning :** Si vous devez fine-tuner le modèle Phi-3, assurez-vous que la logique est incluse après la génération des embeddings.

## Étapes pour Intégrer le Modèle Phi-3
**Charger le Modèle Phi-3 :** En supposant que vous ayez une classe Phi3Model pour le modèle Phi-3 vanilla ou fine-tuné.
**Modifier la Préparation des Données :** Ajustez la préparation des données pour répondre aux exigences d'entrée du modèle Phi-3.
**Intégrer les Embeddings Phi-3 :** Remplacez la partie où les embeddings de CLIP sont générés par la génération d'embeddings du modèle Phi-3.

```
from transformers import CLIPProcessor, CLIPModel
import torch
 
# Load pre-trained CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
 
# Load Phi-3 model (vanilla or fine-tuned)
# Assuming you have a load_phi3_model function to load your Phi-3 model
phi3_model = load_phi3_model(fine_tuned=True)
 
# Prepare your data
images = [...]  # List of images
inputs = clip_processor(images=images, return_tensors="pt")
 
# Generate embeddings using CLIP (for comparison)
with torch.no_grad():
    clip_embeddings = clip_model.get_image_features(**inputs)
 
# Generate embeddings using Phi-3
# Adjust this part according to how your Phi-3 model processes inputs
phi3_inputs = process_for_phi3_model(images)
with torch.no_grad():
    phi3_embeddings = phi3_model.get_image_features(phi3_inputs)
 
# Fine-tuning or further processing (if needed)
# Define your fine-tuning logic here
``

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatisés par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.