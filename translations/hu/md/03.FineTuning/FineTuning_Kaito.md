## Finomhangolás Kaitóval

[Kaito](https://github.com/Azure/kaito) egy operátor, amely automatizálja az AI/ML inferencia modellek telepítését egy Kubernetes klaszterben.

A Kaito az alábbi kulcsfontosságú eltéréseket kínál a legtöbb, virtuális gépekre épülő mainstream modelltelepítési módszertanhoz képest:

- Modellfájlok kezelése konténerképek segítségével. Egy HTTP szerver biztosítja az inferencia hívások végrehajtását a modellkönyvtár használatával.
- Előre beállított konfigurációk révén elkerülhető a telepítési paraméterek GPU hardverhez való igazítása.
- Automatikus GPU csomópontok biztosítása a modell követelményei alapján.
- Nagy méretű modellképek tárolása a nyilvános Microsoft Container Registry-ben (MCR), ha a licenc ezt megengedi.

A Kaitóval a Kubernetesben történő nagy AI inferencia modellek bevezetésének munkafolyamata jelentősen leegyszerűsödik.

## Architektúra

A Kaito a klasszikus Kubernetes Custom Resource Definition (CRD)/kontroller tervezési mintát követi. A felhasználó egy `workspace` egyéni erőforrást kezel, amely leírja a GPU követelményeket és az inferencia specifikációt. A Kaito kontrollerek automatizálják a telepítést azáltal, hogy egyeztetik a `workspace` egyéni erőforrást.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architektúra" alt="Kaito architektúra">
</div>

A fenti ábra bemutatja a Kaito architektúra áttekintését. Főbb komponensei a következők:

- **Munkaterület-kontroller**: Egyezteti a `workspace` egyéni erőforrást, létrehozza a `machine` (lentebb magyarázva) egyéni erőforrásokat a csomópontok automatikus biztosításának elindításához, és létrehozza az inferencia munkaterhelést (`deployment` vagy `statefulset`) a modell előre beállított konfigurációi alapján.
- **Csomópont-biztosító kontroller**: A kontroller neve *gpu-provisioner* a [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) keretében. A `machine` CRD-t használja, amely a [Karpenter](https://sigs.k8s.io/karpenter) projektből származik, hogy kapcsolatot teremtsen a munkaterület-kontrollerrel. Az Azure Kubernetes Service (AKS) API-kat integrálja új GPU csomópontok hozzáadásához az AKS klaszterhez.  
> Megjegyzés: A [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) egy nyílt forráskódú komponens. Lecserélhető más kontrollerekre, ha azok támogatják a [Karpenter-core](https://sigs.k8s.io/karpenter) API-kat.

## Áttekintő videó  
[Nézd meg a Kaito demót](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)  
## Telepítés

Kérjük, tekintsd meg a telepítési útmutatót [itt](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Gyors kezdés

A Kaito telepítése után az alábbi parancsok segítségével indítható egy finomhangolási szolgáltatás.

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

A munkaterület állapota az alábbi parancs futtatásával követhető nyomon. Amikor a WORKSPACEREADY oszlop értéke `True`, a modell sikeresen telepítve lett.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Ezután megkereshető az inferencia szolgáltatás klaszter IP címe, és egy ideiglenes `curl` pod segítségével tesztelhető a szolgáltatás végpontja a klaszteren belül.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Jogi nyilatkozat**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.