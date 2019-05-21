import RPi.GPIO as GPIO
import time
import os
from flask import Flask
from flask_ask import Ask, request, session, question, statement
GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.IN)
while True:
    if(GPIO.input(27)):
        os.system("irsend send_once Dyson POWER")
        break
time.sleep(1)
