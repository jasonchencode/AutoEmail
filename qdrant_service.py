from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from ingestQdrant import COLLECTION_NAME

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_email_examples(query, limit=2): 
    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name = COLLECTION_NAME,
        query = query_vector,
        limit = limit
    )

    examples = []
    for result in results.points:
        examples.append({
            "text": result.payload["text"],
            "type": result.payload["type"],
            "score": result.score
        })
    
    return examples