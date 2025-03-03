## Chào mừng đến với các phòng thí nghiệm Phi sử dụng C#

Có một loạt các phòng thí nghiệm giới thiệu cách tích hợp các phiên bản mạnh mẽ khác nhau của mô hình Phi trong môi trường .NET.

## Yêu cầu trước

Trước khi chạy mẫu, hãy đảm bảo bạn đã cài đặt các thành phần sau:

**.NET 9:** Đảm bảo bạn đã cài đặt [phiên bản mới nhất của .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) trên máy của mình.

**(Tùy chọn) Visual Studio hoặc Visual Studio Code:** Bạn sẽ cần một IDE hoặc trình chỉnh sửa mã có khả năng chạy các dự án .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) hoặc [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) được khuyến nghị.

**Sử dụng git** để sao chép một trong các phiên bản Phi-3, Phi3.5 hoặc Phi-4 từ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) về máy cục bộ.

**Tải xuống các mô hình Phi-4 ONNX** về máy cục bộ của bạn:

### chuyển đến thư mục để lưu trữ các mô hình

```bash
cd c:\phi\models
```

### thêm hỗ trợ cho lfs

```bash
git lfs install 
```

### sao chép và tải xuống mô hình Phi-4 mini instruct và mô hình Phi-4 đa phương thức

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Tải xuống các mô hình Phi-3 ONNX** về máy cục bộ của bạn:

### sao chép và tải xuống mô hình Phi-3 mini 4K instruct và mô hình Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Quan trọng:** Các bản demo hiện tại được thiết kế để sử dụng các phiên bản ONNX của mô hình. Các bước trên sẽ sao chép các mô hình sau.

## Về các phòng thí nghiệm

Giải pháp chính có một số phòng thí nghiệm mẫu minh họa khả năng của các mô hình Phi sử dụng C#.

| Dự án | Mô hình | Mô tả |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 hoặc Phi-3.5 | Ứng dụng console mẫu cho phép người dùng đặt câu hỏi. Dự án tải một mô hình Phi-3 ONNX cục bộ bằng `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Chạy dự án với lệnh

    ```bash
    dotnet run
    ```

1. Dự án mẫu sẽ yêu cầu đầu vào từ người dùng và trả lời bằng chế độ cục bộ.

   Bản demo đang chạy sẽ giống như sau:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.