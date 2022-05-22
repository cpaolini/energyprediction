#==================================================================================================

import json
import requests
import datetime

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







#========================= API Starts =========================
'''
dhi, dni, ghi and clearsky from OpenWeather site but its paid.
http://api.openweathermap.org/data/2.5/solar_radiation?lat=32.9455&lon=-117.2059&appid=2956baa231c8a75b7ae7a3b4530c1bdb
'''
#==================================================================================================



#==================================================================================================
'''
Solcast site gives DHI, DNI, GHI but we only have 14 free API calls per day
so we will call it once and get the forecast for the complete day

API Key: dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA
&api_key=dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA
https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=32.9455&longitude=-117.2059&hours=168

This should work only at 12.00am and combine all values into a list
'''

# Below code will access the site and will get the data



#sol_url = "https://api.solcast.com.au/world_radiation/forecasts?latitude=32.9455&longitude=-117.2059&hours=24&api_key=dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA&format=json"
sol_url = "https://api.solcast.com.au/world_radiation/forecasts?latitude="+latitude_val+"&longitude="+longitude_val+"&hours=24&api_key=dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA&format=json"
sol_json = requests.get(sol_url)
sol_data = sol_json.json()
#print(sol_data)



#======================= Start Loop =======================

filled = bool(sol_data)

# if filled = empty, that is filled = false. Then we want to keep on accessing the data in interval of 0.5 seconds
# As filled = false, then we use a while loop with condition of => not(filled) = not(false) = true
# When there is no data accessed then condition is not filled as true
# In this condition we will again keep on pinging and request data but in increments on 0.5 seconds 
# Update: No need to sleep as ping will be done continuously until data accessed

'''
If API gets its data in first instance then output will be Hit top, Hit bottom 
If API fails to get data in first instance then output will be Hit top, Hit middle(while block), Hit bottom   
'''

while(not filled):   # while(true)
    #sol_url = "https://api.solcast.com.au/world_radiation/forecasts?latitude=32.9455&longitude=-117.2059&hours=24&api_key=dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA&format=json"
    sol_url = "https://api.solcast.com.au/world_radiation/forecasts?latitude="+latitude_val+"&longitude="+longitude_val+"&hours=24&api_key=dFoociHZ1jHNuSI5Fy-bZ4_yM92shTTA&format=json"
    sol_json = requests.get(sol_url)
    sol_data = sol_json.json()
    filled = bool(sol_data)

#======================= End Loop =======================





#------------------------------------------------------------------------------
# This block of code will save the python dictionary to a JSON file

with open("irad_final.json","w") as f:
    json.dump(sol_data,f)


#------------------------------------------------------------------------------
# The below code will read the json file containing dictionary

with open("irad_final.json","r") as f:
    obj = json.load(f)
    
    ghi1 = str(obj['forecasts'][0]['ghi'])
    ghi2 = str(obj['forecasts'][2]['ghi'])
    ghi3 = str(obj['forecasts'][4]['ghi'])
    ghi4 = str(obj['forecasts'][6]['ghi'])
    ghi5 = str(obj['forecasts'][8]['ghi'])
    ghi6 = str(obj['forecasts'][10]['ghi'])
    ghi7 = str(obj['forecasts'][12]['ghi'])
    ghi8 = str(obj['forecasts'][14]['ghi'])
    ghi9 = str(obj['forecasts'][16]['ghi'])
    ghi10 = str(obj['forecasts'][18]['ghi'])
    ghi11= str(obj['forecasts'][20]['ghi'])
    ghi12 = str(obj['forecasts'][22]['ghi'])
    ghi13 = str(obj['forecasts'][24]['ghi'])
    ghi14 = str(obj['forecasts'][26]['ghi'])
    ghi15 = str(obj['forecasts'][28]['ghi'])
    ghi16 = str(obj['forecasts'][30]['ghi'])
    ghi17 = str(obj['forecasts'][32]['ghi'])
    ghi18 = str(obj['forecasts'][34]['ghi'])
    ghi19 = str(obj['forecasts'][36]['ghi'])
    ghi20 = str(obj['forecasts'][38]['ghi'])
    ghi21 = str(obj['forecasts'][40]['ghi'])
    ghi22 = str(obj['forecasts'][42]['ghi'])
    ghi23 = str(obj['forecasts'][44]['ghi'])
    ghi24 = str(obj['forecasts'][46]['ghi'])
    
    ghi_final = [ghi1,ghi2,ghi3,ghi4,ghi5,ghi6,ghi7,ghi8,ghi9,ghi10,ghi11,ghi12,ghi13,ghi14,ghi15,ghi16,ghi17,ghi18,ghi19,ghi20,ghi21,ghi22,ghi23,ghi24]
    #print(ghi_final)
    

#------------------------------------------------------------------------------



    dni1 = str(obj['forecasts'][0]['dni'])
    dni2 = str(obj['forecasts'][2]['dni'])
    dni3 = str(obj['forecasts'][4]['dni'])
    dni4 = str(obj['forecasts'][6]['dni'])
    dni5 = str(obj['forecasts'][8]['dni'])
    dni6 = str(obj['forecasts'][10]['dni'])
    dni7 = str(obj['forecasts'][12]['dni'])
    dni8 = str(obj['forecasts'][14]['dni'])
    dni9 = str(obj['forecasts'][16]['dni'])
    dni10 = str(obj['forecasts'][18]['dni'])
    dni11= str(obj['forecasts'][20]['dni'])
    dni12 = str(obj['forecasts'][22]['dni'])
    dni13 = str(obj['forecasts'][24]['dni'])
    dni14 = str(obj['forecasts'][26]['dni'])
    dni15 = str(obj['forecasts'][28]['dni'])
    dni16 = str(obj['forecasts'][30]['dni'])
    dni17 = str(obj['forecasts'][32]['dni'])
    dni18 = str(obj['forecasts'][34]['dni'])
    dni19 = str(obj['forecasts'][36]['dni'])
    dni20 = str(obj['forecasts'][38]['dni'])
    dni21 = str(obj['forecasts'][40]['dni'])
    dni22 = str(obj['forecasts'][42]['dni'])
    dni23 = str(obj['forecasts'][44]['dni'])
    dni24 = str(obj['forecasts'][46]['dni'])
    
    dni_final = [dni1,dni2,dni3,dni4,dni5,dni6,dni7,dni8,dni9,dni10,dni11,dni12,dni13,dni14,dni15,dni16,dni17,dni18,dni19,dni20,dni21,dni22,dni23,dni24]
    #print(dni_final)

#---------------------------------------------------------------------------


    dhi1 = str(obj['forecasts'][0]['dhi'])
    dhi2 = str(obj['forecasts'][2]['dhi'])
    dhi3 = str(obj['forecasts'][4]['dhi'])
    dhi4 = str(obj['forecasts'][6]['dhi'])
    dhi5 = str(obj['forecasts'][8]['dhi'])
    dhi6 = str(obj['forecasts'][10]['dhi'])
    dhi7 = str(obj['forecasts'][12]['dhi'])
    dhi8 = str(obj['forecasts'][14]['dhi'])
    dhi9 = str(obj['forecasts'][16]['dhi'])
    dhi10 = str(obj['forecasts'][18]['dhi'])
    dhi11= str(obj['forecasts'][20]['dhi'])
    dhi12 = str(obj['forecasts'][22]['dhi'])
    dhi13 = str(obj['forecasts'][24]['dhi'])
    dhi14 = str(obj['forecasts'][26]['dhi'])
    dhi15 = str(obj['forecasts'][28]['dhi'])
    dhi16 = str(obj['forecasts'][30]['dhi'])
    dhi17 = str(obj['forecasts'][32]['dhi'])
    dhi18 = str(obj['forecasts'][34]['dhi'])
    dhi19 = str(obj['forecasts'][36]['dhi'])
    dhi20 = str(obj['forecasts'][38]['dhi'])
    dhi21 = str(obj['forecasts'][40]['dhi'])
    dhi22 = str(obj['forecasts'][42]['dhi'])
    dhi23 = str(obj['forecasts'][44]['dhi'])
    dhi24 = str(obj['forecasts'][46]['dhi'])
    
    dhi_final = [dhi1,dhi2,dhi3,dhi4,dhi5,dhi6,dhi7,dhi8,dhi9,dhi10,dhi11,dhi12,dhi13,dhi14,dhi15,dhi16,dhi17,dhi18,dhi19,dhi20,dhi21,dhi22,dhi23,dhi24]
    #print(dhi_final)
    

#---------------------------------------------------
#Output all 3 lists into header file



#GHI_h = "{" + ghi1 + "," + ghi2 + "," + ghi3 + "," + ghi4 + "," + ghi5 + "," + ghi6 + "," + ghi7 + "," + ghi8 + "," + ghi9 + "," + ghi10 + "," + ghi11 + "," + ghi12 + "," + ghi13 + "," + ghi14 + "," + ghi15 + ","  + ghi16 + "," + ghi17 + "," + ghi18 + "," + ghi19 + "," + ghi20 + "," + ghi21 + "," + ghi22 + "," + ghi23 + "," + ghi24 + "}"
#DHI_h = "{" + dhi1 + "," + dhi2 + "," + dhi3 + "," + dhi4 + "," + dhi5 + "," + dhi6 + "," + dhi7 + "," + dhi8 + "," + dhi9 + "," + dhi10 + "," + dhi11 + "," + dhi12 + "," + dhi13 + "," + dhi14 + "," + dhi15 + ","  + dhi16 + "," + dhi17 + "," + dhi18 + "," + dhi19 + "," + dhi20 + "," + dhi21 + "," + dhi22 + "," + dhi23 + "," + dhi24 + "}"
#DNI_h = "{" + dni1 + "," + dni2 + "," + dni3 + "," + dni4 + "," + dni5 + "," + dni6 + "," + dni7 + "," + dni8 + "," + dni9 + "," + dni10 + "," + dni11 + "," + dni12 + "," + dni13 + "," + dni14 + "," + dni15 + ","  + dni16 + "," + dni17 + "," + dni18 + "," + dni19 + "," + dni20 + "," + dni21 + "," + dni22 + "," + dni23 + "," + dni24 + "}"


GHI_h = [ghi1, ghi2, ghi3, ghi4, ghi5, ghi6, ghi7, ghi8, ghi9, ghi10, ghi11, ghi12, ghi13, ghi14, ghi15, ghi16, ghi17, ghi18, ghi19, ghi20, ghi21, ghi22, ghi23, ghi24]
DHI_h = [dhi1, dhi2, dhi3, dhi4, dhi5, dhi6, dhi7, dhi8, dhi9, dhi10, dhi11, dhi12, dhi13, dhi14, dhi15, dhi16, dhi17, dhi18, dhi19, dhi20, dhi21, dhi22, dhi23, dhi24]
DNI_h = [dni1, dni2, dni3, dni4, dni5, dni6, dni7, dni8, dni9, dni10, dni11, dni12, dni13, dni14, dni15, dni16, dni17, dni18, dni19, dni20, dni21, dni22, dni23, dni24]


f = open("irradiance_ghi.json","w")
json.dump(GHI_h, f)
f.close()


f = open("irradiance_dhi.json","w")
json.dump(DHI_h, f)
f.close()

f = open("irradiance_dni.json","w")
json.dump(DNI_h, f)
f.close()




#========================= API ENDS =========================







#========================= API Starts =========================
'''
Solar Zenith Angle:
We cannot fetch hourly values, so we will combine all 24 hourly values into a list

https://midcdmz.nrel.gov/apps/solpos.pl?syear=2021&smonth=7&sday=8&eyear=2021&emonth=7&eday=8&step=60&stepunit=1&latitude=32.9455&longitude=-117.2059&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33
https://midcdmz.nrel.gov/apps/solpos.pl?syear={2021}&smonth={7}&sday={8}&eyear={2021}&emonth={7}&eday={8}&step=60&stepunit=1&latitude=32.9455&longitude=-117.2059&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33

'''



import requests
import datetime
import html

dt = datetime.datetime.today()
year = str(dt.year)
month = str(dt.month)
day = str(dt.day)


#query = "https://midcdmz.nrel.gov/apps/solpos.pl?syear="+year+"&smonth="+month+"&sday="+day+"&eyear="+year+"&emonth="+month+"&eday="+day+"&step=60&stepunit=1&latitude=32.9455&longitude=-117.2059&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33"
query = "https://midcdmz.nrel.gov/apps/solpos.pl?syear="+year+"&smonth="+month+"&sday="+day+"&eyear="+year+"&emonth="+month+"&eday="+day+"&step=60&stepunit=1&latitude="+latitude_val+"&longitude="+longitude_val+"&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33"
response = requests.get(query)
data = html.unescape(response.text)




#======================= Loop Starts =======================
filled = bool(data)

while(not filled):
    #query = "https://midcdmz.nrel.gov/apps/solpos.pl?syear="+year+"&smonth="+month+"&sday="+day+"&eyear="+year+"&emonth="+month+"&eday="+day+"&step=60&stepunit=1&latitude=32.9455&longitude=-117.2059&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33"
    query = "https://midcdmz.nrel.gov/apps/solpos.pl?syear="+year+"&smonth="+month+"&sday="+day+"&eyear="+year+"&emonth="+month+"&eday="+day+"&step=60&stepunit=1&latitude="+latitude_val+"&longitude="+longitude_val+"&timezone=-7.0&press=1013.0&temp=15&aspect=180&tilt=0&solcon=1367&sbwid=7.6&sbrad=31.7&sbsky=0.04&interval=0&field=33"
    response = requests.get(query)
    data = html.unescape(response.text)
    filled = bool(data)

#======================= Loop Ends =======================


# Convert data from html format to C code array
lst = data.split(",")
lst = lst[4::1]
nlst = []

for element in lst:
    nlst.append(element.replace('\n',' '))

nlst = nlst[::2]
new_lst=[]

for element in nlst:
    head, sep, tail = element.partition(' ')
    new_lst.append(head)



#print(type(new_lst))




with open("Solar_Zenith_Angle.json","w") as f:
    json.dump(new_lst, f)
    
    
    

#========================= API ENDS =========================








#==================================================================================================================
