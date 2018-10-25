import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
while True:
    if(GPIO.input(27)):
        os.system("irsend send_once Dyson POWER")
time.sleep(1)
