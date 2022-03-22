import pymongo
from pymongo import MongoClient
import urllib
client = MongoClient("mongodb+srv://username:"+urllib.parse.quote("password")+"mongonodeconnectionstring")
mydb = client["temperatureSeries"]
mycol = mydb["bedroom"]
mycol1=mydb["studyroom"]
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
from datetime import datetime
import csv

def writeCSV(datafile,time,data):
    ofile = open(datafile, 'a')
    try:
        writer = csv.writer(ofile)
        writer.writerow([time,data])
    finally:
        ofile.close()
while True:
    rcv = ser.readline()
    cmd = rcv.decode('utf-8').rstrip()
    if cmd != "":
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string)
        if 'A' in cmd:
            print(cmd)
            data1=cmd.replace('(','').replace(')','').replace('A','')
            writeCSV("bedroom.csv",dt_string,data1)
            dict1={"time":dt_string,"temp":int(data1)}
            mycol.insert_one(dict1)
            data1=""
            dict1={}
        if 'B' in cmd:
            print(cmd)
            data2=cmd.replace('(','').replace(')','').replace('B','')
            writeCSV("studyRoom.csv",dt_string,data2)
            dict2={"time":dt_string,"temp":int(data2)}
            mycol1.insert_one(dict2)
            data2=""
            dict2={}