# Utilisation du CLIPVisionModel pour traiter des images et générer des embeddings d'images avec Phi-3-vision

L'exemple de code python suivant fournit la fonctionnalité nécessaire pour traiter des images et générer des embeddings d'images en utilisant le CLIPVisionModel.

## Qu'est-ce que CLIP
CLIP, qui signifie Contrastive Language-Image Pre-training, est un modèle développé par OpenAI qui apprend efficacement les concepts visuels à partir de la supervision en langage naturel. C’est un modèle multimodal qui combine la compréhension des images et des textes dans un cadre unique. CLIP est entraîné sur une variété d'images provenant d'Internet et sur les textes qui les accompagnent, apprenant à prédire quelles images étaient associées à quels textes, liant ainsi efficacement les deux modalités.

Le modèle fonctionne en prenant une image et un extrait de texte en entrée et en prédisant la probabilité que le texte soit une description précise de l'image. Cette approche permet à CLIP de gérer une large gamme de tâches visuelles, telles que la reconnaissance d'objets, la classification et même la génération de descriptions pour des images qu'il n'a jamais vues auparavant.

L'un des principaux avantages de CLIP est sa capacité à effectuer un apprentissage "zero-shot", où le modèle peut gérer correctement des tâches pour lesquelles il n'a pas été explicitement formé, simplement en lisant la description de la tâche. Cela est possible grâce à la grande quantité de données diverses sur lesquelles il a été entraîné, ce qui l'aide à bien généraliser pour de nouvelles tâches.

## Phi-3-vision
Phi-3-vision est un modèle multimodal de 4,2 milliards de paramètres avec des capacités linguistiques et visuelles, capable de raisonner sur des images du monde réel et des documents numériques, d'extraire et de raisonner sur le texte des images, et de générer des insights et des réponses liées à des graphiques ou des diagrammes.

## Exemple de Code
Ce code définit une classe appelée Phi3ImageEmbedding qui représente un modèle d'embedding d'image. Le but de cette classe est de traiter des images et de générer des embeddings pouvant être utilisés pour des tâches en aval telles que la classification ou la recherche d'images.

La méthode __init__ initialise le modèle en configurant divers composants tels que le dropout des embeddings, le processeur d'images, les paramètres de transformation HD et la projection d'images. Elle prend en entrée un objet config qui contient les paramètres de configuration du modèle. Le paramètre wte est une entrée optionnelle qui représente les embeddings de tokens de mots.

La méthode get_img_features prend un tenseur d'entrée img_embeds représentant des embeddings d'images et retourne un tenseur représentant les caractéristiques d'image extraites. Elle utilise le img_processor pour traiter les embeddings d'images et extraire les caractéristiques souhaitées en fonction des paramètres layer_idx et type_feature.

## Explication du Code
Passons en revue le code étape par étape :

Le code importe les bibliothèques et modules nécessaires, y compris math, torch, torch.nn, et divers composants de la bibliothèque transformers.

Le code définit un objet de configuration appelé CLIP_VIT_LARGE_PATCH14_336_CONFIG qui contient divers hyperparamètres pour le modèle d'embedding d'image.

La classe Phi3ImageEmbedding est définie, qui est une sous-classe de torch.nn.Module. Cette classe représente le modèle d'embedding d'image et contient des méthodes pour la propagation avant et la configuration des caractéristiques d'image.

La méthode __init__ initialise l'objet Phi3ImageEmbedding. Elle prend un objet config en entrée, qui est une instance de la classe PretrainedConfig. Elle prend également un argument optionnel wte.

La méthode __init__ initialise divers attributs de l'objet Phi3ImageEmbedding en fonction de l'objet config fourni. Elle définit la taille cachée, le taux de dropout, le processeur d'image, la projection d'image et d'autres paramètres.

La méthode set_img_features configure les caractéristiques d'image pour le modèle. Elle prend un tenseur de caractéristiques d'image en entrée et l'assigne à l'attribut img_features de l'objet.

La méthode set_img_sizes configure les tailles d'image pour le modèle. Elle prend un tenseur de tailles d'image en entrée et l'assigne à l'attribut img_sizes de l'objet.

La méthode get_img_features extrait les caractéristiques d'image des embeddings d'image en entrée. Elle prend un tenseur d'embeddings d'image en entrée et retourne les caractéristiques d'image extraites.

La méthode forward effectue la propagation avant à travers le modèle. Elle prend les input IDs, les valeurs de pixels et les tailles d'image en entrée et retourne les états cachés du modèle. Elle vérifie d'abord si les caractéristiques et les tailles d'image sont déjà configurées, et si ce n'est pas le cas, elle utilise les entrées fournies pour les configurer. Ensuite, elle traite les input IDs et extrait les caractéristiques d'image en fonction du processeur d'image configuré. Enfin, elle applique la projection d'image aux caractéristiques extraites et retourne les états cachés.

Dans l'ensemble, ce code définit une classe qui représente un modèle d'embedding d'image et fournit des méthodes pour configurer les caractéristiques d'image et effectuer la propagation avant.

[Code Sample](../../../../code/06.E2E/phi3imageembedding.py)
```
import math
import torch
from transformers import CLIPVisionModel, PretrainedConfig
from transformers import CLIPVisionConfig 
from transformers.utils import logging
from datetime import datetime 

# Importer les bibliothèques nécessaires
import torch.nn as nn

# Configurer la journalisation
logger = logging.get_logger(__name__)

# Définir la configuration pour le CLIPVisionModel
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

# Définir la classe Phi3ImageEmbedding
class Phi3ImageEmbedding(nn.Module):
        """Phi3 Embedding d'image."""

        def __init__(self, config: PretrainedConfig, wte=None, **kwargs) -> None:
                super().__init__()

                # Configurer le dropout des embeddings
                hidden_size = config.n_embd si hasattr(config, 'n_embd') else config.hidden_size
                if hasattr(config, 'embd_pdrop') ou hasattr(config, 'embed_pdrop'):
                        embd_drop = config.embd_pdrop si hasattr(config, 'embd_pdrop') else config.embed_pdrop
                        self.drop = nn.Dropout(embd_drop)
                else:
                        self.drop = None

                self.wte = wte

                # Configurer le processeur d'image en fonction de la configuration
                if isinstance(config.img_processor, dict) et config.img_processor.get('name', None) == 'clip_vision_model':
                        assert 'model_name' in config.img_processor, 'model_name doit être fourni pour CLIPVisionModel'
                        assert 'image_dim_out' in config.img_processor, 'image_dim_out doit être fourni pour CLIPVisionModel'
                        assert 'num_img_tokens' in config.img_processor, 'num_img_tokens doit être fourni pour CLIPVisionModel'
                        assert config.img_processor['model_name'] == 'openai/clip-vit-large-patch14-336'
                        clip_config = CLIP_VIT_LARGE_PATCH14_336_CONFIG
                        self.img_processor = CLIPVisionModel(clip_config)
                        image_dim_out = config.img_processor['image_dim_out']
                        self.num_img_tokens = config.img_processor['num_img_tokens']
                else:
                        raise NotImplementedError(f'img_processor = {config.img_processor}, non implémenté')

                self.image_dim_out = image_dim_out
                self.img_sizes = None

                # Configurer les paramètres de transformation HD
                self.use_hd_transform = kwargs.get('use_hd_transform', False)
                self.with_learnable_separator = kwargs.get('with_learnable_separator', False)
                self.hd_transform_order = kwargs.get('hd_transform_order', 'glb_sub')
                assert self.use_hd_transform == self.with_learnable_separator, 'use_hd_transform et with_learnable_separator doivent avoir la même valeur'
                if self.with_learnable_separator:
                        assert self.use_hd_transform, 'le séparateur apprenable est uniquement pour la transformation HD'
                        self.glb_GN = nn.Parameter(torch.zeros([1, 1, self.image_dim_out * 4]))
                        self.sub_GN = nn.Parameter(torch.zeros([1, 1, 1, self.image_dim_out * 4]))
                        logger.info(f'séparateur apprenable activé pour la transformation HD, hd_transform_order = {self.hd_transform_order}')

                # Configurer la projection d'image en fonction de projection_cls
                projection_cls = kwargs.get('projection_cls', 'linear')
                if projection_cls == 'linear':
                        self.img_projection = nn.Linear(image_dim_out, hidden_size)
                elif projection_cls == 'mlp' et self.use_hd_transform:
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
                        raise NotImplementedError(f'projection_cls = {projection_cls}, non implémenté')

                self.vocab_size = config.vocab_size
                self.img_features = None

                # Configurer l'index de couche et le type de caractéristique pour le processeur d'image
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
                else:  # C'est une seule couche nn.Linear  
                        target_device = self.img_projection.bias.device  
                        target_dtype = self.img_projection.bias.dtype  

                if len(positions.tolist()) > 0:
                        with torch.no_grad():
                                g_values = abs(input_ids[positions[:, 0], positions[:, 1]])

                        if self.use_hd_transform et img_sizes is not None et len(img_sizes):
                                hd_transform = True
                                assert img_embeds.ndim == 5, f'img_embeds size: {img_embeds.size()}, expect 5D tensor for hd transform'
                                img_features = self.get_img_features(img_embeds.flatten(0, 1))
                                base_feat_height = base_feat_width = int(img_features.shape[1] ** 0.5)
                                assert base_feat_height == 24 et base_feat_width == 24, f'base_feat_height: {base_feat_height}, base_feat_width: {base_feat_width}, expect 24x24 features for hd transform'
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
                                                raise NotImplementedError(f'hd_transform_order = {self.hd_transform_order}, non implémenté')
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

Avertissement : La traduction a été réalisée à partir de son texte original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez vérifier le résultat et apporter les corrections nécessaires.