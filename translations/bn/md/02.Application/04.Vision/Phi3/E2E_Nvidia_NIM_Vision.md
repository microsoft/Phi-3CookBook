### উদাহরণ পরিস্থিতি

ধরা যাক, আপনার কাছে একটি ছবি (`demo.png`) আছে এবং আপনি এমন একটি Python কোড তৈরি করতে চান যা এই ছবিটি প্রক্রিয়া করবে এবং এর একটি নতুন সংস্করণ সংরক্ষণ করবে (`phi-3-vision.jpg`)।

উপরের কোডটি এই প্রক্রিয়াটি স্বয়ংক্রিয়ভাবে সম্পন্ন করে নিচের ধাপগুলোর মাধ্যমে:

1. পরিবেশ এবং প্রয়োজনীয় কনফিগারেশন সেটআপ করা।
2. একটি প্রম্পট তৈরি করা যা মডেলকে প্রয়োজনীয় Python কোড তৈরি করার নির্দেশ দেয়।
3. প্রম্পটটি মডেলে পাঠানো এবং তৈরি হওয়া কোড সংগ্রহ করা।
4. তৈরি হওয়া কোডটি বের করা এবং চালানো।
5. মূল এবং প্রক্রিয়াজাত ছবিগুলি প্রদর্শন করা।

এই পদ্ধতিটি AI-এর শক্তি ব্যবহার করে ছবি প্রক্রিয়াকরণের কাজগুলো স্বয়ংক্রিয় করে, যা আপনার লক্ষ্য অর্জন করা সহজ এবং দ্রুত করে তোলে।

[নমুনা কোড সমাধান](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

এবার পুরো কোডটি ধাপে ধাপে ব্যাখ্যা করা যাক:

1. **প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    এই কমান্ডটি `langchain_nvidia_ai_endpoints` প্যাকেজটি ইনস্টল করে, নিশ্চিত করে এটি সর্বশেষ সংস্করণ।

2. **প্রয়োজনীয় মডিউল আমদানি করুন**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    এই আমদানিগুলো NVIDIA AI এন্ডপয়েন্টের সাথে ইন্টারঅ্যাক্ট করা, পাসওয়ার্ড নিরাপদে পরিচালনা করা, অপারেটিং সিস্টেমের সাথে ইন্টারঅ্যাক্ট করা এবং base64 ফরম্যাটে ডেটা এনকোড/ডিকোড করার জন্য প্রয়োজনীয় মডিউল নিয়ে আসে।

3. **API কী সেটআপ করুন**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    এই কোডটি পরীক্ষা করে `NVIDIA_API_KEY` পরিবেশ ভেরিয়েবল সেট করা হয়েছে কিনা। যদি না হয়, এটি ব্যবহারকারীকে তাদের API কী নিরাপদে প্রবেশ করতে অনুরোধ করে।

4. **মডেল এবং ইমেজ পাথ সংজ্ঞায়িত করুন**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    এটি ব্যবহৃত মডেলটি সেট করে, নির্দিষ্ট মডেলের সাথে `ChatNVIDIA`-এর একটি উদাহরণ তৈরি করে এবং ছবির ফাইলের পাথ নির্ধারণ করে।

5. **টেক্সট প্রম্পট তৈরি করুন**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    এটি একটি টেক্সট প্রম্পট সংজ্ঞায়িত করে যা মডেলকে একটি ছবির প্রক্রিয়াকরণের জন্য Python কোড তৈরি করার নির্দেশ দেয়।

6. **ছবিটি Base64-এ এনকোড করুন**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    এই কোডটি ছবির ফাইলটি পড়ে, Base64-এ এনকোড করে এবং এনকোড করা ডেটার সাথে একটি HTML ইমেজ ট্যাগ তৈরি করে।

7. **টেক্সট এবং ছবিকে প্রম্পটে একত্রিত করুন**:
    ```python
    prompt = f"{text} {image}"
    ```
    এটি টেক্সট প্রম্পট এবং HTML ইমেজ ট্যাগকে একটি একক স্ট্রিংয়ে একত্রিত করে।

8. **ChatNVIDIA ব্যবহার করে কোড তৈরি করুন**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    এই কোডটি প্রম্পটটি `ChatNVIDIA` model and collects the generated code in chunks, printing and appending each chunk to the `code` স্ট্রিংয়ে পাঠায়।

9. **তৈরিকৃত কনটেন্ট থেকে Python কোড বের করুন**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    এটি তৈরি হওয়া কনটেন্ট থেকে আসল Python কোডটি বের করে Markdown ফরম্যাটিং সরিয়ে।

10. **তৈরিকৃত কোড চালান**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    এটি তৈরিকৃত Python কোডটিকে একটি সাবপ্রসেস হিসেবে চালায় এবং এর আউটপুট সংগ্রহ করে।

11. **ছবিগুলি প্রদর্শন করুন**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    এই লাইনগুলো `IPython.display` মডিউল ব্যবহার করে ছবিগুলি প্রদর্শন করে।

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব নির্ভুলতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকেই নির্ভরযোগ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।