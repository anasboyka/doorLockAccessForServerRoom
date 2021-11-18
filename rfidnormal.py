import re,sys, signal, os, time, datetime
import RPi.GPIO as GPIO
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
def switchinterrupt(channel):
    print("subroutine")
    counter = 0
    while True:
        inputls = GPIO.input(limitswitch)
        if inputls == False and counter == 0:
            print("false and counter = 0")
            while True:               
                print("check limit switch")
                GPIO.output(relay1,GPIO.HIGH)
                inputls = GPIO.input(limitswitch)
                if inputls == True:
                    print("limit switch is off")
                    counter = 2
                    break
                elif inputls == False:
                    print("limit switch is on")
                    continue     
        elif inputls == False and counter ==2:
            print("false and counter = 2")
            GPIO.output(relay1,GPIO.LOW)
            counter = 0
            break
            main1()
            
def doorclose():
    print("limitswitch on")
    counter = 0
    while True:
        inputls = GPIO.input(limitswitch)
        if inputls == False and counter == 0:
            print("false and counter = 0")
            while True:               
                print("check limit switch")
                GPIO.output(relay1,GPIO.HIGH)
                inputls = GPIO.input(limitswitch)
                if inputls == True:
                    print("limit switch is off")
                    counter = 2
                    break
                elif inputls == False:
                    print("limit switch is on")
                    continue     
        elif inputls == False and counter ==2:
            print("false and counter = 2")
            GPIO.output(relay1,GPIO.LOW)
            counter = 0
            break
def main1():    
    while True:
        print("main")
        x = (str(input("scanning..")))
        if x== ("0008510491"):    
            print("anas")
            GPIO.output(relay1,GPIO.HIGH)  #turn OFF relay           #switchinterrupt2()
        else:
            print((str(input("scanning.."))))
            print("unknown id")        
GPIO.add_event_detect(button, GPIO.FALLING,callback = switchinterrupt, bouncetime = 300)
try:
    while GPIO.input(limitswitch) == False:
        main1()
        break
    print("abis")
except KeyboardInterrupt:
    print("keyboard")
finally:
    print("finally")
    GPIO.cleanup()