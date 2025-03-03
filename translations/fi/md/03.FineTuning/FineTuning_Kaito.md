## Kaito hienosäätö

[Kaito](https://github.com/Azure/kaito) on operaattori, joka automatisoi AI/ML-mallien käyttöönoton Kubernetes-klusterissa.

Kaito eroaa merkittävästi useimmista virtuaalikoneinfrastruktuureihin perustuvista mallien käyttöönoton menetelmistä seuraavilla tavoilla:

- Mallitiedostojen hallinta konttikuvien avulla. Tarjolla on HTTP-palvelin, joka suorittaa mallikirjaston avulla ennustepyyntöjä.
- Vältä käyttöparametrien hienosäätö GPU-laitteiston mukaiseksi tarjoamalla valmiiksi määritetyt asetukset.
- GPU-solmujen automaattinen provisiointi mallivaatimusten perusteella.
- Suurten mallikuvien isännöinti julkisessa Microsoft Container Registryssä (MCR), mikäli lisenssi sen sallii.

Kaiton avulla suurten AI-ennustemallien käyttöönoton työnkulku Kubernetesissa yksinkertaistuu huomattavasti.

## Arkkitehtuuri

Kaito noudattaa perinteistä Kubernetesin Custom Resource Definition (CRD) / ohjain -mallia. Käyttäjä hallinnoi `workspace`-resurssia, joka kuvaa GPU-vaatimukset ja ennustemääritykset. Kaiton ohjaimet automatisoivat käyttöönoton sovittamalla `workspace`-resurssin.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito-arkkitehtuuri" alt="Kaito-arkkitehtuuri">
</div>

Yllä oleva kuva esittää Kaiton arkkitehtuurin yleiskatsauksen. Sen keskeiset komponentit ovat:

- **Työtilan ohjain (Workspace controller)**: Sovittaa `workspace`-resurssin, luo `machine` (selitetty alla) -resursseja käynnistääkseen solmujen automaattisen provisioinnin ja luo ennustetyökuorman (`deployment` tai `statefulset`) mallin valmiiksi määritettyjen asetusten perusteella.
- **Solmujen provisiointiohjain (Node provisioner controller)**: Tämän ohjaimen nimi on *gpu-provisioner* [gpu-provisioner helm chartissa](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Se käyttää `machine` CRD:tä, joka on peräisin [Karpenterista](https://sigs.k8s.io/karpenter), kommunikoidakseen työtilan ohjaimen kanssa. Se integroituu Azure Kubernetes Service (AKS) -rajapintoihin lisätäkseen uusia GPU-solmuja AKS-klusteriin.
> Huom: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avoimen lähdekoodin komponentti. Sen voi korvata muilla ohjaimilla, jos ne tukevat [Karpenter-core](https://sigs.k8s.io/karpenter) -rajapintoja.

## Yleiskatsausvideo
[Katso Kaito-demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Asennus

Tarkista asennusohjeet [täältä](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Pika-aloitus

Kun Kaito on asennettu, seuraavilla komennoilla voi aloittaa hienosäätöpalvelun:

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

Työtilan tilaa voi seurata suorittamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu `True`, malli on otettu onnistuneesti käyttöön.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voi etsiä ennustepalvelun klusterin IP-osoitteen ja käyttää väliaikaista `curl`-podia testatakseen palvelun päätepistettä klusterissa.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisia tekoälykäännöspalveluita käyttäen. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista, ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.