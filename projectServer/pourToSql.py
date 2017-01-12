#!/usr/bin/python
#-*- coding: utf-8 -*-

#data type is like this. [[lng, lat], [x1,y1,z1], [x2,y2,z2], []...]
import MySQLdb
import sys

def pour2SQL(array_data): 
    gps_list = getGPSData(array_data) 
    acceleration_list = getAccelerationData(array_data) 
    lat = gps_list[0]
    lng = gps_list[1]

    if len(gps_list) != 2:
        print("err: Length of gps data array is not correct, gps_length: %d" % (len(gps_list))) 
        sys.exit() 

    connector = MySQLdb.connect(host='localhost', db='earthquaker', user="root", passwd="miro", charset="utf8") 
    cursor = connector.cursor() 

    print("Connected to MySQL Database")
    for acce in acceleration_list:  
        if len(acce) != 3:
            print("err: Length of acceleratino data array is not correct, acceleration_length: %d" % (len(acce))) 
            sys.exit() 

        x_axis = acce[0]
        y_axis = acce[1]
        z_axis = acce[2]

        sql = u"insert into test_table values(" + str(lat) + "," + str(lng) + "," + str(x_axis)  + "," + str(y_axis) + "," + str(z_axis) + ")"
        cursor.execute(sql) 

    connector.commit() 
    print("data committed to mysql") 
    cursor.close() 
    connector.close() 

def getAccelerationData(data): 
    return data[1:]

def getGPSData(data): 
    return data[0]

if __name__ == "__main__":
    data = [[35.3883883, 139.4257731], [1,2,3], [4,5,6], [7,8,9], [10,11,12]]
    acce = getAccelerationData(data)
    gps = getGPSData(data) 

    pour2SQL(data)
