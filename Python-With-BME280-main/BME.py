# https://github.com/dafvid/micropython-bmp280

# import the required libraries
from BME.bmp280 import *
from machine import Pin, I2C
import utime
from time import sleep

ERROR = -3 # hPa 

i2c_object = I2C(0, scl = 1,   sda = 0,   freq = 1000000) 

bmp280_object = BMP280(i2c_object, addr = 0x77, use_case = BMP280_CASE_WEATHER)

bmp280_object.power_mode = BMP280_POWER_NORMAL
bmp280_object.oversample = BMP280_OS_HIGH
bmp280_object.temp_os = BMP280_TEMP_OS_8
bmp280_object.press_os = BMP280_TEMP_OS_4
bmp280_object.standby = BMP280_STANDBY_250
bmp280_object.iir = BMP280_IIR_FILTER_2


# altitude from international barometric formula, given in BMP 180 datasheet
def altitude_IBF(pressure):
    local_pressure = pressure    # Unit : hPa
    sea_level_pressure = 1013.25 # Unit : hPa
    pressure_ratio = local_pressure / sea_level_pressure
    altitude = 44330*(1-(pressure_ratio**(1/5.255)))
    return altitude

while True:
    # accquire temperature value in celcius
    temperature_c = bmp280_object.temperature # degree celcius

    pressure = bmp280_object.pressure  # pascal
    
    pressure_hPa = ( pressure * 0.01 ) + ERROR
    altitude = altitude_IBF(pressure_hPa)
    
    temperature_c = bmp280_object.temperature # degree celcius
    pressure = bmp280_object.pressure  # pascal
    pressure_hPa = ( pressure * 0.01 ) + ERROR
    altitude = altitude_IBF(pressure_hPa)

        

  
 
    print("Temperature : ",temperature_c,"C°")
    print("Pressure : ",pressure,"Pa")
    print("Altitude : ", altitude,"m")
    
    
    
    print("\n")
    sleep(2)




        
        
        