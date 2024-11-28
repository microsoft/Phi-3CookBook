# CLIPVisionModel을 사용하여 이미지를 처리하고 Phi-3-vision으로 이미지 임베딩 생성하기

다음 파이썬 샘플은 CLIPVisionModel을 사용하여 이미지를 처리하고 이미지 임베딩을 생성하는 데 필요한 기능을 제공합니다.

## CLIP이란 무엇인가
CLIP은 Contrastive Language-Image Pre-training의 약자로, OpenAI에서 개발한 모델로 자연어 감독을 통해 효율적으로 시각적 개념을 학습합니다. 이 모델은 이미지와 텍스트 이해를 단일 프레임워크에서 결합한 멀티모달 모델입니다. CLIP은 다양한 인터넷 소스의 이미지와 해당 이미지에 포함된 텍스트를 학습하여 어떤 이미지가 어떤 텍스트와 짝지어졌는지 예측합니다. 이를 통해 두 가지 모달리티를 연결합니다.

이 모델은 이미지를 입력받아 텍스트 조각과 함께 입력받고, 해당 텍스트가 이미지의 정확한 설명일 가능성을 예측합니다. 이러한 접근 방식은 CLIP이 객체 인식, 분류 및 이전에 본 적 없는 이미지에 대한 설명 생성과 같은 다양한 시각적 작업을 처리할 수 있게 합니다.

CLIP의 주요 장점 중 하나는 "제로샷" 학습 능력입니다. 이는 모델이 명시적으로 훈련되지 않은 작업을 단순히 작업 설명을 읽음으로써 올바르게 처리할 수 있는 능력입니다. 이는 다양하고 방대한 데이터를 학습했기 때문에 새로운 작업에 대해 잘 일반화할 수 있습니다.

## Phi-3-vision
Phi-3-vision은 42억 개의 파라미터를 가진 멀티모달 모델로, 언어와 시각 기능을 갖추고 있으며, 실제 이미지와 디지털 문서를 통해 추론하고, 이미지에서 텍스트를 추출하고 추론하며, 차트나 다이어그램과 관련된 통찰력과 답변을 생성할 수 있습니다.

**예제 목적:** 이 예제는 CLIP을 사용하여 이미지 임베딩을 생성하고 이를 Phi-3 모델 관련 작업에 적용하는 방법을 보여줍니다. 이는 다른 임베딩 기법(CLIP vs. Phi-3)의 성능과 특성을 비교하는 참고 자료로 사용됩니다.
**통합 과제:** CLIP과 같은 다른 비전 인코더를 Phi-3에 직접 통합하는 것은 복잡합니다. 이는 아키텍처 차이와 맥락이나 성능을 잃지 않으면서 매끄럽게 통합해야 하는 필요성 때문입니다. 통합은 아직 완전히 평가되거나 구현되지 않았기 때문에 이 예제가 포함되었습니다.
**비교 접근법:** 이 코드는 통합 솔루션이 아닌 평행 비교를 제공하는 것을 목표로 합니다. 사용자가 CLIP 임베딩이 Phi-3 임베딩과 나란히 어떻게 작동하는지 확인할 수 있게 하여 잠재적인 이점이나 단점을 파악할 수 있게 합니다.
**명확화:** 이 Phi-3CookBook 예제는 CLIP 임베딩을 Phi-3에 직접 통합하는 것이 아니라 비교 도구로 사용하는 방법을 보여줍니다.
**통합 작업:** CLIP 임베딩을 Phi-3에 완전히 통합하는 것은 여전히 도전 과제로 남아 있으며, 아직 완전히 탐구되지 않았지만 고객이 실험할 수 있도록 제공됩니다.

## 샘플 코드
이 코드는 이미지 임베딩 모델을 나타내는 Phi3ImageEmbedding이라는 클래스를 정의합니다. 이 클래스의 목적은 이미지를 처리하고 이미지 분류나 검색과 같은 다운스트림 작업에 사용할 수 있는 임베딩을 생성하는 것입니다.

__init__ 메서드는 임베딩 드롭아웃, 이미지 프로세서, HD 변환 파라미터 및 이미지 프로젝션과 같은 다양한 구성 요소를 설정하여 모델을 초기화합니다. 이 메서드는 모델의 구성 파라미터를 포함하는 config 객체를 입력으로 받습니다. wte 파라미터는 단어 토큰 임베딩을 나타내는 선택적 입력입니다.

get_img_features 메서드는 이미지 임베딩을 나타내는 img_embeds 입력 텐서를 받아 추출된 이미지 특징을 나타내는 텐서를 반환합니다. 이 메서드는 img_processor를 사용하여 이미지 임베딩을 처리하고 layer_idx 및 type_feature 파라미터를 기반으로 원하는 특징을 추출합니다.

## 코드 설명
코드를 단계별로 살펴보겠습니다:

코드는 math, torch, torch.nn 및 transformers 라이브러리의 다양한 구성 요소를 포함한 필요한 라이브러리와 모듈을 가져옵니다.

코드는 이미지 임베딩 모델을 위한 다양한 하이퍼파라미터를 포함하는 CLIP_VIT_LARGE_PATCH14_336_CONFIG라는 구성 객체를 정의합니다.

Phi3ImageEmbedding 클래스가 정의됩니다. 이 클래스는 torch.nn.Module의 하위 클래스입니다. 이 클래스는 이미지 임베딩 모델을 나타내며, 순방향 전파 및 이미지 특징 설정을 위한 메서드를 포함합니다.

__init__ 메서드는 Phi3ImageEmbedding 객체를 초기화합니다. 이 메서드는 PretrainedConfig 클래스의 인스턴스인 config 객체를 입력으로 받습니다. 또한 선택적 wte 인수를 받습니다.

__init__ 메서드는 제공된 config 객체를 기반으로 Phi3ImageEmbedding 객체의 다양한 속성을 초기화합니다. 숨겨진 크기, 드롭아웃 비율, 이미지 프로세서, 이미지 프로젝션 및 기타 파라미터를 설정합니다.

set_img_features 메서드는 모델의 이미지 특징을 설정합니다. 이 메서드는 이미지 특징의 텐서를 입력으로 받아 객체의 img_features 속성에 할당합니다.

set_img_sizes 메서드는 모델의 이미지 크기를 설정합니다. 이 메서드는 이미지 크기의 텐서를 입력으로 받아 객체의 img_sizes 속성에 할당합니다.

get_img_features 메서드는 입력 이미지 임베딩에서 이미지 특징을 추출합니다. 이 메서드는 이미지 임베딩의 텐서를 입력으로 받아 추출된 이미지 특징을 반환합니다.

forward 메서드는 모델을 통해 순방향 전파를 수행합니다. 이 메서드는 입력 ID, 픽셀 값 및 이미지 크기를 입력으로 받아 모델의 숨겨진 상태를 반환합니다. 먼저 이미지 특징과 크기가 이미 설정되었는지 확인하고, 설정되지 않은 경우 제공된 입력을 사용하여 설정합니다. 그런 다음 입력 ID를 처리하고 구성된 이미지 프로세서를 기반으로 이미지 특징을 추출합니다. 마지막으로 추출된 특징에 이미지 프로젝션을 적용하고 숨겨진 상태를 반환합니다.

전체적으로 이 코드는 이미지 임베딩 모델을 나타내는 클래스를 정의하고 이미지 특징 설정 및 순방향 전파를 수행하는 메서드를 제공합니다.

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

## 파이프라인 구축

위의 예제와 같이 임베딩을 생성하는 코드를 사용할 때는 특정 사용 사례에 따라 파이프라인에 통합하는 것이 일반적입니다.
 
1. 사전 훈련된 모델 로드: Hugging Face에서 사전 훈련된 모델을 로드하는 경우, 이러한 모델은 바이너리입니다. 추가 훈련 없이 직접 임베딩을 생성하는 데 사용할 수 있습니다. 이는 기능 추출이나 의미 검색과 같은 임베딩이 즉시 필요한 작업에 유용합니다.
 
2. 파인 튜닝 파이프라인: 모델을 특정 작업이나 데이터셋에 맞게 조정해야 하는 경우, 코드를 파인 튜닝 파이프라인에 통합합니다. 이는 다음을 포함합니다:
   - 사전 훈련된 모델 로드: Hugging Face에서 사전 훈련된 모델로 시작합니다.
   - 데이터셋 준비: 데이터셋이 훈련에 적합한 형식인지 확인합니다.
   - 파인 튜닝: Hugging Face의 `transformers` and `datasets` 라이브러리를 사용하여 모델을 데이터셋에 맞게 파인 튜닝합니다. 이 단계에서는 모델 가중치를 조정하여 특정 작업에 더 적합하게 만듭니다.
 
예를 들어, Phi-3 Cookbook과 CLIPVision의 맥락에서:
- 임베딩 생성: 사전 훈련된 CLIP 모델을 사용하여 이미지에 대한 임베딩을 생성합니다.
- 파인 튜닝: 임베딩이 응용 프로그램에 더 적합하도록 CLIP 모델을 관련 데이터셋에 맞게 파인 튜닝합니다.
 
다음은 이를 코드에 통합하는 간단한 예입니다:
 
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
 
이 접근 방식은 강력한 사전 훈련된 모델을 활용하고 이를 특정 요구에 맞게 조정할 수 있게 합니다.

## Phi 모델 계열 통합

CLIP을 포함한 제공된 코드 예제를 사용하여 Phi-3 모델을 통합하는 것은 특히 다른 비전 인코더를 고려할 때 도전적일 수 있습니다.
 
다음은 이를 접근하는 방법에 대한 간략한 개요입니다:
 
### 주요 포인트
**데이터 처리:** 이미지가 Phi-3 모델의 입력 요구 사항에 맞게 처리되었는지 확인합니다.
**임베딩 생성:** CLIP 임베딩 생성을 Phi-3 모델의 해당 메서드로 대체합니다.
**파인 튜닝:** Phi-3 모델을 파인 튜닝해야 하는 경우, 임베딩을 생성한 후 논리를 포함합니다.

## Phi-3 모델 통합 단계
**Phi-3 모델 로드:** 기본 또는 파인 튜닝된 Phi-3 모델에 대한 Phi3Model 클래스를 가지고 있다고 가정합니다.
**데이터 준비 수정:** 데이터를 Phi-3 모델의 입력 요구 사항에 맞게 준비합니다.
**Phi-3 임베딩 통합:** CLIP 임베딩이 생성되는 부분을 Phi-3 모델의 임베딩 생성으로 대체합니다.

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

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오역에 대해서는 책임지지 않습니다.