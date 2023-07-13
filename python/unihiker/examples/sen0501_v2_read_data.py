#coding:utf-8

'''
    @DFRobot SEN0501 V2.0  
    @Gravity: High Accuracy Temperature, Humidity, Pressure, Ambient Light and UV Sensor - I2C/UART
    @https://www.dfrobot.com/product-2528.html
    @This code runs on unihiker
    @Only adapted to I2C mode
    @Flip the switch on the sensor to I2C
'''

import time
from DFRobot_Environmental_Sensor import *

from pinpong.board import Board

Board().begin()


SEN0501 = DFRobot_Environmental_Sensor_I2C(bus=0x01,addr=0x22)


'''
  Atmospheric pressure unit select
'''
HPA                       = 0x01
KPA                       = 0X02

'''
  Temperature unit select
'''
TEMP_C                    = 0X03
TEMP_F                    = 0X04
 
def setup():
  while (SEN0501.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1)
  print("Sensor  initialize success!!")
  
def loop():
  ##Obtain sensor data
  print("-----------------------\r\n")
  print("Temp: " + str(SEN0501.get_temperature(TEMP_C)) + " 'C\r\n")
  print("Temp: " + str(SEN0501.get_temperature(TEMP_F)) + " 'F\r\n")
  print("Humidity: " + str(SEN0501.get_humidity()) + " %\r\n")
  print("Ultraviolet intensity: " + str(SEN0501.get_ultraviolet_intensity()) + " mw/cm2\r\n")
  print("LuminousIntensity: " + str(SEN0501.get_luminousintensity()) + " lx\r\n")
  print("Atmospheric pressure: " + str(SEN0501.get_atmosphere_pressure(HPA)) + " hpa\r\n")
  print("Elevation: " + str(SEN0501.get_elevation()) + " m\r\n")
  print("-----------------------\r\n")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
    
