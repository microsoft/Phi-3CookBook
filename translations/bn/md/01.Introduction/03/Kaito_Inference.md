## কাইটো দিয়ে ইনফারেন্স

[Kaito](https://github.com/Azure/kaito) হলো একটি অপারেটর যা Kubernetes ক্লাস্টারে AI/ML ইনফারেন্স মডেল ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

কাইটো মূলধারার ভার্চুয়াল মেশিন ইনফ্রাস্ট্রাকচারের উপর ভিত্তি করে তৈরি মডেল ডিপ্লয়মেন্ট পদ্ধতির তুলনায় নিম্নলিখিত গুরুত্বপূর্ণ পার্থক্যগুলো প্রদান করে:

- কনটেইনার ইমেজ ব্যবহার করে মডেল ফাইল ম্যানেজ করা। মডেল লাইব্রেরি ব্যবহার করে ইনফারেন্স কল সম্পাদনের জন্য একটি HTTP সার্ভার সরবরাহ করা হয়।
- প্রিসেট কনফিগারেশন প্রদান করে GPU হার্ডওয়্যারের সাথে মানানসই ডিপ্লয়মেন্ট প্যারামিটার টিউনিং এড়ানো।
- মডেলের প্রয়োজন অনুযায়ী স্বয়ংক্রিয়ভাবে GPU নোড প্রভিশন করা।
- যদি লাইসেন্স অনুমতি দেয়, তবে পাবলিক Microsoft Container Registry (MCR)-এ বড় মডেল ইমেজ হোস্ট করা।

কাইটো ব্যবহার করে, Kubernetes-এ বড় AI ইনফারেন্স মডেল অনবোর্ডিংয়ের কার্যপ্রণালী অনেকটাই সহজ হয়ে যায়। 

## আর্কিটেকচার

কাইটো ক্লাসিক Kubernetes Custom Resource Definition(CRD)/কন্ট্রোলার ডিজাইন প্যাটার্ন অনুসরণ করে। ব্যবহারকারী একটি `workspace` কাস্টম রিসোর্স পরিচালনা করেন যা GPU প্রয়োজনীয়তা এবং ইনফারেন্স স্পেসিফিকেশন বর্ণনা করে। কাইটো কন্ট্রোলার `workspace` কাস্টম রিসোর্স সমন্বয় করে ডিপ্লয়মেন্ট স্বয়ংক্রিয় করে।

<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

উপরের চিত্রটি কাইটো আর্কিটেকচারের সার্বিক চিত্র উপস্থাপন করে। এর প্রধান উপাদানগুলো হলো:

- **ওয়ার্কস্পেস কন্ট্রোলার**: এটি `workspace` কাস্টম রিসোর্স সমন্বয় করে, `machine` (নীচে ব্যাখ্যা করা হয়েছে) কাস্টম রিসোর্স তৈরি করে নোড স্বয়ংক্রিয় প্রভিশনিং ট্রিগার করার জন্য এবং মডেলের প্রিসেট কনফিগারেশনের উপর ভিত্তি করে ইনফারেন্স ওয়ার্কলোড (`deployment` বা `statefulset`) তৈরি করে।
- **নোড প্রভিশনার কন্ট্রোলার**: এই কন্ট্রোলারের নাম হলো *gpu-provisioner* যা [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)-এ পাওয়া যায়। এটি [Karpenter](https://sigs.k8s.io/karpenter) থেকে উদ্ভূত `machine` CRD ব্যবহার করে ওয়ার্কস্পেস কন্ট্রোলারের সাথে যোগাযোগ করে। এটি Azure Kubernetes Service(AKS) API-এর সাথে ইন্টিগ্রেট করে নতুন GPU নোডগুলো AKS ক্লাস্টারে যোগ করে।
> [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) একটি ওপেন সোর্সড কম্পোনেন্ট। এটি অন্যান্য কন্ট্রোলার দ্বারা প্রতিস্থাপিত হতে পারে যদি তারা [Karpenter-core](https://sigs.k8s.io/karpenter) API সমর্থন করে।

## ইনস্টলেশন

দয়া করে ইনস্টলেশন নির্দেশিকা [এখানে](https://github.com/Azure/kaito/blob/main/docs/installation.md) দেখুন।

## দ্রুত শুরু ইনফারেন্স Phi-3
[নমুনা কোড ইনফারেন্স Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

ওয়ার্কস্পেস স্ট্যাটাস ট্র্যাক করতে নিচের কমান্ডটি চালানো যেতে পারে। যখন WORKSPACEREADY কলাম `True` দেখায়, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ক্লাস্টার আইপিতে ইনফারেন্স সার্ভিসটি খুঁজে বের করুন এবং ক্লাস্টারে সার্ভিস এন্ডপয়েন্ট পরীক্ষা করতে একটি সাময়িক `curl` পড ব্যবহার করুন।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## অ্যাডাপ্টার সহ দ্রুত শুরু ইনফারেন্স Phi-3

কাইটো ইনস্টল করার পর, ইনফারেন্স সার্ভিস শুরু করতে নিচের কমান্ডগুলো ব্যবহার করা যেতে পারে।

[নমুনা কোড ইনফারেন্স Phi-3 অ্যাডাপ্টার সহ](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

ওয়ার্কস্পেস স্ট্যাটাস ট্র্যাক করতে নিচের কমান্ডটি চালানো যেতে পারে। যখন WORKSPACEREADY কলাম `True` দেখায়, তখন মডেল সফলভাবে ডিপ্লয় হয়েছে।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

এরপর, ক্লাস্টার আইপিতে ইনফারেন্স সার্ভিসটি খুঁজে বের করুন এবং ক্লাস্টারে সার্ভিস এন্ডপয়েন্ট পরীক্ষা করতে একটি সাময়িক `curl` পড ব্যবহার করুন।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট যে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।