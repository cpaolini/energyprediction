from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import math


#===========================================================================================================================================

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

#===========================================================================================================================================
'''
Screen 1 => Date/Time and Temperature
Screen 2 => GPS Co-ordinates
Screen 3 => Power Consumption and Price
'''
#===========================================================================================================================================



#===========================================================================================================================================
def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	return output

#time_out = 2
#while(time_out):
lcd.clear()

#========================================================================
'''
Screen 1 data:
# Date and Time
# Temperature
'''
	

with open("Temperature.txt","r") as f:
    tmp_c = f.read()
    tmp_c = float(tmp_c)
    tmp_f = (tmp_c * 1.8) + 32

    tmp_f = str(round(tmp_f,2))
    tmp_c = str(round(tmp_c,2))

tmp = tmp_f + "\337" + "F" + "/" + tmp_c + "\337" + "C"


'''
If the LCD display shows time with resolution of 1 second. Then we need to clear the LCD screen every second.
Clearing the screen every second causes flickering.

Better to have time resolution of 2 second. Causes less flickering.

If time resolution of 1 second is needed then replace x = 5 with x = 10 and sleep(1) with sleep(2)
'''


x = 5

while(x):

    lcd.clear()

    lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
    lcd.message(tmp)


    x = x - 1
    sleep(2)



#========================================================================

'''
Screen 2 data:
	# Latitude
	# Longitude 
'''

lcd.clear()

with open("GPS_DD_cod.txt","r") as f:
    data = f.read().splitlines()
    lat =  data[0]
    long = data[1]

lat = lat[:3] + ":" +lat[9:16]
long = long[:4] + ":" + long[10:19]

lcd.message(lat+"\n")
lcd.message(long)

#print((lat))
#print("\n")
#print(long)
sleep(10)


#=======================================================================

'''
Screen 3 data:
	# Power Consumption
	# Price
'''

lcd.clear()

with open("cout.txt","r") as f:
    data = f.read().splitlines()
    power = data[0]
    price = data[1]

lcd.message("PC: "+power+" kWh"+"\n")
price = float(price)

if(price < 1):
    pr_cents = price * 100
    pr_cents = math.ceil(pr_cents)
    #pr_cents = str(round(price,2))
    pr_cents = str(pr_cents)
    lcd.message("Price: "+pr_cents+" Cents")

# LCD doesn't supports cent symbol 

else:
    pr_dollar = str(round(price,4))
    lcd.message("Price: "+pr_dollar+" $")


sleep(10)

lcd.clear()

#print("LCD Display code is working!")
#time_out = time_out - 1

#==========================================================================


#===========================================================================================================================================








