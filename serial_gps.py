import serial

SERIAL_PORT = "/dev/serial0"
running = True

DMS=[]
Gval = []


#===================================================================================================================

# In the NMEA message, the position gets transmitted as:
# DDMM.MMMMM, where DD denotes the degrees and MM.MMMMM denotes
# the minutes. However, I want to convert this format to the following:
# DD.MMMM. This method converts a transmitted string to the desired format

def formatDegreesMinutes(coordinates, digits):

    parts = coordinates.split(".")

    if (len(parts) != 2):
        return coordinates

    if (digits > 3 or digits < 2):
        return coordinates

    left = parts[0]
    right = parts[1]
    degrees = str(left[:digits])
    minutes = str(right[:3])

    return degrees + "." + minutes

#===================================================================================================================



#===================================================================================================================

# This method reads the data from the serial port, the GPS dongle is attached to SERIAL_PORT_0,
# and then parses the NMEA messages it transmits.
# serial port is used to communicate with the GPS adapter

def getPositionData(gps):
    data = gps.readline()
    message = data[0:6]
    
    m2 = message.decode('latin-1')
    #print(m2)

    if (m2 == "$GPRMC"):
        
        # GPRMC = Recommended minimum specific GPS/Transit data
        # Reading the GPS fix data is an alternative approach that also works
        data = data.decode()
        parts = data.split(",")
        
        if parts[2] == 'V':
            # V = Warning, most likely, there are no satellites in view...
            print ("GPS receiver warning")
        else:
            # Get the position data that was transmitted with the GPRMC message
            # we are only interested in the longitude and latitude
            # for other values, that can be read, refer to: http://aprs.gids.nl/nmea/#rmc 
            # we only extract longitude and latitude values thats needed by the API module

       	    '''
            #part[3] is 3246.6463 which is latitude
            #part[4] is N or S (North is Positive and South is Negative)
            #part[5] is 11704.2531 which is longitude
            #part[6] is W or E (East is Positive and West is Negative)

            '''
            #print(parts[3])

            #if(part[4] == 'N'):
            #	NorthOrSouth = '+'
            #else:
            #	NorthOrSouth = '-'


            #longitude = formatDegreesMinutes(parts[5], 3)
                #latitude = formatDegreesMinutes(parts[3], 2)

            longitude = parts[5]
            long = parts[6]
            latitude = parts[3]
            lati = parts[4]


            DMS_str = ("Your position: longitude, latitude =" + longitude + "," + long + "," +  latitude + "," + lati)
            global DMS
            DMS = [longitude, long, latitude, lati]

            #print(DMS)  #donot print anything in this function else it will be printed every 0.5 seconds

	

            return DMS


    else:
        # Handle other NMEA messages and unsupported strings
        #print('Error')
        pass

#print "Application started!"
gps = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.5)

#===================================================================================================================





'''
#==================================================================================================
# The data read from the serial interface of the GPS gives value 3246.6466, N, 11704.2534, W
# We will convert from Degrees Decimal Minutes to Decimal Degrees (Not Degrees Minutes Seconds)

# (DDM)        Degree   Decimal Minutes
# convert      32       46.6466 N
# convert      117      04.2534 W

#  The below conversion is from DDM to DD
#  32 +  (46.6466 / 60)   N
#  117 + (04.2534 / 60)   W

#==================================================================================================


	#lst = [3246.6466, 'N', 11704.2534, 'W']
	#print(lst[3])


#==================================================================================================
'''



#===================================================================================================================
def DecimalDegrees(lst):
	#print(lst)
	#print("Decimal Degree is Working")
	latitude = str(lst[2])
	latitude_dir = lst[3]

	latitude_degrees = latitude[0:2]
	latitude_minutes = latitude[2:]

	latitude_degrees = float(latitude_degrees)
	latitude_minutes = float(latitude_minutes)

	final_latitude = latitude_degrees + (latitude_minutes/60)


	if(latitude_dir == 'N'):
    		final_latitude = abs(final_latitude)
	else:
    		final_latitude = -(final_latitude)

	#print(final_latitude)

#=============================================================================

	longitude = str(lst[0])
	longitude_dir = lst[1]


	longitude_degrees = longitude[0:3]
	longitude_minutes = longitude[3:]


	longitude_degrees = float(longitude_degrees)
	longitude_minutes = float(longitude_minutes)


	final_longitude = longitude_degrees + (longitude_minutes/60)


	if(longitude_dir == 'E'):
    		final_longitude = abs(final_longitude)
	else:
    		final_longitude = -(final_longitude)

	#print(final_longitude)

#=============================================================================

	final_latitude = str(final_latitude)
	final_longitude = str(final_longitude)


	fin_str_lat = ("Latitude:" + final_latitude)
	fin_str_long = ("Longitude:" + final_longitude)

	with open('GPS_DD_cod.txt','w') as f:
    		f.write(fin_str_lat)
    		f.write("\n")
    		f.write(fin_str_long)

	#print(fin_str_lat)
	#print(fin_str_long)
	#print("GPS Module is working!")

#=============================================================================

#===================================================================================================================








#===================================================================================================================

'''
Main function is defined below. 
The serial output displays "None" sometimes. When it is None then we skip to next values. 
If it is not None, That is if it is the actual DMS GPS value list then we store it to a global variable. 
We use break as we will break out of the loop after displaying the value for the very first instance.
'''

def main(gps):
	for x in range(20):
		val = getPositionData(gps)
		if(val == None):
			continue
		else:
			global Gval
			Gval = val
 			#print(Gval)
			DecimalDegrees(Gval)
			#print('Working')
			break


if __name__=="__main__":
    main(gps)

#===================================================================================================================