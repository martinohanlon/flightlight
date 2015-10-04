import RPi.GPIO as GPIO
import argparse

from flightdata import FlightData
from haversine import points2distance
from time import sleep

#pin of the LED to light
LEDPIN = 17

class LED():
    def __init__(self, ledPin):
        self.ledPin = ledPin
        GPIO.setup(ledPin, GPIO.OUT)

    def on(self):
        GPIO.output(self.ledPin, True)

    def off(self):
        GPIO.output(self.ledPin, False)

#read command line options
parser = argparse.ArgumentParser(description="PiAware Flight Light")
parser.add_argument("lat", type=float, help="The latitude of the receiver")
parser.add_argument("lon", type=float, help="The longitude of the receiver")
parser.add_argument("range", type=int, help="The range in km for how close an aircraft should be to turn on the led")
args = parser.parse_args()

#get the flight data
myflights = FlightData()

#set GPIO mode
GPIO.setmode(GPIO.BCM)

try:

    #create LED
    led = LED(LEDPIN)

    #loop forever
    while True:
        
        plane_in_range = False

        #loop through the aircraft and see if one is in range
        for aircraft in myflights.aircraft:
            if aircraft.validposition == 1:
                startpos = ((args.lat, 0, 0), (args.lon, 0, 0))
                endpos = ((aircraft.lat, 0, 0), (aircraft.lon, 0, 0))
                distance = points2distance(startpos, endpos)
                #debug
                #print(distance)
                if distance <= args.range:
                    plane_in_range = True

        #turn the led on / off
        if plane_in_range:
            led.on()
            #print("on")
        else:
            led.off()
            #print("off")
            
        sleep(1)

        #refresh the data
        myflights.refresh()

finally:
    #tidy up GPIO
    GPIO.cleanup()
