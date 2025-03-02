## تحسين النماذج باستخدام Kaito

[Kaito](https://github.com/Azure/kaito) هو مشغل يقوم بأتمتة نشر نماذج الذكاء الاصطناعي/تعلم الآلة في مجموعة Kubernetes.

يمتلك Kaito الميزات الرئيسية التالية مقارنة بمعظم منهجيات نشر النماذج التقليدية المبنية على بنى تحتية تعتمد على الأجهزة الافتراضية:

- إدارة ملفات النماذج باستخدام صور الحاويات. يتم توفير خادم http لإجراء استدعاءات التنبؤ باستخدام مكتبة النماذج.
- تجنب ضبط معلمات النشر لتلائم أجهزة GPU من خلال توفير إعدادات مسبقة.
- توفير تلقائي لعقد GPU بناءً على متطلبات النماذج.
- استضافة صور النماذج الكبيرة في السجل العام لـ Microsoft Container Registry (MCR) إذا سمحت الرخصة بذلك.

باستخدام Kaito، يتم تبسيط سير العمل الخاص بتضمين نماذج التنبؤ الكبيرة في Kubernetes بشكل كبير.

## الهيكلية

يتبع Kaito نمط التصميم الكلاسيكي الخاص بـ Kubernetes Custom Resource Definition (CRD)/controller. يقوم المستخدم بإدارة المورد المخصص `workspace` الذي يصف متطلبات GPU ومواصفات التنبؤ. يقوم مشغلوا Kaito بأتمتة عملية النشر من خلال التوفيق بين المورد المخصص `workspace`.

<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="هيكلية Kaito" alt="هيكلية Kaito">
</div>

توضح الصورة أعلاه نظرة عامة على هيكلية Kaito. تتكون مكوناته الرئيسية من:

- **مشغل مساحة العمل**: يقوم بتوفيق المورد المخصص `workspace`، وإنشاء الموارد المخصصة `machine` (الموضحة أدناه) لتفعيل توفير العقد التلقائي، وإنشاء أعباء عمل التنبؤ (`deployment` أو `statefulset`) بناءً على الإعدادات المسبقة للنموذج.
- **مشغل توفير العقد**: اسم المشغل هو *gpu-provisioner* في [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). يستخدم CRD `machine` المستمد من [Karpenter](https://sigs.k8s.io/karpenter) للتفاعل مع مشغل مساحة العمل. يتكامل مع واجهات برمجة التطبيقات الخاصة بـ Azure Kubernetes Service (AKS) لإضافة عقد GPU جديدة إلى مجموعة AKS.
> ملاحظة: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) هو مكون مفتوح المصدر. يمكن استبداله بمشغلات أخرى إذا كانت تدعم واجهات برمجة التطبيقات الخاصة بـ [Karpenter-core](https://sigs.k8s.io/karpenter).

## فيديو تعريفي
[شاهد عرض Kaito التوضيحي](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## التثبيت

يرجى مراجعة إرشادات التثبيت [هنا](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## البداية السريعة

بعد تثبيت Kaito، يمكن تجربة الأوامر التالية لبدء خدمة تحسين النماذج.

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

يمكن تتبع حالة مساحة العمل باستخدام الأمر التالي. عندما تصبح قيمة العمود WORKSPACEREADY `True`، يكون النموذج قد تم نشره بنجاح.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

بعد ذلك، يمكن العثور على عنوان IP الخاص بخدمة التنبؤ واستخدام حاوية `curl` مؤقتة لاختبار نقطة النهاية الخاصة بالخدمة داخل المجموعة.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المدعومة بالذكاء الاصطناعي. على الرغم من سعينا لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.