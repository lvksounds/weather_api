from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.infra.db_connection import Base

class Prediction(Base):
  __tablename__ = "predictions" #nome da tabela no banco de dados

  #colunas
  id = Column(Integer, primary_key = True, index = True)
  city = Column(String, index = True)
  humidity = Column(Float)
  date = Column(DateTime, default = datetime.utcnow)
  temperature = Column(Float)
  description = Column(String)