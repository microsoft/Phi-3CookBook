## Тонкая настройка с Kaito

[Kaito](https://github.com/Azure/kaito) — это оператор, который автоматизирует развертывание моделей AI/ML для инференса в кластере Kubernetes.

Kaito имеет следующие ключевые отличия по сравнению с большинством популярных методов развертывания моделей, основанных на инфраструктуре виртуальных машин:

- Управление файлами моделей с использованием образов контейнеров. Предоставляется HTTP-сервер для выполнения инференс-запросов с использованием библиотеки модели.
- Избегание ручной настройки параметров развертывания для соответствия аппаратным требованиям GPU благодаря предоставлению заранее настроенных конфигураций.
- Автоматическое выделение узлов GPU на основе требований модели.
- Хранение больших образов моделей в публичном Microsoft Container Registry (MCR), если это позволяет лицензия.

С помощью Kaito процесс интеграции больших моделей для инференса AI в Kubernetes значительно упрощается.

## Архитектура

Kaito следует классическому шаблону проектирования Custom Resource Definition (CRD)/контроллера в Kubernetes. Пользователь управляет пользовательским ресурсом `workspace`, который описывает требования к GPU и спецификацию инференса. Контроллеры Kaito автоматизируют развертывание, синхронизируя пользовательский ресурс `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Архитектура Kaito" alt="Архитектура Kaito">
</div>

На рисунке выше представлен общий обзор архитектуры Kaito. Основные компоненты включают:

- **Контроллер рабочего пространства**: Синхронизирует пользовательский ресурс `workspace`, создаёт пользовательские ресурсы `machine` (объяснены ниже) для запуска автоматического выделения узлов и создаёт рабочую нагрузку для инференса (`deployment` или `statefulset`) на основе заранее настроенных конфигураций модели.
- **Контроллер выделения узлов**: Контроллер называется *gpu-provisioner* в [Helm-чарте gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Он использует CRD `machine`, происходящий из [Karpenter](https://sigs.k8s.io/karpenter), чтобы взаимодействовать с контроллером рабочего пространства. Он интегрируется с API Azure Kubernetes Service (AKS) для добавления новых GPU-узлов в кластер AKS.  
> Примечание: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) — это компонент с открытым исходным кодом. Его можно заменить другими контроллерами, если они поддерживают API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Обзорное видео
[Смотрите демонстрацию Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Установка

Пожалуйста, ознакомьтесь с руководством по установке [здесь](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Быстрый старт

После установки Kaito можно попробовать следующие команды, чтобы запустить службу тонкой настройки.

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

Статус рабочего пространства можно отследить, выполнив следующую команду. Когда столбец WORKSPACEREADY станет `True`, модель успешно развернута.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Далее можно найти cluster ip службы инференса и использовать временный pod `curl`, чтобы протестировать конечную точку службы в кластере.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматических сервисов перевода на основе ИИ. Хотя мы стремимся к точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования этого перевода.