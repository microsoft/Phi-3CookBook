# **Lượng tử hóa Phi-3.5 bằng Apple MLX Framework**

MLX là một framework mảng dành cho nghiên cứu máy học trên Apple silicon, được phát triển bởi nhóm nghiên cứu máy học của Apple.

MLX được thiết kế bởi các nhà nghiên cứu máy học dành cho chính các nhà nghiên cứu máy học. Framework này nhằm mục tiêu thân thiện với người dùng nhưng vẫn hiệu quả trong việc huấn luyện và triển khai mô hình. Thiết kế của MLX cũng rất đơn giản về mặt khái niệm. Chúng tôi mong muốn giúp các nhà nghiên cứu dễ dàng mở rộng và cải tiến MLX để nhanh chóng thử nghiệm các ý tưởng mới.

LLM có thể được tăng tốc trên các thiết bị Apple Silicon thông qua MLX, và mô hình có thể chạy cục bộ một cách rất tiện lợi.

Hiện tại, Apple MLX Framework hỗ trợ chuyển đổi lượng tử hóa cho Phi-3.5-Instruct(**Apple MLX Framework hỗ trợ**), Phi-3.5-Vision(**MLX-VLM Framework hỗ trợ**) và Phi-3.5-MoE(**Apple MLX Framework hỗ trợ**). Hãy thử ngay sau đây:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Ví dụ cho Phi-3.5 với Apple MLX**

| Labs    | Giới thiệu | Đi tới |
| -------- | ------- |  ------- |
| 🚀 Lab-Giới thiệu Phi-3.5 Instruct  | Tìm hiểu cách sử dụng Phi-3.5 Instruct với Apple MLX framework   |  [Đi tới](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (image) | Tìm hiểu cách sử dụng Phi-3.5 Vision để phân tích hình ảnh với Apple MLX framework     |  [Đi tới](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Giới thiệu Phi-3.5 Vision (moE)   | Tìm hiểu cách sử dụng Phi-3.5 MoE với Apple MLX framework  |  [Đi tới](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Tài nguyên**

1. Tìm hiểu về Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Kho GitHub Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Kho GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin đáng tin cậy nhất. Đối với các thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.