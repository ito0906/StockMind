import os
import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(os.environ["DATABASE_URL"])
        print("✅ Conexión a Neon PostgreSQL establecida correctamente")
        return conexion
    except Exception as error:
        print("❌ Error al conectar a Neon PostgreSQL:", error)
        return None

def desconectar(conexion):
    if conexion is not None:
        conexion.close()
        print("🔒 Conexión cerrada")
