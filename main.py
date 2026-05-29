import uvicorn
from fastapi import FastAPI
from api.routes.upload import router as upload_router
from api.routes.download import router as download_router


app = FastAPI()

app.include_router(upload_router)
app.include_router(download_router)


if __name__ == "__main__":


    uvicorn.run(
        app=app,
        port=8000
    )