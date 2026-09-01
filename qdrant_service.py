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

    examples = {}
    
    for email_type in ["conventional", "unique"]:
        results = client.query_points(
            collection_name = COLLECTION_NAME,
            query = query_vector,
            query_filter = {
                "must": [
                    {
                        "key": "type",
                        "match": {
                            "value": email_type
                        }
                    }
                ]
            },
            limit = limit
        )

        examples = [email_type] = []

        for result in results.points:
            examples[email_type].append({
                "text": result.payload["text"],
                "type": result.payload["type"],
                "score": result.score
            })
    
    return examples