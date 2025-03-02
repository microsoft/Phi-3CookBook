# **Phi-3.5'i Apple MLX Framework ile Kuantize Etme**

MLX, Apple silikonunda makine öğrenimi araştırmaları için Apple makine öğrenimi araştırma ekibi tarafından geliştirilen bir dizi framework'tür.

MLX, makine öğrenimi araştırmacıları tarafından, makine öğrenimi araştırmacıları için tasarlanmıştır. Framework, kullanıcı dostu olmasının yanı sıra modelleri verimli bir şekilde eğitmek ve dağıtmak için optimize edilmiştir. Ayrıca framework'ün tasarımı kavramsal olarak basittir. Araştırmacıların MLX'i genişletmesini ve iyileştirmesini, böylece yeni fikirleri hızla keşfetmesini kolaylaştırmayı amaçlıyoruz.

LLM'ler, Apple Silicon cihazlarında MLX ile hızlandırılabilir ve modeller yerel olarak çok rahat bir şekilde çalıştırılabilir.

Artık Apple MLX Framework, Phi-3.5-Instruct(**Apple MLX Framework desteği**), Phi-3.5-Vision(**MLX-VLM Framework desteği**) ve Phi-3.5-MoE(**Apple MLX Framework desteği**) modellerinin kuantizasyon dönüşümünü destekliyor. Şimdi bunu deneyelim:

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

### **🤖 Apple MLX ile Phi-3.5 için Örnekler**

| Laboratuvarlar    | Tanıtım | Git |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instruct Tanıtımı  | Apple MLX framework ile Phi-3.5 Instruct kullanımını öğrenin   |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (görsel) Tanıtımı | Apple MLX framework ile Phi-3.5 Vision'ı kullanarak görselleri analiz etmeyi öğrenin     |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Phi-3.5 MoE Tanıtımı   | Apple MLX framework ile Phi-3.5 MoE kullanımını öğrenin  |  [Git](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Kaynaklar**

1. Apple MLX Framework hakkında bilgi edinin [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Deposu [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Deposu [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.