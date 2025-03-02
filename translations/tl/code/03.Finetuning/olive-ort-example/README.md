# I-fine-tune ang Phi3 gamit ang Olive

Sa halimbawang ito, gagamitin mo ang Olive upang:

1. I-fine-tune ang isang LoRA adapter para i-classify ang mga parirala bilang Sad, Joy, Fear, Surprise.
1. I-merge ang adapter weights sa base model.
1. I-optimize at i-quantize ang model papunta sa `int4`.

Ipapakita rin namin kung paano mag-inference gamit ang fine-tuned na model sa pamamagitan ng ONNX Runtime (ORT) Generate API.

> **⚠️ Para sa Fine-tuning, kakailanganin mo ng angkop na GPU - halimbawa, A10, V100, A100.**

## 💾 Pag-install

Gumawa ng bagong Python virtual environment (halimbawa, gamit ang `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Sunod, i-install ang Olive at ang mga dependencies para sa fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 I-fine-tune ang Phi3 gamit ang Olive

Ang [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) ay naglalaman ng *workflow* na may sumusunod na *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Sa mataas na antas, ang workflow na ito ay:

1. I-fine-tune ang Phi3 (sa loob ng 150 steps, na maaari mong baguhin) gamit ang [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) na data.
1. I-merge ang LoRA adapter weights sa base model. Magkakaroon ka ng isang model artifact sa ONNX format.
1. Ang Model Builder ay mag-o-optimize ng model para sa ONNX runtime *at* i-quantize ang model papunta sa `int4`.

Upang patakbuhin ang workflow, gamitin ang:

```bash
olive run --config phrase-classification.json
```

Kapag natapos na ng Olive, ang na-optimize na `int4` fine-tuned Phi3 model ay makikita sa: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 I-integrate ang fine-tuned na Phi3 sa iyong application

Upang patakbuhin ang app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ang magiging tugon nito ay isang salitang classification ng parirala (Sad/Joy/Fear/Surprise).

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI-based na pagsasalin. Bagama't pinagsusumikapan naming maging wasto, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.