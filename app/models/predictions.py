from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Prediction(Base):
  __tablename__ = "predictions" #nome da tabela no banco de dados

  #colunas
  id = Column(Integer, primary_key = True, index = True)
  city = Column(String, index = True)
  last_inquiry = Column(DateTime, default = datetime.utcnow)
  temperature = Column(Float)
  description = Column(String)