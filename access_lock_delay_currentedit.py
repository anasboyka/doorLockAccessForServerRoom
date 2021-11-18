import re,sys, signal, time, datetime
import RPi.GPIO as GPIO
import os.path
import threading
import datetime
#os and datetime

##path = '/home/pi/dooraccesslock/'



#GPIO
relay1 = 7
relay2 = 11
button = 13
limitswitch = 15

##file = open("card_id_employee","r")
##card_id = file.read()
##print(card_id)
card_id ={"0003509614":"SAFWAN",
"0006732587":"Teoh Beng Chuan",
"0008510484":"Lim Ai sun",
"0006732472":"Loh Jin Jing",
"0008510491":"Anas"}
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay1, GPIO.OUT, initial = 0)
GPIO.setup(relay2, GPIO.OUT, initial = 0)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(limitswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(relay1,GPIO.LOW)

#fileread card id

##id = { "0008510491":"anas", "0006510491":"blabla"}
##print(id["0008510491"])
def switchinterrupt(n,name):
    print("{} has started".format(name))
    while True:
        time.sleep(0.1)
        #print(n)
        btn = GPIO.input(button)
        if btn== True:
            GPIO.output(relay1,GPIO.HIGH)
            print("btn pressed")
            time.sleep(5)
            GPIO.output(relay1,GPIO.LOW)
def main():
    
##    tdaydate = datetime.datetime.today()
##    name = ("{}".format(tdaydate.strftime("%d %b %Y")))
##    inc = datetime.timedelta(days = 1)
##    tmrw = tdaydate + inc
##    ystd = tdaydate - inc
    while True:
##        tdaydate = datetime.datetime.now()
##        if tdaydate.day == tmrw.day:
##            f = open(os.path.join(path,name),"w+") # create file with path and file name using date
##            inc = datetime.timedelta(days = 1) #create variable for mathematical operation of date
##            tmrw = tdaydate + inc #get tomorrow date
##            print("created file")
        
        x = str(input("scanning"))
        if x in card_id:
            GPIO.output(relay1,GPIO.HIGH)
##            f = open(os.path.join(path,name),"w+") # create file with path and file name using date
##            f.write(x)
            print(card_id[x])
            print(x)
            print("door unlocked")
            time.sleep(5) #delay 5 second
            GPIO.output(relay1,GPIO.LOW)
        else:
            print(x) #print unknown id
            print("unknown id")


intrupt = threading.Thread(target = switchinterrupt, name = 'thread2', args = (button, 'thread2'))
##limit.start()
intrupt.start()
try:
    main()
except KeyboardInterrupt:
    print("Keyboard")
finally:
    GPIO.cleanup()