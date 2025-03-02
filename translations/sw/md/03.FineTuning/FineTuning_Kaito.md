## Kuboresha Ufanisi na Kaito

[Kaito](https://github.com/Azure/kaito) ni opereta anayerahisisha uwekaji wa mifano ya utabiri ya AI/ML kwenye klasta ya Kubernetes.

Kaito ina tofauti kuu zifuatazo ikilinganishwa na mbinu nyingi za kawaida za uwekaji wa mifano ambazo zinategemea miundombinu ya mashine za kawaida:

- Kusimamia faili za mfano kwa kutumia picha za kontena. Seva ya http hutolewa ili kufanya miito ya utabiri kwa kutumia maktaba ya mfano.
- Kuepuka kurekebisha vigezo vya uwekaji ili kuendana na vifaa vya GPU kwa kutoa mipangilio iliyowekwa tayari.
- Kuongeza kiotomatiki nodi za GPU kulingana na mahitaji ya mfano.
- Kuhifadhi picha kubwa za mfano kwenye Microsoft Container Registry (MCR) ya umma ikiwa leseni inaruhusu.

Kwa kutumia Kaito, mchakato wa kuingiza mifano mikubwa ya utabiri wa AI kwenye Kubernetes unarahisishwa kwa kiasi kikubwa.

## Muundo

Kaito hufuata muundo wa kawaida wa Kubernetes wa Custom Resource Definition (CRD)/controller. Mtumiaji husimamia rasilimali maalum ya `workspace` ambayo inaelezea mahitaji ya GPU na vipimo vya utabiri. Vidhibiti vya Kaito vitahakikisha uwekaji kwa kusawazisha rasilimali maalum ya `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Muundo wa Kaito" alt="Muundo wa Kaito">
</div>

Mchoro hapo juu unaonyesha muhtasari wa muundo wa Kaito. Vipengele vyake vikuu ni:

- **Kidhibiti cha Workspace**: Hurekebisha rasilimali maalum ya `workspace`, huunda rasilimali maalum za `machine` (zilizoelezwa hapa chini) ili kuchochea uongezaji wa nodi kiotomatiki, na huunda mzigo wa utabiri (`deployment` au `statefulset`) kulingana na mipangilio ya mfano iliyowekwa tayari.
- **Kidhibiti cha Node Provisioner**: Jina la kidhibiti hiki ni *gpu-provisioner* katika [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Hutumia CRD ya `machine` inayotokana na [Karpenter](https://sigs.k8s.io/karpenter) kuwasiliana na kidhibiti cha workspace. Kinaunganishwa na Azure Kubernetes Service (AKS) APIs ili kuongeza nodi mpya za GPU kwenye klasta ya AKS.  
> Kumbuka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ni sehemu iliyo wazi kwa umma. Inaweza kubadilishwa na vidhibiti vingine ikiwa vinasaidia APIs za [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video ya Muhtasari  
[Tazama Demo ya Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Ufungaji

Tafadhali angalia mwongozo wa usakinishaji [hapa](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kuanza Haraka

Baada ya kusakinisha Kaito, mtu anaweza kujaribu amri zifuatazo ili kuanzisha huduma ya kuboresha ufanisi.

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

Hali ya workspace inaweza kufuatiliwa kwa kuendesha amri ifuatayo. Wakati safu ya WORKSPACEREADY inakuwa `True`, mfano umewekwa kwa mafanikio.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Kisha, mtu anaweza kupata ip ya klasta ya huduma ya utabiri na kutumia pod ya muda ya `curl` kujaribu endpoint ya huduma ndani ya klasta.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa maelezo muhimu, inashauriwa kutumia huduma za wataalamu wa tafsiri ya kibinadamu. Hatutawajibika kwa kutokuelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.