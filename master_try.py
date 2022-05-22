#==========================================================================================================

import schedule
import time
import datetime
import os

#==========================================================================================================


'''
--------------------------------------------------------------------------------------------------------------------
Order is important:
Get GPS co-ordinates then use these co-ordinates to access data from API's. Export API data as header file.
C will import all the header files and do computations. It will give the Power Consumption and Price.
Then clear the LCD screen. Finally import all the data from different text files and display on to the screen.
--------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------
Run GPS => every hour
Run API_24 => every day at 00:00
Run API_hourly => every hour
Run C code => every hour
Run LCD Clear => every hour
Run LCD display => every hour
--------------------------------------------------------------------------------------------------------------------
'''



#==========================================================================================================

# Run GPS every hour

def gps():
    os.system("python serial_gps.py")
    print("GPS hit")
    return

schedule.every().day.at("00:00").do(gps)
schedule.every().day.at("01:00").do(gps)
schedule.every().day.at("02:00").do(gps)
schedule.every().day.at("03:00").do(gps)
schedule.every().day.at("04:00").do(gps)
schedule.every().day.at("05:00").do(gps)
schedule.every().day.at("06:00").do(gps)
schedule.every().day.at("07:00").do(gps)
schedule.every().day.at("08:00").do(gps)
schedule.every().day.at("09:00").do(gps)
schedule.every().day.at("10:00").do(gps)
schedule.every().day.at("11:00").do(gps)
schedule.every().day.at("12:00").do(gps)
schedule.every().day.at("13:00").do(gps)
schedule.every().day.at("14:00").do(gps)
schedule.every().day.at("15:00").do(gps)
schedule.every().day.at("16:00").do(gps)
schedule.every().day.at("17:00").do(gps)
schedule.every().day.at("18:00").do(gps)
schedule.every().day.at("19:00").do(gps)
schedule.every().day.at("20:00").do(gps)
schedule.every().day.at("21:00").do(gps)
schedule.every().day.at("22:00").do(gps)
schedule.every().day.at("23:00").do(gps)

#==========================================================================================================

# Run API_24 file every day at 00:00 am
def api24():
    import weather_API_24
    print("24 hit")
    return

schedule.every().day.at("00:00").do(api24)

#==========================================================================================================

# Run API_hourly every hour

def apiHourly():
    import weather_API_hourly
    print("Hourly hit")
    return

schedule.every().day.at("00:00").do(apiHourly)
schedule.every().day.at("01:00").do(apiHourly)
schedule.every().day.at("02:00").do(apiHourly)
schedule.every().day.at("03:00").do(apiHourly)
schedule.every().day.at("04:00").do(apiHourly)
schedule.every().day.at("05:00").do(apiHourly)
schedule.every().day.at("06:00").do(apiHourly)
schedule.every().day.at("07:00").do(apiHourly)
schedule.every().day.at("08:00").do(apiHourly)
schedule.every().day.at("09:00").do(apiHourly)
schedule.every().day.at("10:00").do(apiHourly)
schedule.every().day.at("11:00").do(apiHourly)
schedule.every().day.at("12:00").do(apiHourly)
schedule.every().day.at("13:00").do(apiHourly)
schedule.every().day.at("14:00").do(apiHourly)
schedule.every().day.at("15:00").do(apiHourly)
schedule.every().day.at("16:00").do(apiHourly)
schedule.every().day.at("17:00").do(apiHourly)
schedule.every().day.at("18:00").do(apiHourly)
schedule.every().day.at("19:00").do(apiHourly)
schedule.every().day.at("20:00").do(apiHourly)
schedule.every().day.at("21:00").do(apiHourly)
schedule.every().day.at("22:00").do(apiHourly)
schedule.every().day.at("23:00").do(apiHourly)

#==========================================================================================================

# Run C code every hour (mlr.c)

def C_code():
    compile = "gcc mlr.c"  # Linux gcc code.c then ./a.out || windows gcc code.c then code (exe file)
    os.system(compile)
    os.system("./a.out")
    print("C hit")
    return

schedule.every().day.at("00:00").do(C_code)
schedule.every().day.at("01:00").do(C_code)
schedule.every().day.at("02:00").do(C_code)
schedule.every().day.at("03:00").do(C_code)
schedule.every().day.at("04:00").do(C_code)
schedule.every().day.at("05:00").do(C_code)
schedule.every().day.at("06:00").do(C_code)
schedule.every().day.at("07:00").do(C_code)
schedule.every().day.at("08:00").do(C_code)
schedule.every().day.at("09:00").do(C_code)
schedule.every().day.at("10:00").do(C_code)
schedule.every().day.at("11:00").do(C_code)
schedule.every().day.at("12:00").do(C_code)
schedule.every().day.at("13:00").do(C_code)
schedule.every().day.at("14:00").do(C_code)
schedule.every().day.at("15:00").do(C_code)
schedule.every().day.at("16:00").do(C_code)
schedule.every().day.at("17:00").do(C_code)
schedule.every().day.at("18:00").do(C_code)
schedule.every().day.at("19:00").do(C_code)
schedule.every().day.at("20:00").do(C_code)
schedule.every().day.at("21:00").do(C_code)
schedule.every().day.at("22:00").do(C_code)
schedule.every().day.at("23:00").do(C_code)

#==========================================================================================================

# Run LCD_Clear code every hour 

def lcd_clr():
    import lcd_clear
    print("LCD clear hit")
    return

schedule.every().day.at("00:00").do(lcd_clr)
schedule.every().day.at("01:00").do(lcd_clr)
schedule.every().day.at("02:00").do(lcd_clr)
schedule.every().day.at("03:00").do(lcd_clr)
schedule.every().day.at("04:00").do(lcd_clr)
schedule.every().day.at("05:00").do(lcd_clr)
schedule.every().day.at("06:00").do(lcd_clr)
schedule.every().day.at("07:00").do(lcd_clr)
schedule.every().day.at("08:00").do(lcd_clr)
schedule.every().day.at("09:00").do(lcd_clr)
schedule.every().day.at("10:00").do(lcd_clr)
schedule.every().day.at("11:00").do(lcd_clr)
schedule.every().day.at("12:00").do(lcd_clr)
schedule.every().day.at("13:00").do(lcd_clr)
schedule.every().day.at("14:00").do(lcd_clr)
schedule.every().day.at("15:00").do(lcd_clr)
schedule.every().day.at("16:00").do(lcd_clr)
schedule.every().day.at("17:00").do(lcd_clr)
schedule.every().day.at("18:00").do(lcd_clr)
schedule.every().day.at("19:00").do(lcd_clr)
schedule.every().day.at("20:00").do(lcd_clr)
schedule.every().day.at("21:00").do(lcd_clr)
schedule.every().day.at("22:00").do(lcd_clr)
schedule.every().day.at("23:00").do(lcd_clr)

#==========================================================================================================

# Run LCD_Display code every hour 

def lcd_display():
    import lcd_code
    print("LCD display hit")
    return

schedule.every().day.at("00:00").do(lcd_display)
schedule.every().day.at("01:00").do(lcd_display)
schedule.every().day.at("02:00").do(lcd_display)
schedule.every().day.at("03:00").do(lcd_display)
schedule.every().day.at("04:00").do(lcd_display)
schedule.every().day.at("05:00").do(lcd_display)
schedule.every().day.at("06:00").do(lcd_display)
schedule.every().day.at("07:00").do(lcd_display)
schedule.every().day.at("08:00").do(lcd_display)
schedule.every().day.at("09:00").do(lcd_display)
schedule.every().day.at("10:00").do(lcd_display)
schedule.every().day.at("11:00").do(lcd_display)
schedule.every().day.at("12:00").do(lcd_display)
schedule.every().day.at("13:00").do(lcd_display)
schedule.every().day.at("14:00").do(lcd_display)
schedule.every().day.at("15:00").do(lcd_display)
schedule.every().day.at("16:00").do(lcd_display)
schedule.every().day.at("17:00").do(lcd_display)
schedule.every().day.at("18:00").do(lcd_display)
schedule.every().day.at("19:00").do(lcd_display)
schedule.every().day.at("20:00").do(lcd_display)
schedule.every().day.at("21:00").do(lcd_display)
schedule.every().day.at("22:00").do(lcd_display)
schedule.every().day.at("23:00").do(lcd_display)

#==========================================================================================================


schedule.run_pending()
print("No schedule hit")


#==========================================================================================================

'''
When this code is executed for the first time then it is possible that it may not be one of the time listed
in our schedule. So we will manually run it for the very first instance
'''

t_s = datetime.datetime.now()

print("Started")
os.system("python serial_gps.py")
import weather_API_hourly

compile = "gcc mlr.c"  # Linux gcc code.c then ./a.out || windows gcc code.c then code (exe file)
os.system(compile)
os.system("./a.out")

import lcd_clear
#import lcd_code

t_e = datetime.datetime.now()

print("Initial hit")
print(t_e - t_s)


#==========================================================================================================




#==========================================================================================================

while True:  # while loop will keep on running and checking the pending tasks
    schedule.run_pending()    # if time comes for a scheduled task then run it
    time.sleep(1) # wait 1 second   # wait for 1 second before again checking the pending tasks
    
#==========================================================================================================    
    




