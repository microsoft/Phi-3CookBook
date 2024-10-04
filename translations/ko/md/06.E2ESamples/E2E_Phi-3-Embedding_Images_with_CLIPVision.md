# CLIPVisionModel을 사용하여 이미지 처리 및 Phi-3-vision으로 이미지 임베딩 생성하기

다음 파이썬 샘플은 CLIPVisionModel을 사용하여 이미지를 처리하고 이미지 임베딩을 생성하는 데 필요한 기능을 제공합니다.

## CLIP이란 무엇인가
CLIP은 Contrastive Language-Image Pre-training의 약자로, 자연어 감독을 통해 시각적 개념을 효율적으로 학습하는 OpenAI가 개발한 모델입니다. 이미지와 텍스트 이해를 하나의 프레임워크로 결합한 멀티모달 모델입니다. CLIP은 다양한 인터넷 소스에서 가져온 이미지와 그와 함께 발견된 텍스트를 학습하여, 어떤 이미지가 어떤 텍스트와 쌍을 이루었는지 예측합니다. 이로써 두 가지 모달리티를 효과적으로 연결합니다.

이 모델은 이미지와 텍스트 조각을 입력으로 받아 텍스트가 이미지의 정확한 설명일 가능성을 예측합니다. 이 접근 방식은 CLIP이 객체 인식, 분류, 심지어 이전에 본 적 없는 이미지에 대한 설명 생성 등 다양한 시각적 작업을 처리할 수 있게 합니다.

CLIP의 주요 장점 중 하나는 "제로샷" 학습을 수행할 수 있다는 것입니다. 이는 모델이 명시적으로 학습되지 않은 작업도 단순히 작업 설명을 읽음으로써 올바르게 처리할 수 있다는 것입니다. 이는 모델이 방대한 양의 다양한 데이터를 학습했기 때문에 새로운 작업에 잘 일반화할 수 있기 때문입니다.

## Phi-3-vision
Phi-3-vision은 언어 및 시각 기능을 갖춘 4.2B 파라미터 멀티모달 모델로, 실제 이미지와 디지털 문서를 분석하고 텍스트를 추출 및 분석하며, 차트나 다이어그램과 관련된 통찰력과 답변을 생성할 수 있습니다.

## 샘플 코드
이 코드는 이미지 임베딩 모델을 나타내는 Phi3ImageEmbedding이라는 클래스를 정의합니다. 이 클래스의 목적은 이미지를 처리하고 이미지 분류나 검색과 같은 다운스트림 작업에 사용할 수 있는 임베딩을 생성하는 것입니다.

__init__ 메서드는 임베딩 드롭아웃, 이미지 프로세서, HD 변환 파라미터 및 이미지 프로젝션과 같은 다양한 구성 요소를 설정하여 모델을 초기화합니다. 이 메서드는 모델의 구성 파라미터를 포함하는 config 객체를 입력으로 받습니다. wte 파라미터는 단어 토큰 임베딩을 나타내는 선택적 입력입니다.

get_img_features 메서드는 이미지 임베딩을 나타내는 입력 텐서 img_embeds를 받아 추출된 이미지 특징을 나타내는 텐서를 반환합니다. 이 메서드는 img_processor를 사용하여 이미지 임베딩을 처리하고 layer_idx 및 type_feature 파라미터에 따라 원하는 특징을 추출합니다.

## 코드 설명
코드를 단계별로 설명해 보겠습니다:

코드는 math, torch, torch.nn 및 transformers 라이브러리의 다양한 구성 요소를 포함한 필요한 라이브러리와 모듈을 임포트합니다.

코드는 이미지 임베딩 모델에 대한 다양한 하이퍼파라미터를 포함하는 CLIP_VIT_LARGE_PATCH14_336_CONFIG라는 구성 객체를 정의합니다.

Phi3ImageEmbedding 클래스가 정의되며, 이는 torch.nn.Module의 하위 클래스입니다. 이 클래스는 이미지 임베딩 모델을 나타내며, 순방향 전파 및 이미지 특징 설정을 위한 메서드를 포함합니다.

__init__ 메서드는 Phi3ImageEmbedding 객체를 초기화합니다. 이 메서드는 PretrainedConfig 클래스의 인스턴스인 config 객체를 입력으로 받습니다. 또한 선택적 wte 인수를 받습니다.

__init__ 메서드는 제공된 config 객체를 기반으로 Phi3ImageEmbedding 객체의 다양한 속성을 초기화합니다. 숨겨진 크기, 드롭아웃 비율, 이미지 프로세서, 이미지 프로젝션 및 기타 파라미터를 설정합니다.

set_img_features 메서드는 모델의 이미지 특징을 설정합니다. 이 메서드는 이미지 특징의 텐서를 입력으로 받아 객체의 img_features 속성에 할당합니다.

set_img_sizes 메서드는 모델의 이미지 크기를 설정합니다. 이 메서드는 이미지 크기의 텐서를 입력으로 받아 객체의 img_sizes 속성에 할당합니다.

get_img_features 메서드는 입력 이미지 임베딩에서 이미지 특징을 추출합니다. 이 메서드는 이미지 임베딩의 텐서를 입력으로 받아 추출된 이미지 특징을 반환합니다.

forward 메서드는 모델을 통해 순방향 전파를 수행합니다. 이 메서드는 입력 ID, 픽셀 값 및 이미지 크기를 입력으로 받아 모델의 숨겨진 상태를 반환합니다. 먼저 이미지 특징과 크기가 이미 설정되어 있는지 확인하고, 그렇지 않으면 제공된 입력을 사용하여 설정합니다. 그런 다음 입력 ID를 처리하고 구성된 이미지 프로세서를 기반으로 이미지 특징을 추출합니다. 마지막으로 추출된 특징에 이미지 프로젝션을 적용하고 숨겨진 상태를 반환합니다.

전반적으로 이 코드는 이미지 임베딩 모델을 나타내는 클래스를 정의하고, 이미지 특징을 설정하고 순방향 전파를 수행하는 메서드를 제공합니다.

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

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서가 작성된 언어의 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.