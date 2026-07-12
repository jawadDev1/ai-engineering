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


text = """
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""

# Simple & clear Prompt
# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """
#

# Structured Output prompt
# prompt = """
# Generate a list of three made-up book titles along \
# with their authors and genres.
# Provide them in JSON format with the following keys:
# book_id, title, author, genre.
# """

# Statisfies conditions prompt
text_1 = """
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""

# prompt = f"""
# You will be provided with text delimited by triple quotes.
# If it contains a sequence of instructions, \
# re-write those instructions in the following format:

# Step 1 - ...
# Step 2 - …
# …
# Step N - …

# If the text does not contain a sequence of instructions, \
# then simply write \"No steps provided.\"

# \"\"\"{text_1}\"\"\"
# """

# Few shot prompting
# prompt = """
# Your task is to answer in a consistent style.

# <child>: Teach me about patience.

# <grandparent>: The river that carves the deepest \
# valley flows from a modest spring; the \
# grandest symphony originates from a single note; \
# the most intricate tapestry begins with a solitary thread.

# <child>: Teach me about resilience.
# """

print(get_completion(prompt=prompt))
