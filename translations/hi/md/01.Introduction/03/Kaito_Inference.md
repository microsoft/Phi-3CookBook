## Kaito के साथ इनफेरेंस 

[Kaito](https://github.com/Azure/kaito) एक ऑपरेटर है जो Kubernetes क्लस्टर में AI/ML इनफेरेंस मॉडल को डिप्लॉय करने को स्वचालित करता है।

Kaito की मुख्यधारा की वर्चुअल मशीन इंफ्रास्ट्रक्चर पर आधारित मॉडल डिप्लॉयमेंट विधियों की तुलना में निम्नलिखित प्रमुख विशेषताएं हैं:

- कंटेनर इमेज के माध्यम से मॉडल फाइल्स को प्रबंधित करना। एक HTTP सर्वर प्रदान किया जाता है जो मॉडल लाइब्रेरी का उपयोग करके इनफेरेंस कॉल्स करता है।
- GPU हार्डवेयर के लिए डिप्लॉयमेंट पैरामीटर को ट्यून करने से बचने के लिए प्रीसेट कॉन्फ़िगरेशन प्रदान करता है।
- मॉडल आवश्यकताओं के आधार पर GPU नोड्स को स्वचालित रूप से प्रोविजन करना।
- यदि लाइसेंस अनुमति देता है, तो बड़े मॉडल इमेज को सार्वजनिक Microsoft Container Registry (MCR) में होस्ट करना।

Kaito का उपयोग करके, Kubernetes में बड़े AI इनफेरेंस मॉडल को ऑनबोर्ड करने का वर्कफ़्लो काफी हद तक सरल हो जाता है।


## आर्किटेक्चर

Kaito क्लासिक Kubernetes Custom Resource Definition (CRD)/कंट्रोलर डिज़ाइन पैटर्न का अनुसरण करता है। उपयोगकर्ता एक `workspace` कस्टम रिसोर्स का प्रबंधन करते हैं, जो GPU आवश्यकताओं और इनफेरेंस स्पेसिफिकेशन का वर्णन करता है। Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्स को रिकॉन्साइल करके डिप्लॉयमेंट को स्वचालित करते हैं।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito आर्किटेक्चर" alt="Kaito आर्किटेक्चर">
</div>

ऊपर दिए गए चित्र में Kaito आर्किटेक्चर का अवलोकन प्रस्तुत किया गया है। इसके प्रमुख घटक निम्नलिखित हैं:

- **वर्कस्पेस कंट्रोलर**: यह `workspace` कस्टम रिसोर्स को रिकॉन्साइल करता है, `machine` (नीचे समझाया गया है) कस्टम रिसोर्स बनाता है ताकि नोड ऑटो प्रोविजनिंग को ट्रिगर किया जा सके, और मॉडल प्रीसेट कॉन्फ़िगरेशन के आधार पर इनफेरेंस वर्कलोड (`deployment` या `statefulset`) बनाता है।
- **नोड प्रोविजनर कंट्रोलर**: इस कंट्रोलर का नाम [gpu-provisioner हेल्म चार्ट](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) में *gpu-provisioner* है। यह [Karpenter](https://sigs.k8s.io/karpenter) से उत्पन्न `machine` CRD का उपयोग वर्कस्पेस कंट्रोलर के साथ बातचीत करने के लिए करता है। यह Azure Kubernetes Service (AKS) APIs के साथ एकीकृत होता है ताकि AKS क्लस्टर में नए GPU नोड्स जोड़े जा सकें।  
> नोट: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक ओपन सोर्स घटक है। इसे अन्य कंट्रोलर्स से बदला जा सकता है यदि वे [Karpenter-core](https://sigs.k8s.io/karpenter) APIs का समर्थन करते हैं।

## इंस्टॉलेशन

कृपया इंस्टॉलेशन गाइडेंस [यहां](https://github.com/Azure/kaito/blob/main/docs/installation.md) देखें।

## क्विक स्टार्ट इनफेरेंस Phi-3
[सैंपल कोड इनफेरेंस Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाए, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, क्लस्टर में इनफेरेंस सर्विस का क्लस्टर आईपी खोजा जा सकता है और एक अस्थायी `curl` पॉड का उपयोग करके क्लस्टर में सर्विस एंडपॉइंट का परीक्षण किया जा सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## क्विक स्टार्ट इनफेरेंस Phi-3 विथ अडैप्टर्स

Kaito को इंस्टॉल करने के बाद, निम्नलिखित कमांड्स का उपयोग करके एक इनफेरेंस सर्विस शुरू की जा सकती है।

[सैंपल कोड इनफेरेंस Phi-3 विथ अडैप्टर्स](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

वर्कस्पेस की स्थिति को निम्नलिखित कमांड चलाकर ट्रैक किया जा सकता है। जब WORKSPACEREADY कॉलम `True` हो जाए, तो मॉडल सफलतापूर्वक डिप्लॉय हो चुका होता है।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

इसके बाद, क्लस्टर में इनफेरेंस सर्विस का क्लस्टर आईपी खोजा जा सकता है और एक अस्थायी `curl` पॉड का उपयोग करके क्लस्टर में सर्विस एंडपॉइंट का परीक्षण किया जा सकता है।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में लिखा गया मूल दस्तावेज़ ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।