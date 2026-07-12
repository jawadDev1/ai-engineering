
## Two types of LLMs

### Base LLm
predicts next word based on text training data.

## Instruction Tuned LLM
Tries to follow instructions.

Fine tuned on instructions, and good attempts to follow the instructions.

RLHF: Reinforment learning with human feedback.

## Principles

### Clear & specific instructions
Clear prompt is not equal to short prompt. To guide a model toward desired outcomes, prompts should be clear, specific, and often lengthier to provide sufficient context, rather than simply short.

#### Use Tactics
Tactic 1:
- Use delimeters like """, ```, --- , <>, to tell model on which text to specifically work and avoid prompt injection.

```prompt
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""
```

Tactic 2:
- Ask for structured output like Json or html.

```prompt
prompt = """
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""
```

Tactic 3:
- Ask model to check weather condition is satisfied or not

```prompt
prompt = f"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

\"\"\"{text_1}\"\"\"
"""
```

Tactic 4:
- few-shot prompting
- Give successfull examples of completing tasks, then ask model to perform task.
```prompt
prompt = """
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""

```

### Give the model time to think
if the task is long, give the model time to think otherwise it will make guesses which will most likely be incorrect.

Tactic 1:
- Describe proper steps
```prompt
prompt_2 = f"""
Perform the following actions:
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```

Your task is to perform the following actions:
1 - Summarize the following text delimited by
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
```

Tactic 2:
- Instruct the model to workout it's own solution before rushing to conclusion


## Model Limitations
Hallucination - makes statement that sound palusible but are not true.

The paper does not exist but model hallucinates and tells descriptions about the paper
```
prompt = """
Summarize the main findings of the paper "Quantum Trees for Neural Reasoning" by John Smith and Alice Doe, published in Nature in 2024. Include three direct quotes.
"""
```
