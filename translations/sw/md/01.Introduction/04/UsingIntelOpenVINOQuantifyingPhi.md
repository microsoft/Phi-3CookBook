# **Kuweka Kiwango Phi-3.5 kwa Kutumia Intel OpenVINO**

Intel ni mtengenezaji wa CPU wa jadi zaidi mwenye watumiaji wengi. Pamoja na kuongezeka kwa ujifunzaji wa mashine na ujifunzaji wa kina, Intel pia imejiunga katika ushindani wa kuongeza kasi ya AI. Kwa uamuzi wa modeli, Intel haitumii tu GPUs na CPUs, bali pia hutumia NPUs.

Tunatarajia kupeleka Familia ya Phi-3.x upande wa mwisho, tukilenga kuwa sehemu muhimu zaidi ya AI PC na Copilot PC. Uwekaji wa modeli upande wa mwisho unategemea ushirikiano wa wazalishaji tofauti wa vifaa. Sura hii inalenga zaidi hali ya matumizi ya Intel OpenVINO kama modeli ya kiasi.

## **OpenVINO ni nini**

OpenVINO ni zana ya wazi ya chanzo kwa kuboresha na kuweka modeli za ujifunzaji wa kina kutoka wingu hadi kwenye ukingo. Inaongeza kasi ya uamuzi wa ujifunzaji wa kina katika hali mbalimbali za matumizi, kama AI ya kizazi, video, sauti, na lugha kwa kutumia modeli kutoka mifumo maarufu kama PyTorch, TensorFlow, ONNX, na zaidi. Geuza na boresha modeli, na uweka kwenye mchanganyiko wa vifaa vya Intel® na mazingira, kwenye eneo, kwenye kifaa, kwenye kivinjari au kwenye wingu.

Sasa kwa OpenVINO, unaweza haraka kuweka kiwango cha modeli ya GenAI kwenye vifaa vya Intel na kuongeza kasi ya marejeo ya modeli.

Sasa OpenVINO inasaidia ubadilishaji wa kiwango cha Phi-3.5-Vision na Phi-3.5 Instruct.

### **Kuweka Mazingira**

Tafadhali hakikisha utegemezi wa mazingira yafuatayo yamewekwa, haya ni yaliyomo kwenye requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kuweka Kiwango cha Phi-3.5-Instruct kwa Kutumia OpenVINO**

Katika Terminal, tafadhali endesha script hii

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kuweka Kiwango cha Phi-3.5-Vision kwa Kutumia OpenVINO**

Tafadhali endesha script hii kwenye Python au Jupyter lab

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

### **🤖 Sampuli za Phi-3.5 na Intel OpenVINO**

| Maabara    | Utangulizi | Nenda |
| -------- | ------- |  ------- |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Instruct  | Jifunze jinsi ya kutumia Phi-3.5 Instruct kwenye AI PC yako    |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Vision (picha) | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchanganua picha kwenye AI PC yako      |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Maabara-Utangulizi wa Phi-3.5 Vision (video)   | Jifunze jinsi ya kutumia Phi-3.5 Vision kuchanganua video kwenye AI PC yako    |  [Nenda](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Rasilimali**

1. Jifunze zaidi kuhusu Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za mtafsiri wa kibinadamu mwenye taaluma. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.