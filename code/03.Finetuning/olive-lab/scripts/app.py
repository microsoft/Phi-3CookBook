import onnxruntime_genai as og
import numpy as np
import time

model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
params.input_ids = tokenizer.encode("<|user|>\nwhere is the best place in london<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"[Travel]: Tell me what to do in London")
start = time.time()
token_count = 0
while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)
    token_count = token_count+1

print("\n")
end = time.time()
print(f"Tk.sec:{token_count/(end - start)}")
