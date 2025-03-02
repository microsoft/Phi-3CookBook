# Đóng góp

Dự án này hoan nghênh các đóng góp và gợi ý. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Đóng góp (CLA), xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết thêm chi tiết, truy cập [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com).

Khi bạn gửi một yêu cầu kéo (pull request), bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và gắn nhãn PR tương ứng (ví dụ: kiểm tra trạng thái, nhận xét). Chỉ cần làm theo hướng dẫn được cung cấp bởi bot. Bạn chỉ cần thực hiện điều này một lần cho tất cả các kho lưu trữ sử dụng CLA của chúng tôi.

## Quy tắc ứng xử

Dự án này đã áp dụng [Quy tắc ứng xử Mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).  
Để biết thêm thông tin, hãy đọc [Câu hỏi thường gặp về Quy tắc ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu bạn có bất kỳ câu hỏi hoặc nhận xét nào khác.

## Lưu ý khi tạo vấn đề (issues)

Vui lòng không mở các vấn đề GitHub để hỏi các câu hỏi hỗ trợ chung vì danh sách GitHub nên được sử dụng cho các yêu cầu tính năng và báo cáo lỗi. Bằng cách này, chúng tôi có thể dễ dàng theo dõi các vấn đề hoặc lỗi thực tế từ mã và giữ cho các cuộc thảo luận chung tách biệt khỏi mã thực tế.

## Cách đóng góp

### Hướng dẫn gửi Pull Request

Khi gửi một yêu cầu kéo (PR) tới kho lưu trữ Phi-3 CookBook, vui lòng tuân thủ các hướng dẫn sau:

- **Fork kho lưu trữ**: Luôn fork kho lưu trữ về tài khoản của bạn trước khi thực hiện các chỉnh sửa.

- **Tách riêng các pull request (PR)**:
  - Gửi từng loại thay đổi trong một PR riêng biệt. Ví dụ, sửa lỗi và cập nhật tài liệu nên được gửi trong các PR riêng.
  - Các sửa lỗi nhỏ và cập nhật tài liệu có thể được kết hợp vào một PR nếu phù hợp.

- **Xử lý xung đột hợp nhất (merge conflicts)**: Nếu PR của bạn xuất hiện xung đột hợp nhất, hãy cập nhật nhánh `main` cục bộ của bạn để phản ánh kho lưu trữ chính trước khi thực hiện các chỉnh sửa.

- **Gửi bản dịch**: Khi gửi một PR dịch thuật, hãy đảm bảo rằng thư mục bản dịch bao gồm bản dịch cho tất cả các tệp trong thư mục gốc.

### Hướng dẫn dịch thuật

> [!IMPORTANT]
>
> Khi dịch nội dung trong kho lưu trữ này, không sử dụng dịch máy. Chỉ tham gia dịch thuật nếu bạn thành thạo ngôn ngữ đó.

Nếu bạn thông thạo một ngôn ngữ không phải tiếng Anh, bạn có thể giúp dịch nội dung. Hãy làm theo các bước sau để đảm bảo đóng góp dịch thuật của bạn được tích hợp đúng cách, vui lòng tuân thủ các hướng dẫn sau:

- **Tạo thư mục dịch thuật**: Điều hướng đến thư mục phần tương ứng và tạo một thư mục dịch thuật cho ngôn ngữ bạn đóng góp. Ví dụ:
  - Đối với phần giới thiệu: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Đối với phần bắt đầu nhanh: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Tiếp tục mẫu này cho các phần khác (03.Inference, 04.Finetuning, v.v.)

- **Cập nhật đường dẫn tương đối**: Khi dịch, điều chỉnh cấu trúc thư mục bằng cách thêm `../../` vào đầu các đường dẫn tương đối trong các tệp markdown để đảm bảo liên kết hoạt động đúng. Ví dụ, thay đổi như sau:
  - Thay `(../../imgs/01/phi3aisafety.png)` bằng `(../../../../imgs/01/phi3aisafety.png)`

- **Tổ chức bản dịch của bạn**: Mỗi tệp dịch nên được đặt trong thư mục dịch thuật tương ứng của phần đó. Ví dụ, nếu bạn đang dịch phần giới thiệu sang tiếng Tây Ban Nha, bạn sẽ tạo như sau:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Gửi một PR đầy đủ**: Đảm bảo rằng tất cả các tệp dịch cho một phần được bao gồm trong một PR. Chúng tôi không chấp nhận các bản dịch không đầy đủ cho một phần. Khi gửi một PR dịch thuật, hãy đảm bảo rằng thư mục dịch thuật bao gồm bản dịch cho tất cả các tệp trong thư mục gốc.

### Hướng dẫn viết

Để đảm bảo tính nhất quán trên tất cả các tài liệu, vui lòng sử dụng các hướng dẫn sau:

- **Định dạng URL**: Đặt tất cả các URL trong dấu ngoặc vuông theo sau là dấu ngoặc đơn, không có khoảng trắng thừa xung quanh hoặc bên trong. Ví dụ: `[example](https://example.com)`.

- **Liên kết tương đối**: Sử dụng `./` cho các liên kết tương đối trỏ đến tệp hoặc thư mục trong thư mục hiện tại và `../` cho các liên kết trong thư mục cha. Ví dụ: `[example](../../path/to/file)` hoặc `[example](../../../path/to/file)`.

- **Không sử dụng locale quốc gia**: Đảm bảo rằng liên kết của bạn không bao gồm locale cụ thể của quốc gia. Ví dụ, tránh `/en-us/` hoặc `/en/`.

- **Lưu trữ hình ảnh**: Lưu tất cả hình ảnh trong thư mục `./imgs`.

- **Đặt tên hình ảnh mô tả**: Đặt tên hình ảnh một cách mô tả bằng các ký tự tiếng Anh, số và dấu gạch ngang. Ví dụ: `example-image.jpg`.

## Quy trình làm việc trên GitHub

Khi bạn gửi một pull request, các quy trình làm việc sau sẽ được kích hoạt để xác thực các thay đổi. Làm theo hướng dẫn dưới đây để đảm bảo PR của bạn vượt qua các kiểm tra quy trình làm việc:

- [Kiểm tra Đường dẫn Tương đối Bị Hỏng](../..)
- [Kiểm tra URL Không Có Locale](../..)

### Kiểm tra Đường dẫn Tương đối Bị Hỏng

Quy trình làm việc này đảm bảo rằng tất cả các đường dẫn tương đối trong tệp của bạn là chính xác.

1. Để đảm bảo liên kết của bạn hoạt động đúng, thực hiện các tác vụ sau bằng VS Code:
    - Di chuột qua bất kỳ liên kết nào trong tệp của bạn.
    - Nhấn **Ctrl + Click** để điều hướng đến liên kết.
    - Nếu bạn nhấp vào một liên kết và nó không hoạt động cục bộ, quy trình làm việc sẽ kích hoạt và không hoạt động trên GitHub.

1. Để khắc phục sự cố này, thực hiện các tác vụ sau bằng các gợi ý đường dẫn do VS Code cung cấp:
    - Gõ `./` hoặc `../`.
    - VS Code sẽ nhắc bạn chọn từ các tùy chọn có sẵn dựa trên những gì bạn đã gõ.
    - Theo dõi đường dẫn bằng cách nhấp vào tệp hoặc thư mục mong muốn để đảm bảo đường dẫn của bạn chính xác.

Khi bạn đã thêm đường dẫn tương đối chính xác, lưu và đẩy các thay đổi của bạn.

### Kiểm tra URL Không Có Locale

Quy trình làm việc này đảm bảo rằng bất kỳ URL web nào không bao gồm locale cụ thể của quốc gia. Vì kho lưu trữ này có thể truy cập toàn cầu, điều quan trọng là đảm bảo rằng các URL không chứa locale quốc gia của bạn.

1. Để xác minh rằng các URL của bạn không có locale quốc gia, thực hiện các tác vụ sau:

    - Kiểm tra văn bản như `/en-us/`, `/en/` hoặc bất kỳ locale ngôn ngữ nào khác trong các URL.
    - Nếu những điều này không có trong URL của bạn, thì bạn sẽ vượt qua kiểm tra này.

1. Để khắc phục sự cố này, thực hiện các tác vụ sau:
    - Mở đường dẫn tệp được quy trình làm việc đánh dấu.
    - Xóa locale quốc gia khỏi các URL.

Khi bạn xóa locale quốc gia, lưu và đẩy các thay đổi của bạn.

### Kiểm tra URL Bị Hỏng

Quy trình làm việc này đảm bảo rằng bất kỳ URL web nào trong tệp của bạn đều hoạt động và trả về mã trạng thái 200.

1. Để xác minh rằng các URL của bạn hoạt động đúng, thực hiện các tác vụ sau:
    - Kiểm tra trạng thái của các URL trong tệp của bạn.

2. Để khắc phục bất kỳ URL bị hỏng nào, thực hiện các tác vụ sau:
    - Mở tệp chứa URL bị hỏng.
    - Cập nhật URL thành URL chính xác.

Khi bạn đã sửa các URL, lưu và đẩy các thay đổi của bạn.

> [!NOTE]
>
> Có thể có các trường hợp kiểm tra URL thất bại ngay cả khi liên kết có thể truy cập. Điều này có thể xảy ra vì một số lý do, bao gồm:
>
> - **Hạn chế mạng:** Máy chủ hành động của GitHub có thể có hạn chế mạng ngăn truy cập vào một số URL nhất định.
> - **Sự cố hết thời gian:** Các URL mất quá nhiều thời gian để phản hồi có thể gây ra lỗi hết thời gian trong quy trình làm việc.
> - **Sự cố máy chủ tạm thời:** Thời gian chết hoặc bảo trì máy chủ tạm thời có thể làm cho URL không khả dụng trong quá trình xác thực.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.