## การปรับแต่งด้วย Kaito

[Kaito](https://github.com/Azure/kaito) เป็นตัวดำเนินการที่ช่วยทำให้การปรับใช้โมเดล AI/ML สำหรับการอนุมานในคลัสเตอร์ Kubernetes เป็นไปโดยอัตโนมัติ

Kaito มีความแตกต่างที่สำคัญเมื่อเทียบกับวิธีการปรับใช้โมเดลแบบดั้งเดิมที่สร้างขึ้นบนโครงสร้างพื้นฐานของเครื่องเสมือน ดังนี้:

- จัดการไฟล์โมเดลด้วยภาพคอนเทนเนอร์ โดยมีเซิร์ฟเวอร์ HTTP สำหรับเรียกใช้งานการอนุมานผ่านไลบรารีของโมเดล
- หลีกเลี่ยงการปรับแต่งพารามิเตอร์การปรับใช้ให้เหมาะสมกับฮาร์ดแวร์ GPU โดยใช้การตั้งค่าที่กำหนดไว้ล่วงหน้า
- จัดหาโหนด GPU โดยอัตโนมัติตามข้อกำหนดของโมเดล
- โฮสต์ภาพโมเดลขนาดใหญ่ใน Microsoft Container Registry (MCR) สาธารณะ หากลิขสิทธิ์อนุญาต

ด้วย Kaito ขั้นตอนการนำโมเดล AI สำหรับการอนุมานขนาดใหญ่เข้าสู่ Kubernetes จะง่ายขึ้นอย่างมาก

## สถาปัตยกรรม

Kaito ใช้รูปแบบการออกแบบที่เป็นมาตรฐานของ Kubernetes Custom Resource Definition (CRD) และตัวควบคุม (controller) ผู้ใช้จัดการทรัพยากรแบบกำหนดเอง `workspace` ซึ่งอธิบายข้อกำหนด GPU และการกำหนดค่าการอนุมาน ตัวควบคุมของ Kaito จะทำการปรับใช้โดยอัตโนมัติผ่านการประสานทรัพยากรแบบกำหนดเอง `workspace`
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

รูปด้านบนแสดงภาพรวมของสถาปัตยกรรม Kaito ซึ่งประกอบด้วยองค์ประกอบหลักดังนี้:

- **Workspace controller**: ทำหน้าที่ประสานทรัพยากรแบบกำหนดเอง `workspace` สร้างทรัพยากรแบบกำหนดเอง `machine` (อธิบายด้านล่าง) เพื่อกระตุ้นการจัดหาโหนดอัตโนมัติ และสร้างภาระงานการอนุมาน (`deployment` หรือ `statefulset`) ตามการตั้งค่าของโมเดลที่กำหนดไว้ล่วงหน้า
- **Node provisioner controller**: ตัวควบคุมนี้ชื่อว่า *gpu-provisioner* ใน [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) โดยใช้ `machine` CRD ซึ่งมีต้นกำเนิดจาก [Karpenter](https://sigs.k8s.io/karpenter) เพื่อสื่อสารกับ workspace controller และผสานรวมกับ Azure Kubernetes Service (AKS) API เพื่อเพิ่มโหนด GPU ใหม่ในคลัสเตอร์ AKS 
> หมายเหตุ: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) เป็นส่วนประกอบที่เปิดเผยซอร์สโค้ด และสามารถเปลี่ยนไปใช้ตัวควบคุมอื่นได้หากรองรับ API ของ [Karpenter-core](https://sigs.k8s.io/karpenter)

## วิดีโอภาพรวม
[ชมการสาธิต Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## การติดตั้ง

โปรดดูคำแนะนำการติดตั้ง [ที่นี่](https://github.com/Azure/kaito/blob/main/docs/installation.md)

## เริ่มต้นใช้งาน

หลังจากติดตั้ง Kaito แล้ว สามารถลองใช้คำสั่งต่อไปนี้เพื่อเริ่มต้นบริการปรับแต่ง

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

สามารถติดตามสถานะของ workspace ได้โดยใช้คำสั่งต่อไปนี้ เมื่อคอลัมน์ WORKSPACEREADY กลายเป็น `True` หมายความว่าโมเดลได้รับการปรับใช้เรียบร้อยแล้ว

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

จากนั้นสามารถค้นหา IP ของบริการอนุมานในคลัสเตอร์ และใช้ `curl` pod ชั่วคราวเพื่อตรวจสอบ endpoint ของบริการในคลัสเตอร์

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติด้วย AI แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้น เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้บริการแปลภาษาจากผู้เชี่ยวชาญที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้