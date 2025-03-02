## Fine-Tuning z Kaito

[Kaito](https://github.com/Azure/kaito) to operator, który automatyzuje wdrażanie modeli wnioskowania AI/ML w klastrze Kubernetes.

Kaito wyróżnia się na tle większości głównych metodologii wdrażania modeli opartych na infrastrukturze maszyn wirtualnych dzięki następującym cechom:

- Zarządzanie plikami modelu za pomocą obrazów kontenerów. Udostępnia serwer http do wykonywania zapytań wnioskowania przy użyciu biblioteki modelu.
- Unikanie dostrajania parametrów wdrożenia do sprzętu GPU dzięki wstępnie zdefiniowanym konfiguracjom.
- Automatyczne przydzielanie węzłów GPU na podstawie wymagań modelu.
- Hostowanie dużych obrazów modeli w publicznym Microsoft Container Registry (MCR), jeśli pozwala na to licencja.

Dzięki Kaito proces wdrażania dużych modeli wnioskowania AI w Kubernetes jest znacznie uproszczony.

## Architektura

Kaito opiera się na klasycznym wzorcu projektowym Kubernetes Custom Resource Definition (CRD)/kontrolera. Użytkownik zarządza zasobem `workspace`, który opisuje wymagania GPU i specyfikację wnioskowania. Kontrolery Kaito automatyzują wdrożenie, synchronizując zasób `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Powyższy diagram przedstawia ogólny przegląd architektury Kaito. Główne komponenty to:

- **Kontroler przestrzeni roboczej**: Synchronizuje zasób `workspace`, tworzy zasoby `machine` (wyjaśnione poniżej) w celu uruchomienia automatycznego przydzielania węzłów oraz generuje obciążenie wnioskowania (`deployment` lub `statefulset`) na podstawie wstępnie zdefiniowanych konfiguracji modelu.
- **Kontroler przydzielania węzłów**: Nazwa kontrolera to *gpu-provisioner* w [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Wykorzystuje CRD `machine` pochodzące z [Karpenter](https://sigs.k8s.io/karpenter) do interakcji z kontrolerem przestrzeni roboczej. Integruje się z API Azure Kubernetes Service (AKS), aby dodawać nowe węzły GPU do klastra AKS.  
> Uwaga: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) jest komponentem open source. Może być zastąpiony innymi kontrolerami, jeśli obsługują API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Film przeglądowy 
[Obejrzyj demonstrację Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Instalacja

Instrukcje instalacji znajdują się [tutaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Szybki start

Po zainstalowaniu Kaito można użyć poniższych poleceń, aby uruchomić usługę fine-tuningu.

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

Status przestrzeni roboczej można śledzić, uruchamiając poniższe polecenie. Gdy kolumna WORKSPACEREADY przyjmie wartość `True`, model został pomyślnie wdrożony.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Następnie można znaleźć adres IP usługi w klastrze i użyć tymczasowego podu `curl`, aby przetestować punkt końcowy usługi w klastrze.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.