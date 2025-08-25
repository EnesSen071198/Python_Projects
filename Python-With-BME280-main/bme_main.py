import BME.BME 
from machine import Pin, I2C
import utime

while True :
  #  Bme.temp_bme(temperature_c)
    temperature_c = bmp280_object.temperature # degree celcius

    pressure = bmp280_object.pressure  # pascal
    
    pressure_hPa = ( pressure * 0.01 ) + ERROR
    altitude = altitude_IBF(pressure_hPa)
    temperature_c = bmp280_object.temperature # degree celcius
    pressure = bmp280_object.pressure  # pascal
    pressure_hPa = ( pressure * 0.01 ) + ERROR
    altitude = altitude_IBF(pressure_hPa)
    print("\n")
    print(BME.BME.temperature_c)
    print(BME.BME.pressure_hPa)
    print(BME.BME.altitude)
    utime.sleep(1)
    
