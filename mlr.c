/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

#include "head.h"
#include "irradiance_final.h"
#include "Solar_Zenith_Angle.h"
#include "weather_API_hourly.h"


//precision -ve => 8 + e^-05 = e^-13 to  e^+18

int main()
{
    /*
    DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,
    CloudType,DewPoint,SolarZenith,
    FillFlag,SurfaceAlbedo,WindSpeed,
    PrecipitableWater,WindDirection,RelativeHumidity,
    Temperature,Pressure
     */

//==================================================================================================================================

    double DHI_v = 0, DNI_v = 0, GHI_v = 0, ClearDHI_v = 0, ClearDNI_v = 0, ClearGHI_v = 0, CloudType_v = 0, DewPoint_v = 0, SolarZenith_v = 0, FillFlag_v = 0, SurfaceAlbedo_v = 0, WindSpeed_v = 0, PrecipitableWater_v = 0, WindDirection_v = 0, RelativeHumidity_v = 0, Temperature_v = 0,Pressure_v = 0;



//=========================================================================================================================================

    time_t now = time(NULL);
    struct tm *tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    //printf("%d",hour);

    /*
    DHI,DNI,GHI,ClearDHI,ClearDNI,ClearGHI,
    CloudType,DewPoint,SolarZenith,
    FillFlag,SurfaceAlbedo,WindSpeed,
    PrecipitableWater,WindDirection,RelativeHumidity,
    Temperature,Pressure
    */

    double power = 0, price = 0, final_price = 0;



//===================================================================================================================================
    DHI_v = DHI[hour];

    DNI_v = DNI[hour];

    GHI_v = GHI[hour];
//===================================================================================================================================

    SolarZenith_v = SZA[hour];

//===================================================================================================================================

// The weather_API_hourly.h file has am array called "hourly" and the format is:
// [Temperature , Pressure, Wind Speed, Wind Direction, Dew Point, Relative Humidity, Clearsky DHI, Clearsky DNI, Clearsky_GHI, Cloud Type, Fill Flag, Surface Albedo, Precipitable water] 


    ClearDHI_v = hourly[6];

    ClearDNI_v = hourly[7];

    ClearGHI_v = hourly[8];

    CloudType_v = hourly[9];

    DewPoint_v = hourly[4];

    FillFlag_v = hourly[10];

    SurfaceAlbedo_v = hourly[11];

    WindSpeed_v = hourly[2];

    PrecipitableWater_v = hourly[12];

    WindDirection_v = hourly[3];

    RelativeHumidity_v = hourly[5];

    Temperature_v = hourly[0];

    Pressure_v = hourly[1];



//===============================================================================================================================================

    power = A[hour][0] + A[hour][1] * DHI_v + A[hour][2] * DNI_v + A[hour][3] * GHI_v + A[hour][4] *ClearDHI_v + A[hour][5] * ClearDNI_v + A[hour][6] * ClearGHI_v + A[hour][7] * CloudType_v + A[hour][8] * DewPoint_v + A[hour][9] * SolarZenith_v + A[hour][10] * FillFlag_v + A[hour][11] * SurfaceAlbedo_v + A[hour][12] * WindSpeed_v + A[hour][13] * PrecipitableWater_v + A[hour][14] * WindDirection_v + A[hour][15] * RelativeHumidity_v + A[hour][16] * Temperature_v + A[hour][17] * Pressure_v;
    power = fabs(power);
    //printf("%0.10lf",power);

//===============================================================================================================================================



if(hour == 0 || hour == 1 || hour == 2 || hour == 3 || hour == 4 || hour == 5){
price = 0.30;    // 30 cents is 0.30 dollars
}

else if(hour == 6 || hour == 7 || hour == 8 || hour == 9){
price = 0.36;
}

else if(hour == 10 || hour == 11 || hour == 12 || hour == 13){
price = 0.30;
}

else if(hour == 14 || hour == 15){
price = 0.36;
}

else if(hour == 16 || hour == 17 || hour == 18 || hour == 19|| hour == 20){
price = 0.61;
}

else if(hour == 21 || hour == 22 || hour == 23){
price = 0.36;
}

else{
price = 0;
}

//=============================================================================================================================================

//printf("\n\n\n");

//printf("%0.5lf",price);

//printf("\n\n\n");

final_price = (power * price);

//printf("%0.10lf",final_price);

//==============================================================================================================================================



FILE *fp = fopen("cout.txt","w+");

fprintf(fp,"%f",power);
fprintf(fp,"\n");
fprintf(fp,"%f",final_price);
fclose(fp);

//===============================================================================================================================================


	//printf("\n\n");

	//printf("%d",hour);

	printf("C code is working!");




//================================================================================================================================================
    /*
    for(int i=0;i<24;i++)
    {
        for(int j=0;j<18;j++)
        {
            printf("%0.18lf\t",A[i][j]);
        }
    }
    */



    return 0;
}
