import sys
sys.path.append('../../Libraries')

import serial  # pyserial is required
from micropyGPS import MicropyGPS #https://github.com/inmcm/micropyGPS

def setup():
    global gps
    global uart
    global x1
    global x2
    global y1
    global y2

    gps = MicropyGPS()
    uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=30)


    x1 = gps.longitude[1]
    y1 = gps.latitude[1]

    x2 = float(input("Enter Latitude"))
    y2 = float(input("Enter Longitude"))

def main():
    while 1:
        sent = uart.readline().decode('utf-8')
        print(sent)
        for x in sent:
            gps.update(x)
        if gps.latitude[1] <= 35:
            print("test")

        #print("fix_type 1 means no fix: ",gps.fix_type)
        print("lat " ,gps.latitude)
        print("long " ,gps.longitude)
        print("speed ", gps.speed)
        #print("satellites_visible " ,gps.satellites_visible())
        #print("direction ", gps.compass_direction())

if __name__== "__main__":
    setup()
    main()