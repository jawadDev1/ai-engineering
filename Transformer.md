# Transformer
Introduced in 2017 by google.

A transformer can transform many things like
Text => Text
Text => Audio
Text => Image

Transformer can be divided into two main parts Encoder & Decoder.

## Encoder
In encoder the input text from user is converted into tokens and contextual embeddings are generated.

## Decoder
Decoder takes the contextual embeddings and tries to predict the next word. Decoder can take two types of inputs, one from encoder and second input is previous words/tokes + newly predicted word.

### Positional Embedding
Model needs to keep track of the position of a workd or token, because if the position of a token is misplaced it can change the meaning on entire sentence.
