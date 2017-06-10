"""
Note: Remember to start pigpio deamon using the command 'sudo pigpiod'
before running this code as this is needed to gain root access to GPIO pins.
This has to be done every time we restart the PI
"""

import pigpio
import DHT22
from time import sleep

# Intite GPIO for pigpio
pi = pigpio.pi()
# Setup the sensor
dht22 = DHT22.sensor(pi, 27) # use the actual GPIO pin name
dht22.trigger()

# We have sleep time above 2 seconds bcoz interval for DHT22 sensor to generate date is 2 secs
sleepTime = 3

def readDHT22():
    # Get a reading
    dht22.trigger()
    # save the data
    humidity = '%.2f' % (dht22.humidity())
    temperature = '%.2f' % (dht22.temperature())
    return (humidity, temperature)

sleep(sleepTime)

while True:
    humidity, temperature = readDHT22()
    print("Humidity:: " + humidity + "%")
    print("Temperature:: " + temperature + "*C")
    # print(humidity + "," + temperature)
    sleep(sleepTime)
