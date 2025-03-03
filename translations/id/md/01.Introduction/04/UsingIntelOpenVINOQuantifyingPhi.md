# **Mengkuantisasi Phi-3.5 menggunakan Intel OpenVINO**

Intel adalah produsen CPU paling tradisional dengan banyak pengguna. Dengan meningkatnya pembelajaran mesin dan pembelajaran mendalam, Intel juga ikut serta dalam persaingan akselerasi AI. Untuk inferensi model, Intel tidak hanya menggunakan GPU dan CPU, tetapi juga NPU.

Kami berharap dapat menerapkan Keluarga Phi-3.x di sisi pengguna akhir, dengan harapan menjadi bagian paling penting dari PC AI dan PC Copilot. Pemrosesan model di sisi pengguna akhir bergantung pada kerja sama dari berbagai produsen perangkat keras. Bab ini terutama berfokus pada skenario aplikasi Intel OpenVINO sebagai model kuantitatif.

## **Apa itu OpenVINO**

OpenVINO adalah toolkit sumber terbuka untuk mengoptimalkan dan menerapkan model pembelajaran mendalam dari cloud ke edge. Toolkit ini mempercepat inferensi pembelajaran mendalam di berbagai kasus penggunaan, seperti AI generatif, video, audio, dan bahasa dengan model dari framework populer seperti PyTorch, TensorFlow, ONNX, dan lainnya. Anda dapat mengonversi dan mengoptimalkan model, serta menerapkannya di berbagai perangkat keras Intel® dan lingkungan, baik di tempat, di perangkat, di browser, maupun di cloud.

Kini dengan OpenVINO, Anda dapat dengan cepat mengkuantisasi model GenAI pada perangkat keras Intel dan mempercepat referensi model.

Saat ini, OpenVINO mendukung konversi kuantisasi untuk Phi-3.5-Vision dan Phi-3.5-Instruct.

### **Persiapan Lingkungan**

Pastikan bahwa ketergantungan lingkungan berikut telah diinstal, ini adalah requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Mengkuantisasi Phi-3.5-Instruct menggunakan OpenVINO**

Di Terminal, jalankan skrip ini:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Mengkuantisasi Phi-3.5-Vision menggunakan OpenVINO**

Silakan jalankan skrip ini di Python atau Jupyter lab:

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

| Labs    | Deskripsi | Akses |
| -------- | ------- |  ------- |
| 🚀 Lab-Perkenalan Phi-3.5 Instruct  | Pelajari cara menggunakan Phi-3.5 Instruct di PC AI Anda    |  [Akses](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (gambar) | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis gambar di PC AI Anda      |  [Akses](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Perkenalan Phi-3.5 Vision (video)   | Pelajari cara menggunakan Phi-3.5 Vision untuk menganalisis video di PC AI Anda    |  [Akses](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Sumber Daya**

1. Pelajari lebih lanjut tentang Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repositori GitHub Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.