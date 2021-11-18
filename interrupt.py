import re,sys, signal, os, time, datetime
import RPi.GPIO as GPIO
import threading
#p = datetime.time()
#print(p)
relay1 = 7
relay2 = 11
counter = 0
button = 13
limitswitch = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT, initial = 0)
GPIO.setup(relay2, GPIO.OUT, initial = 0)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(relay1,GPIO.LOW)

def my_callback1(channel):
    print("mycallback1")


def my_callback2(channel):
    print("my callback2")

def main():
    while True:
        print("running main loop")
        time.sleep(2)

GPIO.add_event_detect(button, GPIO.FALLING,callback = my_callback1, bouncetime = 300)


try:
    main()

except KeyboardInterrupt:
    print("keyboard interrupt")


