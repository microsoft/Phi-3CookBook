## کائیٹو کے ساتھ فائن ٹوننگ 

[Kaito](https://github.com/Azure/kaito) ایک ایسا آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML انفیرنس ماڈل کی تعیناتی کو خودکار بناتا ہے۔

کائیٹو کی درج ذیل اہم خصوصیات اسے زیادہ تر روایتی ماڈل تعیناتی طریقوں سے مختلف بناتی ہیں، جو ورچوئل مشین انفراسٹرکچر پر مبنی ہیں:

- ماڈل فائلز کو کنٹینر امیجز کے ذریعے منظم کریں۔ ایک HTTP سرور فراہم کیا جاتا ہے جو ماڈل لائبریری استعمال کرتے ہوئے انفیرنس کالز انجام دیتا ہے۔
- GPU ہارڈویئر کے مطابق تعیناتی کے پیرامیٹرز کو ایڈجسٹ کرنے کی ضرورت کو ختم کریں، اور پریسیٹ کنفیگریشنز فراہم کریں۔
- ماڈل کی ضروریات کے مطابق خودکار طور پر GPU نوڈز فراہم کریں۔
- اگر لائسنس اجازت دے تو بڑے ماڈل امیجز کو مائیکروسافٹ کنٹینر رجسٹری (MCR) میں ہوسٹ کریں۔

کائیٹو کے ذریعے، Kubernetes میں بڑے AI انفیرنس ماڈلز کو شامل کرنے کا ورک فلو کافی حد تک آسان ہو جاتا ہے۔


## آرکیٹیکچر

کائیٹو کلاسک Kubernetes کسٹم ریسورس ڈیفینیشن (CRD)/کنٹرولر ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف ایک `workspace` کسٹم ریسورس کا انتظام کرتا ہے جو GPU کی ضروریات اور انفیرنس اسپیسفیکیشن کو بیان کرتا ہے۔ کائیٹو کنٹرولرز `workspace` کسٹم ریسورس کو ہم آہنگ کرکے تعیناتی کو خودکار بناتے ہیں۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

اوپر دی گئی تصویر کائیٹو آرکیٹیکچر کا جائزہ پیش کرتی ہے۔ اس کے اہم اجزاء میں شامل ہیں:

- **ورک اسپیس کنٹرولر**: یہ `workspace` کسٹم ریسورس کو ہم آہنگ کرتا ہے، `machine` (نیچے وضاحت کی گئی ہے) کسٹم ریسورسز بناتا ہے تاکہ نوڈ کی خودکار فراہمی کو متحرک کیا جا سکے، اور ماڈل کی پریسیٹ کنفیگریشنز کی بنیاد پر انفیرنس ورک لوڈ (`deployment` یا `statefulset`) تخلیق کرتا ہے۔
- **نوڈ پروویژنر کنٹرولر**: اس کنٹرولر کا نام [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ `machine` CRD استعمال کرتا ہے، جو [Karpenter](https://sigs.k8s.io/karpenter) سے ماخوذ ہے، تاکہ ورک اسپیس کنٹرولر کے ساتھ تعامل کرے۔ یہ Azure Kubernetes Service (AKS) APIs کے ساتھ انضمام کرتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔  
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورسڈ جزو ہے۔ اگر کوئی دوسرا کنٹرولر [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کو سپورٹ کرتا ہو تو اسے تبدیل کیا جا سکتا ہے۔

## جائزہ ویڈیو 
[کائیٹو ڈیمو دیکھیں](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## تنصیب

تنصیب کی رہنمائی کے لیے [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## فوری آغاز

کائیٹو انسٹال کرنے کے بعد، آپ درج ذیل کمانڈز استعمال کر کے ایک فائن ٹوننگ سروس شروع کر سکتے ہیں۔

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

ورک اسپیس کی حالت کو درج ذیل کمانڈ چلا کر ٹریک کیا جا سکتا ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے تعینات ہو چکا ہوگا۔

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، آپ انفیرنس سروس کے کلسٹر آئی پی کو تلاش کر سکتے ہیں اور کلسٹر میں سروس اینڈ پوائنٹ کی جانچ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کر سکتے ہیں۔

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔