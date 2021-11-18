import re,sys, signal, time, datetime
import RPi.GPIO as GPIO
import threading
import datetime
import os.path
path = '/home/pi/access_doorlock' #path to save log data
relay1 = 7 #relay1 gpio variable
relay2 = 11 #relay2 gpio variable
button = 13 #button gpio variable
limitswitch = 15 #limitswitch gpio variable
file = open("card_id_employee1","r") #open card id file
card_id = file.read() #read all card id in a dictionary
print(card_id)
GPIO.setwarnings(False) #disable warning gpio
GPIO.setmode(GPIO.BOARD) #use gpio pin in numbering mode
GPIO.setup(relay1, GPIO.OUT, initial = 0) #declare output
GPIO.setup(relay2, GPIO.OUT, initial = 0)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #declare input
GPIO.setup(limitswitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(relay1,GPIO.LOW) #activate relay initial on
def switchinterrupt(n,name): #switch to turn relay off
    print("{} has started".format(name)) #threading switch started
    tdaydate = datetime.datetime.today() #today date for making a folder everyday
    tdelta = datetime.timedelta(days = 1) #get days difference for arithmetic operation of date
    tmrw = tdaydate + tdelta #get tomorrow date
    print(tmrw)
    filename = ("{}".format(tdaydate.strftime("%d %b %Y"))) #name of the file using today date as string
    f = open(os.path.join(path,filename),"w+") #open or create file in specific folder path
    f.write("NO\tTime\t\t\tCARD ID\t\tNAME\n") #write the title of table in textfile
    f.close() #close file
    while True:
        tdaydate = datetime.datetime.today()
        if tdaydate.day == tmrw.day: #check if today equal to tomorrow so it execute everday just once
            print(tdaydate.day)
            filename = ("{}".format(tdaydate.strftime("%d %b %Y")))
            f = open(os.path.join(path,filename),"w+") # create file with path and file name using date
            f.write("NO\tTime\t\t\tCARD ID\t\tNAME\n") 
            f.close()
            tdelta = datetime.timedelta(days = 1) 
            tmrw = tdaydate+tdelta #get new tomorrow date
            print("created file")
        time.sleep(0.1)
        btn = GPIO.input(n) #check condition of switch
        if btn== True: #if switch pressed and read as 1
            GPIO.output(relay1,GPIO.HIGH) #off relay
            print("btn pressed")
            time.sleep(5) #delay for 5 second
            GPIO.output(relay1,GPIO.LOW) #on relay
def main(): # main program for scanning rfid
    counter = 0 #counter for number of user scan rfid
    file = open("card_id_employee1","r")
    id_dict = {}
    for line in file:
        k, v = line.strip().split('=')
        id_dict[k.strip()] = v.strip()
        file.close
    while True:     
        x = str(input("scanning"))
        if x in id_dict: #if user card id in text file data
            counter = counter+1 #increment
            GPIO.output(relay1,GPIO.HIGH) #relay off
            tdaydate = datetime.datetime.today() #get todaydate for writing date in textfile log data
            filename = ("{}".format(tdaydate.strftime("%d %b %Y")))
            fi = open(os.path.join(path,filename),"a+") # create file with path and file name using date
            fi.write('\n') #write data
            fi.write(str(counter))
            fi.write('\t')
            fi.write(str(tdaydate.time()))
            fi.write('    \t')
            fi.write(str(x))
            fi.write('\t')
            fi.write(id_dict[x])
            fi.write('\n')
            fi.close() #close textfile
            print("door unlocked")
            time.sleep(5) 
            GPIO.output(relay1,GPIO.LOW)
        else:
             print(x)
             print("unknown id")
intrupt = threading.Thread(target = switchinterrupt, name = 'thread2', args = (button, 'thread2')) #declare threading
intrupt.start() #start threading
try:
    main()
except KeyboardInterrupt:
    print("Keyboard")
finally:
    GPIO.cleanup() #gpio set to initial
    file.close() #close card id file