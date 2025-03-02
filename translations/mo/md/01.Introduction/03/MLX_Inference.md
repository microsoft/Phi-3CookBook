# **Inference Phi-3 miaraka amin'ny Apple MLX Framework**

## **Inona ny MLX Framework**

MLX dia rafitra natao ho an'ny fikarohana momba ny fianarana milina eo ambanin'ny Apple silicon, natolotry ny fikarohana fianarana milina an'ny Apple.

Ny MLX dia noforonin'ireo mpikaroka momba ny fianarana milina ho an'ireo mpikaroka ihany koa. Ny rafitra dia natao ho mora ampiasaina, nefa mbola mahomby amin'ny fampiofanana sy fampiharana modely. Tsotra ihany koa ny endrika fototra amin'ny rafitra. Ny tanjona dia ny hanamora ny fanitarana sy fanatsarana ny MLX ho an'ireo mpikaroka mba hahafahana mandinika hevitra vaovao haingana.

Ny LLMs dia azo ampitomboina haingana amin'ny fitaovana Apple Silicon amin'ny alàlan'ny MLX, ary azo ampiasaina eo an-toerana mora foana ireo modely.

## **Fampiasana MLX hanatanterahana Phi-3-mini**

### **1. Amboary ny tontolo iainanao MLX**

1. Python 3.11.x  
2. Mametraka ny Tranomboky MLX  

```bash

pip install mlx-lm

```

### **2. Fampandehanana Phi-3-mini ao amin'ny Terminal amin'ny MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Ny vokatra (ny tontolo iainako dia Apple M1 Max, 64GB) dia toy izao

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.mo.png)

### **3. Fanovàna Phi-3-mini ho INT4 miaraka amin'ny MLX ao amin'ny Terminal**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Fanamarihana：*** Ny modely dia azo avadika amin'ny alàlan'ny mlx_lm.convert, ary ny fanovàna default dia INT4. Amin'ity ohatra ity, Phi-3-mini no avadika ho INT4.

Ny modely dia azo avadika amin'ny alàlan'ny mlx_lm.convert, ary ny fanovàna default dia INT4. Amin'ity ohatra ity, Phi-3-mini dia avadika ho INT4. Rehefa vita ny fanovàna, dia ho voatahiry ao amin'ny lahatahiry default ./mlx_model.

Azontsika atao ny mizaha toetra ny modely novaina tamin'ny MLX avy ao amin'ny terminal.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Ny vokatra dia toy izao

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.mo.png)

### **4. Fampandehanana Phi-3-mini amin'ny MLX ao amin'ny Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.mo.png)

***Fanamarihana:*** Azafady, vakio ity ohatra ity [tsindrio eto](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **Loharano**

1. Mianara momba ny Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

It seems like "mo" could refer to a specific language or dialect, but it isn't clear which one you mean. Could you clarify which language or context you're referring to with "mo"? For example, are you referring to Māori, Mon (spoken in Myanmar and Thailand), or something else?