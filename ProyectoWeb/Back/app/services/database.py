# app/services/database.py - VERSIÓN FINAL
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

class SQLiteCRUDService:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()
    
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_db(self):
        """🎯 TABLA PERSONAS - Campos EXACTOS del formulario"""
        if not self.db_path.exists():
            conn = self._get_connection()
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS personas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    primer_nombres TEXT NOT NULL,
                    segundo_nombre TEXT,
                    primer_apellido TEXT NOT NULL,
                    segundo_apellido TEXT,
                    documento TEXT CHECK(documento IN ('CC', 'TI', 'CE', 'PA')),
                    numero_identificacion TEXT UNIQUE NOT NULL,
                    domicilio TEXT,
                    fecha_nacimiento DATE,
                    edad INTEGER CHECK(edad >= 0 AND edad <= 120),
                    sexo TEXT CHECK(sexo IN ('M', 'F', 'O')),
                    numero_celular TEXT,
                    direccion TEXT NOT NULL,
                    barrio TEXT,
                    email TEXT UNIQUE,
                    activo BOOLEAN DEFAULT 1,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                
                INSERT OR IGNORE INTO personas (
                    primer_nombres, segundo_nombre, primer_apellido, segundo_apellido,
                    documento, numero_identificacion, domicilio, fecha_nacimiento, 
                    edad, sexo, numero_celular, direccion, barrio, email
                ) VALUES 
                    ('Juan Carlos', 'Andrés', 'Pérez', 'Gómez', 'CC', '123456789', 
                     'Calle 123 #45-67', '1990-05-15', 33, 'M', '+573001234567', 
                     'Av. Siempre Viva 742', 'Centro', 'juan.perez@email.com'),
                    ('María José', NULL, 'López', 'Martínez', 'TI', '987654321', 
                     'Carrera 7 #20-30', '1988-11-22', 35, 'F', '+573009876543', 
                     'Diagonal 50 #12-45', 'Laureles', 'maria.lopez@email.com');
            """)
            conn.commit()
            conn.close()
            print(f"✅ DB 'personas' creada para formulario")
    
    # ... resto de métodos SIN CAMBIOS (get_tables, get_structure, etc.)
    def get_tables(self) -> List[str]:
        conn = self._get_connection()
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = [row['name'] for row in cursor.fetchall()]
        conn.close()
        return tables
    
    def get_table_structure(self, table_name: str) -> List[Dict]:
        conn = self._get_connection()
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        columns = []
        for row in cursor.fetchall():
            col = dict(row)
            col['field_type'] = self._map_sql_type(col['type'])
            col['required'] = col['notnull'] == 1 and col['pk'] == 0
            col['is_pk'] = col['pk'] == 1
            columns.append(col)
        conn.close()
        return [c for c in columns if not c['is_pk']]
    
    def _map_sql_type(self, sql_type: str) -> str:
        sql_type = sql_type.upper()
        if 'INT' in sql_type or 'INTEGER' in sql_type: return 'number'
        if 'REAL' in sql_type: return 'number'
        if 'TEXT' in sql_type: return 'text'
        if 'DATE' in sql_type: return 'date'
        if 'BOOLEAN' in sql_type: return 'checkbox'
        return 'text'
    
    # Métodos CRUD (sin cambios)
    def get_table_records(self, table_name: str, page: int = 1, limit: int = 20) -> Dict:
        offset = (page - 1) * limit
        conn = self._get_connection()
        cursor = conn.execute(f"SELECT COUNT(*) as total FROM `{table_name}`")
        total = cursor.fetchone()['total']
        cursor = conn.execute(f"SELECT * FROM `{table_name}` ORDER BY id DESC LIMIT ? OFFSET ?", (limit, offset))
        records = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"records": records, "total": total, "page": page, "limit": limit}
    
    def get_record(self, table_name: str, record_id: int) -> Optional[Dict]:
        conn = self._get_connection()
        cursor = conn.execute(f"SELECT * FROM `{table_name}` WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    
    def insert_record(self, table_name: str, data: Dict) -> int:
        columns = list(data.keys())
        placeholders = ','.join(['?' for _ in columns])
        values = tuple(data.values())
        conn = self._get_connection()
        cursor = conn.execute(f"INSERT INTO `{table_name}` ({','.join(columns)}) VALUES ({placeholders})", values)
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id
    
    def update_record(self, table_name: str, record_id: int, data: Dict) -> bool:
        if not data: return False
        set_clause = ', '.join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values()) + (record_id,)
        conn = self._get_connection()
        cursor = conn.execute(f"UPDATE `{table_name}` SET {set_clause} WHERE id = ?", values)
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result
    
    def delete_record(self, table_name: str, record_id: int) -> bool:
        conn = self._get_connection()
        cursor = conn.execute(f"DELETE FROM `{table_name}` WHERE id = ?", (record_id,))
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result

db_crud = SQLiteCRUDService(Path("database.db"))