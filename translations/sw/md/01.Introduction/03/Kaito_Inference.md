## Utoaji wa Inference na Kaito

[Kaito](https://github.com/Azure/kaito) ni opereta inayorahisisha utumaji wa mifano ya AI/ML ya inference kwenye kundi la Kubernetes.

Kaito ina tofauti kuu zifuatazo ikilinganishwa na mbinu nyingi za kawaida za utumaji wa mifano zilizojengwa juu ya miundombinu ya mashine za kawaida:

- Kusimamia faili za mifano kwa kutumia picha za kontena. Seva ya http hutolewa ili kufanya miito ya inference kwa kutumia maktaba ya mfano.
- Kuepuka kurekebisha vigezo vya utumaji ili kuendana na vifaa vya GPU kwa kutoa usanidi uliowekwa tayari.
- Kuongeza noding GPU kiotomatiki kulingana na mahitaji ya mfano.
- Kuhifadhi picha kubwa za mifano kwenye Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kwa kutumia Kaito, mchakato wa kuanzisha mifano mikubwa ya inference ya AI kwenye Kubernetes umerahisishwa kwa kiasi kikubwa.

## Usanifu

Kaito hufuata muundo wa kawaida wa Kubernetes Custom Resource Definition (CRD)/controller. Mtumiaji husimamia rasilimali maalum ya `workspace` ambayo inaelezea mahitaji ya GPU na maelezo ya inference. Vidhibiti vya Kaito vitafanya utumaji kiotomatiki kwa kuoanisha rasilimali maalum ya `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Mchoro hapo juu unaonyesha muhtasari wa usanifu wa Kaito. Vipengele vyake vikuu vinajumuisha:

- **Workspace controller**: Inaoanisha rasilimali maalum ya `workspace`, huunda rasilimali maalum za `machine` (zinazoelezwa hapa chini) ili kuchochea utoaji wa noding kiotomatiki, na huunda mzigo wa kazi wa inference (`deployment` au `statefulset`) kulingana na usanidi wa mfano uliowekwa tayari.
- **Node provisioner controller**: Jina la kidhibiti hiki ni *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Hutumia CRD ya `machine` inayotokana na [Karpenter](https://sigs.k8s.io/karpenter) kuwasiliana na workspace controller. Inaunganishwa na Azure Kubernetes Service (AKS) APIs kuongeza noding mpya za GPU kwenye kundi la AKS.
> Kumbuka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni kipengele kilichofunguliwa kwa umma. Inaweza kubadilishwa na vidhibiti vingine ikiwa vinaunga mkono APIs za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Usakinishaji

Tafadhali angalia mwongozo wa usakinishaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mwanzo wa Haraka wa Inference Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Hali ya workspace inaweza kufuatiliwa kwa kutumia amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, mfano umesakinishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata ip ya kundi ya huduma ya inference na kutumia pod ya muda `curl` kujaribu mwisho wa huduma kwenye kundi.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Mwanzo wa Haraka wa Inference Phi-3 na Adapters

Baada ya kusakinisha Kaito, mtu anaweza kujaribu amri zifuatazo kuanzisha huduma ya inference.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Hali ya workspace inaweza kufuatiliwa kwa kutumia amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, mfano umesakinishwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Baadaye, mtu anaweza kupata ip ya kundi ya huduma ya inference na kutumia pod ya muda `curl` kujaribu mwisho wa huduma kwenye kundi.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.