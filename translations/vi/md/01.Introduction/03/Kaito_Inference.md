## Suy luận với Kaito

[Kaito](https://github.com/Azure/kaito) là một operator tự động hóa việc triển khai mô hình suy luận AI/ML trong một cụm Kubernetes.

Kaito có những điểm khác biệt chính so với hầu hết các phương pháp triển khai mô hình phổ biến dựa trên cơ sở hạ tầng máy ảo:

- Quản lý các tệp mô hình bằng cách sử dụng hình ảnh container. Một máy chủ http được cung cấp để thực hiện các cuộc gọi suy luận bằng thư viện mô hình.
- Tránh việc điều chỉnh tham số triển khai để phù hợp với phần cứng GPU bằng cách cung cấp các cấu hình được thiết lập sẵn.
- Tự động cung cấp các nút GPU dựa trên yêu cầu của mô hình.
- Lưu trữ các hình ảnh mô hình lớn trong Microsoft Container Registry (MCR) công khai nếu giấy phép cho phép.

Sử dụng Kaito, quy trình tích hợp các mô hình suy luận AI lớn vào Kubernetes được đơn giản hóa đáng kể.

## Kiến trúc

Kaito tuân theo mẫu thiết kế Custom Resource Definition (CRD)/controller cổ điển của Kubernetes. Người dùng quản lý một tài nguyên tùy chỉnh `workspace` mô tả các yêu cầu GPU và thông số kỹ thuật suy luận. Các controller của Kaito sẽ tự động triển khai bằng cách đồng bộ hóa tài nguyên tùy chỉnh `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kiến trúc Kaito" alt="Kiến trúc Kaito">
</div>

Hình trên trình bày tổng quan về kiến trúc Kaito. Các thành phần chính bao gồm:

- **Workspace controller**: Đồng bộ hóa tài nguyên tùy chỉnh `workspace`, tạo các tài nguyên tùy chỉnh `machine` (được giải thích bên dưới) để kích hoạt việc tự động cung cấp nút, và tạo tải công việc suy luận (`deployment` hoặc `statefulset`) dựa trên các cấu hình thiết lập sẵn của mô hình.
- **Node provisioner controller**: Tên của controller này là *gpu-provisioner* trong [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Nó sử dụng CRD `machine` có nguồn gốc từ [Karpenter](https://sigs.k8s.io/karpenter) để tương tác với workspace controller. Nó tích hợp với các API của Azure Kubernetes Service (AKS) để thêm các nút GPU mới vào cụm AKS. 
> Lưu ý: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) là một thành phần mã nguồn mở. Nó có thể được thay thế bằng các controller khác nếu chúng hỗ trợ các API của [Karpenter-core](https://sigs.k8s.io/karpenter).

## Cài đặt

Vui lòng tham khảo hướng dẫn cài đặt [tại đây](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Bắt đầu nhanh với suy luận Phi-3
[Mã mẫu suy luận Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Trạng thái của workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY trở thành `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ IP của dịch vụ suy luận trong cụm và sử dụng một `curl` pod tạm thời để kiểm tra endpoint của dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Bắt đầu nhanh với suy luận Phi-3 và adapters

Sau khi cài đặt Kaito, bạn có thể thử các lệnh sau để khởi động một dịch vụ suy luận.

[Mã mẫu suy luận Phi-3 với Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Trạng thái của workspace có thể được theo dõi bằng cách chạy lệnh sau. Khi cột WORKSPACEREADY trở thành `True`, mô hình đã được triển khai thành công.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Tiếp theo, bạn có thể tìm địa chỉ IP của dịch vụ suy luận trong cụm và sử dụng một `curl` pod tạm thời để kiểm tra endpoint của dịch vụ trong cụm.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi nỗ lực để đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.