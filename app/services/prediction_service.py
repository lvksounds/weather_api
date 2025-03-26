from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from starlette.responses import JSONResponse
from app.models.predictions import Prediction
from app.services.weather_service import get_weather
from app.helpers import dates_helper
from app.helpers.strings_helper import remove_accents

async def create_prediction(city: str, db: Session):
    city = remove_accents(city).lower()
    
    data = await get_weather(city)
    if data.get("Erro"):
        raise HTTPException(status_code=404, detail=data["Erro"])

    if "date" not in data:
        data["date"] = date.today()

    prediction = Prediction(**data)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return JSONResponse(status_code=201, content={"detail": "Previsão criada com sucesso."})

def get_all_predictions(db: Session):
    return db.query(Prediction).all()

def get_prediction_by_city_and_date(city: str, date_str: str, db: Session):
    if not city:
        raise HTTPException(status_code=401, detail="Cidade não informada.")
    if not date_str:
        raise HTTPException(status_code=401, detail="Data não informada.")

    formatted_date = dates_helper.converStringToDate(date_str)
    city = remove_accents(city).lower()
    prediction = db.query(Prediction).filter(Prediction.city == city, Prediction.date == formatted_date).first()
    
    if prediction is None:
        raise HTTPException(status_code=404, detail="Previsão não encontrada.")
    
    return prediction

def delete_prediction(id: int, db: Session):
    prediction = db.query(Prediction).filter(Prediction.id == id).first()
    if not prediction:
        raise HTTPException(status_code=404, detail="Previsão não encontrada.")
    db.delete(prediction)
    db.commit()
    return JSONResponse(status_code=200, content={"detail": "Previsão deletada com sucesso"})