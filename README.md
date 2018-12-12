# Weather Data Generation
# Highlights
Weather_generation.py script is written in python and it creates a toy simulation of the environment (taking into account things like atmosphere, topography, geography,
oceanography, or similar) that evolves over time. It emits the data in the following format:
Location|latitude,longitude,elevation|LocalTime|Condition|Temperature|Pressure|Humidity

Here is the sample of the output data generated: -
Location|latitude,longitude,elevation|LocalTime|Condition|Temperature|Pressure|Humidity
Hobart|-59.58,-27.83,23|2017-04-25T13:55:32Z|Snow|-5|938.1|57
Darwin|-78.33,-38.57,36|2017-10-02T12:32:04Z|Snow|-4|1064.2|57
Melbourne|-23.85,-71.44,14|2016-09-16T06:41:22Z|Rain|19|976.1|63

It works with python 3.7.x. The design primarily involves creating a multithreaded application which can an input geo tif file and generate the output weather data with multiple threads simultaneously working together.

Here is the flow chart of the complete process: -

![alt text](https://github.com/gchandn3413/weather_data/blob/master/img_1.png)

# Limitations
1. Since the objective to present the approach, the script currently generates 10K lines of weather data and can be increased to a greater extent. 
2. The script currenlty parallelizes with 2 threads, however the number of threads can be increased depending upon the cores in the machine.
3. The location attribute is random picked from the list of the locations. The actual location could be different from the latitudes and longitudes. 

# Installation
There is an install_packages.sh script which installs the necessary packages. Essentionally, there are only 3 packages which are required apart from python 3.7.x which are - osgeo, shutil and glob2.

# Python Script Execution
Please execute the below command for weather generation script execution. The script is present in src directory.

python weather_generator.py -i <path_of_input_geo_tif_file> -o <location_of_output_weather_data_file>

# Testing the Weather generation script
For testing the script, python unit test framework has been implemented. The test script name is test_weather_generator.py. Edit this script to specify (1)the input location of geo tif file and (2) Output location of the weather data file.
There are 6 test methods which covers the overall testing for the weather generation script. Below are the ones:

1. test_linecount - This function is used to test the line count in the output file.
2. test_humidity - This function is used to test whether the humidity is in the specified range or not.
3. test_pressure - This function is used to test whether the pressure is in the specified range or not.
4. test_temperature - This function is used to test whether the temperature is in the specified range or not.
5. test_localtime - This function is used to test whether the localtime is in the specified range or not.
6. test_position - This function is used to test whether the position(lat & long) is in the specified range or not.

# Executing test script
Below is the command for executing the test script. The script is present in src directory.

python test_weather_generator.py
