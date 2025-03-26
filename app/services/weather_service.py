import httpx #tipo httpClient no .net, da suporte para async e await
from app.config import API_KEY

async def get_weather(city: str):
  async with httpx.AsyncClient() as client:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt"
    try:
      response = await client.get(url)
      #response.raise_for_status() pegando erros em homolog
      if response.status_code != 200:
          return {"Erro" : "Não foi possivel consultar a cidade."}
      data = response.json()
      return {
        "city": city.lower(),
        "temperature": data["main"]["temp"],
        "humidity":data["main"]["humidity"],
        "description": data["weather"][0]["description"],
      }
    except httpx.HTTPStatusError as e:
      return {"Erro" : f"Erro na requisição HTTP: {e}"}
    except Exception as e:
      return{"Erro" : f"Erro desconhecido."}
    
  