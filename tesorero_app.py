# tesorero_app.py
import sqlite3
import os
from datetime import datetime

DB_PATH = os.getenv("DB_PATH", "tesorero.db")

def init_db():
    """Inicializar base de datos SQLite"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            monto REAL NOT NULL,
            comision REAL NOT NULL,
            fecha TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concepto TEXT NOT NULL,
            monto REAL NOT NULL,
            fecha TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """)

def registrar_venta(producto: str, monto: float, comision: float = None):
    """Registrar una venta en la base de datos"""
    if comision is None:
        comision = monto * 0.15  # 15% por defecto
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO ventas (producto, monto, comision) VALUES (?, ?, ?)",
            (producto, monto, comision)
        )

def registrar_gasto(concepto: str, monto: float):
    """Registrar un gasto"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO gastos (concepto, monto) VALUES (?, ?)",
            (concepto, monto)
        )

def estado():
    """Obtener estado financiero"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(monto) FROM ventas")
        ingresos = cursor.fetchone()[0] or 0.0
        cursor.execute("SELECT SUM(comision) FROM ventas")
        comisiones = cursor.fetchone()[0] or 0.0
        cursor.execute("SELECT SUM(monto) FROM gastos")
        gastos = cursor.fetchone()[0] or 0.0
        cursor.execute("SELECT COUNT(*) FROM ventas")
        ventas_count = cursor.fetchone()[0] or 0
        return {
            "ingresos": ingresos,
            "gastos": gastos,
            "saldo": ingresos - gastos,
            "ventas_count": ventas_count,
            "comisiones": comisiones
        }

# Inicializar DB al importar
init_db()
