import argparse
import onnxruntime_genai as og

parser = argparse.ArgumentParser()
parser.add_argument("--phrase", type=str)
parser.add_argument("--model-path", type=str)
args = parser.parse_args()

prompt = f"<|user|>\n{args.phrase}<|end|>\n<|assistant|>\n"

model=og.Model(f'{args.model_path}')

tokenizer = og.Tokenizer(model)

tokens = tokenizer.encode(prompt)

params=og.GeneratorParams(model)
params.set_search_options(max_length=100)
params.input_ids = tokens

generator=og.Generator(model, params)
tokenizer_stream=tokenizer.create_stream()

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()
    print(tokenizer_stream.decode(generator.get_next_tokens()[0]), end='', flush=True)

