from core.config import settings
from llm.factory import LLMFactory
from services.prompt import rag_prompt




class LLMService:


    def __init__(self):
        
        provider = settings.PROVIDER
        self.llm = LLMFactory.create(provider = provider)
        self.prompt = rag_prompt
        self.chain = self.prompt | self.llm


    def generate(self, raw_text:str):

        response = self.chain.invoke({
            "raw_text": raw_text
        })
        return response.content