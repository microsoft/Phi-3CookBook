# **Quantizing Phi-3.5 menggunakan Intel OpenVINO**

Intel adalah pengeluar CPU yang paling tradisional dengan ramai pengguna. Dengan kebangkitan pembelajaran mesin dan pembelajaran mendalam, Intel juga telah menyertai persaingan untuk pecutan AI. Untuk inferens model, Intel bukan sahaja menggunakan GPU dan CPU, tetapi juga NPU.

Kami berharap dapat melaksanakan Phi-3.x Family di sisi akhir, dengan harapan menjadi bahagian paling penting dalam AI PC dan Copilot PC. Pemuatan model di sisi akhir bergantung kepada kerjasama antara pengeluar perkakasan yang berbeza. Bab ini terutamanya memberi tumpuan kepada senario aplikasi Intel OpenVINO sebagai model kuantitatif.

## **Apa itu OpenVINO**

OpenVINO adalah toolkit sumber terbuka untuk mengoptimumkan dan melaksanakan model pembelajaran mendalam dari awan ke edge. Ia mempercepat inferens pembelajaran mendalam dalam pelbagai kegunaan, seperti AI generatif, video, audio, dan bahasa dengan model dari kerangka popular seperti PyTorch, TensorFlow, ONNX, dan lain-lain. Tukar dan optimumkan model, serta laksanakan pada gabungan perkakasan dan persekitaran Intel®, sama ada di premis atau pada peranti, di pelayar atau di awan.

Kini dengan OpenVINO, anda boleh dengan cepat mengkuantitaskan model GenAI pada perkakasan Intel dan mempercepatkan rujukan model.

Sekarang OpenVINO menyokong penukaran kuantisasi untuk Phi-3.5-Vision dan Phi-3.5-Instruct.

### **Persediaan Persekitaran**

Sila pastikan kebergantungan persekitaran berikut telah dipasang, ini adalah requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Mengkuantitaskan Phi-3.5-Instruct menggunakan OpenVINO**

Di Terminal, sila jalankan skrip ini

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Mengkuantitaskan Phi-3.5-Vision menggunakan OpenVINO**

Sila jalankan skrip ini dalam Python atau Jupyter lab

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

### **🤖 Contoh untuk Phi-3.5 dengan Intel OpenVINO**

| Labs    | Pengenalan | Pergi |
| -------- | ------- |  ------- |
| 🚀 Lab-Pengenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct dalam AI PC anda    |  [Pergi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Pengenalan Phi-3.5 Vision (imej) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis imej dalam AI PC anda      |  [Pergi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Pengenalan Phi-3.5 Vision (video)   | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis video dalam AI PC anda    |  [Pergi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Sumber**

1. Ketahui lebih lanjut tentang Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repositori GitHub Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.