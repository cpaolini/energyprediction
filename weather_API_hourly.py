'''
This code file includes all the API's that are called every hour
Sources are National Weather Service, OpenWeather, Weatherbit, NREL-PSM3 

GPS_DD_cod.txt (in pi Download/python-gps-exanples/)
Latitude:32.7773083333
Longitude:-117.070876667
'''



#==================================================================================================
 
#import json
import requests
import datetime
import json

#==================================================================================================




#==================================================================================================
'''
First read the GPS value from text file and store it in variable
'''
with open("GPS_DD_cod.txt","r") as f:
    data_line = f.read().splitlines()
    
cod = []

for x in data_line:
    numbers = x.split(':')
    cod.append(numbers[1])
    
    
#print(cod)   # cod is list containing Latitude then Longitude 
#print(cod[0])   # Latitude
#print(cod[1])   # Longitude

latitude_val = cod[0]               # Latitude Value
longitude_val = cod[1]              # Longitude Value

#print(type(longitude_val))
#==================================================================================================




# ----------------     API # 1     --------------------------------------
#Section Starts==================================================================================================
'''
National Weather Service  Temperature, windSpeed; DewPoint
For NWS first get co-ordinates from google maps say (x,y). 
Then append co-ordinates in this url https://api.weather.gov/points/x,y
From the webpage grab the url next to forecastHourly
'''

'''
********************************************************************************************************************
 use NWS API only to access the temperature data. NWS temperature values are the most accurate 
********************************************************************************************************************
'''

#sample: nws_url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast"
#nws_url = "https://api.weather.gov/points/32.9455,-117.2059 (co-ordinates from google maps)"
#nws_url = "https://api.weather.gov/gridpoints/SGX/56,23/forecast/hourly"




#nws_url = "https://api.weather.gov/points/32.9455,-117.2059/forecast/hourly"
nws_url = "https://api.weather.gov/points/"+latitude_val+","+longitude_val+"/forecast/hourly"

nws_json = requests.get(nws_url)
nws_data = nws_json.json()



#================== Loop Start ==================
filled = bool(nws_data)               # true if filled, false if empty


# if filled = empty, that is filled = false. Then we want to keep on accessing the data in interval of 0.5 seconds
# As filled = false, then we use a while loop with condition of => not(filled) = not(false) = true
# When there is no data accessed then condition is not filled as true
# In this condition we will again keep on pinging and request data but in increments on 0.5 seconds 
# Update: No need to sleep as ping will be done continuously until data accessed

'''
If API gets its data in first instance then output will be Hit top, Hit bottom 
If API fails to get data in first instance then output will be Hit top, Hit middle(while block), Hit bottom   
'''


while(not filled):         # while(true)
    #nws_url = "https://api.weather.gov/points/32.9455,-117.2059/forecast/hourly"
    nws_url = "https://api.weather.gov/points/"+latitude_val+","+longitude_val+"/forecast/hourly"
    nws_json = requests.get(nws_url)
    nws_data = nws_json.json()
    filled = bool(ow_data)
     

#print(filled)

#================== Loop End ==================



#nws_temp = nws_data['properties']['periods'][1]['temperature']   # temperature is in Fahrenheit
# nws_temp = (nws_temp - 32 ) * (0.5556)

# nws_windSpeed = nws_data['properties']['periods'][1]['windSpeed']  #miles/hr

#print(f'Temperature is {nws_temp}')
#print(f'WindSpeed is {nws_windSpeed}')

'''
nws_temp_file = str(nws_temp)
with open("Temperature.txt","w") as f:
	f.write(nws_temp_file) 
'''


#Section Ends==================================================================================================











# ----------------     API # 2     --------------------------------------
#Section Starts==================================================================================================
"""
OpenWeather 
Co-ordinates: 32.9455,-117.2059
API key: 2956baa231c8a75b7ae7a3b4530c1bdb

api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
"""



#ow_url = "https://api.openweathermap.org/data/2.5/weather?lat=32.9455&lon=-117.2059&appid=2956baa231c8a75b7ae7a3b4530c1bdb"

nws_url = "https://api.weather.gov/points/"+latitude_val+","+longitude_val+"/forecast/hourly"

#ow_url = "https://api.openweathermap.org/data/2.5/weather?lat=32.777308&lon=-117.070876667&appid=2956baa231c8a75b7ae7a3b4530c1bdb"
ow_url = "https://api.openweathermap.org/data/2.5/weather?lat="+latitude_val+"&lon="+longitude_val+"&appid=2956baa231c8a75b7ae7a3b4530c1bdb"
ow_json = requests.get(ow_url)
ow_data = ow_json.json()



#================== Start ==================
filled = bool(ow_data)               # true if filled, false if empty


# if filled = empty, that is filled = false. Then we want to keep on accessing the data in interval of 0.5 seconds
# As filled = false, then we use a while loop with condition of => not(filled) = not(false) = true
# When there is no data accessed then condition is not filled as true
# In this condition we will again keep on pinging and request data but in increments on 0.5 seconds 
# Update: No need to sleep as ping will be done continuously until data accessed

'''
If API gets its data in first instance then output will be Hit top, Hit bottom 
If API fails to get data in first instance then output will be Hit top, Hit middle(while block), Hit bottom   
'''


while(not filled):         # while(true)
    #ow_url = "https://api.openweathermap.org/data/2.5/weather?lat=32.777308&lon=-117.070876667&appid=2956baa231c8a75b7ae7a3b4530c1bdb"
    ow_url = "https://api.openweathermap.org/data/2.5/weather?lat="+latitude_val+"&lon="+longitude_val+"&appid=2956baa231c8a75b7ae7a3b4530c1bdb"
    ow_json = requests.get(ow_url)
    ow_data = ow_json.json()
    filled = bool(ow_data)
     

#print(filled)

#================== End ==================



ow_temp = ow_data['main']['temp']   # temperature is in kelvin but needed in Celsius
#ow_temp = (ow_temp - 273.15) * (9/5) + 32 
ow_temp = (ow_temp - 273.15)

ow_pressure = ow_data['main']['pressure'] # pressure is in Hectopascal (hPa), but needed in millibar (mbar). Both are same, no conversion needed.

ow_humidity = ow_data['main']['humidity']
ow_windSpeed = ow_data['wind']['speed']  # metre/second as NREL dataset unit
ow_windDirection = ow_data['wind']['deg']


#print(f'Temperature is {ow_temp}')
#print(f'Pressure is {ow_pressure}')
#print(f'Wind Speed is {ow_windSpeed}')
#print(f'Wind Direction is {ow_windDirection}')


ow_temp_file = str(ow_temp)
with open("Temperature.txt","w") as f:
	f.write(ow_temp_file) 



#Section Ends==================================================================================================












# ----------------     API # 3     --------------------------------------
#Section Starts==================================================================================================


'''
- DewPoint and Relative Humidity from -> https://www.weatherbit.io/api with key 34b9325cd976468db7b10195fab079eb  (also has dhi,dni,ghi values)
- DewPoint and Relative Humidity from -> https://developer.foreca.com/ with key : (12 months, 1000 requests per day)
    User: san-diego-state-university
    Password: cV7Wx2B4hRjb
    Administrative password (for requesting usage stats): mhBSZF8KKa6f  
    https://fnw-us.foreca.com/
    

Here we will use weatherbit API as it has open unpaid access:
DewPoint and Relative Humidity from -> https://www.weatherbit.io/api with key 34b9325cd976468db7b10195fab079eb  
'''   


#wb_url = "https://api.weatherbit.io/v2.0/current?lat=32.9455&lon=-117.2059&key=34b9325cd976468db7b10195fab079eb&include=hourly"
wb_url = "https://api.weatherbit.io/v2.0/current?lat="+latitude_val+"&lon="+longitude_val+"&key=34b9325cd976468db7b10195fab079eb&include=hourly"
wb_json = requests.get(wb_url)
wb_data = wb_json.json()




#================== Start ==================
filled = bool(wb_data)               # true if filled, false if empty


# if filled = empty, that is filled = false. Then we want to keep on accessing the data in interval of 0.5 seconds
# As filled = false, then we use a while loop with condition of => not(filled) = not(false) = true
# When there is no data accessed then condition is not filled as true
# In this condition we will again keep on pinging and request data but in increments on 0.5 seconds 
# Update: No need to sleep as ping will be done continuously until data accessed

'''
If API gets its data in first instance then output will be Hit top, Hit bottom 
If API fails to get data in first instance then output will be Hit top, Hit middle(while block), Hit bottom   
'''


while(not filled):         # while(true)
    #wb_url = "https://api.weatherbit.io/v2.0/current?lat=32.9455&lon=-117.2059&key=34b9325cd976468db7b10195fab079eb&include=hourly"
    wb_url = "https://api.weatherbit.io/v2.0/current?lat="+latitude_val+"&lon="+longitude_val+"&key=34b9325cd976468db7b10195fab079eb&include=hourly"
    wb_json = requests.get(wb_url)
    wb_data = wb_json.json()
    filled = bool(wb_data)

#print(filled)

#================== End ==================



wb_relativeHumidity = wb_data['data'][0]['rh']
wb_dewPoint = wb_data['data'][0]['dewpt']


#print(f'Dew Point is {wb_dewPoint}')
#print(f'Relative Humidity is {wb_relativeHumidity}')


#print(wb_dewPoint)
#print(wb_relativeHumidity)


#Section Ends==================================================================================================





# ----------------     API # 4     --------------------------------------
#Section Starts==================================================================================================


'''
NREL database is used to access Clearsky DHI, Clearsky DNI, Clearsky GHI, Cloud Type, Fill flag, Surface Albedo, Precipitable water
NREL database returns CSV file, not JSON like the rest of the API's'
Therefore, we need to first pre-process the CSV file in order to get the appropriate values of the features mentioned above 


#Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi
#https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxiEh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi
#32.9455 lon=-117.2059

 
# Source is Year
# Location ID is Month
# City is Day
# State is Hour
# Country is Minute

# Latitude is Clearsky DHI
# Longitude is Clearsky DNI
# Time Zone is Clearsky GHI
# Elevation is Cloud Type
# Local Time Zone is Fill Flag
# Clearsky DHI Units is Surface Albedo
# Clearsky DNI Units is Precipitable Water
'''


import pandas as pd
import numpy as np
#import sys, os
#import csv
import datetime
from datetime import datetime


#==================================================================================================
#df ='http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT(-117.2059%2032.9455)&names=2020&leap_day=false&interval=30&utc=false&full_name=Ved+Sharma&email=vsimpact09@gmail.com&affiliation=San+Diego+State+University&mailing_list=false&reason=Research+Graduate+Thesis&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi&attributes=clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,fill_flag,surface_albedo,total_precipitable_water'
#==================================================================================================




#df = pd.read_csv('https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT(-117.2059%2032.9455)&names=2020&leap_day=false&interval=30&utc=false&full_name=Ved+Sharma&email=vsimpact09@gmail.com&affiliation=San+Diego+State+University&mailing_list=false&reason=Research+Graduate+Thesis&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi&attributes=clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,fill_flag,surface_albedo,total_precipitable_water&skiprows=3',low_memory=False)
df = pd.read_csv("https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT(" + longitude_val+"%20"+latitude_val+")&names=2020&leap_day=false&interval=30&utc=false&full_name=Ved+Sharma&email=vsimpact09@gmail.com&affiliation=San+Diego+State+University&mailing_list=false&reason=Research+Graduate+Thesis&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi&attributes=clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,fill_flag,surface_albedo,total_precipitable_water&skiprows=3",low_memory=False)





#================== Start ==================

#print(len(df.index)==0)  # print(df.empty) => True if empty, False if filled but use len(df.index) as its bit faster

lt = (len(df.index)==0) # True if empty, False if filled
#lt = not lt    # comment/uncomment to change scenario
#print(lt)
#print("Top")


while(lt):
    #df = pd.read_csv('https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT(-117.2059%2032.9455)&names=2020&leap_day=false&interval=30&utc=false&full_name=Ved+Sharma&email=vsimpact09@gmail.com&affiliation=San+Diego+State+University&mailing_list=false&reason=Research+Graduate+Thesis&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi&attributes=clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,fill_flag,surface_albedo,total_precipitable_water&skiprows=3',low_memory=False)
    df = pd.read_csv("https://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT(" + longitude_val+"%20"+latitude_val+")&names=2020&leap_day=false&interval=30&utc=false&full_name=Ved+Sharma&email=vsimpact09@gmail.com&affiliation=San+Diego+State+University&mailing_list=false&reason=Research+Graduate+Thesis&api_key=Eh7ULQ76u3Vsz3sSw6SjPagLdQRlIo2me9j6qKxi&attributes=clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,fill_flag,surface_albedo,total_precipitable_water&skiprows=3",low_memory=False)
    lt = (len(df.index)==0) 
    #print("Middle Function")


#print("Bottom")

#================== End ==================




# df.columns = [''] * len(df.columns)        # This removes the column names
df = df.iloc[2:,:]  # removes the row        # 0 and # 1. Start the dataframe from row # 2


# Below line removes the verbose columns
df = df.drop(['Clearsky GHI Units','Dew Point Units','DHI Units','DNI Units','GHI Units','Solar Zenith Angle Units','Temperature Units','Pressure Units','Relative Humidity Units','Precipitable Water Units','Wind Direction Units','Wind Speed','Cloud Type -15','Cloud Type 0','Cloud Type 1','Cloud Type 2','Cloud Type 3','Cloud Type 4','Cloud Type 5','Cloud Type 6','Cloud Type 7','Cloud Type 8','Cloud Type 9','Cloud Type 10','Cloud Type 11','Cloud Type 12','Fill Flag 0','Fill Flag 1','Fill Flag 2','Fill Flag 3','Fill Flag 4','Fill Flag 5','Surface Albedo Units','Version'], axis=1)

# Below line substitutes the column names with appropriate names
df.columns = ['Year', 'Month','Day','Hour','Minute','Clearsky DHI','Clearsky DNI','Clearsky GHI','Cloud Type','Fill Flag','Surface Albedo','Precipitable Water']

# Dataset CSV file has hour in increments of 30 mins. We will drop the alternate rows. So CSV file only has hourly values.
df = df.iloc[::2]


#=============================================================================================
# At this point dataset only has the values that are required. Verbose values are eliminated.
# We have also removed the alternate rows and renamed the column names
# 
#=============================================================================================

#print(df.iloc[[0]])
#print(df[['Precipitable Water']])
#print(df[['Latitude']])
#print(df.columns.values)
#print(df)
#==================================================================================================



day_of_year = datetime.now().timetuple().tm_yday  # gets the day number of the present year
#print(day_of_year)

now = datetime.now()
hour_of_day = now.hour # + 1 # This line of code gives 0 to 23 but time slots are 1-24. Therefore, + 1
#print(hour_of_day)

if(day_of_year == 1):
    pass
    #row_num = 0 
    
#print(df)
#print(hour_of_day)
#print(day_of_year)
'''    
print(df.iloc[[0]])  ==> OUTPUT OF THIS ==> Month 1 Day 1 Hour 0 Minute 0
print(df.iloc[[1]])  ==> OUTPUT OF THIS ==> Month 1 Day 1 Hour 1 Minute 0
print(df.iloc[[2]])  ==> OUTPUT OF THIS ==> Month 1 Day 1 Hour 2 Minute 0
print(df.iloc[[3]])  ==> OUTPUT OF THIS ==> Month 1 Day 1 Hour 3 Minute 0

[0] is Time_Hour 1
[1] is Time_Hour 2

Therefore => print(df.iloc[[row_num]])
'''


hour_of_year = ( ( day_of_year - 1 )  * 24 ) + hour_of_day  # the total hour ranges from index 0 to index 8759. Therefore, we do - 1
#print(hour_of_year)

entire_row = df.iloc[[hour_of_year]]


Clearsky_DHI = entire_row[['Clearsky DHI']]
Clearsky_DNI = entire_row[['Clearsky DNI']]
Clearsky_GHI = entire_row[['Clearsky GHI']]
Cloud_Type = entire_row[['Cloud Type']]
Fill_Flag = entire_row[['Fill Flag']]
Surface_Albedo = entire_row[['Surface Albedo']]
Precipitable_Water = entire_row[['Precipitable Water']]

#print(entire_row)

#====================================================================================
Clearsky_DHI = Clearsky_DHI.iloc[0]['Clearsky DHI'] # This line of code will grab the value of Clearsky_DHI(integer), from Clearsky_DHI (pandas dataframe format) 
#print(type(Clearsky_DHI))
#print(f"Clearsky DHI is {Clearsky_DHI}")
#====================================================================================
Clearsky_DNI = Clearsky_DNI.iloc[0]['Clearsky DNI']
#print(f"Clearsky DNI is {Clearsky_DNI}")
#====================================================================================
Clearsky_GHI = Clearsky_GHI.iloc[0]['Clearsky GHI']
#print(f"Clearsky GHI is {Clearsky_GHI}")
#====================================================================================
Cloud_Type = Cloud_Type.iloc[0]['Cloud Type']
#print(f"Cloud Type is {Cloud_Type}")
#====================================================================================
Fill_Flag = Fill_Flag.iloc[0]['Fill Flag']
#print(f"Fill flag is {Fill_Flag}")
#====================================================================================
Surface_Albedo = Surface_Albedo.iloc[0]['Surface Albedo']
#print(f"Surface Albedo is {Surface_Albedo}")
#====================================================================================
Precipitable_Water = Precipitable_Water.iloc[0]['Precipitable Water']
#print(f"Precipitable water is {Precipitable_Water}")
#====================================================================================


#Section Ends==================================================================================================








#================ Write data to header file ================


# nws_temp = str(nws_temp)
ow_pressure = str(ow_pressure)
ow_windSpeed = str(ow_windSpeed)
ow_windDirection = str(ow_windDirection)
wb_dewPoint = str(wb_dewPoint)
wb_relativeHumidity = str(wb_relativeHumidity) 

# new_temp or ow_temp
ow_temp = str(ow_temp)



all_list = [ ow_temp, ow_pressure, ow_windSpeed, ow_windDirection, wb_dewPoint, wb_relativeHumidity, Clearsky_DHI, Clearsky_DNI,  Clearsky_GHI , Cloud_Type, Fill_Flag, Surface_Albedo, Precipitable_Water]


with open("weather_API_hourly.json","w") as f:
    json.dump(all_list, f)
    

#===========================================================


#print("API modules are working!")
