# 使用 CLIPVisionModel 處理圖像並生成圖像嵌入與 Phi-3-vision

以下的 Python 範例提供了使用 CLIPVisionModel 處理圖像並生成圖像嵌入的必要功能。

## 什麼是 CLIP
CLIP，全名為 Contrastive Language-Image Pre-training，是由 OpenAI 開發的一個模型，能夠高效地從自然語言監督中學習視覺概念。這是一個多模態模型，將圖像和文字理解結合在一個框架中。CLIP 在各種互聯網來源的圖像和伴隨的文本上進行訓練，學習預測哪些圖像與哪些文本配對，從而有效地將這兩種模態聯繫起來。

該模型通過接收圖像和文本片段作為輸入，然後預測文本是否準確描述了圖像來工作。這種方法使 CLIP 能夠處理各種視覺任務，例如物體識別、分類，甚至為從未見過的圖像生成描述。

CLIP 的一個主要優勢是其“零樣本”學習能力，模型可以正確處理未明確訓練過的任務，只需閱讀任務描述即可。這是因為它在大量多樣化數據上進行了訓練，這有助於它很好地泛化到新任務。

## Phi-3-vision
Phi-3-vision 是一個具有語言和視覺能力的 42 億參數多模態模型，能夠對真實世界圖像和數字文檔進行推理，從圖像中提取並推理文本，並生成與圖表或圖解相關的見解和答案。

**範例目的：** 本範例演示了如何使用 CLIP 生成圖像嵌入以及如何將其應用於與 Phi-3 模型相關的任務。它作為比較不同嵌入技術（CLIP vs. Phi-3）性能和特徵的參考。
**整合挑戰：** 直接將像 CLIP 這樣的視覺編碼器整合到 Phi-3 中確實很複雜。這種複雜性源於架構差異以及在不丟失上下文或性能的情況下實現無縫整合的需求。整合尚未完全評估或實施，因此包含在內。
**比較方法：** 這段代碼旨在提供平行比較，而不是集成解決方案。它允許用戶查看 CLIP 嵌入如何與 Phi-3 嵌入一起運行，提供潛在優勢或缺點的見解。
**澄清：** 這是 Phi-3CookBook 範例：展示如何使用 CLIP 嵌入作為比較工具，而不是直接整合到 Phi-3 中。
**整合工作：** 將 CLIP 嵌入完全整合到 Phi-3 中仍然是一個挑戰，尚未完全探索，但提供給客戶進行實驗。

## 範例代碼
這段代碼定義了一個名為 Phi3ImageEmbedding 的類，代表一個圖像嵌入模型。這個類的目的是處理圖像並生成可用於下游任務（如圖像分類或檢索）的嵌入。

__init__ 方法通過設置各種組件（如嵌入 dropout、圖像處理器、HD 變換參數和圖像投影）來初始化模型。它接收一個配置對象作為輸入，該對象包含模型的配置參數。wte 參數是一個可選輸入，表示詞彙標記嵌入。

get_img_features 方法接收一個表示圖像嵌入的輸入張量 img_embeds，並返回一個表示提取圖像特徵的張量。它使用 img_processor 處理圖像嵌入，並根據 layer_idx 和 type_feature 參數提取所需的特徵。

## 解釋代碼
讓我們一步步解釋這段代碼：

代碼導入了必要的庫和模塊，包括 math、torch、torch.nn 和 transformers 庫中的各種組件。

代碼定義了一個名為 CLIP_VIT_LARGE_PATCH14_336_CONFIG 的配置對象，其中包含圖像嵌入模型的各種超參數。

Phi3ImageEmbedding 類被定義為 torch.nn.Module 的子類。這個類代表圖像嵌入模型，並包含前向傳播和設置圖像特徵的方法。

__init__ 方法初始化 Phi3ImageEmbedding 對象。它接收一個配置對象作為輸入，該對象是 PretrainedConfig 類的實例。它還接收一個可選的 wte 參數。

__init__ 方法根據提供的配置對象初始化 Phi3ImageEmbedding 對象的各種屬性。它設置隱藏層大小、dropout 率、圖像處理器、圖像投影和其他參數。

set_img_features 方法為模型設置圖像特徵。它接收一個圖像特徵張量作為輸入，並將其分配給對象的 img_features 屬性。

set_img_sizes 方法為模型設置圖像大小。它接收一個圖像大小張量作為輸入，並將其分配給對象的 img_sizes 屬性。

get_img_features 方法從輸入的圖像嵌入中提取圖像特徵。它接收一個圖像嵌入張量作為輸入，並返回提取的圖像特徵。

forward 方法通過模型執行前向傳播。它接收輸入 ID、像素值和圖像大小作為輸入，並返回模型的隱藏狀態。它首先檢查圖像特徵和大小是否已設置，如果沒有，則使用提供的輸入來設置它們。然後，它處理輸入 ID 並根據配置的圖像處理器提取圖像特徵。最後，它將圖像投影應用於提取的特徵並返回隱藏狀態。

總的來說，這段代碼定義了一個代表圖像嵌入模型的類，並提供了設置圖像特徵和執行前向傳播的方法。

[代碼範例](../../../../code/06.E2E/phi3imageembedding.py)
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

## 構建你的管道

處理生成嵌入的代碼，如上述範例，通常根據你的具體使用情況將其整合到你的管道中。

1. 加載預訓練模型：如果你從 Hugging Face 加載預訓練模型，這些模型確實是二進制的。你可以直接使用它們來生成嵌入，而不需要額外訓練。這對於需要即用型嵌入的任務（如特徵提取或語義搜索）非常有用。

2. 微調管道：如果你需要將模型適應特定任務或數據集，你可以將代碼整合到微調管道中。這涉及到：
   - 加載預訓練模型：從 Hugging Face 開始使用預訓練模型。
   - 準備你的數據集：確保你的數據集格式正確以進行訓練。
   - 微調：使用 Hugging Face 的 `transformers` and `datasets` 庫在你的數據集上微調模型。這一步調整模型權重以更好地適應你的特定任務。

例如，在 Phi-3 Cookbook 和 CLIPVision 的上下文中，你可能會：
- 生成嵌入：使用預訓練的 CLIP 模型為圖像生成嵌入。
- 微調：如果嵌入需要更具體地適應你的應用，則在與你的使用情況相關的數據集上微調 CLIP 模型。

這裡是一個簡化的代碼整合示例：

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

這種方法允許你利用強大的預訓練模型並將其適應你的具體需求。

## 整合 Phi 家族的模型

將 Phi-3 模型與涉及 CLIP 的代碼範例整合確實具有挑戰性，特別是當考慮不同的視覺編碼器時。

這裡是你可能採取的步驟概述：

### 關鍵點
**數據處理：** 確保圖像的處理方式符合 Phi-3 模型的輸入要求。
**嵌入生成：** 用你的 Phi-3 模型的相應方法替換 CLIP 嵌入生成。
**微調：** 如果你需要微調 Phi-3 模型，確保在生成嵌入後包含這個邏輯。

## 整合 Phi-3 模型的步驟
**加載 Phi-3 模型：** 假設你有一個 Phi3Model 類，用於基礎或微調的 Phi-3 模型。
**修改數據準備：** 調整數據準備以適應 Phi-3 模型的輸入要求。
**整合 Phi-3 嵌入：** 用 Phi-3 模型的嵌入生成替換生成 CLIP 嵌入的部分。

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

**免責聲明**:
本文件是使用機器翻譯服務翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔案作為權威來源。對於關鍵信息，建議進行專業人工翻譯。我們對使用此翻譯所產生的任何誤解或誤讀不承擔任何責任。