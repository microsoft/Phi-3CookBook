## Kaito को साथ Fine-Tuning 

[Kaito](https://github.com/Azure/kaito) एक अपरेटर हो, जसले Kubernetes क्लस्टरमा AI/ML इन्फेरेन्स मोडेलको डिप्लोयमेन्टलाई स्वचालित बनाउँछ।

Kaito ले अधिकांश मुख्यधाराको भर्चुअल मेसिन इन्फ्रास्ट्रक्चरमा आधारित मोडेल डिप्लोयमेन्ट विधिहरूसँग तुलना गर्दा निम्न प्रमुख विशेषताहरू प्रदान गर्दछ:

- मोडेल फाइलहरूलाई कन्टेनर इमेजहरूको माध्यमबाट व्यवस्थापन गर्ने। मोडेल लाइब्रेरी प्रयोग गरेर इन्फेरेन्स कलहरू गर्नको लागि एउटा HTTP सर्भर प्रदान गरिन्छ।
- GPU हार्डवेयरसँग मिलाउनको लागि डिप्लोयमेन्ट प्यारामिटरहरू ट्युन गर्न नपर्ने, किनभने प्रिसेट कन्फिगरेसनहरू उपलब्ध गराइन्छ।
- मोडेल आवश्यकताहरूको आधारमा GPU नोडहरू स्वचालित रूपमा प्रोभिजन गर्ने।
- ठूला मोडेल इमेजहरू, यदि लाइसेन्सले अनुमति दिएमा, सार्वजनिक Microsoft Container Registry (MCR) मा होस्ट गर्ने।

Kaito को प्रयोग गरेर, Kubernetes मा ठूला AI इन्फेरेन्स मोडेलहरूलाई अनबोर्ड गर्ने कार्यप्रवाह धेरै सजिलो बनाइन्छ।

## आर्किटेक्चर

Kaito ले क्लासिक Kubernetes Custom Resource Definition (CRD)/कन्ट्रोलर डिजाइन ढाँचा अनुसरण गर्दछ। प्रयोगकर्ताले GPU आवश्यकताहरू र इन्फेरेन्स स्पेसिफिकेसन वर्णन गर्ने `workspace` कस्टम रिसोर्स व्यवस्थापन गर्छन्। Kaito कन्ट्रोलरहरूले `workspace` कस्टम रिसोर्सलाई समेटेर डिप्लोयमेन्टलाई स्वचालित बनाउँछन्।
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

माथिको चित्रले Kaito को आर्किटेक्चरको अवलोकन प्रस्तुत गर्दछ। यसका मुख्य कम्पोनेन्टहरूमा समावेश छन्:

- **Workspace controller**: यो `workspace` कस्टम रिसोर्सलाई समेट्छ, `machine` (तल व्याख्या गरिएको) कस्टम रिसोर्सहरू सिर्जना गरेर नोड स्वचालित प्रोभिजनिंग सुरु गर्छ, र मोडेल प्रिसेट कन्फिगरेसनको आधारमा इन्फेरेन्स वर्कलोड (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: यस कन्ट्रोलरको नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले [Karpenter](https://sigs.k8s.io/karpenter) बाट उत्पन्न `machine` CRD प्रयोग गरेर Workspace controller सँग अन्तर्क्रिया गर्छ। यो Azure Kubernetes Service (AKS) API हरूसँग एकीकृत भएर AKS क्लस्टरमा नयाँ GPU नोडहरू थप्छ।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एउटा ओपन सोर्स गरिएको कम्पोनेन्ट हो। यदि अन्य कन्ट्रोलरहरूले [Karpenter-core](https://sigs.k8s.io/karpenter) API हरूलाई समर्थन गर्छन् भने यसलाई प्रतिस्थापन गर्न सकिन्छ।

## अवलोकन भिडियो 
[Kaito Demo हेर्नुहोस्](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## इन्स्टलेसन

कृपया इन्स्टलेसन गाइड [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) हेर्नुहोस्।

## छिटो सुरु

Kaito इन्स्टल गरेपछि, निम्न आदेशहरू प्रयोग गरेर फाइन-ट्युनिङ सेवा सुरु गर्न सकिन्छ।

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

Workspace को स्थिति निम्न आदेश चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक डिप्लोय भएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

अर्को चरणमा, इन्फेरेन्स सेवाको क्लस्टर IP फेला पार्न सकिन्छ र क्लस्टरभित्र सेवा एन्डपोइन्ट परीक्षण गर्न अस्थायी `curl` पोड प्रयोग गर्न सकिन्छ।

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको छ। हामी यथासम्भव शुद्धता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।