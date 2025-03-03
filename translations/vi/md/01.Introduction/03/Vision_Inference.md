# **Sử dụng Phi-3-Vision cục bộ**

Phi-3-vision-128k-instruct cho phép Phi-3 không chỉ hiểu ngôn ngữ mà còn có khả năng nhìn nhận thế giới qua hình ảnh. Thông qua Phi-3-vision-128k-instruct, chúng ta có thể giải quyết các vấn đề liên quan đến hình ảnh, như nhận dạng ký tự (OCR), phân tích bảng, nhận diện đối tượng, mô tả hình ảnh, v.v. Chúng ta có thể dễ dàng hoàn thành những nhiệm vụ trước đây cần lượng lớn dữ liệu để huấn luyện. Dưới đây là các kỹ thuật và kịch bản ứng dụng liên quan được trích dẫn bởi Phi-3-vision-128k-instruct.

## **0. Chuẩn bị**

Hãy đảm bảo rằng các thư viện Python sau đã được cài đặt trước khi sử dụng (khuyến nghị sử dụng Python 3.10+)

```bash
pip install transformers -U
pip install datasets -U
pip install torch -U
```

Khuyến nghị sử dụng ***CUDA 11.6+*** và cài đặt flatten

```bash
pip install flash-attn --no-build-isolation
```

Tạo một Notebook mới. Để hoàn thành các ví dụ, khuyến nghị bạn tạo nội dung sau trước.

```python
from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoProcessor

model_id = "microsoft/Phi-3-vision-128k-instruct"

kwargs = {}
kwargs['torch_dtype'] = torch.bfloat16

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype="auto").cuda()

user_prompt = '<|user|>\n'
assistant_prompt = '<|assistant|>\n'
prompt_suffix = "<|end|>\n"
```

## **1. Phân tích hình ảnh với Phi-3-Vision**

Chúng ta muốn AI có khả năng phân tích nội dung trong hình ảnh của mình và đưa ra các mô tả liên quan.

```python
prompt = f"{user_prompt}<|image_1|>\nCould you please introduce this stock to me?{prompt_suffix}{assistant_prompt}"


url = "https://g.foolcdn.com/editorial/images/767633/nvidiadatacenterrevenuefy2017tofy2024.png"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )
generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=True, 
                                  clean_up_tokenization_spaces=False)[0]
```

Chúng ta có thể nhận được câu trả lời liên quan bằng cách chạy đoạn mã sau trong Notebook.

```txt
Certainly! Nvidia Corporation is a global leader in advanced computing and artificial intelligence (AI). The company designs and develops graphics processing units (GPUs), which are specialized hardware accelerators used to process and render images and video. Nvidia's GPUs are widely used in professional visualization, data centers, and gaming. The company also provides software and services to enhance the capabilities of its GPUs. Nvidia's innovative technologies have applications in various industries, including automotive, healthcare, and entertainment. The company's stock is publicly traded and can be found on major stock exchanges.
```

## **2. OCR với Phi-3-Vision**

Ngoài việc phân tích hình ảnh, chúng ta còn có thể trích xuất thông tin từ hình ảnh. Đây chính là quy trình OCR mà trước đây chúng ta phải viết mã phức tạp để hoàn thành.

```python
prompt = f"{user_prompt}<|image_1|>\nHelp me get the title and author information of this book?{prompt_suffix}{assistant_prompt}"

url = "https://marketplace.canva.com/EAFPHUaBrFc/1/0/1003w/canva-black-and-white-modern-alone-story-book-cover-QHBKwQnsgzs.jpg"

image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(prompt, image, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, 
                                  skip_special_tokens=False, 
                                  clean_up_tokenization_spaces=False)[0]

```

Kết quả là

```txt
The title of the book is "ALONE" and the author is Morgan Maxwell.
```

## **3. So sánh nhiều hình ảnh**

Phi-3 Vision hỗ trợ so sánh nhiều hình ảnh. Chúng ta có thể sử dụng mô hình này để tìm ra sự khác biệt giữa các hình ảnh.

```python
prompt = f"{user_prompt}<|image_1|>\n<|image_2|>\n What is difference in this two images?{prompt_suffix}{assistant_prompt}"

print(f">>> Prompt\n{prompt}")

url = "https://hinhnen.ibongda.net/upload/wallpaper/doi-bong/2012/11/22/arsenal-wallpaper-free.jpg"

image_1 = Image.open(requests.get(url, stream=True).raw)

url = "https://assets-webp.khelnow.com/d7293de2fa93b29528da214253f1d8d0/news/uploads/2021/07/Arsenal-1024x576.jpg.webp"

image_2 = Image.open(requests.get(url, stream=True).raw)

images = [image_1, image_2]

inputs = processor(prompt, images, return_tensors="pt").to("cuda:0")

generate_ids = model.generate(**inputs, 
                              max_new_tokens=1000,
                              eos_token_id=processor.tokenizer.eos_token_id,
                              )

generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]

response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```

Kết quả là

```txt
The first image shows a group of soccer players from the Arsenal Football Club posing for a team photo with their trophies, while the second image shows a group of soccer players from the Arsenal Football Club celebrating a victory with a large crowd of fans in the background. The difference between the two images is the context in which the photos were taken, with the first image focusing on the team and their trophies, and the second image capturing a moment of celebration and victory.
```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng các dịch vụ dịch thuật AI tự động. Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.