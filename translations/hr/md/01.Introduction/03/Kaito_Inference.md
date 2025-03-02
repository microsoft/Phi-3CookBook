## Inference s Kaito

[Kaito](https://github.com/Azure/kaito) je operator koji automatizira implementaciju AI/ML inferencijskih modela u Kubernetes klasteru.

Kaito ima sljedeće ključne razlike u usporedbi s većinom glavnih metodologija implementacije modela izgrađenih na infrastrukturi virtualnih strojeva:

- Upravljanje datotekama modela pomoću kontejnerskih slika. Pruža se http poslužitelj za izvođenje inferencijskih poziva koristeći knjižnicu modela.
- Izbjegava podešavanje parametara implementacije kako bi odgovarali GPU hardveru pružajući unaprijed definirane konfiguracije.
- Automatski dodjeljuje GPU čvorove na temelju zahtjeva modela.
- Hostira velike slike modela u javnom Microsoft Container Registry (MCR) ako licenca to dopušta.

Korištenjem Kaita, tijek rada za integraciju velikih AI inferencijskih modela u Kubernetesu uvelike je pojednostavljen.

## Arhitektura

Kaito slijedi klasičan Kubernetes obrazac dizajna s prilagođenom definicijom resursa (CRD)/kontrolerom. Korisnik upravlja prilagođenim resursom `workspace` koji opisuje GPU zahtjeve i specifikaciju inferencije. Kaito kontroleri automatiziraju implementaciju usklađivanjem prilagođenog resursa `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Gornja slika prikazuje pregled Kaito arhitekture. Njegove glavne komponente uključuju:

- **Kontroler radnog prostora**: Usklađuje prilagođeni resurs `workspace`, kreira prilagođene resurse `machine` (objašnjeno u nastavku) kako bi pokrenuo automatsku dodjelu čvorova i kreira inferencijski radni proces (`deployment` ili `statefulset`) na temelju unaprijed definiranih konfiguracija modela.
- **Kontroler za dodjelu čvorova**: Naziv ovog kontrolera je *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potječe iz [Karpenter](https://sigs.k8s.io/karpenter) za interakciju s kontrolerom radnog prostora. Integrira se s API-jem Azure Kubernetes Service (AKS) za dodavanje novih GPU čvorova u AKS klaster.
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je komponenta otvorenog koda. Može se zamijeniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Instalacija

Molimo provjerite upute za instalaciju [ovdje](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak inferencije Phi-3
[Primjer koda za inferenciju Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status radnog prostora može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Zatim možete pronaći cluster IP inferencijske usluge i koristiti privremeni `curl` pod za testiranje krajnje točke usluge u klasteru.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Brzi početak inferencije Phi-3 s adapterima

Nakon instalacije Kaita, možete isprobati sljedeće naredbe za pokretanje inferencijske usluge.

[Primjer koda za inferenciju Phi-3 s adapterima](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status radnog prostora može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Zatim možete pronaći cluster IP inferencijske usluge i koristiti privremeni `curl` pod za testiranje krajnje točke usluge u klasteru.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojnog AI prijevoda. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.