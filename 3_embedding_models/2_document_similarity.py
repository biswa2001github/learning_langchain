from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "What is capital of India?",
    "Virat Kohli is an Indian cricketer.",
    "Rohit Sharma captains Indian team",
    "Prime Minister of India resides in Delhi."
]

query = "What is the political scenario of the country?"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index, score = max(enumerate(scores),key=lambda x:x[1])

print(documents[index])
print(f"Similarity Score: {score}")

