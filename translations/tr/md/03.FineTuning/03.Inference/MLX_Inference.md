# **Apple MLX Framework ile Phi-3 Çıkarımı**

## **MLX Framework Nedir**

MLX, Apple silikon üzerinde makine öğrenimi araştırmaları için Apple makine öğrenimi araştırma ekibi tarafından sunulan bir dizi framework'tür.

MLX, makine öğrenimi araştırmacıları tarafından, makine öğrenimi araştırmacıları için tasarlanmıştır. Framework, kullanıcı dostu olacak şekilde tasarlanmış, ancak yine de modelleri eğitmek ve dağıtmak için verimli bir yapıdadır. Framework'ün tasarımı kavramsal olarak da basittir. Amacımız, araştırmacıların MLX'i kolayca genişletip geliştirmesini sağlamak ve yeni fikirleri hızlı bir şekilde keşfetmelerine yardımcı olmaktır.

Apple Silicon cihazlarında MLX aracılığıyla büyük dil modelleri (LLM'ler) hızlandırılabilir ve modeller yerel olarak oldukça kolay bir şekilde çalıştırılabilir.

## **MLX Kullanarak Phi-3-mini Çıkarımı**

### **1. MLX ortamınızı kurun**

1. Python 3.11.x
2. MLX Kütüphanesini yükleyin

```bash

pip install mlx-lm

```

### **2. Terminalde MLX ile Phi-3-mini Çalıştırma**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Sonuç (benim ortamım Apple M1 Max, 64GB):

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.tr.png)

### **3. Terminalde MLX ile Phi-3-mini Modelini Kuantize Etme**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Not:*** Model, mlx_lm.convert kullanılarak kuantize edilebilir ve varsayılan kuantizasyon INT4'tür. Bu örnekte Phi-3-mini INT4 formatına kuantize edilmiştir.

Model, mlx_lm.convert kullanılarak kuantize edilebilir ve varsayılan kuantizasyon INT4'tür. Bu örnekte Phi-3-mini INT4 formatına kuantize edilmiştir. Kuantizasyon sonrası model varsayılan dizin olan ./mlx_model içine kaydedilir.

Terminalden MLX ile kuantize edilmiş modeli test edebiliriz.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Sonuç:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.tr.png)

### **4. Jupyter Notebook ile MLX Üzerinde Phi-3-mini Çalıştırma**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.tr.png)

***Not:*** Lütfen bu örneği inceleyin [bu bağlantıya tıklayın](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Kaynaklar**

1. Apple MLX Framework'ü hakkında bilgi edinin [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Deposu [https://github.com/ml-explore](https://github.com/ml-explore)

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul etmiyoruz.