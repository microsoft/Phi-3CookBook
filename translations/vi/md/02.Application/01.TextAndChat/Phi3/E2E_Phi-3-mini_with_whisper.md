# Chatbot Phi 3 Mini 4K Tương Tác với Whisper

## Tổng Quan

Chatbot Phi 3 Mini 4K Tương Tác là một công cụ cho phép người dùng tương tác với bản demo hướng dẫn Microsoft Phi 3 Mini 4K bằng cách sử dụng đầu vào văn bản hoặc âm thanh. Chatbot này có thể được sử dụng cho nhiều nhiệm vụ khác nhau, như dịch thuật, cập nhật thời tiết và thu thập thông tin chung.

### Bắt Đầu

Để sử dụng chatbot này, hãy làm theo các bước sau:

1. Mở [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Trong cửa sổ chính của notebook, bạn sẽ thấy giao diện chat với một ô nhập văn bản và nút "Send".
3. Để sử dụng chatbot dựa trên văn bản, chỉ cần nhập tin nhắn vào ô nhập văn bản và nhấn nút "Send". Chatbot sẽ phản hồi bằng một tệp âm thanh có thể phát trực tiếp từ trong notebook.

**Lưu ý**: Công cụ này yêu cầu GPU và truy cập vào các mô hình Microsoft Phi-3 và OpenAI Whisper, được sử dụng cho nhận diện giọng nói và dịch thuật.

### Yêu Cầu GPU

Để chạy bản demo này, bạn cần có GPU với bộ nhớ 12GB.

Yêu cầu bộ nhớ để chạy bản demo **Microsoft-Phi-3-Mini-4K instruct** trên GPU sẽ phụ thuộc vào nhiều yếu tố, như kích thước dữ liệu đầu vào (âm thanh hoặc văn bản), ngôn ngữ được sử dụng để dịch, tốc độ của mô hình, và bộ nhớ sẵn có trên GPU.

Nhìn chung, mô hình Whisper được thiết kế để chạy trên GPU. Lượng bộ nhớ GPU tối thiểu được khuyến nghị để chạy mô hình Whisper là 8 GB, nhưng mô hình này có thể tận dụng bộ nhớ lớn hơn nếu cần.

Cần lưu ý rằng chạy một lượng lớn dữ liệu hoặc yêu cầu xử lý với tần suất cao có thể yêu cầu nhiều bộ nhớ GPU hơn và/hoặc gây ra các vấn đề về hiệu suất. Khuyến nghị thử nghiệm trường hợp sử dụng của bạn với các cấu hình khác nhau và giám sát việc sử dụng bộ nhớ để xác định cấu hình tối ưu cho nhu cầu cụ thể của bạn.

## Ví Dụ E2E cho Chatbot Phi 3 Mini 4K Tương Tác với Whisper

Notebook có tiêu đề [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) minh họa cách sử dụng bản demo Microsoft Phi 3 Mini 4K để tạo văn bản từ đầu vào âm thanh hoặc văn bản. Notebook định nghĩa một số hàm:

1. `tts_file_name(text)`: Hàm này tạo tên tệp dựa trên văn bản đầu vào để lưu tệp âm thanh được tạo.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Hàm này sử dụng Edge TTS API để tạo tệp âm thanh từ danh sách các đoạn văn bản đầu vào. Các tham số đầu vào bao gồm danh sách các đoạn, tốc độ giọng nói, tên giọng nói, và đường dẫn lưu tệp âm thanh được tạo.
1. `talk(input_text)`: Hàm này tạo một tệp âm thanh bằng cách sử dụng Edge TTS API và lưu vào một tên tệp ngẫu nhiên trong thư mục /content/audio. Tham số đầu vào là văn bản cần chuyển đổi thành giọng nói.
1. `run_text_prompt(message, chat_history)`: Hàm này sử dụng bản demo Microsoft Phi 3 Mini 4K để tạo một tệp âm thanh từ tin nhắn đầu vào và thêm nó vào lịch sử trò chuyện.
1. `run_audio_prompt(audio, chat_history)`: Hàm này chuyển đổi một tệp âm thanh thành văn bản bằng cách sử dụng Whisper model API và truyền nó vào hàm `run_text_prompt()`.
1. Code khởi chạy một ứng dụng Gradio cho phép người dùng tương tác với bản demo Phi 3 Mini 4K bằng cách nhập tin nhắn hoặc tải lên tệp âm thanh. Kết quả được hiển thị dưới dạng tin nhắn văn bản trong ứng dụng.

## Xử Lý Sự Cố

Cài đặt trình điều khiển GPU Cuda

1. Đảm bảo ứng dụng Linux của bạn đã được cập nhật

    ```bash
    sudo apt update
    ```

1. Cài đặt trình điều khiển Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Đăng ký vị trí trình điều khiển Cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kiểm tra kích thước bộ nhớ GPU Nvidia (Yêu cầu 12GB bộ nhớ GPU)

    ```bash
    nvidia-smi
    ```

1. Xóa bộ nhớ cache: Nếu bạn đang sử dụng PyTorch, bạn có thể gọi torch.cuda.empty_cache() để giải phóng tất cả bộ nhớ cache không sử dụng để nó có thể được sử dụng bởi các ứng dụng GPU khác

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kiểm tra Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Thực hiện các bước sau để tạo token Hugging Face.

    - Truy cập [Trang Cài Đặt Token của Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chọn **New token**.
    - Nhập **Tên** dự án bạn muốn sử dụng.
    - Chọn **Loại** là **Write**.

> **Lưu ý**
>
> Nếu bạn gặp lỗi sau:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Để khắc phục, hãy nhập lệnh sau vào terminal của bạn.
>
> ```bash
> sudo ldconfig
> ```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn tham khảo chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.