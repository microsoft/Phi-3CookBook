## Inferenssi Kaito:lla

[Kaito](https://github.com/Azure/kaito) on operaattori, joka automatisoi AI/ML-inferenssimallien käyttöönoton Kubernetes-klusterissa.

Kaito eroaa merkittävästi useimmista virtuaalikoneinfrastruktuuriin perustuvista mallien käyttöönoton menetelmistä seuraavilla tavoilla:

- Mallitiedostojen hallinta säilökuvien avulla. HTTP-palvelin tarjotaan inferenssikutsujen suorittamiseen mallikirjaston avulla.
- Valmiit asetukset, jotka poistavat tarpeen hienosäätää käyttöönoton parametreja GPU-laitteiston mukaan.
- GPU-solmujen automaattinen provisiointi mallin vaatimusten perusteella.
- Suurten mallikuvien isännöinti julkisessa Microsoft Container Registry (MCR) -rekisterissä, jos lisenssi sen sallii.

Kaiton avulla suurten AI-inferenssimallien käyttöönotto Kubernetes-ympäristössä yksinkertaistuu huomattavasti.

## Arkkitehtuuri

Kaito noudattaa perinteistä Kubernetes Custom Resource Definition (CRD) / ohjaimen suunnittelumallia. Käyttäjä hallitsee `workspace`-mukautettua resurssia, joka kuvaa GPU-vaatimukset ja inferenssimääritykset. Kaiton ohjaimet automatisoivat käyttöönoton sovittamalla yhteen `workspace`-mukautetun resurssin.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito-arkkitehtuuri" alt="Kaito-arkkitehtuuri">
</div>

Yllä oleva kuva esittelee Kaiton arkkitehtuurin yleiskatsauksen. Sen pääkomponentit koostuvat seuraavista:

- **Työtilan ohjain**: Sovittaa `workspace`-mukautetun resurssin, luo `machine`-mukautettuja resursseja (selitetty alla) käynnistämään solmujen automaattisen provisioinnin ja luo inferenssityökuorman (`deployment` tai `statefulset`) mallin valmiiden asetusten perusteella.
- **Solmujen provisiointiohjain**: Tämän ohjaimen nimi on *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) -projektissa. Se käyttää `machine`-CRD:tä, joka on peräisin [Karpenter](https://sigs.k8s.io/karpenter) -projektista, kommunikoidakseen työtilan ohjaimen kanssa. Se integroituu Azure Kubernetes Service (AKS) -rajapintoihin lisätäkseen uusia GPU-solmuja AKS-klusteriin.
> Huom: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) on avoimen lähdekoodin komponentti. Sen voi korvata muilla ohjaimilla, jos ne tukevat [Karpenter-core](https://sigs.k8s.io/karpenter) -rajapintoja.

## Asennus

Tarkista asennusohjeet [täältä](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Pika-aloitus Inferenssi Phi-3

[Esimerkkikoodi Inferenssi Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Työtilan tilaa voi seurata suorittamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu `True`, malli on otettu onnistuneesti käyttöön.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voit löytää inferenssipalvelun klusterin IP-osoitteen ja käyttää väliaikaista `curl`-podia testataksesi palvelun päätepistettä klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Pika-aloitus Inferenssi Phi-3 adaptereilla

Kun Kaito on asennettu, voit kokeilla seuraavia komentoja käynnistääksesi inferenssipalvelun.

[Esimerkkikoodi Inferenssi Phi-3 adaptereilla](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Työtilan tilaa voi seurata suorittamalla seuraavan komennon. Kun WORKSPACEREADY-sarake muuttuu `True`, malli on otettu onnistuneesti käyttöön.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Seuraavaksi voit löytää inferenssipalvelun klusterin IP-osoitteen ja käyttää väliaikaista `curl`-podia testataksesi palvelun päätepistettä klusterissa.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai tulkintavirheistä, jotka johtuvat tämän käännöksen käytöstä.