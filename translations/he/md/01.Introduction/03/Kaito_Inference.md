## הסקה עם Kaito

[Kaito](https://github.com/Azure/kaito) הוא מפעיל שמבצע אוטומציה לפריסת מודלים של AI/ML בסביבת Kubernetes.

ל-Kaito יש את ההבדלים המרכזיים הבאים בהשוואה לרוב שיטות הפריסה המסורתיות שמבוססות על תשתיות מכונות וירטואליות:

- ניהול קבצי מודל באמצעות תמונות קונטיינר. שרת HTTP מסופק כדי לבצע קריאות הסקה באמצעות ספריית המודל.
- הימנעות מכוונון פרמטרי פריסה להתאמה לחומרת GPU על ידי אספקת תצורות מוגדרות מראש.
- הקצאה אוטומטית של צמתים עם GPU בהתבסס על דרישות המודל.
- אירוח תמונות מודלים גדולות ב-Microsoft Container Registry (MCR) הציבורי אם הרישיון מאפשר זאת.

באמצעות Kaito, תהליך העבודה של שילוב מודלי הסקה גדולים ב-Kubernetes הופך לפשוט בהרבה.

## ארכיטקטורה

Kaito פועל לפי תבנית העיצוב הקלאסית של Kubernetes Custom Resource Definition (CRD)/controller. המשתמש מנהל משאב מותאם אישית מסוג `workspace` שמתאר את דרישות ה-GPU ואת מפרט ההסקה. בקרי Kaito יבצעו אוטומציה לפריסה על ידי סנכרון המשאב המותאם אישית `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="ארכיטקטורת Kaito" alt="ארכיטקטורת Kaito">
</div>

התרשים לעיל מציג את סקירת הארכיטקטורה של Kaito. הרכיבים המרכזיים שלו כוללים:

- **בקר סביבת עבודה**: מסנכרן את המשאב המותאם אישית `workspace`, יוצר משאבים מותאמים אישית `machine` (מוסבר בהמשך) כדי להפעיל הקצאה אוטומטית של צמתים, ויוצר עומס עבודה להסקה (`deployment` או `statefulset`) בהתבסס על תצורות המודל המוגדרות מראש.
- **בקר מקצה צמתים**: שם הבקר הוא *gpu-provisioner* ב-[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-`machine` CRD שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר סביבת העבודה. הוא משתלב עם ממשקי ה-API של Azure Kubernetes Service (AKS) כדי להוסיף צמתים חדשים עם GPU לאשכול AKS.
> הערה: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליף אותו בבקרים אחרים אם הם תומכים ב-[Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## התקנה

אנא עיינו בהנחיות ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה: הסקה Phi-3
[דוגמת קוד הסקה Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ניתן לעקוב אחר מצב סביבת העבודה על ידי הפעלת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל נפרס בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את ה-cluster ip של שירות ההסקה ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## התחלה מהירה: הסקה Phi-3 עם מתאמים

לאחר התקנת Kaito, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות הסקה.

[דוגמת קוד הסקה Phi-3 עם מתאמים](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ניתן לעקוב אחר מצב סביבת העבודה על ידי הפעלת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל נפרס בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את ה-cluster ip של שירות ההסקה ולהשתמש בפוד `curl` זמני כדי לבדוק את נקודת הקצה של השירות באשכול.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בשירותי תרגום מקצועיים על ידי בני אדם. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעת מהשימוש בתרגום זה.