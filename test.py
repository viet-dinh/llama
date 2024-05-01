from llama_cpp import Llama

# conda activate llama
# https://github.com/abetlen/llama-cpp-python

llm = Llama(model_path="./models/mistral-7b-openorca.gguf2.Q4_0.gguf",
            n_gpu_layers=1, n_ctx=4096)

# output = llm.create_completion("""<|im_start|>system
# You are a helpful chatbot.
# <|im_end|>
# <|im_start|>user
# Hello, tell me where can I learn Python?<|im_end|>
# <|im_start|>assistant""", max_tokens=500,  stop=["<|im_end|>"], stream=True)

# for token in output:
#     print(token["choices"][0]["text"], end='', flush=True)

output = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that outputs in JSON.",
        },
        {"role": "user", "content": "Who won the world series in 2020"},
    ],
    response_format={
        "type": "json_object",
    },
    temperature=0.7,
)

print(output)
