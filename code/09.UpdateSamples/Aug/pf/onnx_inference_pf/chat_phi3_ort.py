
from promptflow.core import tool
import onnxruntime_genai as og
import time,uuid


class PhiChatBot:

    model = None
    tokenizer = None
    tokenizer_stream = None
    
    @staticmethod
    def init_phi():
        if PhiChatBot.model is None or PhiChatBot.tokenizer is None or PhiChatBot.tokenizer_stream is None:
            
            PhiChatBot.model = og.Model('Your Phi-3.5-Instruct ONNX Path')
            PhiChatBot.tokenizer = og.Tokenizer(PhiChatBot.model)
            PhiChatBot.tokenizer_stream = PhiChatBot.tokenizer.create_stream()
    

    @staticmethod
    def chat(input: str) -> str:
        # Ensure the model is initialized before trying to chat.
        
        PhiChatBot.init_phi()

        chat_template = '<|user|>\n{input} <|end|>\n<|assistant|>'
            
        prompt = f'{chat_template.format(input=input)}'

        input_tokens = PhiChatBot.tokenizer.encode(prompt)

        search_options = {
            # Set the maximum length of the generated output to 1024 tokens
            "max_length": 512,
            
            # Set the temperature parameter to 0.6, which controls the randomness of the output
            # Lower values make the output more deterministic, while higher values make it more random
            "temperature": 0.3
        }
        
        params = og.GeneratorParams(PhiChatBot.model)
        params.input_ids = input_tokens
        params.set_search_options(**search_options)
        generator = og.Generator(PhiChatBot.model, params)

        result = ''

        while not generator.is_done():
            generator.compute_logits()
            generator.generate_next_token()

            new_token = generator.get_next_tokens()[0]
            result += PhiChatBot.tokenizer_stream.decode(new_token)

        return result

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def chat_with_phi(input: str) -> str:
    return PhiChatBot.chat(input)
