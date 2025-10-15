from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.core.config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

print("DATABASE_URL:", DATABASE_URL)

#Crear el motor de conexión
engine = create_engine(DATABASE_URL)

#Crear una sesión (interfaz etre FastAPI y la base de datos)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)