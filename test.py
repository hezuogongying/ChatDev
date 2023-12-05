from camel.typing import ModelType
from camel.model_backend import OpenAIModel
import os
import json

# 简洁版本测试1
def main():
    question = 'What is the capital of France'
    model_name = ModelType.GPT_3_5_TURBO
    ask_data = [
        {"role": "user", "content": question}
    ]
    model_config_dict = {
        'temperature': 0.2,
        'max_tokens': None
    }
    Gpt = OpenAIModel(model_type=model_name, model_config_dict=model_config_dict)
    response = Gpt.run(messages=ask_data)
    print(type(response))
    print(response)
    return response


if __name__ == "__main__":
    main()