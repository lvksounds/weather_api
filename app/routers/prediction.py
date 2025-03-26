from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infra import db_connection
from app.models.predictions import Prediction
from app.schemas import schemas
from app.services.weather_service import get_weather
from app.services import convert_date_service
from typing import List, Optional
from datetime import date, datetime
from starlette.responses import JSONResponse

router = APIRouter(prefix="/predictions", tags=["Predictions"])

@router.post("/")
async def create_prediction(city: str, db: Session = Depends(db_connection.get_database)):
  """
  Busca a previsão do tempo para uma cidade e armazena no banco de dados.
  """
  try:
    data = await get_weather(city)
    if data.get("Erro"):
      raise HTTPException(status_code=404, detail="Cidade não encontrada")

    if "date" not in data: #só uma maneira preguiçosa de formatar essa data
      data["date"] = date.today()
    
    prediction = Prediction(**data)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return JSONResponse(status_code=201, content={"detail": "Previsão criada com sucesso."})
  except ValueError as ve:
    return {"erro": str(ve)}
  except Exception as e:
    return {"erro": "Ocorreu um erro interno no servidor."}
  

@router.get("/", response_model=List[schemas.PredictionResponse])
async def getAllPredictions(db: Session = Depends(db_connection.get_database)):
  """
  Retorna um lista com todas as previsões do tempo armazenadas no banco de dados.
  """
  return db.query(Prediction).all() 

@router.get("/filter", response_model=Optional[schemas.PredictionResponse])
async def getPrediction(city: Optional[str] = None, date: Optional[str] = 
                        None, db: Session = Depends(db_connection.get_database)):
  """
  Retorna uma previsão do tempo armazenada no banco de dados de acordo com a cidade e a data informadas.
  formato dos inputs:
  city: string
  date: string no formato "DD/MM/YYYY"
  """
  formatedDate = convert_date_service.converStringToDate(date)
  
  if city and date:
    prediction = db.query(Prediction).filter(Prediction.city == city, Prediction.date == formatedDate).first()
    if prediction is None:
      raise HTTPException(status_code=404, detail="Previsão não encontrada.")
    return prediction
  elif city:
     raise HTTPException(status_code=404, detail="Data não informada.")
  elif date:
     raise HTTPException(status_code=404, detail="Cidade não informada.")
  
@router.delete("/delete/{id}")
async def deletePrediction(id: int, db: Session = Depends(db_connection.get_database)):
  """
  Deleta uma previsão do tempo armazenada no banco de dados de acordo com o id informado.
  Obtenha o id a partir do getPrediction ou do getAllPredictions.
  """
  prediction = db.query(Prediction).filter(Prediction.id == id).first()
  if not prediction:
        raise HTTPException(status_code=404, detail="Previsão não encontrada.")
  db.delete(prediction)
  db.commit()
  return JSONResponse(status_code=200, content={"detail": "Previsão deletada com sucesso"})
