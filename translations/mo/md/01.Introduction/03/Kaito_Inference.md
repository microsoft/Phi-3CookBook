## Kaito-თან ინფერენცია

[Kaito](https://github.com/Azure/kaito) არის ოპერატორი, რომელიც ავტომატურად ახორციელებს AI/ML ინფერენციის მოდელის დანერგვას Kubernetes-ის კლასტერში.

Kaito-ს აქვს შემდეგი ძირითადი განსხვავებები ვირტუალურ მანქანებზე დაფუძნებულ მოდელის დანერგვის ძირითად მეთოდოლოგიებთან შედარებით:

- მოდელის ფაილების მართვა კონტეინერის იმიჯების გამოყენებით. უზრუნველყოფილია http სერვერი, რომელიც მოდელის ბიბლიოთეკის გამოყენებით ახორციელებს ინფერენციის მოთხოვნებს.
- GPU აპარატურასთან შესაბამისობისთვის პარამეტრების რეგულირების თავიდან აცილება წინასწარ კონფიგურაციების მიწოდებით.
- GPU ნოდების ავტომატური პროვიზირება მოდელის მოთხოვნების საფუძველზე.
- დიდი მოდელის იმიჯების მასპინძლობა საჯარო Microsoft Container Registry (MCR)-ში, თუ ლიცენზია ამის უფლებას იძლევა.

Kaito-ს გამოყენებით, Kubernetes-ში დიდი AI ინფერენციის მოდელების დანერგვის სამუშაო პროცესი მნიშვნელოვნად მარტივდება.


## არქიტექტურა

Kaito მიჰყვება კლასიკურ Kubernetes Custom Resource Definition (CRD)/კონტროლერის დიზაინის შაბლონს. მომხმარებელი მართავს `workspace` სპეციალურ რესურსს, რომელიც აღწერს GPU მოთხოვნებს და ინფერენციის სპეციფიკაციას. Kaito-ს კონტროლერები ავტომატურად ახორციელებენ დანერგვას `workspace` სპეციალური რესურსის სინქრონიზაციის გზით.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito არქიტექტურა" alt="Kaito არქიტექტურა">
</div>

ზემოთ მოცემულ სურათზე ნაჩვენებია Kaito-ს არქიტექტურის მიმოხილვა. მისი ძირითადი კომპონენტებია:

- **Workspace კონტროლერი**: სინქრონიზაციას უწევს `workspace` სპეციალურ რესურსს, ქმნის `machine` (განსაზღვრული ქვემოთ) სპეციალურ რესურსებს ნოდების ავტომატური პროვიზირების დასაწყებად და ქმნის ინფერენციის სამუშაო დატვირთვას (`deployment` ან `statefulset`) მოდელის წინასწარ კონფიგურაციების საფუძველზე.
- **Node provisioner კონტროლერი**: ამ კონტროლერის სახელია *gpu-provisioner* [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-ში. ის იყენებს `machine` CRD-ს, რომელიც [Karpenter](https://sigs.k8s.io/karpenter)-იდან მოდის, რათა ურთიერთობა ჰქონდეს Workspace კონტროლერთან. ის ინტეგრირდება Azure Kubernetes Service (AKS) API-ებთან, რათა დაამატოს ახალი GPU ნოდები AKS კლასტერში.
> შენიშვნა: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) არის ღია კოდის მქონე კომპონენტი. მისი ჩანაცვლება შესაძლებელია სხვა კონტროლერებით, თუ ისინი მხარს უჭერენ [Karpenter-core](https://sigs.k8s.io/karpenter) API-ებს.

## ინსტალაცია

ინსტალაციის სახელმძღვანელოს სანახავად იხილეთ [აქ](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## სწრაფი დაწყება Phi-3 ინფერენცია
[ნიმუშის კოდი Phi-3 ინფერენციისთვის](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Workspace-ის სტატუსის მონიტორინგი შეგიძლიათ შემდეგი ბრძანების გაშვებით. როდესაც WORKSPACEREADY სვეტი გახდება `True`, მოდელი წარმატებით არის დანერგილი.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

შემდეგ, შეგიძლიათ იპოვოთ ინფერენციის სერვისის კლასტერის IP და გამოიყენოთ დროებითი `curl` პოდი სერვისის საბოლოო წერტილის შესამოწმებლად კლასტერში.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## სწრაფი დაწყება Phi-3 ინფერენცია ადაპტერებით

Kaito-ს ინსტალაციის შემდეგ, შეგიძლიათ სცადოთ შემდეგი ბრძანებები ინფერენციის სერვისის დასაწყებად.

[ნიმუშის კოდი Phi-3 ინფერენციისთვის ადაპტერებით](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace-ის სტატუსის მონიტორინგი შეგიძლიათ შემდეგი ბრძანების გაშვებით. როდესაც WORKSPACEREADY სვეტი გახდება `True`, მოდელი წარმატებით არის დანერგილი.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

შემდეგ, შეგიძლიათ იპოვოთ ინფერენციის სერვისის კლასტერის IP და გამოიყენოთ დროებითი `curl` პოდი სერვისის საბოლოო წერტილის შესამოწმებლად კლასტერში.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

It seems you might be referring to a specific language or abbreviation with "mo." Could you please clarify or specify the language you'd like me to translate the text into? For example, "mo" could refer to Māori, Mongolian, or something else entirely. Let me know so I can assist you better!