
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


text = "Islamabad is the capital of pakistan"

documents = [
    "Widely regarded as one of cricket's greatest all-rounders, Imran khan captained Pakistan to its historic 1992 World Cup victory. His charismatic leadership and lethal fast bowling inspired generations of athletes across the nation.",
    "Wasim Akram Known as the 'Sultan of Swing,' he mastered left-arm pace and reverse swing to become one of the most feared bowlers in cricket history. He remains Pakistan’s all-time leading wicket-taker in both Test and ODI cricket.",
    "shahid afridi Nicknamed 'Boom Boom,' he captivated fans worldwide with his fearless, explosive batting and match-winning leg-spin. His record-shattering 37-ball ODI century held the world record for nearly two decades.",
    "Babar azam Renowned for his picture-perfect cover drive, he established himself as a world-class batsman across all three formats of the game. His steady run-scoring and calm temperament brought him long stints at the top of the ICC rankings.",
    "Shaheen shah afridi, Towering with raw pace and sharp first-over swing, he quickly became the frontline leader of Pakistan's bowling attack. His knack for striking early in the innings makes him one of the most dangerous opening bowlers in modern cricket.",
]


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "tell me about imran khan"
# vector = embedding.embed_query(text)
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index , score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(documents[index])
print("Similarity score :: ", score)