# app/services/database.py
import sqlite3
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

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
                VALUES ('Juan Pérez', 'juan@test.com', 28);
            """)
            conn.commit()
            conn.close()
    
    # ... resto de métodos CRUD (get_tables, get_table_structure, etc.)
    # Copia el código completo de mi respuesta anterior
