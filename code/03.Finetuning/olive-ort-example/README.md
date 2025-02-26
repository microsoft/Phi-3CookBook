# Fine-tune Phi3 using Olive

In this example you'll use Olive to:

1. Fine-tune a LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.
1. Merge the adapter weights into the base model.
1. Optimize and Quantize the model into `int4`.

We'll also show you how to inference the fine-tuned model using the ONNX Runtime (ORT) Generate API.

> **⚠️ For Fine-tuning, you'll need to have a suitable GPU available - for example, an A10, V100, A100.**

## 💾 Install

Create a new Python virtual environment (for example, using `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install the Olive and the dependencies for a fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 using Olive
The [Olive configuration file](./phrase-classification.json) contains a *workflow* with the following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

At a high-level, this workflow will:

1. Fine-tune Phi3 (for 150 steps, which you can modify) using the [dataset/data-classification.json](./dataset/dataset-classification.json) data.
1. Merge the LoRA adapter weights into the base model. This will give you a single model artifact in the ONNX format.
1. Model Builder will optimize the model for the ONNX runtime *and* quantize the model into `int4`.

To execute the workflow, run:

```bash
olive run --config phrase-classification.json
```

When Olive has completed, you're optimized `int4` fine-tuned Phi3 model is available in: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate fine-tuned Phi3 into your application 

To run the app:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

This response should be a single word classification of the phrase (Sad/Joy/Fear/Surprise).




