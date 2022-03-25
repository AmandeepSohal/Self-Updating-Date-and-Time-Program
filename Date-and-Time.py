#clock

#get datetime
from datetime import datetime
import time

#make date time var

#print Month, Day, Year : Hours:Minutes:Seconds
def clock():
    #while true will make this run forever since I don't have a "while false" or break statement that will make it stop
    while True:
        #get the current date and time and set it to the now variable
        now = datetime.now()
        #make this code wait a second before it continutes to run through this function
        time.sleep(1)
        #prints out the Date (MM/DD/YYYY) and the Time (HH:MM:SSSS)
        print ('Date: %02d/%02d/%04d \nTime: %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
        #print a new line after every time it prints Date and Time so it's readable 
        print("")

#output the clock function
clock()
