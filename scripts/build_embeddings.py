import json
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer


# Load catalog
with open("data/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


# Create searchable text
texts = [
    f"{item['name']} {item['description']} {item['test_type']}"
    for item in catalog
]


# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Generate embeddings
embeddings = model.encode(texts)


# Convert type
embeddings = np.array(embeddings).astype("float32")


# Save embeddings
np.save("data/embeddings.npy", embeddings)


# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])

index.add(embeddings)


# Save FAISS index
faiss.write_index(index, "data/faiss.index")


print("Embeddings and FAISS index created successfully.")