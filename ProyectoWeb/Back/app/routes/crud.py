from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Optional
from app.services.database import db_crud

router = APIRouter(prefix="/api", tags=["CRUD"])

class RecordData(BaseModel):
    # Datos dinámicos del formulario
    pass

@router.get("/tables")
async def list_tables():
    """Listar todas las tablas"""
    return {"tables": db_crud.get_tables()}

@router.get("/table/{table_name}/structure")
async def get_table_structure(table_name: str):
    """Estructura para generar formulario"""
    structure = db_crud.get_table_structure(table_name)
    if not structure:
        raise HTTPException(404, f"Tabla '{table_name}' no encontrada")
    return {"table": table_name, "fields": structure}

@router.get("/table/{table_name}")
async def get_table_records(
    table_name: str,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):
    """Lista paginada de registros"""
    if table_name not in db_crud.get_tables():
        raise HTTPException(404, f"Tabla no encontrada")
    
    return db_crud.get_table_records(table_name, page, limit)

@router.get("/table/{table_name}/{record_id}")
async def get_record(table_name: str, record_id: int):
    """Registro específico para editar"""
    record = db_crud.get_record(table_name, record_id)
    if not record:
        raise HTTPException(404, "Registro no encontrado")
    return record

@router.post("/table/{table_name}/insert")
async def insert_record(table_name: str, data: dict):
    """Insertar nuevo registro"""
    try:
        new_id = db_crud.insert_record(table_name, data)
        return {"success": True, "id": new_id, "message": "Registro creado exitosamente"}
    except Exception as e:
        raise HTTPException(400, f"Error insertando: {str(e)}")

@router.put("/table/{table_name}/{record_id}")
async def update_record(table_name: str, record_id: int, data: dict):
    """Actualizar registro"""
    success = db_crud.update_record(table_name, record_id, data)
    if not success:
        raise HTTPException(404, "No se pudo actualizar el registro")
    return {"success": True, "message": "Registro actualizado"}

@router.delete("/table/{table_name}/{record_id}")
async def delete_record(table_name: str, record_id: int):
    """Eliminar registro"""
    success = db_crud.delete_record(table_name, record_id)
    if not success:
        raise HTTPException(404, "Registro no encontrado")
    return {"success": True, "message": "Registro eliminado"}
