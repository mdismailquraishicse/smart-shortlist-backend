import os
import glob
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import FileResponse
from core.config import settings


router = APIRouter(prefix = "/download", tags = ["Download"])
UPLOAD_RESUME = settings.UPLOAD_RESUME_DIR
UPLOAD_JD = settings.UPLOAD_JD_DIR


@router.get("/resume/{id}")
def get_resume(id:str):

    files = glob.glob(f"{UPLOAD_RESUME}/{id}.*")
    if not files:
        raise HTTPException( status_code=404, detail="Resume not found")

    file_path = files[0]

    return FileResponse(
        path=file_path,
        filename=os.path.basename(file_path),
        media_type="application/octet-stream"
        )
