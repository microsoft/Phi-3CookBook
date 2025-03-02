## Fine-Tuning dengan Kaito

[Kaito](https://github.com/Azure/kaito) adalah operator yang mengotomatisasi penerapan model inferensi AI/ML dalam kluster Kubernetes.

Kaito memiliki perbezaan utama berikut berbanding kebanyakan metodologi penerapan model arus perdana yang dibangunkan berdasarkan infrastruktur mesin maya:

- Menguruskan fail model menggunakan imej kontena. Pelayan http disediakan untuk melakukan panggilan inferensi menggunakan perpustakaan model.
- Mengelakkan keperluan untuk menyesuaikan parameter penerapan agar sesuai dengan perkakasan GPU dengan menyediakan konfigurasi yang telah ditetapkan.
- Penyediaan nod GPU secara automatik berdasarkan keperluan model.
- Menempatkan imej model besar dalam Microsoft Container Registry (MCR) awam jika lesen membenarkan.

Dengan menggunakan Kaito, alur kerja untuk membawa masuk model inferensi AI berskala besar dalam Kubernetes menjadi jauh lebih mudah.


## Seni Bina

Kaito mengikuti corak reka bentuk klasik Kubernetes Custom Resource Definition (CRD)/controller. Pengguna menguruskan sumber khusus `workspace` yang menerangkan keperluan GPU dan spesifikasi inferensi. Pengawal Kaito akan mengotomatisasi penerapan dengan menyelaraskan sumber khusus `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Seni bina Kaito" alt="Seni bina Kaito">
</div>

Rajah di atas menunjukkan gambaran keseluruhan seni bina Kaito. Komponen utamanya terdiri daripada:

- **Pengawal workspace**: Ia menyelaraskan sumber khusus `workspace`, mencipta sumber khusus `machine` (dijelaskan di bawah) untuk memicu penyediaan nod secara automatik, dan mencipta beban kerja inferensi (`deployment` atau `statefulset`) berdasarkan konfigurasi model yang telah ditetapkan.
- **Pengawal penyedia nod**: Nama pengawal ini adalah *gpu-provisioner* dalam [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ia menggunakan CRD `machine` yang berasal dari [Karpenter](https://sigs.k8s.io/karpenter) untuk berinteraksi dengan pengawal workspace. Ia berintegrasi dengan API Azure Kubernetes Service (AKS) untuk menambah nod GPU baharu ke dalam kluster AKS. 
> Nota: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) adalah komponen sumber terbuka. Ia boleh digantikan dengan pengawal lain jika mereka menyokong API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video Gambaran Keseluruhan 
[Tonton Demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Pemasangan

Sila semak panduan pemasangan [di sini](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Permulaan Pantas

Selepas memasang Kaito, anda boleh mencuba perintah berikut untuk memulakan perkhidmatan fine-tuning.

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

Status workspace boleh dijejaki dengan menjalankan perintah berikut. Apabila lajur WORKSPACEREADY menjadi `True`, model telah berjaya diterapkan.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Seterusnya, anda boleh mencari ip kluster perkhidmatan inferensi dan menggunakan pod `curl` sementara untuk menguji titik akhir perkhidmatan dalam kluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI berasaskan mesin. Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.