## Kaito के साथ फाइन-ट्यूनिंग

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML इन्फरेंस मॉडल की डिप्लॉयमेंट को स्वचालित करता है।

Kaito में अधिकांश मुख्यधारा की मॉडल डिप्लॉयमेंट मेथडोलॉजीज़ की तुलना में, जो वर्चुअल मशीन इंफ्रास्ट्रक्चर पर आधारित होती हैं, निम्नलिखित प्रमुख विशेषताएँ हैं:

- कंटेनर इमेज का उपयोग करके मॉडल फाइल्स को मैनेज करना। एक HTTP सर्वर प्रदान किया जाता है जो मॉडल लाइब्रेरी का उपयोग करके इन्फरेंस कॉल्स को निष्पादित करता है।
- GPU हार्डवेयर के अनुरूप डिप्लॉयमेंट पैरामीटर्स को ट्यून करने से बचने के लिए प्रीसेट कॉन्फ़िगरेशन प्रदान करना।
- मॉडल की आवश्यकताओं के आधार पर GPU नोड्स का ऑटो-प्रोविजन।
- यदि लाइसेंस अनुमति देता है तो बड़े मॉडल इमेज को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करना।

Kaito का उपयोग करके, Kubernetes में बड़े AI इन्फरेंस मॉडल को ऑनबोर्ड करने का वर्कफ़्लो काफी हद तक सरल हो जाता है।


## आर्किटेक्चर

Kaito क्लासिक Kubernetes Custom Resource Definition (CRD)/कंट्रोलर डिज़ाइन पैटर्न का पालन करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स को मैनेज करता है जो GPU आवश्यकताओं और इन्फरेंस स्पेसिफिकेशन को परिभाषित करता है। Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्स को समेटकर डिप्लॉयमेंट को स्वचालित करते हैं।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito आर्किटेक्चर" alt="Kaito आर्किटेक्चर">
</div>

ऊपर का चित्र Kaito आर्किटेक्चर का ओवरव्यू प्रस्तुत करता है। इसके मुख्य घटक निम्नलिखित हैं:

- **Workspace कंट्रोलर**: यह `workspace` कस्टम रिसोर्स को समेटता है, `machine` (नीचे समझाया गया है) कस्टम रिसोर्स को ट्रिगर करने के लिए क्रिएट करता है ताकि नोड ऑटो-प्रोविजनिंग हो सके, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर इन्फरेंस वर्कलोड (`deployment` या `statefulset`) क्रिएट करता है।
- **Node प्रोविज़नर कंट्रोलर**: इस कंट्रोलर का नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह `machine` CRD का उपयोग करता है, जो [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न हुआ है, Workspace कंट्रोलर के साथ इंटरैक्ट करने के लिए। यह Azure Kubernetes Service (AKS) APIs के साथ इंटीग्रेट करता है ताकि AKS क्लस्टर में नए GPU नोड्स को जोड़ा जा सके।  
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन-सोर्स घटक है। इसे अन्य कंट्रोलर्स से बदला जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) APIs को सपोर्ट करते हों।

## ओवरव्यू वीडियो
[Kaito डेमो देखें](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## इंस्टॉलेशन

कृपया इंस्टॉलेशन गाइडेंस [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## क्विक स्टार्ट

Kaito को इंस्टॉल करने के बाद, निम्नलिखित कमांड्स का उपयोग करके एक फाइन-ट्यूनिंग सर्विस शुरू की जा सकती है।

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

Workspace की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाता है, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, क्लस्टर IP से इन्फरेंस सर्विस को ढूंढा जा सकता है और क्लस्टर में सर्विस एंडपॉइंट का परीक्षण करने के लिए एक टेम्पोरल `curl` पॉड का उपयोग किया जा सकता है।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।