## تنظیم دقیق با Kaito

[Kaito](https://github.com/Azure/kaito) یک اپراتور است که استقرار مدل‌های پیش‌بینی AI/ML را در یک کلاستر Kubernetes به صورت خودکار انجام می‌دهد.

Kaito نسبت به بیشتر روش‌های متداول استقرار مدل که بر زیرساخت‌های ماشین‌های مجازی بنا شده‌اند، تفاوت‌های کلیدی زیر را دارد:

- مدیریت فایل‌های مدل با استفاده از ایمیج‌های کانتینر. یک سرور HTTP ارائه می‌شود که از کتابخانه مدل برای انجام درخواست‌های پیش‌بینی استفاده می‌کند.
- اجتناب از تنظیم پارامترهای استقرار برای تطبیق با سخت‌افزار GPU از طریق ارائه تنظیمات پیش‌فرض.
- تخصیص خودکار گره‌های GPU بر اساس نیازهای مدل.
- میزبانی ایمیج‌های بزرگ مدل در Microsoft Container Registry (MCR) عمومی در صورتی که مجوز آن اجازه دهد.

با استفاده از Kaito، جریان کاری استقرار مدل‌های بزرگ پیش‌بینی AI در Kubernetes به طور قابل توجهی ساده‌تر می‌شود.

## معماری

Kaito از الگوی طراحی کلاسیک Kubernetes Custom Resource Definition(CRD)/controller پیروی می‌کند. کاربر یک منبع سفارشی `workspace` را مدیریت می‌کند که نیازهای GPU و مشخصات پیش‌بینی را توصیف می‌کند. کنترلرهای Kaito استقرار را با همگام‌سازی منبع سفارشی `workspace` به صورت خودکار انجام می‌دهند.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="معماری Kaito" alt="معماری Kaito">
</div>

تصویر بالا نمای کلی معماری Kaito را نشان می‌دهد. اجزای اصلی آن شامل موارد زیر است:

- **کنترلر Workspace**: این کنترلر منبع سفارشی `workspace` را همگام‌سازی می‌کند، منابع سفارشی `machine` (که در ادامه توضیح داده شده) را برای راه‌اندازی خودکار گره‌ها ایجاد می‌کند و بار کاری پیش‌بینی (`deployment` یا `statefulset`) را بر اساس تنظیمات پیش‌فرض مدل ایجاد می‌کند.
- **کنترلر تخصیص گره‌ها**: نام این کنترلر *gpu-provisioner* است که در [چارت helm مربوط به gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) تعریف شده است. این کنترلر از CRD مربوط به `machine` که از [Karpenter](https://sigs.k8s.io/karpenter) نشأت گرفته، برای تعامل با کنترلر Workspace استفاده می‌کند. این کنترلر با APIهای Azure Kubernetes Service (AKS) یکپارچه شده تا گره‌های GPU جدیدی را به کلاستر AKS اضافه کند.
> توجه: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) یک مؤلفه متن‌باز است. این مؤلفه می‌تواند در صورت پشتیبانی از APIهای [Karpenter-core](https://sigs.k8s.io/karpenter) با کنترلرهای دیگری جایگزین شود.

## ویدئوی معرفی
[دموی Kaito را مشاهده کنید](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## نصب

راهنمای نصب را [اینجا](https://github.com/Azure/kaito/blob/main/docs/installation.md) بررسی کنید.

## شروع سریع

پس از نصب Kaito، می‌توانید دستورات زیر را برای شروع یک سرویس تنظیم دقیق امتحان کنید.

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

وضعیت Workspace را می‌توان با اجرای دستور زیر پیگیری کرد. زمانی که ستون WORKSPACEREADY به `True` تغییر کند، مدل با موفقیت مستقر شده است.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

سپس، می‌توانید آدرس IP کلاستر سرویس پیش‌بینی را پیدا کرده و با استفاده از یک پاد موقت `curl` سرویس را در کلاستر آزمایش کنید.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان بومی آن باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.