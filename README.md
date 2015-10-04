#Piaware Flight Light
##Martin O'Hanlon (martin@ohanlonweb.com)
##http://www.stuffaboutcode.com

##Description
A python 3 program which will turn on an LED if an aircraft is detected overhead using [PiAware](http://flightaware.com/adsb/piaware)

[http://www.stuffaboutcode.com/2015/10/piaware-aircraft-overhead-led.html](http://www.stuffaboutcode.com/2015/10/piaware-aircraft-overhead-led.html)

##Structure
* flightdata 
  * flightdata.py - the flightdata python module
  * haversine.py - a module for calculating the distance between GPS coords
  * flightlight.py - main program
* docs - about the project

##Usage

Launch the flightlight program passing the latitude (lat) and longitude (lon) of your PiAware station and the range that should be used to detect if an aircraft is overhead. 

    usage: flightlight.py [-h] lat lon range

##Version history
* 0.1 - Initial stable version

