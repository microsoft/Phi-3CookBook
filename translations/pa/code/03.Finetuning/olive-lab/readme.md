# ਲੈਬ। ਡਿਵਾਈਸ ਉੱਤੇ ਇਨਫਰੈਂਸ ਲਈ AI ਮਾਡਲਾਂ ਨੂੰ ਆਪਟੀਮਾਈਜ਼ ਕਰੋ

## ਜਾਣ ਪਛਾਣ

> [!IMPORTANT]
> ਇਸ ਲੈਬ ਲਈ **Nvidia A10 ਜਾਂ A100 GPU** ਦੀ ਲੋੜ ਹੈ ਜਿਸ ਵਿੱਚ ਸਬੰਧਤ ਡਰਾਈਵਰ ਅਤੇ CUDA ਟੂਲਕਿਟ (ਵਰਜਨ 12+) ਇੰਸਟਾਲ ਹੋਵੇ।

> [!NOTE]
> ਇਹ **35 ਮਿੰਟਾਂ** ਦੀ ਲੈਬ ਹੈ ਜੋ ਤੁਹਾਨੂੰ OLIVE ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਿਵਾਈਸ ਉੱਤੇ ਇਨਫਰੈਂਸ ਲਈ ਮਾਡਲਾਂ ਨੂੰ ਆਪਟੀਮਾਈਜ਼ ਕਰਨ ਦੇ ਮੁੱਖ ਸਿਧਾਂਤਾਂ ਨਾਲ ਹੱਥ-ਉੱਪਰ ਤਜਰਬਾ ਦੇਵੇਗੀ।

## ਸਿਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਲੈਬ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ OLIVE ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- AWQ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ AI ਮਾਡਲ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ।
- ਖਾਸ ਟਾਸਕ ਲਈ AI ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ।
- ONNX ਰੰਟਾਈਮ 'ਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਡਿਵਾਈਸ ਇਨਫਰੈਂਸ ਲਈ LoRA ਅਡਾਪਟਰ (ਫਾਈਨ-ਟਿਊਨ ਮਾਡਲ) ਤਿਆਰ ਕਰਨਾ।

### Olive ਕੀ ਹੈ

Olive (*O*NNX *live*) ਇੱਕ ਮਾਡਲ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟੂਲਕਿਟ ਹੈ ਜਿਸ ਨਾਲ CLI ਵੀ ਸ਼ਾਮਲ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ONNX ਰੰਟਾਈਮ +++https://onnxruntime.ai+++ ਲਈ ਮਾਡਲਾਂ ਨੂੰ ਤਿਆਰ ਕਰਨ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.pa.png)

Olive ਵਿੱਚ ਆਮ ਤੌਰ 'ਤੇ PyTorch ਜਾਂ Hugging Face ਮਾਡਲ ਨੂੰ ਇਨਪੁਟ ਦੇ ਤੌਰ 'ਤੇ ਲਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਨਤੀਜਾ ਇੱਕ ਆਪਟੀਮਾਈਜ਼ ਕੀਤਾ ਹੋਇਆ ONNX ਮਾਡਲ ਹੁੰਦਾ ਹੈ ਜੋ ONNX ਰੰਟਾਈਮ ਚਲਾਉਣ ਵਾਲੇ ਡਿਵਾਈਸ (ਡਿਪਲੌਇਮੈਂਟ ਟਾਰਗੇਟ) 'ਤੇ ਐਕਸਿਕਿਊਟ ਹੁੰਦਾ ਹੈ। Olive ਮਾਡਲ ਨੂੰ ਡਿਪਲੌਇਮੈਂਟ ਟਾਰਗੇਟ ਦੇ AI ਐਕਸਲੇਰੇਟਰ (NPU, GPU, CPU) ਲਈ ਆਪਟੀਮਾਈਜ਼ ਕਰਦਾ ਹੈ ਜੋ ਕਿ Qualcomm, AMD, Nvidia ਜਾਂ Intel ਵਰਗੇ ਹਾਰਡਵੇਅਰ ਵੇਂਡਰਾਂ ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

Olive ਇੱਕ *ਵਰਕਫਲੋ* ਚਲਾਉਂਦਾ ਹੈ, ਜੋ ਕਿ ਵਿਅਕਤੀਗਤ ਮਾਡਲ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟਾਸਕਾਂ ਦੀ ਇੱਕ ਕ੍ਰਮਬੱਧ ਲੜੀ ਹੁੰਦੀ ਹੈ, ਜਿਸਨੂੰ *ਪਾਸੇਜ਼* ਕਿਹਾ ਜਾਂਦਾ ਹੈ - ਉਦਾਹਰਣ ਲਈ: ਮਾਡਲ ਕੰਪ੍ਰੈਸ਼ਨ, ਗ੍ਰਾਫ ਕੈਪਚਰ, ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ, ਗ੍ਰਾਫ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ। ਹਰ ਪਾਸੇ ਵਿੱਚ ਕੁਝ ਪੈਰਾਮੀਟਰ ਹੁੰਦੇ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਸਭ ਤੋਂ ਵਧੀਆ ਮੈਟ੍ਰਿਕਸ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਟਿਊਨ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਐਕੁਰੇਸੀ ਅਤੇ ਲੈਟੈਂਸੀ, ਜਿਹਨਾਂ ਦੀ ਕਦਰ ਸੰਬੰਧਤ ਇਵੈਲੂਏਟਰ ਦੁਆਰਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। Olive ਇੱਕ ਖੋਜ ਰਣਨੀਤੀ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ ਖੋਜ ਐਲਗੋਰਿਦਮ ਦੁਆਰਾ ਹਰ ਪਾਸੇ ਨੂੰ ਇੱਕ-ਇੱਕ ਕਰਕੇ ਜਾਂ ਪਾਸੇਜ਼ ਦੇ ਸੈੱਟ ਨੂੰ ਇਕੱਠੇ ਆਟੋ-ਟਿਊਨ ਕਰਦਾ ਹੈ।

#### Olive ਦੇ ਫਾਇਦੇ

- ਗ੍ਰਾਫ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ, ਕੰਪ੍ਰੈਸ਼ਨ ਅਤੇ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਲਈ ਵੱਖ-ਵੱਖ ਤਕਨੀਕਾਂ ਨਾਲ ਹੱਥ-ਉੱਪਰ ਅਨੁਭਵ ਦੇ ਨਾਲ ਆਜ਼ਮਾਇਸ਼ ਅਤੇ ਗਲਤੀ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ **ਤਣਾਅ ਅਤੇ ਸਮਾਂ ਘਟਾਓ**। ਆਪਣੀਆਂ ਗੁਣਵੱਤਾ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਪਾਬੰਦੀਆਂ ਦਿਓ ਅਤੇ Olive ਨੂੰ ਤੁਹਾਡੇ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮਾਡਲ ਲੱਭਣ ਦਿਓ।
- **40+ ਬਣਾਵਟੀ ਮਾਡਲ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਕੌਮਪੋਨੈਂਟਸ** ਜੋ ਕਿ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ, ਕੰਪ੍ਰੈਸ਼ਨ, ਗ੍ਰਾਫ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਵਿੱਚ ਕੱਟੇਧਾਰ ਤਕਨੀਕਾਂ ਨੂੰ ਕਵਰ ਕਰਦੇ ਹਨ।
- ਆਮ ਮਾਡਲ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਟਾਸਕਾਂ ਲਈ **ਇਜ਼ੀ-ਟੂ-ਯੂਜ਼ CLI**। ਉਦਾਹਰਣ ਲਈ, olive quantize, olive auto-opt, olive finetune।
- ਮਾਡਲ ਪੈਕੇਜਿੰਗ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਬਿਲਟ-ਇਨ।
- **ਮਲਟੀ LoRA ਸਰਵਿੰਗ** ਲਈ ਮਾਡਲ ਤਿਆਰ ਕਰਨ ਦੀ ਸਮਰਥਾ।
- YAML/JSON ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਕਫਲੋ ਬਣਾਓ ਤਾਂ ਜੋ ਮਾਡਲ ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਟਾਸਕਾਂ ਨੂੰ ਵਿਵਸਥਿਤ ਕੀਤਾ ਜਾ ਸਕੇ।
- **Hugging Face** ਅਤੇ **Azure AI** ਦੇ ਨਾਲ ਇੰਟਿਗ੍ਰੇਸ਼ਨ।
- ਖਰਚੇ **ਬਚਾਉਣ ਲਈ** ਬਣਾਵਟੀ **ਕੈਸ਼ਿੰਗ** ਮਕੈਨਿਜ਼ਮ।

## ਲੈਬ ਨਿਰਦੇਸ਼

> [!NOTE]
> ਕਿਰਪਾ ਕਰਕੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਆਪਣਾ Azure AI ਹੱਬ ਅਤੇ ਪ੍ਰਾਜੈਕਟ ਪ੍ਰੋਵਿਜ਼ਨ ਕੀਤਾ ਹੈ ਅਤੇ ਆਪਣਾ A100 ਕੰਪਿਊਟ ਸੈੱਟਅੱਪ ਕੀਤਾ ਹੈ ਜਿਵੇਂ ਕਿ ਲੈਬ 1 ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ।

### ਚਰਣ 0: ਆਪਣੇ Azure AI ਕੰਪਿਊਟ ਨਾਲ ਜੁੜੋ

ਤੁਸੀਂ **VS Code** ਦੇ ਰਿਮੋਟ ਫੀਚਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ Azure AI ਕੰਪਿਊਟ ਨਾਲ ਜੁੜੋਗੇ।

1. ਆਪਣੀ **VS Code** ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ ਖੋਲ੍ਹੋ:
1. **Shift+Ctrl+P** ਦੀ ਵਰਤੋਂ ਕਰਕੇ **ਕਮਾਂਡ ਪੈਲਟ** ਖੋਲ੍ਹੋ।
1. ਕਮਾਂਡ ਪੈਲਟ ਵਿੱਚ **AzureML - remote: Connect to compute instance in New Window** ਲੱਭੋ।
1. ਕਮਾਂਡ ਪੈਲਟ ਵਿੱਚ ਦਿੱਤੇ ਗਏ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਇਸ ਵਿੱਚ ਤੁਹਾਡੀ Azure Subscription, Resource Group, Project ਅਤੇ Compute name ਚੁਣਨਾ ਸ਼ਾਮਲ ਹੋਵੇਗਾ ਜੋ ਤੁਸੀਂ ਲੈਬ 1 ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਸੀ।
1. ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ Azure ML ਕੰਪਿਊਟ ਨਾਲ ਜੁੜਦੇ ਹੋ, ਤਾਂ ਇਹ **Visual Code ਦੇ ਖੱਬੇ ਹੇਠਲੇ ਹਿੱਸੇ** ਵਿੱਚ ਦਿਖਾਈ ਦੇਵੇਗਾ `><Azure ML: Compute Name`

### ਚਰਣ 1: ਇਸ ਰਿਪੋ ਨੂੰ ਕਲੋਨ ਕਰੋ

VS Code ਵਿੱਚ, ਤੁਸੀਂ **Ctrl+J** ਨਾਲ ਨਵਾਂ ਟਰਮੀਨਲ ਖੋਲ੍ਹ ਸਕਦੇ ਹੋ ਅਤੇ ਇਸ ਰਿਪੋ ਨੂੰ ਕਲੋਨ ਕਰ ਸਕਦੇ ਹੋ:

ਟਰਮੀਨਲ ਵਿੱਚ ਤੁਹਾਨੂੰ ਇਹ ਪ੍ਰੋਮਪਟ ਦਿਖਾਈ ਦੇਵੇਗਾ

```
azureuser@computername:~/cloudfiles/code$ 
```
ਸੋਲੂਸ਼ਨ ਕਲੋਨ ਕਰੋ

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### ਚਰਣ 2: ਫੋਲਡਰ VS Code ਵਿੱਚ ਖੋਲ੍ਹੋ

ਸੰਬੰਧਿਤ ਫੋਲਡਰ ਵਿੱਚ VS Code ਖੋਲ੍ਹਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ, ਜੋ ਇੱਕ ਨਵੀਂ ਵਿੰਡੋ ਖੋਲ੍ਹੇਗਾ:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

ਵਿਕਲਪਕ ਤੌਰ ਤੇ, ਤੁਸੀਂ **File** > **Open Folder** ਚੁਣ ਕੇ ਫੋਲਡਰ ਖੋਲ੍ਹ ਸਕਦੇ ਹੋ।

### ਚਰਣ 3: Dependencies

Azure AI ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਵਿੱਚ VS Code ਦੇ ਟਰਮੀਨਲ ਵਿੰਡੋ (ਸੁਝਾਅ: **Ctrl+J**) ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾਓ ਤਾਂ ਜੋ Dependencies ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਜਾ ਸਕਣ:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> ਸਾਰੀਆਂ Dependencies ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਵਿੱਚ ਲਗਭਗ ~5 ਮਿੰਟ ਲੱਗਣਗੇ।

ਇਸ ਲੈਬ ਵਿੱਚ ਤੁਸੀਂ ਮਾਡਲਾਂ ਨੂੰ Azure AI ਮਾਡਲ ਕੈਟਾਲੌਗ ਵਿੱਚ ਡਾਊਨਲੋਡ ਅਤੇ ਅੱਪਲੋਡ ਕਰੋਗੇ। ਤਾਂ ਜੋ ਤੁਸੀਂ ਮਾਡਲ ਕੈਟਾਲੌਗ ਤੱਕ ਪਹੁੰਚ ਸਕੋ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ Azure ਵਿੱਚ ਲੌਗਇਨ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

```bash
az login
```

> [!NOTE]
> ਲੌਗਇਨ ਸਮੇਂ ਤੁਹਾਨੂੰ ਆਪਣੀ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣਨ ਲਈ ਕਿਹਾ ਜਾਵੇਗਾ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਇਸ ਲੈਬ ਲਈ ਪ੍ਰਦਾਨ ਕੀਤੀ ਗਈ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨੂੰ ਸੈੱਟ ਕਰਦੇ ਹੋ।

### ਚਰਣ 4: Olive ਕਮਾਂਡ ਚਲਾਓ

Azure AI ਕੰਪਿਊਟ ਇੰਸਟੈਂਸ ਵਿੱਚ VS Code ਦੇ ਟਰਮੀਨਲ ਵਿੰਡੋ (ਸੁਝਾਅ: **Ctrl+J**) ਖੋਲ੍ਹੋ ਅਤੇ ਯਕੀਨੀ ਬਣਾਓ ਕਿ `olive-ai` ਕੋਂਡਾ ਐਨਵਾਇਰਮੈਂਟ ਐਕਟੀਵੇਟ ਕੀਤਾ ਹੋਇਆ ਹੈ:

```bash
conda activate olive-ai
```

ਫਿਰ, ਹੇਠਾਂ ਦਿੱਤੇ Olive ਕਮਾਂਡ ਕਮਾਂਡ ਲਾਈਨ ਵਿੱਚ ਚਲਾਓ।

1. **ਡਾਟਾ ਦੀ ਜਾਂਚ ਕਰੋ:** ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ, ਤੁਸੀਂ Phi-3.5-Mini ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰ ਰਹੇ ਹੋ ਤਾਂ ਜੋ ਇਹ ਯਾਤਰਾ ਨਾਲ ਜੁੜੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਮਾਹਰ ਹੋਵੇ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਡਾਟਾਸੈਟ ਦੇ ਪਹਿਲੇ ਕੁਝ ਰਿਕਾਰਡ ਦਿਖਾਉਂਦਾ ਹੈ, ਜੋ JSON ਲਾਈਨਜ਼ ਫਾਰਮੈਟ ਵਿੱਚ ਹਨ:

    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **ਮਾਡਲ ਕਵਾਂਟਾਈਜ਼ ਕਰੋ:** ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ ਕਵਾਂਟਾਈਜ਼ ਕਰਦੇ ਹੋ ਜੋ Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ ਨਾਮਕ ਤਕਨੀਕ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। AWQ ਮਾਡਲ ਦੇ ਵਜ਼ਨਾਂ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਦਾ ਹੈ ਜਦੋਂ ਇਹ ਇਨਫਰੈਂਸ ਦੌਰਾਨ ਪ੍ਰਾਪਤ ਹੋਣ ਵਾਲੀਆਂ ਐਕਟਿਵੇਸ਼ਨਜ਼ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦਾ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਪ੍ਰਕਿਰਿਆ ਐਕਟਿਵੇਸ਼ਨਜ਼ ਵਿੱਚ ਅਸਲ ਡਾਟਾ ਡਿਸਟ੍ਰਿਬਿਊਸ਼ਨ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਰਵਾਇਤੀ ਵਜ਼ਨ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਵਿਧੀਆਂ ਦੇ ਮੁਕਾਬਲੇ ਮਾਡਲ ਦੀ ਸ਼ੁੱਧਤਾ ਨੂੰ ਬਿਹਤਰ ਢੰਗ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਪੂਰਾ ਕਰਨ ਵਿੱਚ **~8 ਮਿੰਟ** ਲੱਗਦੇ ਹਨ, ਜੋ **ਮਾਡਲ ਦਾ ਆਕਾਰ ~7.5GB ਤੋਂ ~2.5GB ਤੱਕ ਘਟਾ ਦਿੰਦਾ ਹੈ**।

    ਇਸ ਲੈਬ ਵਿੱਚ, ਅਸੀਂ ਤੁਹਾਨੂੰ Hugging Face ਤੋਂ ਮਾਡਲ ਇਨਪੁਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਦਿਖਾ ਰਹੇ ਹਾਂ (ਉਦਾਹਰਣ ਲਈ: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` ਕਮਾਂਡ ਕਵਾਂਟਾਈਜ਼ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਦਾ ਹੈ। ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ ਬਿਹਤਰ ਸਹੀਤਾ ਦਿੰਦਾ ਹੈ ਕਿਉਂਕਿ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪ੍ਰਕਿਰਿਆ ਕੁਝ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਨੁਕਸਾਨ ਨੂੰ ਵਾਪਸ ਪ੍ਰਾਪਤ ਕਰ ਲੈਂਦੀ ਹੈ।

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    ਫਾਈਨ-ਟਿਊਨਿੰਗ (100 ਸਟੈਪਾਂ ਨਾਲ) ਪੂਰਾ ਕਰਨ ਵਿੱਚ **~6 ਮਿੰਟ** ਲੱਗਦੇ ਹਨ।

1. **ਆਪਟੀਮਾਈਜ਼ ਕਰੋ:** ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਦੇ ਬਾਅਦ, ਹੁਣ ਤੁਸੀਂ Olive ਦੇ `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` ਆਰਗਯੂਮੈਂਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਡਲ ਨੂੰ ਆਪਟੀਮਾਈਜ਼ ਕਰਦੇ ਹੋ - ਪਰ ਇਸ ਲੈਬ ਦੇ ਉਦੇਸ਼ਾਂ ਲਈ ਅਸੀਂ CPU ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ।

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    ਆਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਪੂਰਾ ਕਰਨ ਵਿੱਚ **~5 ਮਿੰਟ** ਲੱਗਦੇ ਹਨ।

### ਚਰਣ 5: ਮਾਡਲ ਇਨਫਰੈਂਸ ਦਾ ਛੋਟਾ ਟੈਸਟ

ਮਾਡਲ ਦੇ ਇਨਫਰੈਂਸ ਨੂੰ ਟੈਸਟ ਕਰਨ ਲਈ, ਆਪਣੇ ਫੋਲਡਰ ਵਿੱਚ **app.py** ਨਾਮਕ ਇੱਕ ਪਾਇਥਨ ਫਾਈਲ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਕਾਪੀ-ਪੇਸਟ ਕਰੋ:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

ਕੋਡ ਚਲਾਓ:

```bash
python app.py
```

### ਚਰਣ 6: ਮਾਡਲ ਨੂੰ Azure AI 'ਤੇ ਅੱਪਲੋਡ ਕਰੋ

ਮਾਡਲ ਨੂੰ ਇੱਕ Azure AI ਮਾਡਲ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਅੱਪਲੋਡ ਕਰਨ ਨਾਲ ਮਾਡਲ ਤੁਹਾਡੇ ਵਿਕਾਸ ਟੀਮ ਦੇ ਹੋਰ ਮੈਂਬਰਾਂ ਨਾਲ ਸਾਂਝਾ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਮਾਡਲ ਦੇ ਵਰਜਨ ਕੰਟਰੋਲ ਨੂੰ ਵੀ ਹੈਂਡਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਮਾਡਲ ਨੂੰ ਅੱਪਲੋਡ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

> [!NOTE]
> `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup" ਅਤੇ Azure AI Project name ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ 

```
az ml workspace show
```

ਜਾਂ +++ai.azure.com+++ ਤੇ ਜਾ ਕੇ **management center** **project** **overview** ਚੁਣੋ।

`{}` ਪਲੇਸਹੋਲਡਰ ਨੂੰ ਆਪਣੇ ਰਿਸੋਰਸ ਗਰੁੱਪ ਅਤੇ Azure AI ਪ੍ਰਾਜੈਕਟ ਦੇ ਨਾਮ ਨਾਲ ਅਪਡੇਟ ਕਰੋ।

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
ਤੁਸੀਂ ਫਿਰ ਆਪਣਾ ਅੱਪਲੋਡ ਕੀਤਾ ਮਾਡਲ ਵੇਖ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੇ ਮਾਡਲ ਨੂੰ https://ml.azure.com/model/list 'ਤੇ ਡਿਪਲੌਇ ਕਰ ਸਕਦੇ ਹੋ।

**ਅਸਵੀਕਾਰਨਯੋਗ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।