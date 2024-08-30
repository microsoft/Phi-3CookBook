# Phi-3のハードウェアサポート

Microsoft Phi-3はONNX Runtime用に最適化されており、Windows DirectMLをサポートしています。GPU、CPU、さらにはモバイルデバイスなど、さまざまなハードウェアタイプでうまく動作します。

## デバイスハードウェア
具体的には、サポートされているハードウェアには次のものが含まれます：

- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB (CUDA)
- CPU SKU: Standard F64s v2 (64 vCPUs, 128 GiBメモリ)

## モバイルSKU

- Android - Samsung Galaxy S21
- Apple iPhone 14またはそれ以上のA16/A17プロセッサ

## Phi-3ハードウェア仕様

- 必要な最小構成
- Windows: DirectX 12対応のGPUと最小4GBのRAM

CUDA: NVIDIA GPU with Compute Capability >= 7.02

![HardwareSupport](../../imgs/00/phi3hardware.png)

## 複数のGPUでのonnxruntimeの実行

現在利用可能なPhi-3 ONNXモデルは1つのGPUのみを対象としています。Phi-3モデルでマルチGPUをサポートすることは可能ですが、2つのGPUを使用したORTは2つのORTインスタンスと比較してより高いスループットを保証するものではありません。

[Build 2024のGenAI ONNXチーム](https://youtu.be/WLW4SE8M9i8?si=EtG04UwDvcjunyfC)は、Phiモデルに対してマルチGPUではなくマルチインスタンスを有効にしたことを発表しました。

現在、これにより、次のようにCUDA_VISIBLE_DEVICES環境変数を使用して1つのonnnxruntimeまたはonnxruntime-genaiインスタンスを実行できます。

```Python
CUDA_VISIBLE_DEVICES=0 python infer.py
CUDA_VISIBLE_DEVICES=1 python infer.py
```

[Azure AI Studio](https://ai.azure.com)でPhi-3をさらに探索してください。
