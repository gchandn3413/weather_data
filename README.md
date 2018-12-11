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

![alt text](https://github.com/gchandn3413/weather_data/blob/master/img.png)
