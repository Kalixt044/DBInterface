# app/services/database.py - CÓDIGO COMPLETO Y CORREGIDO
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional

class SQLiteCRUDService:
    def __init__(self, db_path: Path):
        """Inicializador con creación automática de DB"""
        self.db_path = db_path
        self._init_db()  # ✅ Llamada al método que faltaba
    
    def _get_connection(self):
        """Conexión segura para múltiples hilos"""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _init_db(self):
        """🆕 CREAR TABLA USERS con campos del FORMULARIO"""
        if not self.db_path.exists():
            conn = self._get_connection()
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    telefono TEXT,
                    edad INTEGER CHECK(edad >= 0),
                    fecha_nacimiento DATE,
                    ciudad TEXT,
                    pais TEXT,
                    activo BOOLEAN DEFAULT 1,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                
                -- 📊 Datos de ejemplo para el formulario
                INSERT OR IGNORE INTO users (nombre, apellido, email, telefono, edad, fecha_nacimiento, ciudad, pais, activo) 
                VALUES 
                    ('Juan', 'Pérez', 'juan@test.com', '+573001234567', 28, '1995-03-15', 'Bogotá', 'Colombia', 1),
                    ('María', 'López', 'maria@test.com', '+573009876543', 34, '1989-07-22', 'Medellín', 'Colombia', 1),
                    ('Ana', 'Gómez', 'ana@test.com', '+573005555555', 29, '1994-05-20', 'Cali', 'Colombia', 1);
            """)
            conn.commit()
            conn.close()
            print(f"✅ DB creada: {self.db_path}")
    
    def get_tables(self) -> List[str]:
        """📋 Listar tablas disponibles"""
        conn = self._get_connection()
        cursor = conn.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
        """)
        tables = [row['name'] for row in cursor.fetchall()]
        conn.close()
        return tables
    
    def get_table_structure(self, table_name: str) -> List[Dict]:
        """📝 Estructura para formularios dinámicos"""
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
        return [c for c in columns if not c['is_pk']]  # Excluir ID
    
    def _map_sql_type(self, sql_type: str) -> str:
        """🔄 SQL → HTML input types"""
        sql_type = sql_type.upper()
        if 'INT' in sql_type or 'INTEGER' in sql_type:
            return 'number'
        elif 'REAL' in sql_type:
            return 'number'
        elif 'TEXT' in sql_type:
            return 'text'
        elif 'DATE' in sql_type:
            return 'date'
        elif 'BOOLEAN' in sql_type:
            return 'checkbox'
        return 'text'
    
    def get_table_records(self, table_name: str, page: int = 1, limit: int = 20) -> Dict:
        """📊 Registros paginados"""
        offset = (page - 1) * limit
        conn = self._get_connection()
        
        cursor = conn.execute(f"SELECT COUNT(*) as total FROM `{table_name}`")
        total = cursor.fetchone()['total']
        
        cursor = conn.execute(f"""
            SELECT * FROM `{table_name}` 
            ORDER BY id DESC 
            LIMIT ? OFFSET ?
        """, (limit, offset))
        
        records = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return {"records": records, "total": total, "page": page, "limit": limit}
    
    def get_record(self, table_name: str, record_id: int) -> Optional[Dict]:
        """✏️ Registro por ID"""
        conn = self._get_connection()
        cursor = conn.execute(f"SELECT * FROM `{table_name}` WHERE id = ?", (record_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    
    def insert_record(self, table_name: str, data: Dict) -> int:
        """➕ Insertar nuevo registro"""
        columns = list(data.keys())
        placeholders = ','.join(['?' for _ in columns])
        values = tuple(data.values())
        
        conn = self._get_connection()
        cursor = conn.execute(f"""
            INSERT INTO `{table_name}` ({','.join(columns)}) 
            VALUES ({placeholders})
        """, values)
        
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id
    
    def update_record(self, table_name: str, record_id: int, data: Dict) -> bool:
        """🔄 Actualizar registro"""
        if not data:
            return False
        
        set_clause = ', '.join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values()) + (record_id,)
        
        conn = self._get_connection()
        cursor = conn.execute(f"""
            UPDATE `{table_name}` SET {set_clause} WHERE id = ?
        """, values)
        
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result
    
    def delete_record(self, table_name: str, record_id: int) -> bool:
        """🗑️ Eliminar registro"""
        conn = self._get_connection()
        cursor = conn.execute(f"DELETE FROM `{table_name}` WHERE id = ?", (record_id,))
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result

# 🎯 Instancia global para routes
db_crud = SQLiteCRUDService(Path("database.db"))