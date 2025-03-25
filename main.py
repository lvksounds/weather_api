from fastapi import FastAPI
from app.routers.prediction import router
from app.infra.db_connection import engine, Base 

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Weather API", description="API para buscar e armazenar previsões do tempo", version="0.1.0")
app.include_router(router)

@app.get("/")
def Home():
  return {"message": "API para Previsão do Tempo"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)