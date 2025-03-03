# **Phi-3.5-ийг Apple MLX Framework ашиглан квантачлах**

MLX нь Apple silicon дээр машин сургалтын судалгаанд зориулсан array framework бөгөөд Apple-ийн машин сургалтын судалгааны багийн бүтээл юм.

MLX нь машин сургалтын судлаачдад зориулан, тэдний хэрэгцээнд нийцүүлэн бүтээгдсэн. Энэхүү framework нь ашиглахад хялбар, гэхдээ загваруудыг үр ашигтай сургаж, нэвтрүүлэх боломжтой. Framework-ийн өөрийн загвар нь ойлгомжтой, энгийн бөгөөд судлаачид MLX-ийг өргөтгөж, сайжруулахад хялбар байх зорилготой. Ингэснээр шинэ санааг хурдан турших боломжийг бүрдүүлдэг.

Apple Silicon төхөөрөмж дээр LLM-уудыг MLX ашиглан хурдасгах боломжтой бөгөөд загваруудыг орон нутгийн түвшинд маш хялбар ажиллуулж болно.

Одоо Apple MLX Framework нь Phi-3.5-Instruct(**Apple MLX Framework дэмжлэгтэй**), Phi-3.5-Vision(**MLX-VLM Framework дэмжлэгтэй**), болон Phi-3.5-MoE(**Apple MLX Framework дэмжлэгтэй**) загваруудыг квантачлалд хөрвүүлэхийг дэмжиж байна. Дараах алхмуудыг туршаад үзье:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX ашиглан Phi-3.5-ийн жишээнүүд**

| Лаборатори   | Танилцуулга | Шилжих |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Phi-3.5 Instruct-ийг Apple MLX framework ашиглан хэрхэн хэрэглэхийг сурна уу   |  [Шилжих](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Phi-3.5 Vision-ийг ашиглан зургийг хэрхэн шинжлэхийг Apple MLX framework-ээр сурна уу     |  [Шилжих](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Phi-3.5 MoE-ийг Apple MLX framework ашиглан хэрхэн хэрэглэхийг сурна уу  |  [Шилжих](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Нөөцүүд**

1. Apple MLX Framework-ийн талаар судлах [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

It seems like "mo" could refer to a language or a shorthand for something. Could you clarify what "mo" refers to? For example, are you referring to Maori, Mongolian, or another language?