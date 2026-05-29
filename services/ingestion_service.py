import json
from core.logger import logger
from core.config import settings
from services.llm_service import LLMService
from services.embedding_service import EmbeddingService
from db.qdrant_db import VectorDB




class IngestionService:


    def __init__(self):
        
        self.llm = LLMService()
        self.embedding_service = EmbeddingService()
        self.db = VectorDB(host = settings.HOST, port = settings.QDRANT_PORT)


    def ingest_file(self, path:str, collection_name:str, id:str):

        docs = self.embedding_service.extract_text(path = path)
        contents = self.embedding_service.preprocess_documents(docs = docs.copy())
        text = "\n".join(contents)
        user_details = self.llm.generate(raw_text = text)
        user_details = json.loads(user_details)
        payload = {
            "user": user_details,
            "text": text
        }
        print(f"user details: {user_details}")
        print(f"type: {type(user_details)}")
        embeddings = self.embedding_service.embed_query(query = text)
        # self.db.delete_collection(collection_name = collection_name)
        self.db.create_collection(collection_name = collection_name)
        upserted = self.db.upsert_to_db(embeddings = [embeddings],
                             payload = [payload],
                             collection_name = collection_name, id=id)

        # logger.info(f"data upserted successfully")
        return upserted
    

    def delete_collection(self, collection_name:str):

        self.db.delete_collection(collection_name = collection_name)


    def create_collection(self, collection_name:str):

        self.db.create_collection(collection_name = collection_name)


    def scroll(self, collection_name:str):

        return self.db.scroll(collection_name=collection_name)
