## Инференс с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание AI/ML моделей для инференса в кластере Kubernetes.

Основные отличия Kaito от большинства традиционных методов развертывания моделей, построенных на инфраструктуре виртуальных машин:

- Управление файлами моделей с помощью контейнерных образов. Предоставляется HTTP-сервер для выполнения запросов инференса с использованием библиотеки модели.
- Избежание настройки параметров развертывания под оборудование GPU за счет использования заранее заданных конфигураций.
- Автоматическое добавление GPU-узлов в зависимости от требований модели.
- Размещение больших контейнерных образов моделей в публичном Microsoft Container Registry (MCR), если это позволяет лицензия.

С использованием Kaito процесс интеграции крупных моделей для инференса в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому паттерну проектирования Kubernetes Custom Resource Definition (CRD)/контроллер. Пользователь управляет ресурсом `workspace`, который описывает требования к GPU и спецификацию инференса. Контроллеры Kaito автоматизируют развертывание, синхронизируя ресурс `workspace`.  
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

На рисунке выше представлена общая архитектура Kaito. Основные компоненты включают:

- **Контроллер рабочей области (Workspace controller)**: Синхронизирует ресурс `workspace`, создает ресурсы `machine` (описаны ниже) для запуска автоматического добавления узлов, а также создает рабочую нагрузку для инференса (`deployment` или `statefulset`) на основе заранее заданных конфигураций модели.
- **Контроллер добавления узлов (Node provisioner controller)**: Этот контроллер называется *gpu-provisioner* в [Helm-чарте gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, основанный на [Karpenter](https://sigs.k8s.io/karpenter), для взаимодействия с контроллером рабочей области. Интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.  
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Он может быть заменен другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Установка

Инструкции по установке доступны [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт: Инференс Phi-3
[Пример кода для инференса Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Статус рабочей области можно отслеживать с помощью следующей команды. Когда в колонке WORKSPACEREADY появится значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Затем можно найти кластерный IP-адрес сервиса инференса и использовать временный pod `curl` для проверки конечной точки сервиса в кластере.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Быстрый старт: Инференс Phi-3 с адаптерами

После установки Kaito можно выполнить следующие команды для запуска сервиса инференса.

[Пример кода для инференса Phi-3 с адаптерами](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Статус рабочей области можно отслеживать с помощью следующей команды. Когда в колонке WORKSPACEREADY появится значение `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Затем можно найти кластерный IP-адрес сервиса инференса и использовать временный pod `curl` для проверки конечной точки сервиса в кластере.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с использованием машинных сервисов искусственного интеллекта. Хотя мы стремимся к точности, имейте в виду, что автоматизированные переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.