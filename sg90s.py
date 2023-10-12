#!/usr/bin/env python3 
#-*- coding: utf-8 -*- 
# 30 11 * * * /hp-printer-sg90-web-python/sg90s.py
print(2)
"""
import RPi.GPIO as GPIO
import time
import signal
import atexit
  
atexit.register(GPIO.cleanup)

pin = 32
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
  time.sleep(0.2)

while(True):
  for i in range(0,181,10): 
    moveToAngle(i)

  for i in range(181,0,-10):  
    moveToAngle(i)
"""