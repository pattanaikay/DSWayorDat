"""
Write Python code to compute embeddings using OpenAI’s API and perform cosine similarity for document retrieval

"""

import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

openai.api_key = ""

def get_embedding(text):
    response = openai.embeddings.create(input=text, model="text-embedding-ada-002")

    return np.array(response['data'][0]['embedding'])

query = ""
documents = []

# compute embeddings
query_embeddings = get_embedding(query)
document_embeddings = np.array([get_embedding(doc) for doc in documents])

# perform cosine similarities
similarities = cosine_similarity([query_embeddings], document_embeddings)[0]
best_match_idx = np.argmax(similarities)
print(best_match_idx)