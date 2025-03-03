## Fine-Tuning dengan Kaito

[Kaito](https://github.com/Azure/kaito) adalah sebuah operator yang mengotomatisasi penerapan model inferensi AI/ML dalam kluster Kubernetes.

Kaito memiliki beberapa perbedaan utama dibandingkan dengan sebagian besar metode penerapan model yang dibangun di atas infrastruktur mesin virtual:

- Mengelola file model menggunakan image container. Sebuah server http disediakan untuk melakukan panggilan inferensi menggunakan pustaka model.
- Menghindari pengaturan parameter penerapan agar sesuai dengan perangkat keras GPU dengan menyediakan konfigurasi bawaan.
- Secara otomatis menyediakan node GPU berdasarkan kebutuhan model.
- Menyimpan image model besar di Microsoft Container Registry (MCR) publik jika lisensinya memungkinkan.

Dengan menggunakan Kaito, alur kerja untuk mengintegrasikan model inferensi AI besar dalam Kubernetes menjadi jauh lebih sederhana.

## Arsitektur

Kaito mengikuti pola desain klasik Kubernetes Custom Resource Definition (CRD)/controller. Pengguna mengelola sebuah sumber daya khusus `workspace` yang menjelaskan kebutuhan GPU dan spesifikasi inferensi. Controller Kaito akan mengotomatisasi penerapan dengan menyelaraskan sumber daya khusus `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arsitektur Kaito" alt="Arsitektur Kaito">
</div>

Gambar di atas menunjukkan gambaran umum arsitektur Kaito. Komponen utamanya terdiri dari:

- **Workspace controller**: Menyelaraskan sumber daya khusus `workspace`, membuat sumber daya khusus `machine` (dijelaskan di bawah) untuk memicu penyediaan node otomatis, dan membuat beban kerja inferensi (`deployment` atau `statefulset`) berdasarkan konfigurasi bawaan model.
- **Node provisioner controller**: Nama controller ini adalah *gpu-provisioner* dalam [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Controller ini menggunakan CRD `machine` yang berasal dari [Karpenter](https://sigs.k8s.io/karpenter) untuk berinteraksi dengan workspace controller. Controller ini terintegrasi dengan API Azure Kubernetes Service (AKS) untuk menambahkan node GPU baru ke kluster AKS.
> Catatan: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) adalah komponen open source. Komponen ini dapat diganti dengan controller lain jika mendukung API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video Ringkasan 
[Tonton Demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalasi

Silakan cek panduan instalasi [di sini](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Panduan Cepat

Setelah menginstal Kaito, Anda dapat mencoba perintah berikut untuk memulai layanan fine-tuning.

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

Status workspace dapat dilacak dengan menjalankan perintah berikut. Ketika kolom WORKSPACEREADY menjadi `True`, model telah berhasil diterapkan.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Selanjutnya, Anda dapat menemukan IP kluster layanan inferensi dan menggunakan pod `curl` sementara untuk menguji endpoint layanan di dalam kluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memberikan hasil yang akurat, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.