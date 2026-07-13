
GPT - Generative Pre-trained Transformer

Google first introduced the transformer model, for Google translate.
The transformer takes an input text and transforms it into some output it can be text or image.

The transformer perdicts the next word.

# Transformer Architecture
## Encoding
### Tokenization
When we get the text from user, the first task is to tokenize it, split it into tokens (words).
Tokenization is the processing of diving user text and mapping each token to a particular number. It varies according to model for example
in Gpt-4o, the tokenization looks like this
```
Tokens:
<|im_start|>user<|im_sep|>I am a token<|im_end|><|im_start|>assistant<|im_sep|>

Mapped Numbers - Tokens for machine:
200264, 1428, 200266, 40, 939, 261, 6602, 200265, 200264, 173781, 200266

```

It maps to numbers because it easier for computer to understand and process

Each model has a vocabulary size, voc size decide how big or complex a token can be for example for some model Hey can be a single token and for some H a toke, E a token and Y a token.

### Vector Embeddings
A vector embedding converts any data point (word, sentence, image, audio, etc.) into an n‑dimensional array of numbers that captures the data’s essential characteristics so machine‑learning models can process it.

## Positional Encoding
Adds some data about the position of the toeksn in the sentence.

## Multi-head attention
Self Attention it allow to have context. the words meanings changes with context. 
The multi-head attention allows vector embeddings to talk to each other.
