[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

এই কোডটি একটি মডেলকে OpenVINO ফরম্যাটে রপ্তানি করে, এটি লোড করে এবং প্রদত্ত প্রম্পটের ভিত্তিতে একটি প্রতিক্রিয়া তৈরি করতে ব্যবহার করে।

1. **মডেল রপ্তানি করা**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - এই কমান্ডটি `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4` ব্যবহার করে।

2. **প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট করা**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - এই লাইনগুলো `transformers` library and the `optimum.intel.openvino` মডিউল থেকে ক্লাস ইম্পোর্ট করে, যা মডেল লোড এবং ব্যবহার করার জন্য প্রয়োজন।

3. **মডেল ডিরেক্টরি এবং কনফিগারেশন সেটআপ করা**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` একটি ডিকশনারি যা OpenVINO মডেলকে কম ল্যাটেন্সি প্রাধান্য দিতে, এক ইনফারেন্স স্ট্রিম ব্যবহার করতে এবং ক্যাশ ডিরেক্টরি ব্যবহার না করতে কনফিগার করে।

4. **মডেল লোড করা**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - এই লাইনটি নির্দিষ্ট ডিরেক্টরি থেকে মডেল লোড করে, পূর্বে সংজ্ঞায়িত কনফিগারেশন সেটিংস ব্যবহার করে। এটি প্রয়োজনে রিমোট কোড এক্সিকিউশনকেও অনুমতি দেয়।

5. **টোকেনাইজার লোড করা**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - এই লাইনটি টোকেনাইজার লোড করে, যা টেক্সটকে টোকেনে রূপান্তর করে যা মডেল বুঝতে পারে।

6. **টোকেনাইজার আর্গুমেন্ট সেটআপ করা**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - এই ডিকশনারি নির্দিষ্ট করে যে বিশেষ টোকেন টোকেনাইজড আউটপুটে যোগ করা উচিত নয়।

7. **প্রম্পট সংজ্ঞায়িত করা**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - এই স্ট্রিংটি একটি কথোপকথনের প্রম্পট সেটআপ করে যেখানে ব্যবহারকারী এআই সহকারীকে নিজেকে পরিচয় করাতে বলে।

8. **প্রম্পট টোকেনাইজ করা**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - এই লাইনটি প্রম্পটকে টোকেনে রূপান্তর করে যা মডেল প্রসেস করতে পারে এবং ফলাফল PyTorch টেনসর হিসেবে ফেরত দেয়।

9. **প্রতিক্রিয়া তৈরি করা**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - এই লাইনটি ইনপুট টোকেনের ভিত্তিতে মডেল ব্যবহার করে একটি প্রতিক্রিয়া তৈরি করে, সর্বাধিক 1024 নতুন টোকেন সহ।

10. **প্রতিক্রিয়া ডিকোড করা**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - এই লাইনটি তৈরি করা টোকেনগুলোকে আবার মানুষের পাঠযোগ্য স্ট্রিংয়ে রূপান্তর করে, বিশেষ টোকেন এড়িয়ে যায় এবং প্রথম ফলাফলটি ফেরত দেয়।

**অস্বীকৃতি**:  
এই নথিটি মেশিন-ভিত্তিক এআই অনুবাদ পরিষেবাগুলির মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে দয়া করে সচেতন থাকুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসংগতি থাকতে পারে। নথিটির মূল ভাষায় থাকা সংস্করণটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।