from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

#print("DATABASE_URL:", DATABASE_URL)

#Crear el motor de conexión
engine = create_engine(DATABASE_URL)

#Crear una sesión (interfaz etre FastAPI y la base de datos)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Función que genera una sesión de BD en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    print("🔍 Probando conexión a la base de datos...")
    try:
        with engine.connect() as connection:
            print("✅ Conexión exitosa a la base de datos")
    except Exception as e:
        print("❌ Error de conexión:", e)