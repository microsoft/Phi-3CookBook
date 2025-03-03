# **Generative AI extensions for onnxruntime দিয়ে Phi ফ্যামিলি কোয়ান্টাইজ করা**

## **Generative AI extensions for onnxruntime কী**

এই এক্সটেনশনটি আপনাকে ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) দিয়ে জেনারেটিভ AI চালাতে সাহায্য করে। এটি ONNX মডেলের জন্য জেনারেটিভ AI লুপ সরবরাহ করে, যার মধ্যে ইনফারেন্স, লগিট প্রসেসিং, সার্চ ও স্যাম্পলিং এবং KV ক্যাশ ম্যানেজমেন্ট অন্তর্ভুক্ত। ডেভেলপাররা একটি উচ্চ-স্তরের generate() মেথড কল করতে পারেন, অথবা লুপের মধ্যে মডেলের প্রতিটি ইটারেশন চালিয়ে একবারে একটি টোকেন তৈরি করতে পারেন এবং লুপের ভিতরে জেনারেশন প্যারামিটার আপডেট করতে পারেন। এটি গ্রিডি/বিম সার্চ এবং TopP, TopK স্যাম্পলিংয়ের মাধ্যমে টোকেন সিকোয়েন্স তৈরি এবং রিপিটিশন পেনাল্টির মতো বিল্ট-ইন লগিট প্রসেসিং সমর্থন করে। এছাড়াও, কাস্টম স্কোরিং সহজেই যোগ করা যায়।

অ্যাপ্লিকেশন লেভেলে, আপনি Generative AI extensions for onnxruntime ব্যবহার করে C++/ C# / Python-এ অ্যাপ্লিকেশন তৈরি করতে পারেন। মডেল লেভেলে, এটি ব্যবহার করে ফাইন-টিউনড মডেলগুলো মার্জ এবং সংশ্লিষ্ট কোয়ান্টিটেটিভ ডেপ্লয়মেন্ট কাজ করতে পারেন।  

## **Generative AI extensions for onnxruntime দিয়ে Phi-3.5 কোয়ান্টাইজ করা**

### **সমর্থিত মডেল**

Generative AI extensions for onnxruntime Microsoft Phi, Google Gemma, Mistral, Meta LLaMA-এর কোয়ান্টাইজড কনভার্সন সমর্থন করে।  

### **Generative AI extensions for onnxruntime-এ মডেল বিল্ডার**

মডেল বিল্ডার ONNX Runtime-এর generate() API দিয়ে অপ্টিমাইজড এবং কোয়ান্টাইজড ONNX মডেল তৈরি করার প্রক্রিয়া দ্রুততর করে।  

মডেল বিল্ডারের মাধ্যমে, আপনি মডেলটিকে INT4, INT8, FP16, FP32-তে কোয়ান্টাইজ করতে পারেন এবং CPU, CUDA, DirectML, Mobile ইত্যাদির মতো বিভিন্ন হার্ডওয়্যার অ্যাক্সিলারেশন পদ্ধতির সঙ্গে একত্রিত করতে পারেন।  

মডেল বিল্ডার ব্যবহার করতে আপনাকে ইনস্টল করতে হবে  

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```  

ইনস্টল করার পর, টার্মিনাল থেকে মডেল বিল্ডার স্ক্রিপ্ট চালিয়ে মডেলের ফরম্যাট এবং কোয়ান্টাইজড কনভার্সন করতে পারবেন।  

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```  

প্রাসঙ্গিক প্যারামিটারগুলো বুঝুন  

1. **model_name** এটি হাগিং ফেস-এর মডেল, যেমন microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct ইত্যাদি। এটি আপনার সংরক্ষিত মডেলের পথও হতে পারে।  

2. **path_to_output_folder** কোয়ান্টাইজড কনভার্সনের সেভ পাথ।  

3. **execution_provider** বিভিন্ন হার্ডওয়্যার অ্যাক্সিলারেশন সাপোর্ট, যেমন cpu, cuda, DirectML।  

4. **cache_dir_to_save_hf_files** আমরা হাগিং ফেস থেকে মডেল ডাউনলোড করি এবং এটি লোকালি ক্যাশ করি।  

***নোটঃ***  

## **কীভাবে মডেল বিল্ডার ব্যবহার করে Phi-3.5 কোয়ান্টাইজ করবেন**

মডেল বিল্ডার এখন Phi-3.5 Instruct এবং Phi-3.5-Vision-এর জন্য ONNX মডেল কোয়ান্টাইজেশন সমর্থন করে।  

### **Phi-3.5-Instruct**

**কোয়ান্টাইজড INT 4-এর জন্য CPU অ্যাক্সিলারেটেড কনভার্সন**  

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```  

**কোয়ান্টাইজড INT 4-এর জন্য CUDA অ্যাক্সিলারেটেড কনভার্সন**  

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```  

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```  

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. টার্মিনালে এনভায়রনমেন্ট সেট করুন  

```bash

mkdir models

cd models 

```  

2. মডেলস ফোল্ডারে microsoft/Phi-3.5-vision-instruct ডাউনলোড করুন  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)  

3. নিচের ফাইলগুলো আপনার Phi-3.5-vision-instruct ফোল্ডারে ডাউনলোড করুন  

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)  

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)  

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)  

4. এই ফাইলটি মডেলস ফোল্ডারে ডাউনলোড করুন  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)  

5. টার্মিনালে যান  

    FP32 সহ ONNX সাপোর্টে কনভার্ট করুন  

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```  

### **নোটঃ**

1. মডেল বিল্ডার বর্তমানে Phi-3.5-Instruct এবং Phi-3.5-Vision-এর কনভার্সন সমর্থন করে, তবে Phi-3.5-MoE নয়।  

2. ONNX-এর কোয়ান্টাইজড মডেল ব্যবহার করতে চাইলে, Generative AI extensions for onnxruntime SDK ব্যবহার করতে পারেন।  

3. আরও দায়িত্বশীল AI নিশ্চিত করতে, মডেল কোয়ান্টাইজেশন কনভার্সনের পরে কার্যকর ফলাফলের পরীক্ষা করা সুপারিশ করা হয়।  

4. CPU INT4 মডেল কোয়ান্টাইজ করার মাধ্যমে আমরা এটি Edge Device-এ ডেপ্লয় করতে পারি, যা আরও ভালো অ্যাপ্লিকেশন দৃশ্যপট প্রদান করে। এজন্য আমরা INT 4-এর চারপাশে Phi-3.5-Instruct সম্পন্ন করেছি।  

## **রিসোর্স**

1. Generative AI extensions for onnxruntime সম্পর্কে আরও জানুন [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)  

2. Generative AI extensions for onnxruntime-এর GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)  

**অস্বীকৃতি**:  
এই নথি মেশিন-ভিত্তিক কৃত্রিম বুদ্ধিমত্তা অনুবাদ পরিষেবা ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা বজায় রাখার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণ্য উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে, পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।