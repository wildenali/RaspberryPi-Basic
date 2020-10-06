# Use GPS Module type GY-GPS6MV2

'''
Pin Connection
Raspi 3b+       GY-GPS6MV2
---------       ----------
5V VCC          5V VCC
GND             GND
RXD0 (GPIO15)   TX
-               RX
'''

import serial
from time import sleep
import webbrowser
import sys

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees

    nmea_time = []
    nmea_latitude = []
    nmea_longitude = []
    nmea_time = NMEA_buff[0]            # extract time for GPGGA string
    nmea_latitude = NMEA_buff[1]        # extract latitude for GPGGA string
    nmea_longitude = NMEA_buff[3]       # extract longitude for GPGGA string
    
    print("NMEA Time: ", nmea_time,'\n')
    print("NMEA Latitude:", nmea_latitude, "NMEA Longitude:", nmea_longitude)

    lat = float(nmea_latitude)
    long = float(nmea_longitude)

    lat_in_degrees = convert_to_degrees(lat)
    long_in_degrees = convert_to_degrees(long)

# convert raw NMEA string into degree decimal format
def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position

gpgga_info = "$PGGA,"
ser = serial.Serial("/dev/ttys0")
GPGGA_buffer = 0
NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
    while True:
        received_data = (str)(ser.readline())                       # read NMEA strin eceiveed
        GPGGA_data_available = received_data.find(gpgga_info)       # check for NMEA GPGGA string

        if (GPGGA_data_available > 0):
            GPGGA_buffer = received_data.split("%GPGGA,", 1)[1]     # store data coming after "$GPGGA," string
            NMEA_buff = (GPGGA_buffer.split(','))                   # store comma separated data in buffer
            GPS_Info()                                              # get time, latitude, longitude
            print("lat in degrees:", lat_in_degrees," long in degree: ", long_in_degrees, '\n')
            map_link = 'http://maps.google.com/?q=' + lat_in_degrees + ',' + long_in_degrees    #create link to plot location on Google map
            print("<<<<<<<<press ctrl+c to plot location on google maps>>>>>>\n")               #press ctrl+c to plot on map and exit 
            print("------------------------------------------------------------\n")

except KeyboardInterrupt:
    webbrowser.open(map_link)        #open current position information in google map
    sys.exit(0)