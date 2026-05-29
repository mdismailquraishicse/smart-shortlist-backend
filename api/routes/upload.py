import os
import shutil
import uuid
import traceback
from core.config import settings
from fastapi import APIRouter, File, UploadFile
from services.ingestion_service import IngestionService
from services.ranking_service import Rank



router = APIRouter(prefix = "/upload", tags = ["Upload"])
ingestion = IngestionService()
rank = Rank()

COLLECTION_JD = settings.COLLECTION_JD
COLLECTION_RESUME = settings.COLLECTION_RESUME
UPLOAD_RESUME = settings.UPLOAD_RESUME_DIR
UPLOAD_JD = settings.UPLOAD_JD_DIR



@router.post("/resume")
def upload_resume(file:UploadFile = File(...)):

    try:
        print(f"uploading resume...")
        id = str(uuid.uuid4())
        ext = file.filename.split(".")[-1]
        file_path = f"{UPLOAD_RESUME}/{id}.{ext}"
        os.makedirs(f"{UPLOAD_RESUME}", exist_ok=True)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        ingestion.ingest_file(path=file_path, collection_name = COLLECTION_RESUME, id=id)
        return {
            "status": "success",
            "result": True,
            "message": "file uploaded successfully",
            "error": None
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": traceback.format_exc(),
            "result": None,
            "message": str(e)
        }


@router.post("/jd")
def upload_jd(file:UploadFile = File(...)):

    try:
        print(f"uploading jd...")
        file_path = f"{UPLOAD_JD}/{file.filename}"
        os.makedirs(f"{UPLOAD_JD}", exist_ok=True)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        similar_docs = rank.rank(path = file_path, collection_name = COLLECTION_RESUME, k = 100)
        return {
            "status": "success",
            "message": "file uploaded successfully",
            "result": similar_docs,
            "error": None
        }

    except Exception as e:

        return {
            "status": "failed",
            "message": str(e),
            "result": [],
            "error": traceback.format_exc()
        }
