#==========================================================================================================
#import lcd_clear
#import lcd_code
#==========================================================================================================
#import schedule
import time
import datetime
import os


#==========================================================================================================


'''
--------------------------------------------------------------------------------------------------------------------
Order is important:
Get GPS co-ordinates then use these co-ordinates to access data from API's. Export API data as header file.
MLR will import all the header files and do computations. It will give the Power Consumption and Price.
Then clear the LCD screen. Finally import all data from different text files and display on to the screen.
--------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------
Run GPS => every hour
Run API_24 => every day at 00:00
Run API_hourly => every hour
Run MLR.c or MLR.py => every hour
Run LCD Clear => every hour
Run LCD display => every hour
--------------------------------------------------------------------------------------------------------------------
'''



#==========================================================================================================

'''
When this code is executed for the first time then it is possible that it may not be one of the time listed
in our schedule. So we will run it for the very first instance
'''



#===========================================================================================================

ter_op = os.popen("uptime -p").read()
ter_op = ter_op.strip('\n')


if( (ter_op == "up 0 minutes") or (ter_op == "up 1 minute") or (ter_op == "up 2 minutes") ):
    
    #import lcd_clear
    #import lcd_code
    
    os.system("sudo python serial_gps.py")
    
    import weather_API_hourly
    
    import MultiLR
    import Send_data
    #compile = "gcc mlr.c"  # Linux gcc code.c then ./a.out || windows gcc code.c then code (exe file)
    #os.system(compile)
    #os.system("./a.out")
    
    
    #print("C hit")
    
    #import lcd_clear
    #print("LCD clear hit")

    #import lcd_code
    #print("LCD display hit")
    
    #print("boot all ends")

#==========================================================================================================


from datetime import datetime
now = datetime.now()

#current_time = now.strftime("%H:%M:%S")

c_time = now.strftime("%H:%M")
#print(c_time)   # time format will be 19:48
#print(type(c_time))   # string type

if( (c_time == "00:00") or (c_time == "00:01") or (c_time == "00:02")):
    
    
    os.system("sudo python serial_gps.py")
    
    import weather_API_24

    import weather_API_hourly
    
    import MultiLR
    import Send_data
    
    '''    
    #compile = "gcc mlr.c"  # Linux gcc code.c then ./a.out || windows gcc code.c then code (exe file)
    #os.system(compile)
    #os.system("./a.out")
    #print("C hit")
    
    #import lcd_clear
    #print("LCD clear hit")

    #import lcd_code
    #print("LCD display hit")
    #print("24 all ends")
    '''
#==========================================================================================================

elif((c_time == "01:00") or (c_time == "01:01") or (c_time == "02:00") or (c_time == "02:01") or (c_time == "03:00") or (c_time == "03:01") or (c_time == "04:00") or (c_time == "04:01") or (c_time == "05:00") or (c_time == "05:01") or (c_time == "06:00") or (c_time == "06:01") or (c_time == "07:00") or (c_time == "07:01") or (c_time == "08:00") or (c_time == "08:01") or (c_time == "09:00") or (c_time == "09:01") or (c_time == "10:00") or (c_time == "10:01") or (c_time == "11:00") or (c_time == "11:01") or (c_time == "12:00") or (c_time == "12:01") or (c_time == "13:00") or (c_time == "13:01") or (c_time == "14:00") or (c_time == "14:01") or (c_time == "15:00") or (c_time == "15:01") or (c_time == "16:00") or (c_time == "16:01") or (c_time == "17:00") or (c_time == "17:01") or (c_time == "18:00") or (c_time == "18:01") or (c_time == "19:00") or (c_time == "19:01") or (c_time == "20:00") or (c_time == "20:01") or (c_time == "21:00") or (c_time == "21:01") or (c_time == "22:00") or (c_time == "22:01") or (c_time == "23:00") or (c_time == "23:01")):
    
    #import lcd_clear
    #import lcd_code
    

    os.system("sudo python serial_gps.py")
    
    import weather_API_hourly
    
    import MultiLR
    import Send_data
    
    '''
    #compile = "gcc mlr.c"  # Linux gcc code.c then ./a.out || windows gcc code.c then code (exe file)
    #os.system(compile)
    #os.system("./a.out")
    #print("C hit")
    
    #import lcd_clear
    #print("LCD clear hit")

    #import lcd_code
    #print("LCD display hit")    
    #print("Hourly all ends")
    '''
#==========================================================================================================

else:
    #import lcd_clear
    #import lcd_code
    pass

#==========================================================================================================

#print("Master Ends")

#==========================================================================================================
