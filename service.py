import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.IN)
while True:
    if(GPIO.input(27)):
        os.system("irsend send_once Dyson POWER")
        break
time.sleep(1)