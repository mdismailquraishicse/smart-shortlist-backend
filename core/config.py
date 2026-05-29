from pydantic_settings import BaseSettings



class Settings(BaseSettings):



    HUGGINGFACEHUB_API_TOKEN:str
    # QDRANT CREDS
    HOST:str = "localhost"
    QDRANT_PORT:int = 6333
    COLLECTION_RESUME:str = "resume"
    COLLECTION_JD:str = "jd"

    # LLM
    MODEL_NAME:str = "Qwen/Qwen2.5-72B-Instruct"
    PROVIDER:str = "hf"
    TOP_K:int = 5
    TOP_P:float = 0.8
    TEMPERATURE:float = 0.5
    MAX_NEW_TOKENS:int = 50

    # FOLDERS
    UPLOAD_RESUME_DIR:str = "uploads/resume"
    UPLOAD_JD_DIR:str = "uploads/jd"

    class Config:
        env_file = ".env"


settings = Settings()