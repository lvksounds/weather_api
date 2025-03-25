from datetime import datetime

def converStringToDate(date: str) -> datetime:
  date_obj = datetime.strptime(date, "%d/%m/%Y")
  formated_date = date_obj.strftime("%Y-%m-%d 00:00:00.000000") # feio isso aqui
  return formated_date