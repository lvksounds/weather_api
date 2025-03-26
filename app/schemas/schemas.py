# mesmo que dtos no .net - definindo dados de entrada e saida
from pydantic import BaseModel
from datetime import datetime 

class PredictionBase(BaseModel):
  city: str

class CreatePrediction(PredictionBase):
  pass

class PredictionResponse(PredictionBase):
  id: int
  temperature: float
  humidity: float
  description: str
  date: datetime

  class Config:
    from_attributes = True