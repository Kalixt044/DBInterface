# app/services/database.py - CÓDIGO COMPLETO
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
        if not self.db_path.exists():
            conn = self._get_connection()
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    age INTEGER,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL CHECK(price > 0),
                    category TEXT,
                    in_stock BOOLEAN DEFAULT 1
                );
                INSERT OR IGNORE INTO users (name, email, age) 
                VALUES ('Juan Pérez', 'juan@test.com', 28),
                       ('María López', 'maria@test.com', 34);
                INSERT OR IGNORE INTO products (name, price, category) 
                VALUES ('Laptop Dell', 899.99, 'Electrónicos');
            """)
            conn.commit()
            conn.close()
    
    def get_tables(self) -> List[str]:
        conn = self._get_connection()
        cursor = conn.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name NOT LIKE 'sqlite_%'
        """)
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
        if 'INT' in sql_type: return 'number'
        if 'REAL' in sql_type: return 'number'
        if 'TEXT' in sql_type: return 'text'
        if 'DATE' in sql_type: return 'date'
        return 'text'
    
    def get_table_records(self, table_name: str, page: int = 1, limit: int = 20) -> Dict:
        offset = (page - 1) * limit
        conn = self._get_connection()
        cursor = conn.execute("SELECT COUNT(*) as total FROM `{}`".format(table_name))
        total = cursor.fetchone()['total']
        cursor = conn.execute("SELECT * FROM `{}` ORDER BY id DESC LIMIT ? OFFSET ?".format(table_name), (limit, offset))
        records = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"records": records, "total": total, "page": page, "limit": limit}
    
    def get_record(self, table_name: str, record_id: int) -> Optional[Dict]:
        conn = self._get_connection()
        cursor = conn.execute("SELECT * FROM `{}` WHERE id = ?".format(table_name), (record_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    
    def insert_record(self, table_name: str, data: Dict) -> int:
        columns = list(data.keys())
        placeholders = ','.join(['?' for _ in columns])
        values = tuple(data.values())
        conn = self._get_connection()
        cursor = conn.execute("INSERT INTO `{}` ({}) VALUES ({})".format(
            table_name, ','.join(columns), placeholders), values)
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id
    
    def update_record(self, table_name: str, record_id: int, data: Dict) -> bool:
        if not data: return False
        set_clause = ', '.join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values()) + (record_id,)
        conn = self._get_connection()
        cursor = conn.execute("UPDATE `{}` SET {} WHERE id = ?".format(table_name, set_clause), values)
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result
    
    def delete_record(self, table_name: str, record_id: int) -> bool:
        conn = self._get_connection()
        cursor = conn.execute("DELETE FROM `{}` WHERE id = ?".format(table_name), (record_id,))
        result = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return result

# Instancia global
db_crud = SQLiteCRUDService(Path("database.db"))
