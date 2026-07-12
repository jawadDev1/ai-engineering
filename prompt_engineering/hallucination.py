import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_completion(prompt, model="gemini-2.5-flash"):
    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )

    return response.text


# Hallucination
# the paper does not exist but model hallucinates
prompt = """
Summarize the main findings of the paper "Quantum Trees for Neural Reasoning" by John Smith and Alice Doe, published in Nature in 2024. Include three direct quotes.
"""

print(get_completion(prompt=prompt))
