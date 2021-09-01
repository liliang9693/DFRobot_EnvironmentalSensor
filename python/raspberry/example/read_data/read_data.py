# -*- coding: utf-8 -*
'''
  * @file  gain_heartbeat_SPO2.py
  *@brief 这个demo演示获取SEN050X传感器上的数据，通过IIC或串口连接传感器
  *@n 将SEN050X返回的数据打印在串口监视器上
  * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  * @licence     The MIT License (MIT)
  * @author      PengKaixing(jie.tang@dfrobot.com)
  * @version     V1.0
  * @date        2021-08-31
  * @get         from https://www.dfrobot.com
  * @url         https://github.com
'''
import sys
import os
import time
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from dfrobot_multifunctional_environmental_sensor import *

'''
  ctype=1：UART
  ctype=0：IIC
'''
ctype=1

if ctype==0:
  I2C_1       = 0x01               # I2C_1 使用i2c1接口驱动传感器， 可以调整为i2c0但是需要配置树莓派的文件
  I2C_ADDRESS = 0x22               # I2C 设备的地址，可以更改A1、A0来更换地址，默认地址为0x77
  sen050x = dfrobot_multifunctional_environmental_sensor_i2c(I2C_1 ,I2C_ADDRESS)
else:
  sen050x = dfrobot_multifunctional_environmental_sensor_uart(9600)


'''设备选择'''
DEVICE_PID_GRAVITY        = 0x1F5
DEVICE_PID_BREAKOUT       = 0x1F4

'''大气压强单位选择'''
HPA                       = 0x01
KPA                       = 0X02

'''温度单位选择'''
TEMP_C                    = 0X03
TEMP_F                    = 0X04
 
def setup():
  '''
  * @brief 初始化SEN050X传感器
  * 
  * @param pid 初始化传感器的PID
  * @n     DEVICE_PID_GRAVITY 初始化SEN0501传感器
  * @n     DEVICE_PID_BREAKOUT 初始化SEN0500传感器
  * @return 返回值;
  * @n      0：成功
  * @n      -1:失败
  '''
  sen050x.test()
  while (sen050x.begin(DEVICE_PID_GRAVITY) == False):
    print("init fail!")
    time.sleep(1)
  print("init success!")
  
def loop():
  print("-----------------------\r\n")
  print("Temp: " + str(sen050x.get_temperature(TEMP_C)) + " 'C\r\n")
  print("Temp: " + str(sen050x.get_temperature(TEMP_F)) + " 'F\r\n")
  print("Humidity: " + str(sen050x.get_humidity()) + " %\r\n")
  print("Ultraviolet intensity: " + str(sen050x.get_ultraviolet_intensity()) + " mw/cm2\r\n")
  print("LuminousIntensity: " + str(sen050x.get_luminousintensity()) + " lx\r\n")
  print("Atmospheric pressure: " + str(sen050x.get_atmosphere_pressure(HPA)) + " hpa\r\n")
  print("Elevation: " + str(sen050x.get_elevation()) + " m\r\n")
  print("-----------------------\r\n")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()