# 使用 CLIPVisionModel 处理图像并生成图像嵌入与 Phi-3-vision

以下 Python 示例提供了使用 CLIPVisionModel 处理图像并生成图像嵌入所需的功能。

## 什么是 CLIP
CLIP，全称为对比语言-图像预训练，是 OpenAI 开发的一个模型，通过自然语言监督高效地学习视觉概念。它是一个多模态模型，在单一框架内结合了图像和文本理解。CLIP 在各种互联网来源的图像及其对应的文本上进行训练，学习预测哪些图像与哪些文本配对，从而有效地将两种模态联系起来。

该模型通过输入图像和文本片段来预测文本是否准确描述图像。这种方法使 CLIP 能够处理广泛的视觉任务，如物体识别、分类，甚至为从未见过的图像生成描述。

CLIP 的一个关键优势是其“零样本”学习能力，即模型可以正确处理未明确训练过的任务，只需阅读任务描述即可。这得益于它在大量多样化数据上的训练，帮助其很好地泛化到新任务。

## Phi-3-vision
Phi-3-vision 是一个具有语言和视觉能力的 42 亿参数多模态模型，能够对现实世界图像和数字文档进行推理，从图像中提取和推理文本，并生成与图表或图解相关的见解和答案。

**示例目的：** 本示例展示了使用 CLIP 生成图像嵌入，并说明其如何应用于与 Phi-3 模型相关的任务。它作为参考，用于比较不同嵌入技术（CLIP 与 Phi-3）的性能和特性。
**集成挑战：** 将另一个视觉编码器如 CLIP 直接集成到 Phi-3 中确实复杂。这种复杂性源于架构差异以及在不丢失上下文或性能的情况下实现无缝集成。集成尚未完全评估或实现，因此包含在此。
**比较方法：** 代码旨在提供平行比较而非集成解决方案。它允许用户查看 CLIP 嵌入与 Phi-3 嵌入的表现，为潜在的优缺点提供见解。
**澄清：** 这个 Phi-3CookBook 示例：展示了如何使用 CLIP 嵌入作为比较工具，而不是直接集成到 Phi-3 中。
**集成工作：** 将 CLIP 嵌入完全集成到 Phi-3 中仍然是一个挑战，并未完全探索，但提供给客户进行实验。

## 示例代码
此代码定义了一个名为 Phi3ImageEmbedding 的类，表示一个图像嵌入模型。这个类的目的是处理图像并生成可用于下游任务（如图像分类或检索）的嵌入。

__init__ 方法通过设置各种组件（如嵌入 dropout、图像处理器、HD 变换参数和图像投影）来初始化模型。它接受一个 config 对象作为输入，该对象包含模型的配置参数。wte 参数是一个可选输入，表示词嵌入。

get_img_features 方法接受一个表示图像嵌入的输入张量 img_embeds，并返回一个表示提取图像特征的张量。它使用 img_processor 处理图像嵌入，并根据 layer_idx 和 type_feature 参数提取所需特征。

## 代码解释
让我们逐步解析代码：

代码导入了必要的库和模块，包括 math、torch、torch.nn 以及 transformers 库的各种组件。

代码定义了一个名为 CLIP_VIT_LARGE_PATCH14_336_CONFIG 的配置对象，包含图像嵌入模型的各种超参数。

定义了 Phi3ImageEmbedding 类，它是 torch.nn.Module 的子类。这个类表示图像嵌入模型，并包含前向传播和设置图像特征的方法。

__init__ 方法初始化 Phi3ImageEmbedding 对象。它接受一个 config 对象作为输入，该对象是 PretrainedConfig 类的实例。它还接受一个可选的 wte 参数。

__init__ 方法根据提供的 config 对象初始化 Phi3ImageEmbedding 对象的各种属性。它设置了隐藏大小、dropout 率、图像处理器、图像投影等参数。

set_img_features 方法为模型设置图像特征。它接受一个图像特征张量作为输入，并将其分配给对象的 img_features 属性。

set_img_sizes 方法为模型设置图像大小。它接受一个图像大小张量作为输入，并将其分配给对象的 img_sizes 属性。

get_img_features 方法从输入的图像嵌入中提取图像特征。它接受一个图像嵌入张量作为输入，并返回提取的图像特征。

forward 方法通过模型进行前向传播。它接受输入 ID、像素值和图像大小作为输入，并返回模型的隐藏状态。它首先检查是否已设置图像特征和大小，如果没有，则使用提供的输入进行设置。然后，它处理输入 ID 并根据配置的图像处理器提取图像特征。最后，它将图像投影应用于提取的特征，并返回隐藏状态。

总体而言，这段代码定义了一个表示图像嵌入模型的类，并提供了设置图像特征和进行前向传播的方法。

[代码示例](../../../../code/06.E2E/phi3imageembedding.py)
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

## 构建你的流水线

使用生成嵌入的代码，如上述示例，通常根据具体用例将其集成到你的流水线中。

1. 加载预训练模型：如果你从 Hugging Face 加载预训练模型，这些模型确实是二进制的。你可以直接使用它们生成嵌入，无需额外训练。这对于需要现成嵌入的任务（如特征提取或语义搜索）非常有用。

2. 微调流水线：如果你需要将模型适应于特定任务或数据集，你需要将代码集成到微调流水线中。这涉及：
   - 加载预训练模型：从 Hugging Face 开始加载一个预训练模型。
   - 准备你的数据集：确保你的数据集格式正确以便训练。
   - 微调：使用 Hugging Face 的 `transformers` and `datasets` 等库在你的数据集上微调模型。这一步调整模型权重以更好地适应你的特定任务。

例如，在 Phi-3 Cookbook 和 CLIPVision 的上下文中，你可能会：
- 生成嵌入：使用预训练的 CLIP 模型生成图像嵌入。
- 微调：如果嵌入需要更具体地适应你的应用，微调 CLIP 模型以适应与你用例相关的数据集。

以下是你可能在代码中集成的简化示例：

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

这种方法允许你利用强大的预训练模型并将其适应于你的具体需求。

## 集成 Phi 系列模型

将 Phi-3 模型与包含 CLIP 的示例代码集成确实具有挑战性，特别是考虑到不同的视觉编码器。

以下是你可能采用的简要方法：

### 关键点
**数据处理：** 确保图像的处理方式符合 Phi-3 模型的输入要求。
**嵌入生成：** 用你的 Phi-3 模型的相应方法替换 CLIP 嵌入生成。
**微调：** 如果需要微调 Phi-3 模型，请确保在生成嵌入后包含逻辑。

## 集成 Phi-3 模型的步骤
**加载 Phi-3 模型：** 假设你有一个用于原版或微调 Phi-3 模型的 Phi3Model 类。
**修改数据准备：** 调整数据准备以适应 Phi-3 模型的输入要求。
**集成 Phi-3 嵌入：** 用 Phi-3 模型的嵌入生成替换生成 CLIP 嵌入的部分。

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

**免责声明**：
本文档使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。