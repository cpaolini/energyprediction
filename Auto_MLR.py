
import pandas as pd
from sklearn import linear_model


'''
This code file will take 24 CSV files as input. Then it generates the intercept and co-efficient and saves them in a text file.

Replace the location 
f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
with Location where you need to save the co-efficient text file.

Replace the location 
name=f"D:\\Thesis\\Organized\\6-24\\616_after\\{x}.csv"
with directory where all 24 CSV files are saved

'''

 

#f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
f.close()

for z in range(1,25):   # iterate over 24 csv files
   
    x = str(z)
    name=f"D:\\Thesis\\Organized\\6-24\\616_after\\{x}.csv"   
    dataset = pd.read_csv(name)
    
    
    X = dataset.drop('PC',axis = 1)
    y = dataset.PC
    
    #features = ['DHI','DNI','GHI','ClearDHI','ClearDNI','ClearGHI','CloudType','DewPoint','SolarZenith','FillFlag','SurfaceAlbedo','WindSpeed','PrecipitableWater','WindDirection','RelativeHumidity','Temperature','Pressure']
    
    ols = linear_model.LinearRegression()   # fit the Linear Regression Model 
    model = ols.fit(X, y)
    
    og_list = str(model.coef_)
    og_list = og_list.replace("  "," ")
    og_list = og_list.lstrip("[")
    og_list = og_list.rstrip("]")           # Extract the coefficient value and save it to a list. Remove whitespaces and brackets. 
        
    #print(model.intercept_)
    #print(model.coef_) 
    #print(og_list)
    
    ele=og_list.split(" ") # convert coefficients into list of strings
    ele[:] = [x for x in ele if x] # remove all the blank elements from the list
    final_list = [] 
    
    for word in ele: # remove all the newline characters
        final_list.append(word.strip())
        
    #print(final_list)  
     
    intercept = str(model.intercept_)
    #print(type(intercept))
        
    #-----------------------------------------------------------------------------------------------------
    
    # Each csv file corresponds to a specific time hour. From heatmap we remove the highly correlated feature. 
    # Assign 0 value to features. Assigning 0 value is equivalent to removing a feature. 
    # 
        
    # Block 1 starts
    if ( (z == 1) or (z == 2) or (z == 3) or (z == 4) or (z == 5) ):
        
        DHI = 0
        DHI = str(DHI)
        DNI = 0
        DNI = str(DNI) 
        GHI = 0
        GHI = str(GHI)
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        ClearDNI = 0
        ClearDNI = str(ClearDNI)
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        CloudType = final_list[0]
        DewPoint = final_list[1]
        SolarZenith = final_list[2]
        FillFlag = final_list[3]
        SurfaceAlbedo = final_list[4]
        WindSpeed = final_list[5]
        PrecipitableWater = final_list[6]
        WindDirection = final_list[7]
        RelativeHumidity = final_list[8]
        Temperature = final_list[9]
        Pressure = final_list[10]
        
        #print(type(DHI))
        
        # Create a list to save all the coefficients and intercept. Save the list to text file. 
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 1 ends
    
    
    
    
    #-----------------------------------------------------------------------------------------------------
    
    
    
     # Block 2 starts
    if ( (z == 6) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2]
        
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        ClearDNI = 0
        ClearDNI = str(ClearDNI)
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[3]
        DewPoint = final_list[4]
        SolarZenith = final_list[5]
        FillFlag = final_list[6]
        SurfaceAlbedo = final_list[7]
        WindSpeed = final_list[8]
        PrecipitableWater = final_list[9]
        WindDirection = final_list[10]
        RelativeHumidity = final_list[11]
        Temperature = final_list[12]
        Pressure = final_list[13]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 2 ends
    
    
    #-----------------------------------------------------------------------------------------------------
    
    
    
     # Block 3 starts
    if ( (z == 7) or (z == 8) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2]
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]
        
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[5]
        DewPoint = final_list[6]
        SolarZenith = final_list[7]
        FillFlag = final_list[8]
        SurfaceAlbedo = final_list[9]
        WindSpeed = final_list[10]
        PrecipitableWater = final_list[11]
        WindDirection = final_list[12]
        RelativeHumidity = final_list[13]
        Temperature = final_list[14]
        Pressure = final_list[15]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 3 ends
        
        
     #-----------------------------------------------------------------------------------------------------    
      
    
    
     # Block 4 starts
    if ( (z == 9) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2]
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]
        ClearGHI = final_list[5]
        CloudType = final_list[6]
        DewPoint = final_list[7]
        SolarZenith = final_list[8]
        FillFlag = final_list[9]
        SurfaceAlbedo = final_list[10]
        WindSpeed = final_list[11]
        PrecipitableWater = final_list[12]
        WindDirection = final_list[13]
        RelativeHumidity = final_list[14]
        Temperature = final_list[15]
        Pressure = final_list[16]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 4 ends
        
        
     #-----------------------------------------------------------------------------------------------------   
       
    
    
     # Block 5 starts
    if ( (z == 10) or (z == 11) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]
        
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[5]
        DewPoint = final_list[6]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[7]
        SurfaceAlbedo = final_list[8]
        WindSpeed = final_list[9]
        PrecipitableWater = final_list[10]
        WindDirection = final_list[11]
        RelativeHumidity = final_list[12]
        Temperature = final_list[13]
        Pressure = final_list[14]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 5 ends
        
        
     #-----------------------------------------------------------------------------------------------------   
       
    
    
     # Block 6 starts
    if ( (z == 12) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        
        ClearDNI = final_list[3]
        
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[4]
        DewPoint = final_list[5]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[6]
        SurfaceAlbedo = final_list[7]
        WindSpeed = final_list[8]
      
        PrecipitableWater = 0
        PrecipitableWater = str(PrecipitableWater)
        
        WindDirection = final_list[9]
        RelativeHumidity = final_list[10]
        Temperature = final_list[11]
        Pressure = final_list[12]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 6 ends
        
        
     #-----------------------------------------------------------------------------------------------------   
   
    
    
     # Block 7 starts
    if ( (z == 13) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]        
        ClearGHI = final_list[5]
        CloudType = final_list[6]
        DewPoint = final_list[7]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[8]
        SurfaceAlbedo = final_list[9]
        WindSpeed = final_list[10]
        PrecipitableWater = final_list[11]
        WindDirection = final_list[12]
        RelativeHumidity = final_list[13]
        Temperature = final_list[14]
        Pressure = final_list[15]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 7 ends
        
        
     #----------------------------------------------------------------------------------------------------- 
    
    
    
     # Block 8 starts
    if ( (z == 14) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]        
        ClearGHI = final_list[5]
        CloudType = final_list[6]
        DewPoint = final_list[7]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[8]
        SurfaceAlbedo = final_list[9]
        WindSpeed = final_list[10]
        
        PrecipitableWater = 0
        PrecipitableWater = str(PrecipitableWater)
        
        WindDirection = final_list[11]
        RelativeHumidity = final_list[12]
        Temperature = final_list[13]
        Pressure = final_list[14]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 8 ends
        
        
     #----------------------------------------------------------------------------------------------------- 
      
    
    
     # Block 9 starts
    if ( (z == 15) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        
        ClearDNI = final_list[3]
        
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[4]
        DewPoint = final_list[5]
        
        SolarZenith = final_list[6]
        
        FillFlag = final_list[7]
        SurfaceAlbedo = final_list[8]
        WindSpeed = final_list[9]
      
        PrecipitableWater = 0
        PrecipitableWater = str(PrecipitableWater)
        
        WindDirection = final_list[10]
        RelativeHumidity = final_list[11]
        Temperature = final_list[12]
        Pressure = final_list[13]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 9 ends
        
        
     #-----------------------------------------------------------------------------------------------------   
      
    
    
     # Block 10 starts
    if ( (z == 16) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        
        ClearDNI = final_list[3]
        
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        
        CloudType = final_list[4]
        DewPoint = final_list[5]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[6]
        SurfaceAlbedo = final_list[7]
        WindSpeed = final_list[8]
        PrecipitableWater = final_list[9]        
        WindDirection = final_list[10]
        RelativeHumidity = final_list[11]
        Temperature = final_list[12]
        Pressure = final_list[13]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 10 ends
        
        
     #----------------------------------------------------------------------------------------------------- 
     
    
    
     # Block 11 starts
    if ( (z == 17) ):
        
        DHI = 0
        DHI = str(DHI)
        
        DNI = final_list[0]
        GHI = final_list[1] 
        
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        
        ClearDNI = final_list[2]
        ClearGHI = final_list[3]
        CloudType = final_list[4]
        DewPoint = final_list[5]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[6]
        SurfaceAlbedo = final_list[7]
        WindSpeed = final_list[8]
        
        PrecipitableWater = 0        
        PrecipitableWater = str(PrecipitableWater)
        
        WindDirection = final_list[9]
        RelativeHumidity = final_list[10]
        Temperature = final_list[11]
        Pressure = final_list[12]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 11 ends
        
        
     #----------------------------------------------------------------------------------------------------- 
    
    
    
     # Block 12 starts
    if ( (z == 18) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2] 
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]        
        ClearGHI = final_list[5]
        CloudType = final_list[6]
        DewPoint = final_list[7]
        
        SolarZenith = 0
        SolarZenith = str(SolarZenith)
        
        FillFlag = final_list[8]
        SurfaceAlbedo = final_list[9]
        WindSpeed = final_list[10]
        PrecipitableWater = final_list[11]
        WindDirection = final_list[12]
        RelativeHumidity = final_list[13]
        Temperature = final_list[14]
        Pressure = final_list[15]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 12 ends
        
        
     #----------------------------------------------------------------------------------------------------- 
     
    
    
     # Block 13 starts
    if ( (z == 19) ):
        
        DHI = final_list[0]
        DNI = final_list[1]
        GHI = final_list[2]
        ClearDHI = final_list[3]
        ClearDNI = final_list[4]
        ClearGHI = final_list[5]
        CloudType = final_list[6]
        DewPoint = final_list[7]
        SolarZenith = final_list[8]
        FillFlag = final_list[9]
        SurfaceAlbedo = final_list[10]
        WindSpeed = final_list[11]
        PrecipitableWater = final_list[12]
        WindDirection = final_list[13]
        RelativeHumidity = final_list[14]
        Temperature = final_list[15]
        Pressure = final_list[16]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 13 ends
        
        
     #-----------------------------------------------------------------------------------------------------   
    
    
    
    
     # Block 14 starts
    if ( (z == 20) or (z == 21) or (z == 22) or (z == 23) or (z == 24) ):
        
        DHI = 0
        DHI = str(DHI)
        DNI = 0
        DNI = str(DNI) 
        GHI = 0
        GHI = str(GHI)
        ClearDHI = 0
        ClearDHI = str(ClearDHI)
        ClearDNI = 0
        ClearDNI = str(ClearDNI)
        ClearGHI = 0
        ClearGHI = str(ClearGHI)
        CloudType = final_list[0]
        DewPoint = final_list[1]
        SolarZenith = final_list[2]
        FillFlag = final_list[3]
        SurfaceAlbedo = final_list[4]
        WindSpeed = final_list[5]
        PrecipitableWater = final_list[6]
        WindDirection = final_list[7]
        RelativeHumidity = final_list[8]
        Temperature = final_list[9]
        Pressure = final_list[10]
        
        #print(type(DHI))
        
    
        features = [intercept,DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,CloudType,DewPoint,SolarZenith,FillFlag,SurfaceAlbedo,WindSpeed,PrecipitableWater,WindDirection,RelativeHumidity,Temperature,Pressure]
        #print(features)
        
        
        #f = open("D:\\Thesis\\Organized\\coefficients_auto.txt","a")
        f = open("D:\\Thesis\\________________Thesis Code Final_____________________\\no C_ MLR_final_all edits\\MLR_final_edit 1\\coefficients_auto.txt","a")
        for obj in features:
            f.write(obj + "\t")
        
        f.write("\n")
        f.close()
            
        
        print(features)
        
        # Block 14 ends
    
    
    #-----------------------------------------------------------------------------------------------------
    
    

    
    '''
    print(f"{x}")
    print(model.coef_)
    print(model.intercept_)    
    print("---------------------------------------")

    #print(model.score(X, y))
    
   '''
   
   