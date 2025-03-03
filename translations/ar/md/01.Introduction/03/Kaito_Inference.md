## الاستدلال باستخدام Kaito

[Kaito](https://github.com/Azure/kaito) هو مشغل يقوم بأتمتة نشر نموذج الاستدلال AI/ML داخل مجموعة Kubernetes.

يمتلك Kaito الفروقات الرئيسية التالية مقارنة بمعظم منهجيات نشر النماذج التقليدية المبنية على بنية تحتية تعتمد على الأجهزة الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم HTTP لإجراء مكالمات الاستدلال باستخدام مكتبة النماذج.
- تجنب ضبط معلمات النشر لتناسب أجهزة GPU من خلال توفير إعدادات مسبقة.
- التوفير التلقائي لعقد GPU استنادًا إلى متطلبات النموذج.
- استضافة صور النماذج الكبيرة في سجل الحاويات العام الخاص بـ Microsoft (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير العمل الخاص بإعداد نماذج استدلال AI الكبيرة في Kubernetes بشكل كبير.

## الهيكلية

يتبع Kaito النمط الكلاسيكي لـ Kubernetes المتمثل في تعريف الموارد المخصصة (CRD) ووحدات التحكم. يقوم المستخدم بإدارة مورد مخصص `workspace` يصف متطلبات GPU ومواصفات الاستدلال. ستقوم وحدات التحكم في Kaito بأتمتة عملية النشر من خلال مطابقة المورد المخصص `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

تعرض الصورة أعلاه نظرة عامة على هيكلية Kaito. المكونات الرئيسية تشمل:

- **وحدة التحكم في مساحة العمل**: تقوم بمطابقة المورد المخصص `workspace`، وإنشاء الموارد المخصصة `machine` (الموضحة أدناه) لتفعيل التوفير التلقائي للعقد، وإنشاء عبء العمل الخاص بالاستدلال (`deployment` أو `statefulset`) بناءً على إعدادات النماذج المسبقة.
- **وحدة التحكم في توفير العقد**: اسم وحدة التحكم هو *gpu-provisioner* في [مخطط gpu-provisioner الخاص بـ helm](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). تستخدم CRD `machine` المستمدة من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع وحدة التحكم في مساحة العمل. تتكامل مع واجهات برمجة التطبيقات الخاصة بـ Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى مجموعة AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بوحدات تحكم أخرى إذا كانت تدعم واجهات برمجة التطبيقات الخاصة بـ [Karpenter-core](https://sigs.k8s.io/karpenter).

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## البدء السريع لاستدلال Phi-3
[كود مثال لاستدلال Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

يمكن تتبع حالة مساحة العمل عن طريق تشغيل الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY هي `True`، فهذا يعني أن النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## البدء السريع لاستدلال Phi-3 باستخدام المحولات

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة الاستدلال.

[كود مثال لاستدلال Phi-3 باستخدام المحولات](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

يمكن تتبع حالة مساحة العمل عن طريق تشغيل الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY هي `True`، فهذا يعني أن النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة الاستدلال واستخدام بود `curl` مؤقت لاختبار نقطة نهاية الخدمة داخل المجموعة.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. على الرغم من أننا نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.