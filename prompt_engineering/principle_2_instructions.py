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
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
# example 1
# prompt = f"""
# Perform the following actions:
# 1 - Summarize the following text delimited by triple \
# backticks with 1 sentence.
# 2 - Translate the summary into French.
# 3 - List each name in the French summary.
# 4 - Output a json object that contains the following \
# keys: french_summary, num_names.

# Separate your answers with line breaks.

# Text:
# ```{text}```
# """
# prompt_2 = f"""
# Perform the following actions:
# 1 - Summarize the following text delimited by triple \
# backticks with 1 sentence.
# 2 - Translate the summary into French.
# 3 - List each name in the French summary.
# 4 - Output a json object that contains the following \
# keys: french_summary, num_names.

# Separate your answers with line breaks.

# Text:
# ```{text}```

# Your task is to perform the following actions:
# 1 - Summarize the following text delimited by
#   <> with 1 sentence.
# 2 - Translate the summary into French.
# 3 - List each name in the French summary.
# 4 - Output a json object that contains the
#   following keys: french_summary, num_names.

# Use the following format:
# Text: <text to summarize>
# Summary: <summary>
# Translation: <summary translation>
# Names: <list of names in summary>
# Output JSON: <json with summary and num_names>

# Text: <{text}>
# """

# ||||||||| Tactic 2 - Work out your own solution first ||||||||||||

# Model says solution is correct even though solution is wrong only the last line and asnwer is correct that why model says it's correct
# prompt = """
# Determine if the student's solution is correct or not.

# Question:
# I'm building a solar power installation and I need \
#  help working out the financials.
# - Land costs $100 / square foot
# - I can buy solar panels for $250 / square foot
# - I negotiated a contract for maintenance that will cost \
# me a flat $100k per year, and an additional $10 / square \
# foot
# What is the total cost for the first year of operations
# as a function of the number of square feet.

# Student's Solution:
# Let x be the size of the installation in square feet.
# Costs:
# 1. Land cost: 100x
# 2. Solar panel cost: 250x
# 3. Maintenance cost: 100,000 + 100x
# Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
# """

prompt = """
Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem including the final total.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations \
as a function of the number of square feet.
```
Student's solution:
```
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:
"""

print(get_completion(prompt=prompt))
