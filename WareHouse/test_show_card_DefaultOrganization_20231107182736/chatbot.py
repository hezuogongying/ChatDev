'''
This file contains the Chatbot class responsible for generating responses.
'''
from transformers import GPT2LMHeadModel, GPT2Tokenizer
class Chatbot:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    def generate_response(self, message):
        input_ids = self.tokenizer.encode(message, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=100, num_return_sequences=1)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response