## การใช้งาน Kaito 

[Kaito](https://github.com/Azure/kaito) เป็นโอเปอเรเตอร์ที่ช่วยทำให้การปรับใช้โมเดล AI/ML สำหรับการอนุมานใน Kubernetes cluster เป็นไปโดยอัตโนมัติ

Kaito มีจุดเด่นที่แตกต่างจากวิธีการปรับใช้โมเดลแบบดั้งเดิมที่ใช้โครงสร้างพื้นฐานแบบ Virtual Machine ดังนี้:

- จัดการไฟล์โมเดลโดยใช้ container images พร้อมทั้งมี http server สำหรับเรียกใช้งานโมเดล
- ลดความยุ่งยากในการปรับแต่งพารามิเตอร์สำหรับฮาร์ดแวร์ GPU โดยมีการตั้งค่าที่เตรียมไว้ล่วงหน้า
- จัดเตรียม GPU nodes โดยอัตโนมัติตามความต้องการของโมเดล
- โฮสต์ภาพโมเดลขนาดใหญ่ใน Microsoft Container Registry (MCR) สาธารณะ หากได้รับอนุญาตจากลิขสิทธิ์

ด้วย Kaito กระบวนการเริ่มต้นใช้งานโมเดล AI ขนาดใหญ่ใน Kubernetes จะง่ายขึ้นอย่างมาก


## สถาปัตยกรรม

Kaito ใช้รูปแบบการออกแบบ Custom Resource Definition(CRD)/controller ของ Kubernetes แบบคลาสสิก ผู้ใช้จะจัดการทรัพยากร `workspace` ซึ่งอธิบายถึงความต้องการ GPU และข้อกำหนดการอนุมาน Kaito controllers จะดำเนินการปรับใช้โดยการทำให้ทรัพยากร `workspace` สอดคล้องกัน
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

ภาพด้านบนแสดงภาพรวมของสถาปัตยกรรม Kaito ซึ่งประกอบด้วยส่วนประกอบหลักดังนี้:

- **Workspace controller**: ทำหน้าที่ปรับทรัพยากร `workspace` ให้สอดคล้องกัน สร้างทรัพยากร `machine` (อธิบายด้านล่าง) เพื่อกระตุ้นการจัดเตรียมโหนดโดยอัตโนมัติ และสร้างงานอนุมาน (`deployment` หรือ `statefulset`) ตามการตั้งค่าโมเดลที่เตรียมไว้
- **Node provisioner controller**: ตัวควบคุมนี้มีชื่อว่า *gpu-provisioner* ใน [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) โดยใช้ CRD `machine` ที่มาจาก [Karpenter](https://sigs.k8s.io/karpenter) เพื่อติดต่อกับ workspace controller และผสานรวมกับ Azure Kubernetes Service(AKS) APIs เพื่อเพิ่ม GPU nodes ใหม่เข้าไปในคลัสเตอร์ AKS  
> หมายเหตุ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) เป็นส่วนประกอบโอเพนซอร์สที่สามารถเปลี่ยนไปใช้ตัวควบคุมอื่นได้ หากรองรับ API ของ [Karpenter-core](https://sigs.k8s.io/karpenter)

## การติดตั้ง

โปรดตรวจสอบคำแนะนำการติดตั้ง [ที่นี่](https://github.com/Azure/kaito/blob/main/docs/installation.md)

## เริ่มต้นใช้งาน Inference Phi-3
[ตัวอย่างโค้ด Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

สามารถติดตามสถานะของ workspace ได้โดยรันคำสั่งต่อไปนี้ เมื่อคอลัมน์ WORKSPACEREADY แสดง `True` หมายความว่าโมเดลได้ถูกปรับใช้งานสำเร็จแล้ว

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

จากนั้นสามารถหา cluster ip ของบริการอนุมานและใช้ `curl` pod ชั่วคราวเพื่อตรวจสอบ service endpoint ในคลัสเตอร์

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## เริ่มต้นใช้งาน Inference Phi-3 พร้อม adapters

หลังจากติดตั้ง Kaito สามารถลองใช้คำสั่งต่อไปนี้เพื่อเริ่มต้นบริการอนุมาน

[ตัวอย่างโค้ด Inference Phi-3 พร้อม Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

สามารถติดตามสถานะของ workspace ได้โดยรันคำสั่งต่อไปนี้ เมื่อคอลัมน์ WORKSPACEREADY แสดง `True` หมายความว่าโมเดลได้ถูกปรับใช้งานสำเร็จแล้ว

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

จากนั้นสามารถหา cluster ip ของบริการอนุมานและใช้ `curl` pod ชั่วคราวเพื่อตรวจสอบ service endpoint ในคลัสเตอร์

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติที่ใช้ปัญญาประดิษฐ์ (AI) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่คลาดเคลื่อนซึ่งเกิดจากการใช้การแปลนี้