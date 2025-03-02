## Tinh chỉnh với Kaito 

[Kaito](https://github.com/Azure/kaito) là một công cụ tự động hóa việc triển khai mô hình suy luận AI/ML trong cụm Kubernetes.

Kaito có những điểm khác biệt chính so với hầu hết các phương pháp triển khai mô hình phổ biến hiện nay dựa trên hạ tầng máy ảo:

- Quản lý tệp mô hình bằng cách sử dụng hình ảnh container. Một máy chủ http được cung cấp để thực hiện các cuộc gọi suy luận thông qua thư viện mô hình.
- Tránh việc tinh chỉnh tham số triển khai để phù hợp với phần cứng GPU bằng cách cung cấp các cấu hình cài đặt sẵn.
- Tự động cung cấp các node GPU dựa trên yêu cầu của mô hình.
- Lưu trữ các hình ảnh mô hình lớn trong Microsoft Container Registry (MCR) công khai nếu giấy phép cho phép.

Với Kaito, quy trình tích hợp các mô hình suy luận AI lớn vào Kubernetes trở nên đơn giản hơn rất nhiều.

## Kiến trúc

Kaito tuân theo mô hình thiết kế truyền thống của Kubernetes Custom Resource Definition (CRD)/controller. Người dùng quản lý một tài nguyên tùy chỉnh `workspace` mô tả yêu cầu GPU và thông số kỹ thuật suy luận. Các controller của Kaito sẽ tự động hóa việc triển khai bằng cách đồng bộ hóa tài nguyên tùy chỉnh `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Hình trên minh họa tổng quan kiến trúc của Kaito. Các thành phần chính bao gồm:

- **Workspace controller**: Quản lý tài nguyên tùy chỉnh `workspace`, tạo ra các tài nguyên tùy chỉnh `machine` (giải thích bên dưới) để kích hoạt tự động cung cấp node, và tạo khối lượng công việc suy luận (`deployment` hoặc `statefulset`) dựa trên các cấu hình cài đặt sẵn của mô hình.
- **Node provisioner controller**: Tên của controller này là *gpu-provisioner* trong [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Nó sử dụng CRD `machine` từ [Karpenter](https://sigs.k8s.io/karpenter) để tương tác với workspace controller. Nó tích hợp với các API của Azure Kubernetes Service (AKS) để thêm các node GPU mới vào cụm AKS.
> Lưu ý: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) là một thành phần mã nguồn mở. Nó có thể được thay thế bằng các controller khác nếu chúng hỗ trợ các API của [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video tổng quan 
[Xem bản demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Cài đặt

Vui lòng tham khảo hướng dẫn cài đặt [tại đây](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Bắt đầu nhanh

Sau khi cài đặt Kaito, bạn có thể thử các lệnh sau để khởi động dịch vụ tinh chỉnh.

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

Trạng thái workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY trở thành `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ ip cụm của dịch vụ suy luận và sử dụng một pod `curl` tạm thời để kiểm tra điểm cuối của dịch vụ trong cụm.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin có thẩm quyền. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.