#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

# GPIO pin
pin = 40
# angle
end_angle = 120
# 中间停顿时间，单位：s
wait_time = 0.1

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
time.sleep(2)

for i in range(0,end_angle,3): 
  moveToAngle(i)

time.sleep(wait_time)

for i in range(end_angle,0,-3):  
  moveToAngle(i)

pwm.stop()
GPIO.cleanup
