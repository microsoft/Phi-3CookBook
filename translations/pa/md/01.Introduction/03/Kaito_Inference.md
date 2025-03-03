## ਕੈਟੋ ਨਾਲ ਅਨੁਮਾਨ ਲਗਾਉਣਾ

[Kaito](https://github.com/Azure/kaito) ਇੱਕ ਓਪਰੇਟਰ ਹੈ ਜੋ Kubernetes ਕਲਸਟਰ ਵਿੱਚ AI/ML ਅਨੁਮਾਨ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦਾ ਹੈ।

ਕੈਟੋ ਦੇ ਹੇਠ ਲਿਖੇ ਮੁੱਖ ਅੰਤਰ ਹਨ ਜਿਹੜੇ ਜ਼ਿਆਦਾਤਰ ਪ੍ਰਚਲਿਤ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਤਰੀਕਿਆਂ ਨਾਲ ਤੁਲਨਾ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਜੋ ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਢਾਂਚਿਆਂ 'ਤੇ ਬਣੇ ਹੁੰਦੇ ਹਨ:

- ਮਾਡਲ ਫਾਈਲਾਂ ਨੂੰ ਕੰਟੇਨਰ ਇਮੇਜਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ। ਇੱਕ HTTP ਸਰਵਰ ਮੁਹੱਈਆ ਕੀਤਾ ਗਿਆ ਹੈ ਜੋ ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਮਾਨ ਕਾਲਾਂ ਕਰਦਾ ਹੈ।
- ਪ੍ਰੀ-ਸੈਟ ਸੰਰਚਨਾਵਾਂ ਮੁਹੱਈਆ ਕਰਕੇ GPU ਹਾਰਡਵੇਅਰ ਲਈ ਡਿਪਲੋਇਮੈਂਟ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਟਿਊਨ ਕਰਨ ਤੋਂ ਬਚੋ।
- ਮਾਡਲ ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ ਦੇ ਅਧਾਰ 'ਤੇ GPU ਨੋਡਾਂ ਦੀ ਆਟੋਮੈਟਿਕ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ।
- ਜੇ ਲਾਇਸੈਂਸ ਦੀ ਆਗਿਆ ਹੋਵੇ, ਤਾਂ ਵੱਡੇ ਮਾਡਲ ਇਮੇਜਾਂ ਨੂੰ Microsoft Container Registry (MCR) ਵਿੱਚ ਹੋਸਟ ਕਰੋ।

ਕੈਟੋ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, Kubernetes ਵਿੱਚ ਵੱਡੇ AI ਅਨੁਮਾਨ ਮਾਡਲਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ ਦਾ ਵਰਕਫਲੋ ਕਾਫ਼ੀ ਹੱਦ ਤੱਕ ਸਧਾਰਨ ਬਣ ਜਾਂਦਾ ਹੈ।


## ਆਰਕੀਟੈਕਚਰ

ਕੈਟੋ ਪਰੰਪਰਾਗਤ Kubernetes Custom Resource Definition(CRD)/ਕੰਟਰੋਲਰ ਡਿਜ਼ਾਇਨ ਪੈਟਰਨ ਦਾ ਪਾਲਣ ਕਰਦਾ ਹੈ। ਯੂਜ਼ਰ ਇੱਕ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਪ੍ਰਬੰਧਿਤ ਕਰਦਾ ਹੈ ਜੋ GPU ਦੀਆਂ ਜ਼ਰੂਰਤਾਂ ਅਤੇ ਅਨੁਮਾਨ ਵਿਸ਼ੇਸ਼ਤਾ ਨੂੰ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। ਕੈਟੋ ਕੰਟਰੋਲਰਾਂ ਦੁਆਰਾ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕੰਸਾਈਲ ਕਰਕੇ ਡਿਪਲੋਇਮੈਂਟ ਨੂੰ ਆਟੋਮੇਟ ਕਰਦੇ ਹਨ।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ਉਪਰੋਕਤ ਚਿੱਤਰ ਕੈਟੋ ਆਰਕੀਟੈਕਚਰ ਦਾ ਜ਼ਾਇਜ਼ਾ ਪੇਸ਼ ਕਰਦਾ ਹੈ। ਇਸ ਦੇ ਮੁੱਖ ਹਿੱਸੇ ਸ਼ਾਮਲ ਹਨ:

- **ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ**: ਇਹ `workspace` ਕਸਟਮ ਰਿਸੋਰਸ ਨੂੰ ਰੀਕੰਸਾਈਲ ਕਰਦਾ ਹੈ, `machine` (ਹੇਠ ਵਿਆਖਿਆ ਕੀਤੀ ਗਈ) ਕਸਟਮ ਰਿਸੋਰਸ ਬਣਾਉਂਦਾ ਹੈ ਜੋ ਨੋਡ ਦੀ ਆਟੋ ਪ੍ਰੋਵਿਜ਼ਨਿੰਗ ਨੂੰ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ, ਅਤੇ ਮਾਡਲ ਪ੍ਰੀਸੈਟ ਸੰਰਚਨਾਵਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਅਨੁਮਾਨ ਵਰਕਲੋਡ (`deployment` ਜਾਂ `statefulset`) ਬਣਾਉਂਦਾ ਹੈ।
- **ਨੋਡ ਪ੍ਰੋਵਿਜ਼ਨਰ ਕੰਟਰੋਲਰ**: ਇਸ ਕੰਟਰੋਲਰ ਦਾ ਨਾਮ [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) ਵਿੱਚ *gpu-provisioner* ਹੈ। ਇਹ [Karpenter](https://sigs.k8s.io/karpenter) ਤੋਂ ਆਏ `machine` CRD ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਕਸਪੇਸ ਕੰਟਰੋਲਰ ਨਾਲ ਸੰਚਾਰ ਕਰਦਾ ਹੈ। ਇਹ Azure Kubernetes Service(AKS) APIs ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ AKS ਕਲਸਟਰ ਵਿੱਚ ਨਵੇਂ GPU ਨੋਡ ਜੋੜੇ ਜਾ ਸਕਣ।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਘਟਕ ਹੈ। ਜੇ ਹੋਰ ਕੰਟਰੋਲਰ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ਨੂੰ ਸਹਾਰਾ ਦਿੰਦੇ ਹਨ, ਤਾਂ ਇਸਨੂੰ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਇੰਸਟਾਲੇਸ਼ਨ

ਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲੇਸ਼ਨ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ [ਇੱਥੇ](https://github.com/Azure/kaito/blob/main/docs/installation.md) ਦੇਖੋ।

## ਫੀ-3 ਅਨੁਮਾਨ ਲਈ ਜਲਦੀ ਸ਼ੁਰੂਆਤ
[ਫੀ-3 ਅਨੁਮਾਨ ਲਈ ਨਮੂਨਾ ਕੋਡ](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟ੍ਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਬਣ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੋਇ ਹੋ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲਾ, ਕੋਈ ਵੀ ਅਨੁਮਾਨ ਸਰਵਿਸ ਦਾ ਕਲਸਟਰ IP ਲੱਭ ਸਕਦਾ ਹੈ ਅਤੇ ਕਲਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੌਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## ਐਡਾਪਟਰਾਂ ਨਾਲ ਫੀ-3 ਅਨੁਮਾਨ ਲਈ ਜਲਦੀ ਸ਼ੁਰੂਆਤ

ਕੈਟੋ ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਅਨੁਮਾਨ ਸਰਵਿਸ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੇ ਹੁਕਮਾਂ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।

[ਐਡਾਪਟਰਾਂ ਨਾਲ ਫੀ-3 ਅਨੁਮਾਨ ਲਈ ਨਮੂਨਾ ਕੋਡ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ਵਰਕਸਪੇਸ ਦੀ ਸਥਿਤੀ ਨੂੰ ਹੇਠ ਲਿਖੇ ਕਮਾਂਡ ਚਲਾ ਕੇ ਟ੍ਰੈਕ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਜਦੋਂ WORKSPACEREADY ਕਾਲਮ `True` ਬਣ ਜਾਂਦਾ ਹੈ, ਤਾਂ ਮਾਡਲ ਸਫਲਤਾਪੂਰਵਕ ਡਿਪਲੋਇ ਹੋ ਗਿਆ ਹੈ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

ਅਗਲਾ, ਕੋਈ ਵੀ ਅਨੁਮਾਨ ਸਰਵਿਸ ਦਾ ਕਲਸਟਰ IP ਲੱਭ ਸਕਦਾ ਹੈ ਅਤੇ ਕਲਸਟਰ ਵਿੱਚ ਸਰਵਿਸ ਐਂਡਪੌਇੰਟ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਅਸਥਾਈ `curl` ਪੌਡ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ਅਸਵੀਕਰਤੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।