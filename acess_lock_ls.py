import re,sys, signal, os, time, datetime
import RPi.GPIO as GPIO
import threading
import datetime
#import lcddriver
relay1 = 7
relay2 = 11
button = 13
limitswitch = 15
card_id = {"0008510491":"Anas","0003509614":"BOSS SAFWAN"}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay1, GPIO.OUT, initial = 0)
GPIO.setup(relay2, GPIO.OUT, initial = 0)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(relay1,GPIO.LOW)
#lcd = lcddriver.lcd()

def doorclose(ls, name):
    counter = 0
    while True:
        inputls = GPIO.input(ls)
        if inputls == False and counter == 0:
            while True:
                inputls = GPIO.input(ls)
                if inputls == True:
                    print("limit sw is off")
                    counter = 2
                    break
                elif inputls == False:
                    print("limit switch is on")
                    continue
        elif inputls == False and counter ==2:
            print("False and counter =2")
            GPIO.output(relay1, GPIO.LOW)
##            lcd.lcd_clear()
##            lcd.lcd_display_string("Door Locked",1)
##            lcd.lcd_display_string("Please Scan RFID",2)
            counter = 0
        else:
            continue

def switchinterrupt(n,name):
    print("{} has started".format(name))
    while True:
        btn = GPIO.input(n)
        if btn== False:
            GPIO.output(relay1,GPIO.HIGH)
##            lcd.lcd_clear()
##            lcd.lcd_display_string("Door unlocked",1)

def main():
    while True:
        x = str(input("scanning"))
        if x in card_id:
            GPIO.output(relay1,GPIO.HIGH)
##            lcd.lcd_clear()
##            lcd.lcd_display_string("Door Unlocked",1)
##            lcd.lcd_display_string(("Welcome {}".format(card_id[x])),2)
        else:
             print(x)
             print("unknown id")

##lcd.lcd_display_string("Door Locked",1)
##lcd.lcd_display_string("Please scan RFID",2)
limit = threading.Thread(target = doorclose, name = 'thread1', args = (limitswitch,'thread1'))
intrupt = threading.Thread(target = switchinterrupt, name = 'thread2', args = (button, 'thread2'))
limit.start()
intrupt.start()
try:
    main()
except KeyboardInterrupt:
    print("Keyboard")
finally:
    GPIO.cleanup()