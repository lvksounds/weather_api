import httpx #tipo httpClient no .net, da suporte para async e await
import os 

async def get_weather(city: str):
  async with httpx.AsyncClient() as client:
    response = await client.get(
      f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    )
    data = response.json()

    if response.status_code != 200:
      raise Exception(data["City not found."])
  return {
    "city": city,
    "temperature": data["main"]["temp"],
    "description": data["weather"][0]["description"]
  }