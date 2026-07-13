# LLM Working - Raw version

## Parameters
Parameters are the model's learned knowledge represented as numerical weights. During inference, the model uses these parameters together with the input prompt to predict the next most likely token.

## In-Context Learning
When you give a few-shot prompt (prompt with examples) to an llm, it identifies and recognizes the pattern, and tries to learn and continue the pattern to predict the next token based on pattern provided.
For example
```
  "hello": "안녕하세요",
  "thank you": "감사합니다",
  "water": "물",
  "food": "음식",
  "friend": "친구",
  "school": "학교",
  "book": "책",
  "house": "집",
  "computer": "컴퓨터",
  "love": 
```
the model will continue the patter and translate love to korean.
