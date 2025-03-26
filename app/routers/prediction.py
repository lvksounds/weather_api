from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from app.infra import db_connection
from app.schemas import schemas
from app.services import prediction_service

router = APIRouter(prefix="/predictions", tags=["Predictions"])

@router.post("/")
async def create_prediction(city: str, db: Session = Depends(db_connection.get_database)):
    """
    Busca a previsão do tempo para uma cidade e armazena no banco de dados.
    """
    return await prediction_service.create_prediction(city, db)

@router.get("/", response_model=List[schemas.PredictionResponse])
async def get_all_predictions(db: Session = Depends(db_connection.get_database)):
    """
    Retorna uma lista com todas as previsões armazenadas no banco de dados.
    """
    return prediction_service.get_all_predictions(db)

@router.get("/filter", response_model=Optional[schemas.PredictionResponse])
async def get_prediction(city: Optional[str] = None, date: Optional[str] = None, db: Session = Depends(db_connection.get_database)):
    """
    Retorna uma previsão específica com base na cidade e na data informadas.\n
    Formato dos parâmetros:\n
    - city: str (obrigatório)\n
    - date: str (obrigatório) no formato "dd/mm/aaaa"\n
    """
    return prediction_service.get_prediction_by_city_and_date(city, date, db)

@router.delete("/delete/{id}")
async def delete_prediction(id: int, db: Session = Depends(db_connection.get_database)):
    """
    Deleta uma previsão do tempo pelo ID.
    """
    return prediction_service.delete_prediction(id, db)
