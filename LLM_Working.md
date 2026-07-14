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


The tokens are in one dimenssional sequence.

### Model needs token to think
Each token goes through a finite neural network of computations. Now if you ask model to return the answer in one token, it will most likely be incorrect. but if you allow the model to use many tokens, it will in iterative reasoning approach, go step by step as trained by human lablers, and there is maximum chance of getting a correct answer.
The models are not good at couting, so if i give the model this prompt
```
how many dots are below

.....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................

use single token to answer, do not use any tools
```

The model takes a random guess which is incorrect (as of July 2026 models). Then you allow it to use code, or reasoning it can come up with the correct answer. So always ask the model to use tools or reasoning when doing such thinking or computational task.
But the models are improving at an incredible fast pace maybe because of large training data like we hear billions of parameters.

### Few things models are not good at
1 - Spelling, models don't see characters or words , they see tokens, so 3 char can be a single token, so they struggle with this.
2 - Counting

## Stages of Model
```
Raw Text
    │
    ▼
Pretraining
    │
    ▼
Base Model
    │
    ▼
Supervised Fine-Tuning (SFT)
    │
    ▼
Preference Optimization
(RLHF, DPO, RFT, etc.)
    │
    ▼
Safety & Alignment Training
    │
    ▼
Post-Trained Model

```

A base model is the model immediately after its initial large-scale training on massive amounts of text. A post-trained model is that same base model after it has undergone additional training to make it more helpful, safe, and better at following instructions.

| Base Model                                            | Post-Training Model                                                    |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| Learns language patterns from raw text.               | Learns how to interact with users effectively.                         |
| Predicts the next token based on the prompt.          | Follows instructions, answers questions, and behaves conversationally. |
| May produce unsafe, irrelevant, or unhelpful outputs. | Is aligned to be safer, more helpful, and more truthful.               |
| Doesn't naturally follow instructions well.           | Specifically optimized for instruction following.                      |

## RLHF
Reinforcement learning teaches a model to improve its behavior by rewarding desirable outputs and discouraging undesirable ones, rather than simply memorizing example answers.


## Vector
A vector in LLM is a numerical representation of a token meaning and relationships.
No human decide the what numbers represent a token, the numbers are generated over thousands of iterations of training. first model predicts a random number to represent a token, then tries to predict the word in a sentence. An optimizer (algorithm Adam or SGD) then see the word and decides to tweak the vector if the prediction is wrong, this happens billions of times and eventually we have a useful representation.

### Dimenssions
Humans decide how many dimenssions the vector will have.
If the embedding dimension is 4096, then every token is represented by a vector of 4096 numbers.

| Model        | Embedding Dimension |
| ------------ | ------------------: |
| Small model  |                 256 |
| Medium model |                 768 |
| GPT-2 Small  |                 768 |
| Llama 3 8B   |                4096 |

Why thousands of dimensions?
Each individual number in a vector represents a attribute or you can say answers a question. For example describing a person, we can't represent it with only two attributes like heigh or age, if we add more attributes like hair color, gender, profession, language etc, now we have a better chance of representing human. Instead of 2 features, an LLM might have 4096 learned features.
