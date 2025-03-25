from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Weather API", description="API para buscar e armazenar previsões do tempo", version="0.1.0")

app.include_router(router)

@app.get("/")
def Home():
  return {"message": "API para Previsão do Tempo"}