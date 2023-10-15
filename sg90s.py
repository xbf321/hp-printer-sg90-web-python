#!/usr/bin/env python3 
#-*- coding: utf-8 -*- 
# 30 11 * * * /hp-printer-sg90-web-python/sg90s.py
import configparser
import RPi.GPIO as GPIO
import time
import signal
import atexit

# atexit.register(GPIO.cleanup)

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
pin = int(config['DEFAULT'].get('pin', 32))
end_angle = int(config['DEFAULT'].get('end_angle', 120))

#pin = 32
#end_angle = 116
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
# 50HZ 
pwm = GPIO.PWM(pin,50)
pwm.start(0)
time.sleep(2)

def moveToAngle(angle):
  # 设置转动角度
  pwm.ChangeDutyCycle(2.5 + 10 * angle / 180)
  # 等该 20ms 周期结束
  time.sleep(0.02)
  # 归零信号
  pwm.ChangeDutyCycle(0)           
  time.sleep(0.02)


moveToAngle(0)
time.sleep(1)

for i in range(0,end_angle,3): 
    moveToAngle(i)

time.sleep(3)

for i in range(end_angle,0,-3):  
    moveToAngle(i)

pwm.stop()
GPIO.cleanup
"""
while(True):
  for i in range(0,181,10): 
    moveToAngle(i)

  for i in range(181,0,-10):  
    moveToAngle(i)
"""