## Фина настройка с Kaito

[Kaito](https://github.com/Azure/kaito) е оператор, който автоматизира внедряването на AI/ML модели за извършване на предсказания в Kubernetes клъстер.

Kaito има следните ключови предимства в сравнение с повечето традиционни методологии за внедряване на модели, базирани на виртуални машини:

- Управлява файловете на моделите чрез контейнерни образи. Осигурява http сървър за извършване на предсказания с помощта на библиотеката на модела.
- Избягва необходимостта от настройка на параметрите на внедряване, за да отговарят на GPU хардуера, като предоставя предварително зададени конфигурации.
- Автоматично осигурява GPU възли според изискванията на модела.
- Хоства големи образи на модели в публичния Microsoft Container Registry (MCR), ако лицензът го позволява.

С помощта на Kaito работният процес за внедряване на големи AI модели за предсказания в Kubernetes е значително опростен.

## Архитектура

Kaito следва класическия дизайн модел на Kubernetes Custom Resource Definition (CRD)/контролер. Потребителят управлява ресурс от тип `workspace`, който описва GPU изискванията и спецификацията за предсказания. Контролерите на Kaito автоматизират внедряването, като синхронизират ресурса `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Архитектура на Kaito" alt="Архитектура на Kaito">
</div>

Горната фигура представя общия преглед на архитектурата на Kaito. Основните ѝ компоненти включват:

- **Контролер на работното пространство**: Синхронизира ресурса `workspace`, създава ресурси `machine` (обяснени по-долу) за задействане на автоматично осигуряване на възли и създава работно натоварване за предсказания (`deployment` или `statefulset`) въз основа на предварително зададените конфигурации на модела.
- **Контролер за осигуряване на възли**: Контролерът се нарича *gpu-provisioner* в [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Той използва CRD `machine`, произлизащ от [Karpenter](https://sigs.k8s.io/karpenter), за взаимодействие с контролера на работното пространство. Интегрира се с API на Azure Kubernetes Service (AKS), за да добавя нови GPU възли към AKS клъстера.
> Забележка: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) е компонент с отворен код. Може да бъде заменен с други контролери, ако поддържат API на [Karpenter-core](https://sigs.k8s.io/karpenter).

## Видео преглед
[Гледайте демонстрацията на Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Инсталация

Моля, проверете ръководството за инсталация [тук](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Бърз старт

След като инсталирате Kaito, можете да използвате следните команди, за да стартирате услуга за фина настройка.

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

Статусът на работното пространство може да бъде проследен чрез изпълнение на следната команда. Когато колоната WORKSPACEREADY стане `True`, моделът е успешно внедрен.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

След това можете да намерите IP адреса на клъстера за услугата за предсказания и да използвате временен `curl` pod, за да тествате крайния адрес на услугата в клъстера.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от отговорност**:  
Този документ е преведен с помощта на машинни AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетния източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за недоразумения или погрешни тълкувания, възникнали в резултат на използването на този превод.