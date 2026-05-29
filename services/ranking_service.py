# import pandas as pd
from core.config import settings
from db.qdrant_db import VectorDB
from services.embedding_service import EmbeddingService



class Rank:



    def __init__(self):
        
        self.db = VectorDB(host = settings.HOST, port = settings.QDRANT_PORT)
        self.embedding_service = EmbeddingService()


    def rank(self, path:str, collection_name:str, k:int):

        docs = self.embedding_service.extract_text(path = path)
        contents = self.embedding_service.preprocess_documents(docs = docs)
        text = "\n".join(contents)
        embeddings = self.embedding_service.embed_query(query = text)
        similar_docs = self.db.search_similar_docs(embedding = embeddings,
                                    collection_name = collection_name, k = k).points

        result = []
        for doc in similar_docs:
            user = {}
            payload = doc.payload or {}
            curr_user = payload.get("user", {})

            user["id"] = doc.id
            user["score"] = doc.score
            user["name"] = curr_user.get("name")
            user["mobile"] = curr_user.get("mobile")
            user["email"] = curr_user.get("email")
            user["city"] = curr_user.get("city")
            result.append(user)

        # df = pd.DataFrame(result)
        # print(df)
        return result