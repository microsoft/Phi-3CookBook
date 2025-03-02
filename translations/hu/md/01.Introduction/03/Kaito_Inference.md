## Következtetés Kaito-val

[Kaito](https://github.com/Azure/kaito) egy operátor, amely automatizálja az AI/ML következtetési modellek telepítését egy Kubernetes klaszterben.

Kaito a következő kulcsfontosságú különbségekkel rendelkezik a legtöbb, virtuális gép infrastruktúrákra épülő mainstream modelltelepítési módszertanhoz képest:

- Modellfájlok kezelése konténerképek segítségével. Egy HTTP szerver biztosítja a következtetési hívások végrehajtását a modellkönyvtár használatával.
- Elkerüli a telepítési paraméterek GPU hardverhez való igazítását előre beállított konfigurációk biztosításával.
- Automatikusan biztosít GPU csomópontokat a modell követelményei alapján.
- Nagy méretű modellképek tárolása a nyilvános Microsoft Container Registry (MCR) szolgáltatásban, ha a licenc ezt engedélyezi.

Kaito segítségével az AI következtetési modellek Kubernetesbe való integrálásának folyamata jelentősen leegyszerűsödik.

## Architektúra

Kaito a klasszikus Kubernetes Custom Resource Definition (CRD)/vezérlő tervezési mintát követi. A felhasználó egy `workspace` egyedi erőforrást kezel, amely leírja a GPU követelményeket és a következtetési specifikációt. A Kaito vezérlők automatizálják a telepítést az `workspace` egyedi erőforrás összehangolásával.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architektúra" alt="Kaito architektúra">
</div>

A fenti ábra a Kaito architektúra áttekintését mutatja be. Főbb összetevői:

- **Munkaterület-vezérlő**: Összehangolja az `workspace` egyedi erőforrást, létrehozza az `machine` (alább magyarázva) egyedi erőforrásokat a csomópontok automatikus biztosításának elindításához, és létrehozza a következtetési munkaterhelést (`deployment` vagy `statefulset`) a modell előre beállított konfigurációi alapján.
- **Csomópont-biztosító vezérlő**: A vezérlő neve *gpu-provisioner* a [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) szerint. Az `machine` CRD-t használja, amely a [Karpenter](https://sigs.k8s.io/karpenter) projektből származik, hogy kapcsolatba lépjen a munkaterület-vezérlővel. Integrálódik az Azure Kubernetes Service (AKS) API-kkal, hogy új GPU csomópontokat adjon hozzá az AKS klaszterhez. 
> Megjegyzés: A [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) egy nyílt forráskódú komponens. Lecserélhető más vezérlőkre, ha támogatják a [Karpenter-core](https://sigs.k8s.io/karpenter) API-kat.

## Telepítés

Kérjük, tekintse meg a telepítési útmutatót [itt](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Gyors kezdés Phi-3 következtetéssel
[Phi-3 következtetés mintakód](https://github.com/Azure/kaito/tree/main/examples/inference)

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

A munkaterület állapota a következő parancs futtatásával követhető nyomon. Amikor a WORKSPACEREADY oszlop értéke `True`, a modell sikeresen települt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ezután megkereshető a következtetési szolgáltatás klaszter IP-je, és egy ideiglenes `curl` pod használható a szolgáltatás végpontjának tesztelésére a klaszteren belül.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Gyors kezdés Phi-3 következtetéssel adapterekkel

Kaito telepítése után az alábbi parancsokkal indítható el egy következtetési szolgáltatás.

[Phi-3 következtetés mintakód adapterekkel](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

A munkaterület állapota a következő parancs futtatásával követhető nyomon. Amikor a WORKSPACEREADY oszlop értéke `True`, a modell sikeresen települt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ezután megkereshető a következtetési szolgáltatás klaszter IP-je, és egy ideiglenes `curl` pod használható a szolgáltatás végpontjának tesztelésére a klaszteren belül.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatásokkal lett lefordítva. Bár igyekszünk a pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.