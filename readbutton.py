import re,sys, signal, os, time, datetime
import RPi.GPIO as GPIO
import threading
#p = datetime.time()
#print(p)
relay1 = 7
relay2 = 11
counter = 0
button = 16
limitswitch = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT, initial = 0)
GPIO.setup(relay2, GPIO.OUT, initial = 0)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limitswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(relay1,GPIO.LOW)


while True:
    inputls = GPIO.input(limitswitch)
    inputbtn = GPIO.input(button)
    print(inputbtn)
    if inputbtn == True:
        print("end")
        GPIO.output(relay1, GPIO.HIGH)
        break

print("done")
GPIO.cleanup()