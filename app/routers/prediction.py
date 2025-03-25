from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infra import db_connection
from app.models.predictions import Prediction
from app.schemas import schemas
from app.services.weather_service import get_weather
from typing import List, Optional
from datetime import date

router = APIRouter(prefix="/predictions", tags=["Predictions"])

@router.post("/", response_model = schemas.PredicitionResponse)
async def create_prediction(city: str, db: Session = Depends(db_connection.get_database)):
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