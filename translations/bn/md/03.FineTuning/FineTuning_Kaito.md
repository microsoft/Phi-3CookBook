## কাইটো দিয়ে ফাইন-টিউনিং 

[Kaito](https://github.com/Azure/kaito) একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML ইনফারেন্স মডেলের ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

কাইটো-এর প্রধান বৈশিষ্ট্যসমূহ যা সাধারণ ভার্চুয়াল মেশিন অবকাঠামোর উপর ভিত্তি করে তৈরি মডেল ডিপ্লয়মেন্ট পদ্ধতির থেকে আলাদা:

- মডেল ফাইলগুলো কন্টেইনার ইমেজ ব্যবহার করে ম্যানেজ করা। একটি HTTP সার্ভার প্রদান করা হয় মডেল লাইব্রেরি ব্যবহার করে ইনফারেন্স কল চালানোর জন্য।
- GPU হার্ডওয়্যারের সাথে মানানসই করার জন্য ডিপ্লয়মেন্ট প্যারামিটার টিউন করার প্রয়োজন এড়ানো হয়, কারণ পূর্বনির্ধারিত কনফিগারেশন সরবরাহ করা হয়।
- মডেলের প্রয়োজন অনুযায়ী স্বয়ংক্রিয়ভাবে GPU নোড প্রভিশন করা।
- যদি লাইসেন্স অনুমোদন করে, তবে বড় মডেল ইমেজগুলো পাবলিক Microsoft Container Registry (MCR)-এ হোস্ট করা।

কাইটো ব্যবহার করে Kubernetes-এ বড় AI ইনফারেন্স মডেল অনবোর্ড করার প্রক্রিয়া অনেকটাই সহজ হয়ে যায়। 


## আর্কিটেকচার

কাইটো ক্লাসিক Kubernetes Custom Resource Definition (CRD)/কন্ট্রোলার ডিজাইন প্যাটার্ন অনুসরণ করে। ব্যবহারকারী একটি `workspace` কাস্টম রিসোর্স ম্যানেজ করেন, যা GPU প্রয়োজন এবং ইনফারেন্স স্পেসিফিকেশন বর্ণনা করে। কাইটো কন্ট্রোলারগুলো `workspace` কাস্টম রিসোর্স রিকনসাইল করে ডিপ্লয়মেন্ট স্বয়ংক্রিয়ভাবে সম্পন্ন করে। 
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

উপরের চিত্রটি কাইটো আর্কিটেকচারের ওভারভিউ উপস্থাপন করে। এর প্রধান কম্পোনেন্টগুলো হলো:

- **ওয়ার্কস্পেস কন্ট্রোলার**: এটি `workspace` কাস্টম রিসোর্স রিকনসাইল করে, `machine` (নিচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে নোড স্বয়ংক্রিয় প্রভিশনিং ট্রিগার করতে, এবং মডেলের পূর্বনির্ধারিত কনফিগারেশনের উপর ভিত্তি করে ইনফারেন্স ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **নোড প্রভিশনার কন্ট্রোলার**: এই কন্ট্রোলারের নাম [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-এ *gpu-provisioner*। এটি `machine` CRD ব্যবহার করে, যা [Karpenter](https://sigs.k8s.io/karpenter) থেকে এসেছে, ওয়ার্কস্পেস কন্ট্রোলারের সাথে ইন্টারঅ্যাক্ট করতে। এটি Azure Kubernetes Service (AKS) API-এর সাথে ইন্টিগ্রেটেড হয়ে AKS ক্লাস্টারে নতুন GPU নোড যোগ করে। 
> নোট: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্স কম্পোনেন্ট। এটি অন্য কন্ট্রোলার দিয়ে প্রতিস্থাপন করা যেতে পারে যদি তারা [Karpenter-core](https://sigs.k8s.io/karpenter) API সমর্থন করে। 

## ওভারভিউ ভিডিও 
[কাইটো ডেমো দেখুন](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## ইনস্টলেশন

ইনস্টলেশন নির্দেশাবলী [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) দেখুন।

## দ্রুত শুরু

কাইটো ইনস্টল করার পর, নিচের কমান্ডগুলো ব্যবহার করে একটি ফাইন-টিউনিং সার্ভিস শুরু করা যেতে পারে।

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

ওয়ার্কস্পেসের স্ট্যাটাস ট্র্যাক করার জন্য নিচের কমান্ডটি চালানো যেতে পারে। যখন WORKSPACEREADY কলামটি `True` দেখাবে, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ইনফারেন্স সার্ভিসের ক্লাস্টার আইপি খুঁজে বের করে একটি অস্থায়ী `curl` পড ব্যবহার করে ক্লাস্টারের সার্ভিস এন্ডপয়েন্ট পরীক্ষা করা যেতে পারে।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক কৃত্রিম বুদ্ধিমত্তা অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকেই প্রামাণ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদের সুপারিশ করা হয়। এই অনুবাদ ব্যবহার থেকে উদ্ভূত যে কোনও ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।