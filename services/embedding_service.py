from core.logger import logger
from langchain_community.document_loaders import PyMuPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings




class EmbeddingService:


    def __init__(self):
        
        self.embedder = HuggingFaceEmbeddings()

    
    def extract_text(self, path:str):

        loader = PyMuPDFLoader(path)
        documents = loader.load()
        return documents
    

    def preprocess_documents(self, docs:list):

        contents = [doc.page_content.lower().
                    replace("\n", " ").
                    replace("-"," ").strip()
                    for doc in docs]

        return contents
    

    def embed_text(self, text: list[str]):

        return self.embedder.embed_documents(text)
    

    def embed_query(self, query:str):

        return self.embedder.embed_query(query)