## Fino nastavljanje s Kaito

[Kaito](https://github.com/Azure/kaito) je operater, ki avtomatizira uvajanje AI/ML inferenčnih modelov v Kubernetes grozdu.

Kaito se od večine običajnih metod uvajanja modelov, ki temeljijo na virtualnih strojih, razlikuje po naslednjem:

- Upravljanje datotek modelov z uporabo slik vsebnikov. Na voljo je HTTP strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modela.
- Izogibanje prilagajanju parametrov uvajanja za ustreznost GPU strojne opreme s prednastavljenimi konfiguracijami.
- Samodejno dodeljevanje GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če licenca to dovoljuje.

S pomočjo Kaitoja je potek dela za uvajanje velikih AI inferenčnih modelov v Kubernetes znatno poenostavljen.

## Arhitektura

Kaito sledi klasičnemu vzorcu zasnove Kubernetes Custom Resource Definition (CRD)/krmilnik. Uporabnik upravlja z `workspace` prilagojenim virom, ki opisuje zahteve za GPU in specifikacijo inferenc. Kaito krmilniki bodo avtomatizirali uvajanje z usklajevanjem `workspace` prilagojenega vira.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Zgornja slika prikazuje pregled arhitekture Kaitoja. Njegove glavne komponente vključujejo:

- **Krmilnik delovnega prostora**: Usklajuje `workspace` prilagojen vir, ustvarja `machine` (pojasnjeno spodaj) prilagojene vire za sprožitev samodejnega dodeljevanja vozlišč in na podlagi prednastavljenih konfiguracij modela ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`).
- **Krmilnik za dodeljevanje vozlišč**: Ime krmilnika je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izvira iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo s krmilnikom delovnega prostora. Integrira se z Azure Kubernetes Service (AKS) API-ji za dodajanje novih GPU vozlišč v AKS grozd.
> Opomba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokodna komponenta. Lahko ga zamenjate z drugimi krmilniki, če podpirajo [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Pregledni video 
[Oglejte si predstavitev Kaitoja](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Namestitev

Prosimo, preverite navodila za namestitev [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hiter začetek

Po namestitvi Kaitoja lahko preizkusite naslednje ukaze za zagon storitve za fino nastavljanje.

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

Stanje delovnega prostora lahko spremljate z zagonom naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je bil model uspešno uveden.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete naslov IP inferenčne storitve v grozdu in uporabite začasni `curl` pod za testiranje končne točke storitve v grozdu.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo strojnih AI prevajalskih storitev. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni prevod s strani človeka. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.