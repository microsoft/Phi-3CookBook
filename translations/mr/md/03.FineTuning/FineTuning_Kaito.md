## काइटोसह फाइन-ट्यूनिंग

[Kaito](https://github.com/Azure/kaito) हा एक ऑपरेटर आहे जो Kubernetes क्लस्टरमध्ये AI/ML इन्फरन्स मॉडेल डिप्लॉयमेंट स्वयंचलित करतो.

काइटोला मुख्य प्रवाहातील वर्च्युअल मशीन इन्फ्रास्ट्रक्चरवर आधारित बहुतेक मॉडेल डिप्लॉयमेंट पद्धतींपेक्षा खालील महत्त्वाच्या वेगळेपणामुळे वेगळे ठरते:

- कंटेनर इमेजेस वापरून मॉडेल फायली व्यवस्थापित करा. मॉडेल लायब्ररी वापरून इन्फरन्स कॉल करण्यासाठी एक http सर्व्हर प्रदान केला जातो.
- GPU हार्डवेअरशी जुळण्यासाठी डिप्लॉयमेंट पॅरामीटर्स ट्यून करण्याची गरज टाळा, कारण पूर्वनिर्धारित कॉन्फिगरेशन्स दिल्या जातात.
- मॉडेलच्या गरजांनुसार GPU नोड्स स्वयंचलितपणे प्रोव्हिजन करा.
- जर परवानगी असेल तर मोठ्या मॉडेल इमेजेस सार्वजनिक Microsoft Container Registry (MCR) मध्ये होस्ट करा.

काइटो वापरून, Kubernetes मध्ये मोठ्या AI इन्फरन्स मॉडेल्सची ऑनबोर्डिंग प्रक्रिया खूप सोपी होते.

## आर्किटेक्चर

काइटो पारंपरिक Kubernetes Custom Resource Definition(CRD)/कंट्रोलर डिझाईन पॅटर्नचा अवलंब करते. वापरकर्ता GPU गरजा आणि इन्फरन्स तपशीलांचे वर्णन करणारा `workspace` कस्टम रिसोर्स व्यवस्थापित करतो. काइटो कंट्रोलर `workspace` कस्टम रिसोर्सशी जुळवून डिप्लॉयमेंट स्वयंचलित करतात.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="काइटो आर्किटेक्चर" alt="काइटो आर्किटेक्चर">
</div>

वरील आकृती काइटो आर्किटेक्चरचे विहंगावलोकन सादर करते. त्याचे प्रमुख घटक खालीलप्रमाणे आहेत:

- **वर्कस्पेस कंट्रोलर**: हे `workspace` कस्टम रिसोर्सशी जुळवते, नोड स्वयंचलित प्रोव्हिजनिंग ट्रिगर करण्यासाठी `machine` (खाली स्पष्ट केले आहे) कस्टम रिसोर्स तयार करते आणि मॉडेलच्या पूर्वनिर्धारित कॉन्फिगरेशन्सवर आधारित इन्फरन्स वर्कलोड (`deployment` किंवा `statefulset`) तयार करते.
- **नोड प्रोव्हिजनर कंट्रोलर**: या कंट्रोलरचे नाव [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) मध्ये *gpu-provisioner* आहे. हे [Karpenter](https://sigs.k8s.io/karpenter) कडून उत्पन्न झालेल्या `machine` CRD चा वापर करून वर्कस्पेस कंट्रोलरसह संवाद साधते. हे Azure Kubernetes Service(AKS) APIs सह समाकलित होते जेणेकरून AKS क्लस्टरमध्ये नवीन GPU नोड्स जोडता येतील.
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) हा एक ओपन सोर्स घटक आहे. तो [Karpenter-core](https://sigs.k8s.io/karpenter) APIs ला समर्थन देणाऱ्या इतर कंट्रोलर्सने बदलला जाऊ शकतो.

## विहंगावलोकन व्हिडिओ
[काइटो डेमो पाहा](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## इन्स्टॉलेशन

कृपया इन्स्टॉलेशन मार्गदर्शनासाठी [येथे](https://github.com/Azure/kaito/blob/main/docs/installation.md) तपासा.

## झटपट सुरुवात

काइटो इन्स्टॉल केल्यानंतर, फाइन-ट्यूनिंग सेवा सुरू करण्यासाठी खालील कमांड्स वापरून पहा.

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

वर्कस्पेसची स्थिती खालील कमांड चालवून ट्रॅक केली जाऊ शकते. जेव्हा WORKSPACEREADY कॉलम `True` होतो, तेव्हा मॉडेल यशस्वीरित्या डिप्लॉय केले गेले आहे.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

यानंतर, क्लस्टरमधील इन्फरन्स सेवेसाठी क्लस्टर आयपी शोधा आणि तात्पुरत्या `curl` पॉडचा वापर करून सेवा एंडपॉइंटची चाचणी करा.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**अस्वीकरण**:  
हा दस्तऐवज मशीन-आधारित AI अनुवाद सेवांचा वापर करून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावण्यास आम्ही जबाबदार राहणार नाही.