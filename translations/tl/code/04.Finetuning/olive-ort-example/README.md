# I-fine-tune ang Phi3 gamit ang Olive

Sa halimbawang ito, gagamitin mo ang Olive para:

1. I-fine-tune ang isang LoRA adapter upang mauri ang mga parirala bilang Sad, Joy, Fear, Surprise.
1. Pagsamahin ang mga adapter weights sa base model.
1. I-optimize at i-quantize ang model sa `int4`.

Ipapakita rin namin kung paano mag-inference gamit ang fine-tuned na modelo gamit ang ONNX Runtime (ORT) Generate API.

> **⚠️ Para sa Fine-tuning, kailangan mong magkaroon ng angkop na GPU - halimbawa, A10, V100, A100.**

## 💾 Pag-install

Gumawa ng bagong Python virtual environment (halimbawa, gamit ang `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Susunod, i-install ang Olive at ang mga dependencies para sa fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 I-fine-tune ang Phi3 gamit ang Olive

Ang [Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) ay naglalaman ng isang *workflow* na may sumusunod na *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Sa mataas na antas, ang workflow na ito ay gagawin ang sumusunod:

1. I-fine-tune ang Phi3 (sa loob ng 150 steps, na maaari mong baguhin) gamit ang [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) na data.
1. Pagsamahin ang LoRA adapter weights sa base model. Magreresulta ito sa isang model artifact sa ONNX format.
1. Ang Model Builder ay i-o-optimize ang modelo para sa ONNX runtime *at* i-quantize ang modelo sa `int4`.

Upang i-execute ang workflow, patakbuhin:

```bash
olive run --config phrase-classification.json
```

Kapag natapos na ang Olive, ang iyong na-optimize na `int4` fine-tuned Phi3 model ay matatagpuan sa: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 I-integrate ang fine-tuned Phi3 sa iyong application 

Upang patakbuhin ang app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Ang magiging sagot ay isang solong salita na klasipikasyon ng parirala (Sad/Joy/Fear/Surprise).

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na batay sa makina. Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.