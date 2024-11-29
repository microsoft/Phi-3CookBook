# CLIPVisionModelを使用して画像を処理し、Phi-3-visionで画像埋め込みを生成する

以下のPythonサンプルは、CLIPVisionModelを使用して画像を処理し、画像埋め込みを生成するための必要な機能を提供します。

## CLIPとは
CLIP（Contrastive Language-Image Pre-training）は、OpenAIによって開発されたモデルで、自然言語による監督学習から視覚的な概念を効率的に学習します。これは、画像とテキストの理解を単一のフレームワークに統合したマルチモーダルモデルです。CLIPは、インターネットから収集した多様な画像とそれに付随するテキストを用いて訓練され、どの画像がどのテキストとペアになっているかを予測することで、2つのモダリティを効果的にリンクさせます。

このモデルは、画像とテキストのスニペットを入力として受け取り、テキストが画像の正確な説明である可能性を予測することで機能します。このアプローチにより、CLIPは物体認識、分類、さらには未見の画像に対する説明生成など、幅広い視覚タスクに対応できます。

CLIPの主な利点の一つは、「ゼロショット」学習を行う能力です。これは、明示的に訓練されていないタスクでも、タスクの説明を読むだけで正しく処理できることを意味します。これは、多様なデータで訓練されているため、新しいタスクに対してもよく一般化できるからです。

## Phi-3-vision
Phi-3-visionは、4.2Bパラメータを持つマルチモーダルモデルで、言語と視覚の能力を備えています。実世界の画像やデジタルドキュメントを対象に推論を行い、画像からテキストを抽出し、それに基づいてチャートや図に関連する洞察や回答を生成することができます。

**例の目的:** この例は、CLIPを使用して画像埋め込みを生成する方法を示し、Phi-3モデルに関連するタスクにどのように適用できるかを示します。これは、異なる埋め込み技術（CLIP vs. Phi-3）の性能と特性を比較するためのリファレンスとして機能します。
**統合の課題:** CLIPのような別の視覚エンコーダをPhi-3に直接統合することは確かに複雑です。この複雑さは、アーキテクチャの違いや、コンテキストや性能を失わずにシームレスに統合する必要があるためです。統合はまだ完全には評価されておらず、実装されていないため、ここではそのまま含めています。
**比較アプローチ:** このコードは、統合されたソリューションではなく、並列比較を提供することを目的としています。ユーザーがCLIP埋め込みとPhi-3埋め込みの性能を比較できるようにし、潜在的な利点や欠点について洞察を提供します。
**明確化:** このPhi-3CookBookの例は、Phi-3に直接統合するのではなく、比較ツールとしてCLIP埋め込みを使用する方法を示しています。
**統合作業:** CLIP埋め込みをPhi-3に完全に統合することは依然として課題であり、完全には探求されていませんが、顧客が実験できるように提供されています。

## サンプルコード
このコードは、画像埋め込みモデルを表すPhi3ImageEmbeddingというクラスを定義しています。このクラスの目的は、画像を処理し、画像分類や検索などの下流タスクに使用できる埋め込みを生成することです。

__init__メソッドは、埋め込みドロップアウト、画像プロセッサ、HD変換パラメータ、画像プロジェクションなどのさまざまなコンポーネントを設定してモデルを初期化します。これは、モデルの設定パラメータを含むconfigオブジェクトを入力として受け取ります。wteパラメータは、単語トークン埋め込みを表すオプションの入力です。

get_img_featuresメソッドは、画像埋め込みを表す入力テンソルimg_embedsを受け取り、抽出された画像特徴を表すテンソルを返します。これは、img_processorを使用して画像埋め込みを処理し、layer_idxおよびtype_featureパラメータに基づいて目的の特徴を抽出します。

## コードの説明
コードをステップバイステップで見ていきましょう：

コードは、math、torch、torch.nn、およびtransformersライブラリからのさまざまなコンポーネントを含む必要なライブラリとモジュールをインポートします。

コードは、画像埋め込みモデルのさまざまなハイパーパラメータを含むCLIP_VIT_LARGE_PATCH14_336_CONFIGという設定オブジェクトを定義します。

Phi3ImageEmbeddingクラスが定義されており、これはtorch.nn.Moduleのサブクラスです。このクラスは画像埋め込みモデルを表し、前方伝播および画像特徴の設定のためのメソッドを含みます。

__init__メソッドはPhi3ImageEmbeddingオブジェクトを初期化します。これはPretrainedConfigクラスのインスタンスであるconfigオブジェクトを入力として受け取ります。また、オプションのwte引数も受け取ります。

__init__メソッドは、提供されたconfigオブジェクトに基づいてPhi3ImageEmbeddingオブジェクトのさまざまな属性を初期化します。これは、隠れサイズ、ドロップアウト率、画像プロセッサ、画像プロジェクション、およびその他のパラメータを設定します。

set_img_featuresメソッドは、モデルの画像特徴を設定します。これは画像特徴のテンソルを入力として受け取り、それをオブジェクトのimg_features属性に割り当てます。

set_img_sizesメソッドは、モデルの画像サイズを設定します。これは画像サイズのテンソルを入力として受け取り、それをオブジェクトのimg_sizes属性に割り当てます。

get_img_featuresメソッドは、入力画像埋め込みから画像特徴を抽出します。これは画像埋め込みのテンソルを入力として受け取り、抽出された画像特徴を返します。

forwardメソッドは、モデルを通じて前方伝播を行います。これは入力ID、ピクセル値、および画像サイズを入力として受け取り、モデルの隠れ状態を返します。まず、画像特徴とサイズがすでに設定されているかどうかを確認し、設定されていない場合は提供された入力を使用してそれらを設定します。その後、入力IDを処理し、設定された画像プロセッサに基づいて画像特徴を抽出します。最後に、抽出された特徴に画像プロジェクションを適用し、隠れ状態を返します。

全体として、このコードは画像埋め込みモデルを表すクラスを定義し、画像特徴の設定および前方伝播を行うためのメソッドを提供します。

[Code Sample](../../../../code/06.E2E/phi3imageembedding.py)
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

## パイプラインの構築

上記の例のように埋め込みを生成するコードを使用する場合、通常は特定のユースケースに応じてパイプラインに統合します。

1. 事前訓練されたモデルの読み込み: Hugging Faceから事前訓練されたモデルを読み込む場合、これらのモデルはバイナリです。追加の訓練なしで埋め込みを生成するために直接使用できます。これは、特徴抽出やセマンティック検索のように、すぐに埋め込みが必要なタスクに役立ちます。

2. ファインチューニングパイプライン: モデルを特定のタスクやデータセットに適応させる必要がある場合、コードをファインチューニングパイプラインに統合します。これには以下が含まれます:
   - 事前訓練されたモデルの読み込み: Hugging Faceから事前訓練されたモデルを開始します。
   - データセットの準備: データセットが訓練用の正しい形式であることを確認します。
   - ファインチューニング: Hugging Faceの`transformers` and `datasets`ライブラリを使用して、データセット上でモデルをファインチューニングします。このステップでは、モデルの重みを特定のタスクにより適応させるために調整します。

例えば、Phi-3 CookbookとCLIPVisionのコンテキストでは、次のようにします:
- 埋め込みの生成: 事前訓練されたCLIPモデルを使用して画像の埋め込みを生成します。
- ファインチューニング: 埋め込みがアプリケーションにより特化する必要がある場合、関連するデータセット上でCLIPモデルをファインチューニングします。

以下に、この統合方法の簡略化された例を示します:

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

このアプローチにより、強力な事前訓練モデルを活用し、特定のニーズに適応させることができます。

## Phiファミリーのモデルの統合

CLIPを含むコード例とPhi-3モデルを統合することは、特に異なる視覚エンコーダを考慮する場合、確かに挑戦的です。

以下は、このアプローチの概要です:

### 重要なポイント
**データ処理:** 画像がPhi-3モデルの入力要件に適合するように処理されていることを確認します。
**埋め込み生成:** CLIPの埋め込み生成を、Phi-3モデルの対応するメソッドに置き換えます。
**ファインチューニング:** Phi-3モデルをファインチューニングする必要がある場合、埋め込み生成後にそのロジックを含めるようにします。

## Phi-3モデルを統合する手順
**Phi-3モデルの読み込み:** バニラまたはファインチューニングされたPhi-3モデル用のPhi3Modelクラスを持っていると仮定します。
**データ準備の修正:** データ準備をPhi-3モデルの入力要件に適応させます。
**Phi-3埋め込みの統合:** CLIP埋め込みが生成される部分をPhi-3モデルの埋め込み生成に置き換えます。

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

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期すために努めていますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語での原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は一切の責任を負いません。