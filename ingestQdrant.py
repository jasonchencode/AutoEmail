from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams
from sentence_transformers import SentenceTransformer

from defaultQdrant import email_examples

client = QdrantClient(host="localhost", port=6333)

model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a persisten collection if it doesn't already exist
if not client.collection_exists("email_examples"):
    client.create_collection(
        collection_name="email_examples",
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

points = []

for email in email_examples: # can be changed into enumerate, with default IDs
    vector = model.encode(email["text"]).tolist()
    
    points.append(
        PointStruct(
            id=email["id"],
            vector=vector,
            payload={
                "text": email["text"],
                "source": "defaultQdrant.py",
                "type": email["type"]
            }
        )
    )

client.upsert(
    collection_name="email_examples",
    points=points
)

print(f"Added {len(points)} examples to Qdrant")