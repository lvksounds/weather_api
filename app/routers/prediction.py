from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infra import db_connection
from app.models.predictions import Prediction
from app.schemas import schemas
from app.services.weather_service import get_weather
from app.services import convert_date_service
from typing import List, Optional
from datetime import date, datetime

router = APIRouter(prefix="/predictions", tags=["Predictions"])

@router.post("/", response_model = schemas.PredicitionResponse)
async def create_prediction(city: str, db: Session = Depends(db_connection.get_database)):
  """
  Cria uma nova previsão do tempo para uma cidade e armazena no banco de dados.
  """
  try:
    data = await get_weather(city)
    if data["Erro"]:
        raise HTTPException(status_code=404, detail="Cidade não encontrada")

    if "date" not in data:
        data["date"] = date.today()
    
    prediction = Prediction(**data)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction
  except ValueError as ve:
    return {"erro": str(ve)}
  except Exception as e:
    return {"erro": "Ocorreu um erro interno no servidor."}
  

@router.get("/", response_model=List[schemas.PredicitionResponse])
async def getAllPredictions(db: Session = Depends(db_connection.get_database)):
  """
  Retorna todas as previsões do tempo armazenadas no banco de dados.
  """
  return db.query(Prediction).all()


@router.get("/filter", response_model=Optional[schemas.PredicitionResponse])
async def getPrediction(city: Optional[str] = None, date: Optional[str] = 
                        None, db: Session = Depends(db_connection.get_database)):
  """
  Retorna uma previsão do tempo armazenada no banco de dados de acordo com a cidade e a data informadas.
  """
  formatedDate = convert_date_service.converStringToDate(date)
  
  if city and date:
     data = db.query(Prediction).filter(Prediction.city == city, Prediction.date == formatedDate).first()
     return data
  elif city:
     return HTTPException(status_code=404, detail="Data não informada.")
  elif date:
     return HTTPException(status_code=404, detail="Cidade não informada.")