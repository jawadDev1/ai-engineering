import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="featherless-ai",
    api_key=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)


result = client.chat_completion(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[{"role": "user", "content": "what is the capital of pakistan"}],
)

print(result)
