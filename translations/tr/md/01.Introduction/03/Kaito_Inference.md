## Kaito ile Çıkarım 

[Kaito](https://github.com/Azure/kaito), Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerine inşa edilen çoğu yaygın model dağıtım yöntemine kıyasla aşağıdaki temel farklara sahiptir:

- Model dosyalarını konteyner imajları kullanarak yönetir. Model kütüphanesini kullanarak çıkarım çağrıları yapmak için bir HTTP sunucusu sağlar.
- Önceden ayarlanmış yapılandırmalar sunarak GPU donanımına uygun dağıtım parametrelerini ayarlama ihtiyacını ortadan kaldırır.
- Model gereksinimlerine göre otomatik GPU düğüm sağlama yapar.
- Lisans izin verdiği sürece büyük model imajlarını Microsoft Container Registry (MCR) üzerinde barındırır.

Kaito kullanılarak Kubernetes'te büyük AI çıkarım modellerinin benimsenme süreci büyük ölçüde basitleştirilmiştir.

## Mimari

Kaito, klasik Kubernetes Özel Kaynak Tanımı (CRD)/kontrolör tasarım desenini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım özelliklerini tanımlayan bir `workspace` özel kaynağı yönetir. Kaito kontrolörleri, `workspace` özel kaynağını uzlaştırarak dağıtımı otomatikleştirir.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito mimarisi" alt="Kaito mimarisi">
</div>

Yukarıdaki şekil, Kaito mimarisinin genel görünümünü sunmaktadır. Ana bileşenleri şunlardır:

- **Workspace kontrolörü**: `workspace` özel kaynağını uzlaştırır, düğüm otomatik sağlama işlemini tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynaklarını oluşturur ve modelin ön ayar yapılandırmalarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Düğüm sağlayıcı kontrolörü**: Bu kontrolör, [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak adlandırılır. Workspace kontrolörü ile etkileşimde bulunmak için [Karpenter](https://sigs.k8s.io/karpenter) kaynaklı `machine` CRD'sini kullanır. Azure Kubernetes Service (AKS) API'leri ile entegre olarak AKS kümesine yeni GPU düğümleri ekler.
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner), açık kaynaklı bir bileşendir. [Karpenter-core](https://sigs.k8s.io/karpenter) API'lerini destekliyorsa başka kontrolörlerle değiştirilebilir.

## Kurulum

Kurulum rehberine [buradan](https://github.com/Azure/kaito/blob/main/docs/installation.md) ulaşabilirsiniz.

## Phi-3 Çıkarımı Hızlı Başlangıç
[Phi-3 Çıkarımı Örnek Kod](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Workspace durumunu aşağıdaki komutu çalıştırarak takip edebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Daha sonra, çıkarım hizmetinin küme IP'sini bulabilir ve kümedeki hizmet uç noktasını test etmek için geçici bir `curl` podu kullanabilirsiniz.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adaptörlerle Phi-3 Çıkarımı Hızlı Başlangıç

Kaito kurulduktan sonra, bir çıkarım hizmeti başlatmak için aşağıdaki komutları deneyebilirsiniz.

[Adaptörlerle Phi-3 Çıkarımı Örnek Kod](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Workspace durumunu aşağıdaki komutu çalıştırarak takip edebilirsiniz. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmış demektir.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Daha sonra, çıkarım hizmetinin küme IP'sini bulabilir ve kümedeki hizmet uç noktasını test etmek için geçici bir `curl` podu kullanabilirsiniz.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Feragatname**:  
Bu belge, yapay zeka tabanlı makine çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama konusunda sorumluluk kabul edilmez.