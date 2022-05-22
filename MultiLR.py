'''
header => header_coefficients.json

hourly => weather_API_hourly.json

Irradiance =>
                Solar_Zenith_Angle.json
                irradiance_ghi.json
                irradiance_dhi.json
                irradiance_dni.json



'''
import datetime
import math
import json


#-----------------------------------------Import Data Start-----------------------------------------




#===================================================================================================
# head.h

with open("header_coefficients.json","r") as f:
    A = json.load(f)
    
#print(type(A))

#===================================================================================================



    
#===================================================================================================
# weather_API_hourly.h

with open("weather_API_hourly.json","r") as f:
    hourly = json.load(f)
    

#print(type(hourly))
     
#===================================================================================================



#===================================================================================================
# weather_API_24.h
with open("irradiance_ghi.json","r") as f:
    GHI = json.load(f)
    
    
with open("irradiance_dhi.json","r") as f:
    DHI = json.load(f)
    
    
with open("irradiance_dni.json","r") as f:
    DNI = json.load(f)

with open("Solar_Zenith_Angle.json","r") as f:
    SZA = json.load(f)

#print(type(SZA))

#===================================================================================================

 
#-----------------------------------------Import Data End-----------------------------------------






#===================================================================================================

hour = datetime.datetime.now().hour
#print(hour)

power = 0
price = 0
final_price = 0

#===================================================================================================

DHI_v = float(DHI[hour])

DNI_v = float(DNI[hour])

GHI_v = float(GHI[hour])

#===================================================================================================

SolarZenith_v = float(SZA[hour])

#===================================================================================================

 
# The weather_API_hourly.h file has an array called "hourly" and the format is:
# [Temperature , Pressure, Wind Speed, Wind Direction, Dew Point, Relative Humidity, Clearsky DHI, Clearsky DNI, Clearsky_GHI, Cloud Type, Fill Flag, Surface Albedo, Precipitable water] 


ClearDHI_v = float(hourly[6])

ClearDNI_v = float(hourly[7])

ClearGHI_v = float(hourly[8])

CloudType_v = float(hourly[9])

DewPoint_v = float(hourly[4])

FillFlag_v = float(hourly[10])

SurfaceAlbedo_v = float(hourly[11])

WindSpeed_v = float(hourly[2])

PrecipitableWater_v = float(hourly[12])

WindDirection_v = float(hourly[3])

RelativeHumidity_v = float(hourly[5])

Temperature_v = float(hourly[0])

Pressure_v = float(hourly[1])



#print(type(Pressure_v))



#===============================================================================================================================================


power = A[hour][0] + A[hour][1] * DHI_v + A[hour][2] * DNI_v + A[hour][3] * GHI_v + A[hour][4] *ClearDHI_v + A[hour][5] * ClearDNI_v + A[hour][6] * ClearGHI_v + A[hour][7] * CloudType_v + A[hour][8] * DewPoint_v + A[hour][9] * SolarZenith_v + A[hour][10] * FillFlag_v + A[hour][11] * SurfaceAlbedo_v + A[hour][12] * WindSpeed_v + A[hour][13] * PrecipitableWater_v + A[hour][14] * WindDirection_v + A[hour][15] * RelativeHumidity_v + A[hour][16] * Temperature_v + A[hour][17] * Pressure_v             
power = math.fabs(power)
print(power)


#===============================================================================================================================================





if(hour == 0 or hour == 1 or hour == 2 or hour == 3 or hour == 4 or hour == 5):
    price = 0.30    # 30 cents is 0.30 dollars


elif(hour == 6 or hour == 7 or hour == 8 or hour == 9):
    price = 0.36


elif(hour == 10 or hour == 11 or hour == 12 or hour == 13):
    price = 0.30


elif(hour == 14 or hour == 15):
    price = 0.36


elif(hour == 16 or hour == 17 or hour == 18 or hour == 19 or hour == 20):
    price = 0.61


elif(hour == 21 or hour == 22 or hour == 23):
    price = 0.36


else:
    price = 0   


#//=============================================================================================================================================


#print(price)

final_price = (power * price)

print()
print(final_price)


#//==============================================================================================================================================


power = str(power)
final_price = str(final_price)


with open("MultiLR.txt","w+") as f:
    f.write(power)
    f.write("\n")
    f.write(final_price)



#//===============================================================================================================================================


#print(hour)

#print("C code is working!")


#//================================================================================================================================================



