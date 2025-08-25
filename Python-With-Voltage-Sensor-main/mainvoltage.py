import time
import machine
from machine import Pin, I2C, UART, ADC

adc = ADC(Pin(26, mode=Pin.IN))#voltaj sensörü
value = int((adc.read_u16()))
volt = (3.3/65535*4.9) * value
time.sleep(1)
print(volt)
        


      
