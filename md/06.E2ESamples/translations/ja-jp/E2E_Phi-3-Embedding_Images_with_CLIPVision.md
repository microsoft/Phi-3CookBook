# CLIPVisionModelを使用して画像を処理し、Phi-3-visionで画像埋め込みを生成する

以下のPythonサンプルは、CLIPVisionModelを使用して画像を処理し、画像埋め込みを生成するために必要な機能を提供します。

## CLIPとは
CLIP（Contrastive Language-Image Pre-training）は、OpenAIによって開発されたモデルで、自然言語の監督から視覚的な概念を効率的に学習します。これは、画像とテキストの理解を単一のフレームワークに組み合わせたマルチモーダルモデルです。CLIPは、インターネットから収集されたさまざまな画像とそれに関連するテキストでトレーニングされ、どの画像がどのテキストとペアになっているかを予測することで、2つのモダリティを効果的にリンクします。

このモデルは、画像とテキストのスニペットを入力として受け取り、テキストが画像の正確な説明である可能性を予測することで機能します。このアプローチにより、CLIPは物体認識、分類、さらにはこれまで見たことのない画像の説明を生成するなど、さまざまな視覚タスクを処理できます。

CLIPの主な利点の1つは、「ゼロショット」学習を実行する能力です。これは、モデルが明示的にトレーニングされていないタスクを、タスクの説明を読むだけで正しく処理できることを意味します。これは、トレーニングされた多様なデータの膨大な量のおかげで、新しいタスクにうまく一般化できるためです。

## Phi-3-vision
Phi-3-visionは、言語と視覚の機能を備えた42億パラメータのマルチモーダルモデルで、現実世界の画像やデジタルドキュメントに対して推論を行い、画像からテキストを抽出して推論し、チャートや図に関連する洞察や回答を生成します。

## サンプルコード
このコードは、画像埋め込みモデルを表すPhi3ImageEmbeddingというクラスを定義しています。このクラスの目的は、画像を処理し、画像分類や検索などの下流タスクに使用できる埋め込みを生成することです。

__init__メソッドは、埋め込みドロップアウト、画像プロセッサ、HD変換パラメータ、画像プロジェクションなどのコンポーネントを設定することでモデルを初期化します。これは、モデルの構成パラメータを含むconfigオブジェクトを入力として受け取ります。wteパラメータは、単語トークン埋め込みを表すオプションの入力です。

get_img_featuresメソッドは、画像埋め込みを表す入力テンソルimg_embedsを受け取り、抽出された画像特徴を表すテンソルを返します。これは、img_processorを使用して画像埋め込みを処理し、layer_idxおよびtype_featureパラメータに基づいて必要な特徴を抽出します。

## コードの説明
コードをステップバイステップで説明します：

コードは、math、torch、torch.nn、およびtransformersライブラリのさまざまなコンポーネントを含む必要なライブラリとモジュールをインポートします。

コードは、画像埋め込みモデルのさまざまなハイパーパラメータを含むCLIP_VIT_LARGE_PATCH14_336_CONFIGという構成オブジェクトを定義します。

Phi3ImageEmbeddingクラスが定義されており、これはtorch.nn.Moduleのサブクラスです。このクラスは画像埋め込みモデルを表し、前方伝播と画像特徴の設定のためのメソッドを含みます。

__init__メソッドは、Phi3ImageEmbeddingオブジェクトを初期化します。これは、PretrainedConfigクラスのインスタンスであるconfigオブジェクトを入力として受け取ります。また、オプションのwte引数も受け取ります。

__init__メソッドは、提供されたconfigオブジェクトに基づいてPhi3ImageEmbeddingオブジェクトのさまざまな属性を初期化します。これには、隠れサイズ、ドロップアウト率、画像プロセッサ、画像プロジェクション、およびその他のパラメータが設定されます。

set_img_featuresメソッドは、モデルの画像特徴を設定します。これは、画像特徴のテンソルを入力として受け取り、オブジェクトのimg_features属性に割り当てます。

set_img_sizesメソッドは、モデルの画像サイズを設定します。これは、画像サイズのテンソルを入力として受け取り、オブジェクトのimg_sizes属性に割り当てます。

get_img_featuresメソッドは、入力画像埋め込みから画像特徴を抽出します。これは、画像埋め込みのテンソルを入力として受け取り、抽出された画像特徴を返します。

forwardメソッドは、モデルを通じて前方伝播を実行します。これは、入力ID、ピクセル値、および画像サイズを入力として受け取り、モデルの隠れ状態を返します。最初に画像特徴とサイズが既に設定されているかどうかを確認し、設定されていない場合は提供された入力を使用してそれらを設定します。次に、入力IDを処理し、構成された画像プロセッサに基づいて画像特徴を抽出します。最後に、抽出された特徴に画像プロジェクションを適用し、隠れ状態を返します。

全体として、このコードは画像埋め込みモデルを表すクラスを定義し、画像特徴の設定と前方伝播の実行のためのメソッドを提供します。

[コードサンプル](../../../../code/06.E2E/phi3imageembedding.py)
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
