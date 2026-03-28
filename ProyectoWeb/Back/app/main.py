from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.crud import router as crud_router

app = FastAPI(title="DB CRUD API - SQLite")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud_router)

@app.get("/")
async def root():
    return {"message": "DB CRUD API funcionando", "docs": "/docs"}
