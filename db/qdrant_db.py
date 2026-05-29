from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams


class VectorDB:


    def __init__(self, host:str, port:int):
        
        self.client = QdrantClient(
            host = host,
            port = port
        )

        self.vector_config = VectorParams(
            size = 768,
            distance = Distance.COSINE
        )


    def create_collection(self, collection_name:str):

        collections = self.client.get_collections().collections
        existing = [collection.name for collection in collections]
        if collection_name not in existing:
            response = self.client.create_collection(
                collection_name = collection_name,
                vectors_config = self.vector_config
            )
            return response
    

    def delete_collection(self, collection_name:str):

        return self.client.delete_collection(collection_name = collection_name)
    

    def upsert_to_db(self, embeddings, payload, collection_name:str, id:str):

        for i in range(0, len(embeddings)):

            self.client.upsert(
                collection_name = collection_name,
                wait = True,
                points = [PointStruct(
                    id = id,
                    vector = embeddings[i],
                    payload = {
                        "text" : payload[i].get("text"),
                        "user": payload[i].get("user")
                        }
                )]
            )

        return True
    

    def search_similar_docs(self, embedding, collection_name:str, k:int):

        data = self.client.query_points(
            collection_name = collection_name,
            query = embedding,
            with_payload = True,
            limit = k
        )

        return data
    

    def scroll(self, collection_name:str):

        all_points = []
        offset = None

        while True:
            points, offset = self.client.scroll(
                collection_name=collection_name,
                limit=100,
                offset=offset
            )

            all_points.extend(points)

            if offset is None:
                break

        print(f"Total points: {len(all_points)}")
        return all_points