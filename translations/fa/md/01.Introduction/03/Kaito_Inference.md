## استنتاج با Kaito

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که فرآیند استقرار مدل‌های استنتاج AI/ML را در یک کلاستر Kubernetes خودکار می‌کند.

Kaito نسبت به بیشتر روش‌های رایج استقرار مدل که بر روی زیرساخت‌های ماشین مجازی ساخته شده‌اند، تفاوت‌های کلیدی زیر را دارد:

- مدیریت فایل‌های مدل با استفاده از تصاویر کانتینر. یک سرور HTTP برای انجام فراخوانی‌های استنتاج با استفاده از کتابخانه مدل ارائه می‌شود.
- اجتناب از تنظیم پارامترهای استقرار برای تطبیق با سخت‌افزار GPU با ارائه پیکربندی‌های پیش‌فرض.
- تأمین خودکار گره‌های GPU بر اساس نیازهای مدل.
- میزبانی تصاویر مدل‌های بزرگ در رجیستری کانتینر عمومی مایکروسافت (MCR) در صورتی که مجوز آن اجازه دهد.

با استفاده از Kaito، فرآیند پیاده‌سازی مدل‌های بزرگ استنتاج AI در Kubernetes به طور قابل توجهی ساده‌تر می‌شود.

## معماری

Kaito از الگوی طراحی کلاسیک تعریف منبع سفارشی (CRD)/کنترلر در Kubernetes پیروی می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات استنتاج را توصیف می‌کند. کنترلرهای Kaito استقرار را با همگام‌سازی منبع سفارشی `workspace` خودکار می‌کنند.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="معماری Kaito" alt="معماری Kaito">
</div>

تصویر بالا نمای کلی از معماری Kaito را نشان می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر فضای کاری**: این کنترلر منبع سفارشی `workspace` را همگام‌سازی می‌کند، منابع سفارشی `machine` (که در ادامه توضیح داده شده‌اند) را برای شروع تأمین خودکار گره ایجاد می‌کند، و بار کاری استنتاج (`deployment` یا `statefulset`) را بر اساس پیکربندی‌های پیش‌فرض مدل ایجاد می‌کند.
- **کنترلر تأمین گره**: نام این کنترلر در [چارت هلم gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) *gpu-provisioner* است. این کنترلر از CRD `machine` که از [Karpenter](https://sigs.k8s.io/karpenter) نشأت گرفته، برای تعامل با کنترلر فضای کاری استفاده می‌کند. این کنترلر با APIهای Azure Kubernetes Service (AKS) یکپارچه می‌شود تا گره‌های GPU جدید را به کلاستر AKS اضافه کند.
> توجه: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک کامپوننت متن‌باز است. در صورتی که کنترلرهای دیگری از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter) پشتیبانی کنند، می‌توان آن را جایگزین کرد.

## نصب

لطفاً راهنمای نصب را [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

## شروع سریع استنتاج Phi-3
[نمونه کد استنتاج Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

وضعیت فضای کاری را می‌توان با اجرای دستور زیر ردیابی کرد. وقتی ستون WORKSPACEREADY به مقدار `True` تغییر کند، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

در مرحله بعد، می‌توان آدرس IP کلاستر سرویس استنتاج را پیدا کرد و از یک پاد `curl` موقت برای آزمایش نقطه پایانی سرویس در کلاستر استفاده کرد.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## شروع سریع استنتاج Phi-3 با آداپتورها

پس از نصب Kaito، می‌توان با اجرای دستورات زیر یک سرویس استنتاج را راه‌اندازی کرد.

[نمونه کد استنتاج Phi-3 با آداپتورها](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

وضعیت فضای کاری را می‌توان با اجرای دستور زیر ردیابی کرد. وقتی ستون WORKSPACEREADY به مقدار `True` تغییر کند، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

در مرحله بعد، می‌توان آدرس IP کلاستر سرویس استنتاج را پیدا کرد و از یک پاد `curl` موقت برای آزمایش نقطه پایانی سرویس در کلاستر استفاده کرد.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس یا حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ گونه مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.