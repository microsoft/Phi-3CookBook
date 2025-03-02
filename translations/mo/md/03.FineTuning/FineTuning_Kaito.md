## Fine-Tuning miaraka amin'i Kaito

[Kaito](https://github.com/Azure/kaito) dia mpandraharaha manamora ny fampiharana modely AI/ML amin'ny Kubernetes cluster.

Ireto avy ireo tombony lehibe ananan'i Kaito raha oharina amin'ny fomba fampiharana modely mahazatra izay mifototra amin'ny infrastruktiora virtoaly:

- Tantano ny rakitra modely amin'ny alalan'ny sary container. Misy http server izay azo ampiasaina hanaovana antso inference mampiasa ny tranomboky modely.
- Esory ny filàna fanitsiana ny paramètre deployment mba hifanaraka amin'ny fitaovana GPU amin'ny alalan'ny preset configurations.
- Mamorona ho azy GPU nodes mifanaraka amin'ny filàna modely.
- Ampiantrano ireo sary modely lehibe ao amin'ny Microsoft Container Registry (MCR) ho an'ny daholobe raha toa ka manome alalana ny fahazoan-dalana.

Miaraka amin'i Kaito, dia lasa tsotra kokoa ny workflow amin'ny fampidirana modely AI inference lehibe ao amin'ny Kubernetes.


## Rafitra

Kaito dia manaraka ny fomba fanao mahazatra amin'ny Kubernetes Custom Resource Definition (CRD)/controller. Ny mpampiasa dia mitantana `workspace` custom resource izay mamaritra ny filàna GPU sy ny famaritana inference. Ny Kaito controllers no manatanteraka ny deployment amin'ny alalan'ny fandrindrana ny `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ny sary etsy ambony dia mampiseho ny topi-maso momba ny rafitra Kaito. Ny ampahany lehibe ao aminy dia ahitana:

- **Workspace controller**: Io no mandrindra ny `workspace` custom resource, mamorona `machine` (hazavaina etsy ambany) custom resources mba hanombohana ny auto provisioning ny nodes, ary mamorona ny inference workload (`deployment` na `statefulset`) mifototra amin'ny preset configurations modely.
- **Node provisioner controller**: Ny anaran'ity controller ity dia *gpu-provisioner* ao amin'ny [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Izy io dia mampiasa ny `machine` CRD izay niandoha avy amin'ny [Karpenter](https://sigs.k8s.io/karpenter) mba hifandraisana amin'ny workspace controller. Izy io dia mampiditra ny Azure Kubernetes Service (AKS) APIs mba hanampy GPU nodes vaovao ao amin'ny AKS cluster. 
> Fanamarihana: Ny [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) dia singa misokatra loharano. Azo soloina amin'ny controllers hafa izy raha toa ka manohana ny [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ireo controllers ireo.

## Horonan-tsary topi-maso 
[Jereo ny Demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Fametrahana

Azafady, jereo ny torolalana momba ny fametrahana [eto](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Fanombohana haingana

Rehefa avy nametraka Kaito, dia afaka manandrana ny baiko manaraka ny mpampiasa mba hanombohana ny fine-tuning service.

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

Ny sata workspace dia azo arahi-maso amin'ny alalan'ny fampiasana ity baiko manaraka ity. Rehefa lasa `True` ny tsanganana WORKSPACEREADY, dia tafapetraka soa aman-tsara ny modely.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Manaraka izany, dia afaka mahita ny cluster ip an'ny inference service ny mpampiasa ary mampiasa `curl` pod vonjimaika mba hizaha toetra ny service endpoint ao amin'ny cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

It seems like "mo" might refer to a specific language or abbreviation. Could you clarify what "mo" refers to (e.g., Maori, Mongolian, or another language) so I can assist you with the correct translation?