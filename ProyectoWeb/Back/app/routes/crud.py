# app/routes/crud.py - Completo
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.database import db_crud

router = APIRouter(prefix="/api", tags=["CRUD"])

@router.get("/tables")
async def list_tables():
    return {"tables": db_crud.get_tables()}

@router.get("/table/{table_name}/structure")
async def get_table_structure(table_name: str):
    structure = db_crud.get_table_structure(table_name)
    if not structure:
        raise HTTPException(404, f"Tabla '{table_name}' no encontrada")
    return {"table": table_name, "fields": structure}

# ... resto de rutas CRUD