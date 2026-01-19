from fastapi import FastAPI
from app.api.items import router as items_router

app = FastAPI(
    title="My Portfolio API",
    version="1.0.0"
)

app.include_router(items_router, prefix="/items")

@app.get("/")
def root():
    return {"message": "FastAPI Portfolio is running!"}
