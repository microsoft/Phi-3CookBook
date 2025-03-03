## Fine-Tuning עם Kaito 

[Kaito](https://github.com/Azure/kaito) הוא מפעיל (operator) שמבצע אוטומציה לפריסת מודלי חיזוי AI/ML באשכול Kubernetes.

לקייטו יש מספר יתרונות עיקריים בהשוואה לשיטות פריסת מודלים נפוצות המבוססות על תשתיות של מכונות וירטואליות:

- ניהול קבצי מודל באמצעות תמונות קונטיינר. שרת HTTP מסופק לביצוע קריאות חיזוי בעזרת ספריית המודל.
- הימנעות מכוונון פרמטרי פריסה להתאמה לחומרת GPU על ידי מתן תצורות מוגדרות מראש.
- פריסה אוטומטית של צמתי GPU בהתאם לדרישות המודל.
- אירוח תמונות מודלים גדולות ברישום הקונטיינרים הציבורי של Microsoft (MCR) אם הרישיון מאפשר זאת.

באמצעות קייטו, תהליך השילוב של מודלים גדולים לחיזוי AI באשכול Kubernetes הופך לפשוט בהרבה.

## ארכיטקטורה

קייטו פועל לפי תבנית העיצוב הקלאסית של Kubernetes Custom Resource Definition (CRD)/controller. המשתמש מנהל משאב מותאם אישית מסוג `workspace` שמתאר את דרישות ה-GPU ואת מפרט החיזוי. בקרי קייטו מבצעים אוטומציה לפריסה על ידי סנכרון המשאב המותאם אישית `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="ארכיטקטורת קייטו" alt="ארכיטקטורת קייטו">
</div>

התרשים לעיל מציג את סקירת הארכיטקטורה של קייטו. הרכיבים העיקריים שלו כוללים:

- **בקר מרחב עבודה (Workspace controller)**: מסנכרן את המשאב המותאם אישית `workspace`, יוצר משאבים מותאמים אישית מסוג `machine` (מוסבר בהמשך) לצורך הפעלת פריסה אוטומטית של צמתים, ויוצר את עומס החיזוי (`deployment` או `statefulset`) בהתבסס על תצורות המודל המוגדרות מראש.
- **בקר פריסת צמתים (Node provisioner controller)**: שם הבקר הוא *gpu-provisioner* ב-[תרשים ההלם של gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). הוא משתמש ב-CRD מסוג `machine` שמקורו ב-[Karpenter](https://sigs.k8s.io/karpenter) כדי לתקשר עם בקר מרחב העבודה. הוא משתלב עם ממשקי ה-API של Azure Kubernetes Service (AKS) כדי להוסיף צמתי GPU חדשים לאשכול ה-AKS.
> הערה: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) הוא רכיב בקוד פתוח. ניתן להחליפו בבקרים אחרים אם הם תומכים בממשקי ה-API של [Karpenter-core](https://sigs.k8s.io/karpenter).

## סרטון סקירה 
[צפו בהדגמת קייטו](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## התקנה

אנא עיינו בהנחיות ההתקנה [כאן](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## התחלה מהירה

לאחר התקנת קייטו, ניתן לנסות את הפקודות הבאות כדי להפעיל שירות כוונון עדין.

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

ניתן לעקוב אחר מצב מרחב העבודה על ידי הפעלת הפקודה הבאה. כאשר העמודה WORKSPACEREADY הופכת ל-`True`, המודל נפרס בהצלחה.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

לאחר מכן, ניתן למצוא את הכתובת הפנימית של שירות החיזוי ולהשתמש ב-pod זמני מסוג `curl` כדי לבדוק את נקודת הקצה של השירות בתוך האשכול.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.