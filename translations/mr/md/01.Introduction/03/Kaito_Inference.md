## Kaito सह इन्फरन्स

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML इन्फरन्स मॉडेल डिप्लॉयमेंट स्वयंचलित करतो.

Kaito च्या खालील महत्त्वाच्या वैशिष्ट्यांमुळे तो पारंपरिक वर्च्युअल मशीन इन्फ्रास्ट्रक्चरवर आधारित इतर मुख्य मॉडेल डिप्लॉयमेंट पद्धतींपेक्षा वेगळा ठरतो:

- कंटेनर इमेजेस वापरून मॉडेल फायली व्यवस्थापित करा. मॉडेल लायब्ररी वापरून इन्फरन्स कॉल करण्यासाठी http सर्व्हर पुरवला जातो.
- GPU हार्डवेअरशी जुळण्यासाठी डिप्लॉयमेंट पॅरामीटर्स ट्यून करण्याची गरज नाही, कारण पूर्वनिर्धारित कॉन्फिगरेशन्स पुरवली जातात.
- मॉडेलच्या गरजांनुसार GPU नोड्स आपोआप प्रोव्हिजन करा.
- परवाना परवानगी असल्यास मोठ्या मॉडेल इमेजेस सार्वजनिक Microsoft Container Registry (MCR) मध्ये होस्ट करा.

Kaito वापरून, Kubernetes मध्ये मोठ्या AI इन्फरन्स मॉडेल्स डिप्लॉय करण्याची प्रक्रिया खूप सोपी होते.

## आर्किटेक्चर

Kaito पारंपरिक Kubernetes Custom Resource Definition(CRD)/कंट्रोलर डिझाईन पॅटर्नचे अनुसरण करतो. वापरकर्ता GPU आवश्यकतांशी संबंधित आणि इन्फरन्स तपशील वर्णन करणारा `workspace` कस्टम रिसोर्स व्यवस्थापित करतो. Kaito कंट्रोलर्स `workspace` कस्टम रिसोर्सशी ताळमेळ साधून डिप्लॉयमेंट स्वयंचलित करतात.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

वरील आकृती Kaito आर्किटेक्चरचा आढावा दर्शवते. त्याचे मुख्य घटक खालीलप्रमाणे आहेत:

- **Workspace कंट्रोलर**: तो `workspace` कस्टम रिसोर्सशी ताळमेळ साधतो, `machine` (खाली स्पष्ट केले आहे) कस्टम रिसोर्सेस तयार करून नोड ऑटो प्रोव्हिजनिंग ट्रिगर करतो, आणि मॉडेलच्या पूर्वनिर्धारित कॉन्फिगरेशन्सवर आधारित इन्फरन्स वर्कलोड (`deployment` किंवा `statefulset`) तयार करतो.
- **Node provisioner कंट्रोलर**: या कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. तो [Karpenter](https://sigs.k8s.io/karpenter) पासून आलेल्या `machine` CRD चा वापर करून Workspace कंट्रोलरशी संवाद साधतो. Azure Kubernetes Service(AKS) APIs शी एकत्रित होऊन AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडतो.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) हा एक ओपन सोर्स घटक आहे. जर इतर कंट्रोलर्स [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ला सपोर्ट करत असतील, तर त्यांचा पर्याय म्हणून वापर करता येतो.

## इंस्टॉलेशन

कृपया इंस्टॉलेशन मार्गदर्शनासाठी [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) पहा.

## Phi-3 इन्फरन्स जलद सुरुवात

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

Workspace ची स्थिती खालील कमांड चालवून ट्रॅक करता येते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीरित्या डिप्लॉय झाले आहे.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, क्लस्टरमधील इन्फरन्स सर्व्हिसचा क्लस्टर ip शोधता येईल आणि एक तात्पुरता `curl` पॅड वापरून क्लस्टरमधील सर्व्हिस एंडपॉईंटची चाचणी घेता येईल.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Phi-3 इन्फरन्स अ‍ॅडॅप्टर्ससह जलद सुरुवात

Kaito इंस्टॉल केल्यानंतर, इन्फरन्स सर्व्हिस सुरू करण्यासाठी खालील कमांड वापरून पाहू शकता.

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

Workspace ची स्थिती खालील कमांड चालवून ट्रॅक करता येते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीरित्या डिप्लॉय झाले आहे.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, क्लस्टरमधील इन्फरन्स सर्व्हिसचा क्लस्टर ip शोधता येईल आणि एक तात्पुरता `curl` पॅड वापरून क्लस्टरमधील सर्व्हिस एंडपॉईंटची चाचणी घेता येईल.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित एआय भाषांतर सेवांचा वापर करून भाषांतरित करण्यात आले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.