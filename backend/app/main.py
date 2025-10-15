from fastapi import FastAPI

# Se crea la aplicación FastAPI
app = FastAPI(title = "SGSST API")

# Endpoint simple para verificar el estado del servidor
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend funcionando correctamente"}

from backend.app.core.database import engine

@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return {"status": "ok", "message": "Conexión a la base de datos exitosa"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


from backend.app.core.config import settings

@app.get("/env-check")
def env_check():
    return {
        "POSTGRES_USER": settings.POSTGRES_USER,
        "POSTGRES_PASSWORD": settings.POSTGRES_PASSWORD,
        "POSTGRES_DB": settings.POSTGRES_DB,
        "POSTGRES_HOST": settings.POSTGRES_HOST,
        "POSTGRES_PORT": settings.POSTGRES_PORT,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host = "127.0.0.1", port = 8000, reload = True)
