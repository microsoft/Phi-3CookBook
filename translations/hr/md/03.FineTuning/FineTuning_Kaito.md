## Fino Podešavanje s Kaito

[Kaito](https://github.com/Azure/kaito) je operator koji automatizira implementaciju AI/ML modela za inferenciju u Kubernetes klasteru.

Kaito se razlikuje od većine mainstream metodologija implementacije modela temeljenih na infrastrukturi virtualnih strojeva po sljedećem:

- Upravljanje datotekama modela pomoću slika kontejnera. Pruža se HTTP poslužitelj za izvođenje inferencijskih poziva pomoću knjižnice modela.
- Izbjegavanje podešavanja parametara implementacije za prilagodbu GPU hardveru pružanjem unaprijed postavljenih konfiguracija.
- Automatsko osiguravanje GPU čvorova na temelju zahtjeva modela.
- Hostiranje velikih slika modela u javnom Microsoft Container Registry (MCR) ako to licenca dopušta.

Uz Kaito, tijek rada za uvođenje velikih AI inferencijskih modela u Kubernetes uvelike je pojednostavljen.

## Arhitektura

Kaito slijedi klasičan dizajn obrazaca Kubernetes Custom Resource Definition (CRD)/kontrolera. Korisnik upravlja prilagođenim resursom `workspace` koji opisuje GPU zahtjeve i specifikaciju za inferenciju. Kaito kontroleri automatiziraju implementaciju usklađivanjem prilagođenog resursa `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Gornja slika prikazuje pregled arhitekture Kaito. Njegove glavne komponente uključuju:

- **Kontroler radnog prostora**: Usklađuje prilagođeni resurs `workspace`, stvara prilagođene resurse `machine` (objašnjeno u nastavku) za pokretanje automatskog osiguravanja čvorova i stvara radno opterećenje za inferenciju (`deployment` ili `statefulset`) na temelju unaprijed postavljenih konfiguracija modela.
- **Kontroler za osiguravanje čvorova**: Ime ovog kontrolera je *gpu-provisioner* u [gpu-provisioner helm chartu](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potječe iz [Karpentera](https://sigs.k8s.io/karpenter) za interakciju s kontrolerom radnog prostora. Integrira se s Azure Kubernetes Service (AKS) API-jima kako bi dodao nove GPU čvorove u AKS klaster.  
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je otvorenog koda. Može se zamijeniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Pregledni video
[Pogledajte Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalacija

Molimo provjerite upute za instalaciju [ovdje](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak

Nakon instalacije Kaito-a, možete isprobati sljedeće naredbe za pokretanje usluge fino podešavanja.

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

Status radnog prostora može se pratiti pokretanjem sljedeće naredbe. Kada stupac WORKSPACEREADY postane `True`, model je uspješno implementiran.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Zatim možete pronaći cluster IP usluge za inferenciju i koristiti privremeni `curl` pod za testiranje krajnje točke usluge u klasteru.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prevođenja. Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.