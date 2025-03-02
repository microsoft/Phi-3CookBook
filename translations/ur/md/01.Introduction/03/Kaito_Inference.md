## Kaito کے ساتھ انفرنس

[Kaito](https://github.com/Azure/kaito) ایک آپریٹر ہے جو Kubernetes کلسٹر میں AI/ML انفرنس ماڈل کی ڈپلائمنٹ کو خودکار بناتا ہے۔

Kaito کے پاس زیادہ تر عام ماڈل ڈپلائمنٹ طریقوں کے مقابلے میں درج ذیل اہم خصوصیات ہیں، جو ورچوئل مشین انفراسٹرکچر پر مبنی ہیں:

- ماڈل فائلز کو کنٹینر امیجز کے ذریعے مینیج کریں۔ ایک HTTP سرور فراہم کیا جاتا ہے تاکہ ماڈل لائبریری کا استعمال کرتے ہوئے انفرنس کالز کی جا سکیں۔
- GPU ہارڈویئر کے مطابق ڈپلائمنٹ پیرامیٹرز کو ایڈجسٹ کرنے سے بچنے کے لیے پہلے سے طے شدہ کنفیگریشنز فراہم کی جاتی ہیں۔
- ماڈل کی ضروریات کے مطابق GPU نوڈز کو خودکار طریقے سے پروویژن کریں۔
- اگر لائسنس اجازت دے تو بڑے ماڈل امیجز کو مائیکروسافٹ کنٹینر رجسٹری (MCR) میں عوامی طور پر ہوسٹ کریں۔

Kaito کے ذریعے، Kubernetes میں بڑے AI انفرنس ماڈلز کی آن بورڈنگ کا ورک فلو بہت آسان ہو جاتا ہے۔


## آرکیٹیکچر

Kaito کلاسک Kubernetes کسٹم ریسورس ڈیفینیشن (CRD)/کنٹرولر ڈیزائن پیٹرن کی پیروی کرتا ہے۔ صارف `workspace` کسٹم ریسورس کو مینیج کرتا ہے جو GPU کی ضروریات اور انفرنس کی تفصیلات کو بیان کرتا ہے۔ Kaito کنٹرولرز `workspace` کسٹم ریسورس کو ہم آہنگ کر کے ڈپلائمنٹ کو خودکار بناتے ہیں۔
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito آرکیٹیکچر" alt="Kaito آرکیٹیکچر">
</div>

اوپر دی گئی تصویر Kaito آرکیٹیکچر کا خلاصہ پیش کرتی ہے۔ اس کے اہم اجزاء درج ذیل ہیں:

- **ورک اسپیس کنٹرولر**: یہ `workspace` کسٹم ریسورس کو ہم آہنگ کرتا ہے، `machine` (جس کی وضاحت نیچے کی گئی ہے) کسٹم ریسورسز بناتا ہے تاکہ نوڈز کو خودکار طریقے سے پروویژن کیا جا سکے، اور ماڈل کی پہلے سے طے شدہ کنفیگریشنز کی بنیاد پر انفرنس ورک لوڈ (`deployment` یا `statefulset`) بناتا ہے۔
- **نوڈ پروویژنر کنٹرولر**: اس کنٹرولر کا نام [gpu-provisioner helm چارٹ](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) میں *gpu-provisioner* ہے۔ یہ `machine` CRD کا استعمال کرتا ہے جو [Karpenter](https://sigs.k8s.io/karpenter) سے ماخوذ ہے تاکہ ورک اسپیس کنٹرولر کے ساتھ تعامل کیا جا سکے۔ یہ Azure Kubernetes Service (AKS) APIs کے ساتھ مربوط ہوتا ہے تاکہ AKS کلسٹر میں نئے GPU نوڈز شامل کیے جا سکیں۔  
> نوٹ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ایک اوپن سورسڈ جزو ہے۔ اسے دیگر کنٹرولرز سے تبدیل کیا جا سکتا ہے اگر وہ [Karpenter-core](https://sigs.k8s.io/karpenter) APIs کو سپورٹ کرتے ہوں۔

## انسٹالیشن

براہ کرم انسٹالیشن کی رہنمائی [یہاں](https://github.com/Azure/kaito/blob/main/docs/installation.md) دیکھیں۔

## کوئیک اسٹارٹ انفرنس Phi-3
[سمپل کوڈ انفرنس Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ورک اسپیس کی حیثیت کو درج ذیل کمانڈ کے ذریعے ٹریک کیا جا سکتا ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے ڈپلائمنٹ ہو چکا ہو گا۔

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، کوئی بھی انفرنس سروس کا کلسٹر آئی پی تلاش کر سکتا ہے اور کلسٹر میں سروس اینڈ پوائنٹ کو ٹیسٹ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کر سکتا ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## کوئیک اسٹارٹ انفرنس Phi-3 ایڈاپٹرز کے ساتھ

Kaito انسٹال کرنے کے بعد، درج ذیل کمانڈز کو استعمال کر کے انفرنس سروس شروع کی جا سکتی ہے۔

[سمپل کوڈ انفرنس Phi-3 ایڈاپٹرز کے ساتھ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ورک اسپیس کی حیثیت کو درج ذیل کمانڈ کے ذریعے ٹریک کیا جا سکتا ہے۔ جب WORKSPACEREADY کالم `True` ہو جائے، تو ماڈل کامیابی سے ڈپلائمنٹ ہو چکا ہو گا۔

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

اس کے بعد، کوئی بھی انفرنس سروس کا کلسٹر آئی پی تلاش کر سکتا ہے اور کلسٹر میں سروس اینڈ پوائنٹ کو ٹیسٹ کرنے کے لیے ایک عارضی `curl` پوڈ استعمال کر سکتا ہے۔

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔