# Fine-tune Phi3 using Olive

In this example, you will use Olive to:

1. Fine-tune a LoRA adapter to classify phrases into Sad, Joy, Fear, Surprise.
2. Merge the adapter weights into the base model.
3. Optimize and quantize the model into `int4`.

We'll also demonstrate how to perform inference with the fine-tuned model using the ONNX Runtime (ORT) Generate API.

> **⚠️ For fine-tuning, you'll need access to a suitable GPU, such as an A10, V100, or A100.**

## 💾 Install

Start by creating a new Python virtual environment (e.g., using `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Next, install Olive along with the dependencies needed for the fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 using Olive
The [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) defines a *workflow* that includes the following *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

At a high level, this workflow will:

1. Fine-tune Phi3 (for 150 steps by default, which you can adjust) using the data from [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
2. Merge the LoRA adapter weights into the base model, resulting in a single ONNX-format model artifact.
3. Use Model Builder to optimize the model for ONNX Runtime and quantize it into `int4`.

To execute the workflow, run:

```bash
olive run --config phrase-classification.json
```

Once Olive completes the process, your optimized `int4` fine-tuned Phi3 model will be available at: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integrate fine-tuned Phi3 into your application 

To run the application:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

The response will be a single-word classification of the phrase (Sad/Joy/Fear/Surprise).

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.