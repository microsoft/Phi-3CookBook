# Tạo tập dữ liệu hình ảnh bằng cách tải DataSet từ Hugging Face và các hình ảnh liên quan

### Tổng quan

Script này chuẩn bị một tập dữ liệu cho học máy bằng cách tải xuống các hình ảnh cần thiết, lọc bỏ các dòng mà việc tải hình ảnh thất bại, và lưu tập dữ liệu dưới dạng tệp CSV.

### Yêu cầu trước

Trước khi chạy script này, hãy đảm bảo rằng bạn đã cài đặt các thư viện sau: `Pandas`, `Datasets`, `requests`, `PIL`, và `io`. Bạn cũng cần thay thế `'Insert_Your_Dataset'` ở dòng 2 bằng tên của tập dữ liệu của bạn từ Hugging Face.

Các thư viện cần thiết:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Chức năng

Script thực hiện các bước sau:

1. Tải tập dữ liệu từ Hugging Face bằng cách sử dụng `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` để tải hình ảnh từ URL và lưu trữ cục bộ bằng thư viện Pillow Image Library (PIL) và module `io`. Hàm này trả về True nếu hình ảnh được tải thành công, và False nếu ngược lại. Hàm cũng sẽ tạo ra một ngoại lệ với thông báo lỗi khi yêu cầu thất bại.

### Hoạt động như thế nào

Hàm download_image nhận hai tham số: image_url, là URL của hình ảnh cần tải xuống, và save_path, là đường dẫn nơi hình ảnh tải xuống sẽ được lưu.

Cách hàm hoạt động:

Hàm bắt đầu bằng việc thực hiện một yêu cầu GET tới image_url sử dụng phương thức requests.get. Điều này giúp lấy dữ liệu hình ảnh từ URL.

Dòng response.raise_for_status() kiểm tra xem yêu cầu có thành công hay không. Nếu mã trạng thái phản hồi chỉ ra lỗi (ví dụ: 404 - Không tìm thấy), nó sẽ tạo ra một ngoại lệ. Điều này đảm bảo rằng chúng ta chỉ tiếp tục tải hình ảnh nếu yêu cầu thành công.

Dữ liệu hình ảnh sau đó được truyền vào phương thức Image.open từ module PIL (Python Imaging Library). Phương thức này tạo một đối tượng Image từ dữ liệu hình ảnh.

Dòng image.save(save_path) lưu hình ảnh vào save_path được chỉ định. Save_path nên bao gồm tên tệp và phần mở rộng mong muốn.

Cuối cùng, hàm trả về True để chỉ ra rằng hình ảnh đã được tải xuống và lưu thành công. Nếu có bất kỳ ngoại lệ nào xảy ra trong quá trình này, nó sẽ bắt ngoại lệ, in ra thông báo lỗi chỉ ra thất bại, và trả về False.

Hàm này hữu ích để tải hình ảnh từ URL và lưu trữ cục bộ. Nó xử lý các lỗi tiềm năng trong quá trình tải xuống và cung cấp phản hồi về việc tải xuống có thành công hay không.

Đáng chú ý rằng thư viện requests được sử dụng để thực hiện các yêu cầu HTTP, thư viện PIL được sử dụng để làm việc với hình ảnh, và lớp BytesIO được sử dụng để xử lý dữ liệu hình ảnh dưới dạng luồng byte.

### Kết luận

Script này cung cấp một cách tiện lợi để chuẩn bị tập dữ liệu cho học máy bằng cách tải xuống các hình ảnh cần thiết, lọc bỏ các dòng mà việc tải hình ảnh thất bại, và lưu tập dữ liệu dưới dạng tệp CSV.

### Script mẫu

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Tải mã nguồn mẫu 
[Script tạo tập dữ liệu mới](../../../../code/04.Finetuning/generate_dataset.py)

### Tập dữ liệu mẫu
[Ví dụ về tập dữ liệu mẫu từ ví dụ fine-tuning với LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ ban đầu nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp từ con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.