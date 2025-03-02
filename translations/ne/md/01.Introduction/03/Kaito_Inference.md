## Kaito सँग Inference

[Kaito](https://github.com/Azure/kaito) एउटा अपरेटर हो जसले Kubernetes क्लस्टरमा AI/ML inference मोडेल तैनातीलाई स्वचालित बनाउँछ।

Kaito ले मुख्यधाराको भर्चुअल मेसिन पूर्वाधारमा आधारित मोडेल तैनाती विधिहरूसँग तुलना गर्दा निम्न प्रमुख भिन्नताहरू प्रदान गर्दछ:

- कन्टेनर इमेजहरूको प्रयोग गरेर मोडेल फाइलहरू व्यवस्थापन गर्नु। मोडेल पुस्तकालय प्रयोग गरेर inference कलहरू गर्नका लागि एउटा HTTP सर्भर प्रदान गरिएको छ।
- GPU हार्डवेयरको लागि तैनाती प्यारामिटरहरू ट्युन गर्न आवश्यक पर्दैन; यसको सट्टा पूर्वनिर्धारित कन्फिगरेसनहरू उपलब्ध गराइन्छ।
- मोडेल आवश्यकताहरूको आधारमा GPU नोडहरू स्वचालित रूपमा प्रावधान गर्ने।
- यदि लाइसेन्सले अनुमति दिन्छ भने, सार्वजनिक Microsoft Container Registry (MCR) मा ठूला मोडेल इमेजहरू होस्ट गर्ने।

Kaito प्रयोग गर्दा, Kubernetes मा ठूला AI inference मोडेलहरू समायोजन गर्ने कार्यप्रवाह धेरै हदसम्म सरल हुन्छ।


## आर्किटेक्चर

Kaito ले परम्परागत Kubernetes Custom Resource Definition(CRD)/controller डिजाइन ढाँचा अनुसरण गर्दछ। प्रयोगकर्ताले GPU आवश्यकताहरू र inference विशिष्टता वर्णन गर्ने `workspace` कस्टम स्रोत व्यवस्थापन गर्छ। Kaito कन्ट्रोलरहरूले उक्त `workspace` कस्टम स्रोत समायोजन गरेर तैनातीलाई स्वचालित बनाउँछ।  
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

माथिको चित्रले Kaito को आर्किटेक्चर अवलोकन प्रस्तुत गर्दछ। यसका प्रमुख कम्पोनेन्टहरूमा समावेश छन्:

- **Workspace controller**: यो `workspace` कस्टम स्रोत समायोजन गर्छ, `machine` (तल व्याख्या गरिएको) कस्टम स्रोतहरू सिर्जना गर्छ GPU नोड स्वचालित प्रावधान गर्न ट्रिगर गर्नका लागि, र मोडेलको पूर्वनिर्धारित कन्फिगरेसनहरूका आधारमा inference workload (`deployment` वा `statefulset`) सिर्जना गर्छ।
- **Node provisioner controller**: यो कन्ट्रोलरको नाम [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मा *gpu-provisioner* हो। यसले [Karpenter](https://sigs.k8s.io/karpenter) बाट उत्पन्न `machine` CRD प्रयोग गरेर workspace controller सँग अन्तर्क्रिया गर्छ। यो Azure Kubernetes Service(AKS) APIs सँग एकीकृत हुन्छ र AKS क्लस्टरमा नयाँ GPU नोडहरू थप्छ।
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) एक खुला स्रोत कम्पोनेन्ट हो। यसलाई अन्य कन्ट्रोलरहरूले प्रतिस्थापन गर्न सक्छन् यदि तिनीहरूले [Karpenter-core](https://sigs.k8s.io/karpenter) API हरू समर्थन गर्छन् भने।  

## स्थापना

कृपया स्थापना निर्देशन [यहाँ](https://github.com/Azure/kaito/blob/main/docs/installation.md) हेर्नुहोस्।

## Phi-3 को लागि Quick Start Inference  
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

वर्कस्पेसको स्थिति निम्न कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक तैनात भएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

त्यसपछि, क्लस्टरमा inference सेवाको क्लस्टर ip फेला पार्न सकिन्छ र अस्थायी `curl` pod प्रयोग गरेर क्लस्टरमा सेवा endpoint परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Adapters सँग Phi-3 को लागि Quick Start Inference

Kaito स्थापना गरेपछि, निम्न कमाण्डहरू चलाएर inference सेवा सुरु गर्न सकिन्छ।

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

वर्कस्पेसको स्थिति निम्न कमाण्ड चलाएर ट्र्याक गर्न सकिन्छ। जब WORKSPACEREADY स्तम्भ `True` हुन्छ, मोडेल सफलतापूर्वक तैनात भएको हुन्छ।

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

त्यसपछि, क्लस्टरमा inference सेवाको क्लस्टर ip फेला पार्न सकिन्छ र अस्थायी `curl` pod प्रयोग गरेर क्लस्टरमा सेवा endpoint परीक्षण गर्न सकिन्छ।

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असत्यताहरू हुन सक्छ। मूल भाषामा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।