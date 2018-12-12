# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:05:11 2018

@author: Gaurav-PC
"""

#The purpose of this script is to test the complete functionalty of the weather_generator script. It utilizes
#unit test module of python. It takes 2 arguments - input file (geo tif) and output file location (containing the sample data)

#import necessary libraries
import unittest
import math
from datetime import datetime
import weather_generator as pc

#The test case class for weather_generator script.
class TestWeatherGenerator(unittest.TestCase):
    
    #define intial variables
    ClassIsSetup = False
    outputloc = ''
    linecount=10000
    
    #The setup and setupClass functions are used to perform the intial setup i.e. reading the geo tif file
    #and generating the weather data file.
    def setUp(self):
        if not self.ClassIsSetup:
            print("****Initializing testing enviornment****")
            self.setupClass()
            self.__class__.ClassIsSetup = True
    
    #This function used to limit the initialization i.e. reading the geo tif file and generating the weather data file
    #only once and not before each test function. This helps in effectively utilizing the system resources.
    def setupClass(self):
        print("****In setup..Calling weather generation****")
        unittest.TestCase.setUp(self)
        #Change the location based on the specific machine.
        inputfile = 'C:/Users/Gaurav-PC/Downloads/gebco_08_rev_elev_B2_grey_geo.tif'
        
        global outputloc
        
        #Change the location based on the specific machine.
        outputloc = 'C:/Users/Gaurav-PC/Downloads/weather_out.txt'
        
        #Step1. call initialize function of source script to be tested.
        pc.initialize(inputfile)
        
        #Step2. call transform function of the source script to be tested.
        pc.transform()
        
        #Step3. call mergeFiles function of the source script to be tested.
        pc.mergeFiles(outputloc)
    
    #This is an utility function to test whether the values in a list are within the min and max range or not.
    #It takes list, min value and max value.
    #It returns boolean based on the check.
    def checkVal(self, list1, min_val, max_val): 
        retval = False
        for x in list1: 
            if int(math.floor(float(x))) >= int(min_val) and int(math.floor(float(x))) <= int(max_val):
                retval = True
            else:
                retval = False
        return retval
    
    #This function is used to test the line count in the output file.
    def test_linecount(self):
        print("****Testing Line Count****")
        cnt = 0
        
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        for line in fileHandle:
            if len(line.strip()) != 0 :
                cnt = cnt+1
                
        #close the output file.
        fileHandle.close()
        self.assertEqual(cnt, self.linecount)
    
    #This function is used to test whether the humidity is in the specified range or not.
    def test_humidity(self):
        print("****Testing Humidity****")
        
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        humidity_list = [] 
        for line in fileHandle:
            fields = line.split('|')
            humidity_list.append(fields[6])
        
        #close the output file.
        fileHandle.close()
        
        #pass the list which contains humidity values for the output file, min and max values.
        returnval = self.checkVal(humidity_list, int(55), int(70))
        self.assertEqual(returnval,True)
        
    #This function is used to test whether the pressure is in the specified range or not.
    def test_pressure(self):
        print("****Testing pressure****")
        
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        pressure_list = [] 
        for line in fileHandle:
            fields = line.split('|')
            pressure_list.append(fields[5])
           
        #close the output file.
        fileHandle.close()
        
        #pass the list which contains pressure values for the output file, min and max values.
        returnval = self.checkVal(pressure_list, int(700), int(1200))
        
        self.assertEqual(returnval,True)
    
    #This function is used to test whether the temperature is in the specified range or not.
    def test_temperature(self):
        print("****Testing temperature****")
        
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        temperature_list = [] 
        for line in fileHandle:
            fields = line.split('|')
            temperature_list.append(fields[4])
        
        #close the output file.
        fileHandle.close()
        
        #pass the list which contains temperature values for the output file, min and max values.
        returnval = self.checkVal(temperature_list, int(-7), int(40))
        self.assertEqual(returnval,True)

    #This function is used to test whether the localtime is in the specified range or not.
    def test_localtime(self):
        print("****Testing local time****")
        retval = False
       
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        for line in fileHandle:
            fields = line.split('|')
            datetime_object = datetime.strptime(fields[2], '%Y-%m-%dT%H:%M:%SZ')
            #Check if the date falls between current year and past 2 years.
            if int(datetime.now().year - 2) <= int(datetime_object.year) <= int(datetime.now().year) :
                retval = True
            else :
                retval = False
        
        #close the output file.
        fileHandle.close()        
        self.assertEqual(retval,True)
    
    #This function is used to test whether the position(lat & long) is in the specified range or not.
    def test_position(self):
        print("****Testing position****")
        retval = False
        
        #open the output file in read mode.
        fileHandle = open(outputloc, 'r')
        for line in fileHandle:
            fields = line.split('|')
            subfields = fields[1].split(',')
            lat = float(subfields[0])
            long = float(subfields[1])
            
            #Check if the position falls with in the range of the input file
            if float(pc.miny_lat) <= lat <= float(pc.maxy_lat) and float(pc.minx_long) <= long <= float(pc.maxx_long) :
                retval = True
            else :
                retval = False
        
        #close the output file.    
        fileHandle.close()
        self.assertEqual(retval,True)

#main method
if __name__ == '__main__':
    unittest.main()