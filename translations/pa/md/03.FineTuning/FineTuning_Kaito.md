## ਕਾਈਟੋ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ 

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਆਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲਸਟਰ ਵਿੱਚ AI/ML ਇਨਫਰੈਂਸ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਇੰਫਰਾਸਟ੍ਰਕਚਰਾਂ 'ਤੇ ਆਧਾਰਿਤ ਮੁੱਖ ਧਾਰਾ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਤਰੀਕਿਆਂ ਨਾਲ ਤੁਲਨਾ ਕਰਨ 'ਤੇ, ਕਾਈਟੋ ਵਿੱਚ ਹੇਠ ਲਿਖੇ ਮੁੱਖ ਫਰਕ ਹਨ:

- ਮਾਡਲ ਫਾਈਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਇਮੇਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੈਨੇਜ ਕਰੋ। ਇੱਕ HTTP ਸਰਵਰ ਮੁਹੱਈਆ ਕਰਵਾਇਆ ਜਾਂਦਾ ਹੈ ਜੋ ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਨਫਰੈਂਸ ਕਾਲਾਂ ਕਰਦਾ ਹੈ।
- ਪ੍ਰੀਸੈਟ ਕਾਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਰਾਹੀਂ GPU ਹਾਰਡਵੇਅਰ ਲਈ ਡਿਪਲੌਇਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਐਡਜਸਟ ਕਰਨ ਤੋਂ ਬਚਾਓ।
- ਮਾਡਲ ਦੀਆਂ ਲੋੜਾਂ ਦੇ ਆਧਾਰ 'ਤੇ GPU ਨੋਡਸ ਦਾ ਆਟੋ-ਪ੍ਰੋਵਿਜ਼ਨ ਕਰੋ।
- ਜੇ ਲਾਇਸੈਂਸ ਦੀ ਆਗਿਆ ਹੋਵੇ, ਤਾਂ ਵੱਡੀਆਂ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ ਪਬਲਿਕ Microsoft Container Registry (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰੋ।

ਕਾਈਟੋ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਇਨਫਰੈਂਸ ਮਾਡਲਾਂ ਨੂੰ ਅਪਨਾਉਣ ਦੀ ਵਰਕਫਲੋ ਕਾਫੀ ਸਧਾਰਨ ਬਣ ਜਾਂਦੀ ਹੈ।


## ਆਰਕੀਟੈਕਚਰ

ਕਾਈਟੋ ਕਲਾਸਿਕ Kubernetes Custom Resource Definition(CRD)/ਕੰਟਰੋਲਰ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨ ਦੀ ਪਾਲਣਾ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਮੈਨੇਜ ਕਰਦਾ ਹੈ ਜੋ GPU ਦੀਆਂ ਲੋੜਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। ਕਾਈਟੋ ਕੰਟਰੋਲਰਜ਼ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕੌਨਸਾਇਲ ਕਰਕੇ ਡਿਪਲੌਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ਉਪਰੋਕਤ ਚਿੱਤਰ ਕਾਈਟੋ ਦੇ ਆਰਕੀਟੈਕਚਰ ਦਾ ਓਵਰਵਿਊ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਇਸ ਦੇ ਮੁੱਖ ਘਟਕਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ**: ਇਹ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕੌਨਸਾਇਲ ਕਰਦਾ ਹੈ, `machine` (ਹੇਠ ਵਿਆਖਿਆ ਕੀਤੀ ਗਈ ਹੈ) ਕਸਟਮ ਰਿਸੋਰਸ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਨੋਡ ਆਟੋ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ ਨੂੰ ਟ੍ਰਿਗਰ ਕਰਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਸੈਟ ਕਾਨਫਿਗਰੇਸ਼ਨਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਇਨਫਰੈਂਸ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **ਨੋਡ ਪ੍ਰੋਵਿਜ਼ਨਰ ਕੰਟਰੋਲਰ**: ਇਸ ਕੰਟਰੋਲਰ ਦਾ ਨਾਮ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ `machine` CRD ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ ਜੋ [Karpenter](https://sigs.k8s.io/karpenter) ਤੋਂ ਆਈ ਹੈ ਅਤੇ ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ ਨਾਲ ਸੰਚਾਰ ਕਰਦਾ ਹੈ। ਇਹ Azure Kubernetes Service(AKS) APIs ਨਾਲ ਇੰਟੇਗਰੇਟ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ AKS ਕਲਸਟਰ ਵਿੱਚ ਨਵੇਂ GPU ਨੋਡਸ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾ ਸਕਣ।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਕੰਪੋਨੈਂਟ ਹੈ। ਜੇਕਰ ਹੋਰ ਕੰਟਰੋਲਰ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ, ਤਾਂ ਇਸਨੂੰ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਓਵਰਵਿਊ ਵੀਡੀਓ 
[ਕਾਈਟੋ ਡੈਮੋ ਦੇਖੋ](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਗਾਈਡੈਂਸ [ਇੱਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਚੈਕ ਕਰੋ।

## ਕੁਇਕ ਸਟਾਰਟ

ਕਾਈਟੋ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਇੱਕ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਸਰਵਿਸ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

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

ਵਰਕਸਪੇਸ ਸਥਿਤੀ ਨੂੰ ਹੇਠ ਲਿਖੀ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਹੋ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੌਇ ਹੋ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲਾ, ਕੋਈ ਵੀ ਇਨਫਰੈਂਸ ਸਰਵਿਸ ਦਾ ਕਲਸਟਰ IP ਲੱਭ ਸਕਦਾ ਹੈ ਅਤੇ ਕਲਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੌਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ਅਸਵੀਕਾਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਚਤਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।