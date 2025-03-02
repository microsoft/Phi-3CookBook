## Kaito ile İnce Ayar

[Kaito](https://github.com/Azure/kaito), bir Kubernetes kümesinde AI/ML çıkarım modeli dağıtımını otomatikleştiren bir operatördür.

Kaito, sanal makine altyapıları üzerine inşa edilen çoğu yaygın model dağıtım yöntemine kıyasla şu temel farklılıklara sahiptir:

- Model dosyalarını konteyner imajlarıyla yönetir. Model kütüphanesini kullanarak çıkarım çağrıları gerçekleştiren bir HTTP sunucusu sağlar.
- GPU donanımına uyum sağlamak için dağıtım parametrelerini ayarlamaktan kaçınarak önceden ayarlanmış konfigürasyonlar sunar.
- Model gereksinimlerine göre GPU düğümlerini otomatik olarak sağlar.
- Lisans izin verdiği sürece büyük model imajlarını Microsoft Container Registry (MCR) üzerinde barındırır.

Kaito kullanarak Kubernetes'te büyük AI çıkarım modellerini devreye alma iş akışı büyük ölçüde basitleştirilir.

## Mimari

Kaito, klasik Kubernetes Özel Kaynak Tanımı (CRD)/kontrolcü tasarım modelini takip eder. Kullanıcı, GPU gereksinimlerini ve çıkarım özelliklerini tanımlayan bir `workspace` özel kaynağını yönetir. Kaito kontrolcüleri, `workspace` özel kaynağını uzlaştırarak dağıtımı otomatikleştirir.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito mimarisi" alt="Kaito mimarisi">
</div>

Yukarıdaki şekil, Kaito'nun mimari genel görünümünü sunar. Başlıca bileşenleri şunlardır:

- **Çalışma alanı kontrolcüsü**: `workspace` özel kaynağını uzlaştırır, düğüm otomatik sağlama işlemini tetiklemek için `machine` (aşağıda açıklanmıştır) özel kaynaklarını oluşturur ve model ön ayar konfigürasyonlarına göre çıkarım iş yükünü (`deployment` veya `statefulset`) oluşturur.
- **Düğüm sağlayıcı kontrolcüsü**: Bu kontrolcünün adı [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) içinde *gpu-provisioner* olarak geçer. Çalışma alanı kontrolcüsüyle etkileşim kurmak için [Karpenter](https://sigs.k8s.io/karpenter) kaynaklı `machine` CRD'sini kullanır. Azure Kubernetes Service (AKS) API'leriyle entegre olarak AKS kümesine yeni GPU düğümleri ekler. 
> Not: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner), açık kaynaklı bir bileşendir. Eğer [Karpenter-core](https://sigs.k8s.io/karpenter) API'lerini destekliyorlarsa, diğer kontrolcülerle değiştirilebilir.

## Genel Bakış Videosu 
[Kaito Demoyu İzleyin](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Kurulum

Kurulum rehberi için lütfen [buraya](https://github.com/Azure/kaito/blob/main/docs/installation.md) göz atın.

## Hızlı Başlangıç

Kaito'yu kurduktan sonra, bir ince ayar hizmeti başlatmak için aşağıdaki komutlar denenebilir.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
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
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
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
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

Çalışma alanı durumu, aşağıdaki komut çalıştırılarak izlenebilir. WORKSPACEREADY sütunu `True` olduğunda, model başarıyla dağıtılmıştır.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Daha sonra, çıkarım hizmetinin küme IP'si bulunabilir ve küme içindeki hizmet uç noktasını test etmek için geçici bir `curl` podu kullanılabilir.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.