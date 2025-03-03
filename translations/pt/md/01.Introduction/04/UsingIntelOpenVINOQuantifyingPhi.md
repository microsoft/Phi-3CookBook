# **Quantizando o Phi-3.5 usando Intel OpenVINO**

A Intel é o fabricante de CPUs mais tradicional, com muitos usuários. Com o crescimento do aprendizado de máquina e aprendizado profundo, a Intel também entrou na competição pela aceleração de IA. Para inferência de modelos, a Intel utiliza não apenas GPUs e CPUs, mas também NPUs.

Esperamos implantar a Família Phi-3.x no lado do dispositivo, com o objetivo de se tornar a parte mais importante do PC de IA e do PC Copilot. O carregamento do modelo no lado do dispositivo depende da cooperação de diferentes fabricantes de hardware. Este capítulo foca principalmente no cenário de aplicação do Intel OpenVINO como modelo quantizado.

## **O que é o OpenVINO**

OpenVINO é um kit de ferramentas de código aberto para otimizar e implantar modelos de aprendizado profundo da nuvem para a borda. Ele acelera a inferência de aprendizado profundo em diversos casos de uso, como IA generativa, vídeo, áudio e linguagem, com modelos de frameworks populares como PyTorch, TensorFlow, ONNX e outros. Converta e otimize modelos e implante-os em uma combinação de hardware Intel® e ambientes, no local ou no dispositivo, no navegador ou na nuvem.

Agora, com o OpenVINO, você pode quantizar rapidamente o modelo GenAI no hardware Intel e acelerar a referência do modelo.

Atualmente, o OpenVINO suporta a conversão quantizada de Phi-3.5-Vision e Phi-3.5 Instruct.

### **Configuração do Ambiente**

Certifique-se de que as seguintes dependências do ambiente estão instaladas, este é o arquivo requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizando o Phi-3.5-Instruct usando OpenVINO**

No Terminal, execute este script:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizando o Phi-3.5-Vision usando OpenVINO**

Execute este script no Python ou no Jupyter Lab:

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 Exemplos para Phi-3.5 com Intel OpenVINO**

| Laboratórios    | Introdução | Acessar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introdução ao Phi-3.5 Instruct  | Aprenda como usar o Phi-3.5 Instruct no seu PC de IA    |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introdução ao Phi-3.5 Vision (imagem) | Aprenda como usar o Phi-3.5 Vision para analisar imagens no seu PC de IA      |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introdução ao Phi-3.5 Vision (vídeo)   | Aprenda como usar o Phi-3.5 Vision para analisar vídeos no seu PC de IA    |  [Acessar](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Recursos**

1. Saiba mais sobre o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repositório GitHub do Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.