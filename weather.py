# import the module
import python_weather

import asyncio


def kind_ish(n):
  print(n)
  out = ""
  #class python_weather.enums.Kind
  #A weather forecast kind.
  # CLOUDY = 119
  if n == 119: out = "CLDY"
  # FOG = 143
  if n == 143: out = "FOG"
  # HEAVY_RAIN = 302
  if n == 302: out = "RAIN"
  # HEAVY_SHOWERS = 299
  if n == 299: out = "H\nRAIN"
  # HEAVY_SNOW = 230
  if n == 230: out = "H\nSNOW"
  # HEAVY_SNOW_SHOWERS = 335
  if n == 335: out = "H\nSNOW"
  # LIGHT_RAIN = 266
  if n == 299: out = "L\nRAIN"
  # LIGHT_SHOWERS = 176
  if n == 176: out = "L\nRAIN"
  # LIGHT_SLEET = 182
  if n == 179: out = "L\nSLET"
  # LIGHT_SLEET_SHOWERS = 179
  if n == 179: out = "L\nSLET"
  # LIGHT_SNOW = 227
  if n == 227: out = "L\nSNOW"
  # LIGHT_SNOW_SHOWERS = 323
  if n == 323: out = "L\nSNOW"
  # PARTLY_CLOUDY = 116
  if n == 116: out = "P\nCLDY"
  # SUNNY = 113
  if n == 113: out = "SUNY"
  # THUNDERY_HEAVY_RAIN = 389
  if n == 389: out = "T\nRAIN"
  # THUNDERY_SHOWERS = 200
  if n == 200: out = "T\nRAIN"
  # THUNDERY_SNOW_SHOWERS = 392
  if n == 392: out = "T\nSNOW"
  # VERY_CLOUDY = 122
  if n == 122: out = "V\nCLDY"
  #property emoji: str
  #  The emoji representing this enum.
  return out

async def getweather() -> None:
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Chili, NY')
    
    # returns the current day's forecast temperature (int)
    print(f"{weather.temperature}{chr(176)}" )
    print(weather.kind.index)
    print(weather.kind.emoji)
    print(kind_ish(weather.kind))
    print(weather.description)
    
    print(weather)

    # get the weather forecast for a few days
    #for daily in weather:
    #  print(daily)
    #  
    #  # hourly forecasts
    #  for hourly in daily:
    #    print(f' --> {hourly!r}')

if __name__ == '__main__':
  
  asyncio.run(getweather())
