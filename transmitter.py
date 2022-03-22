# Write your code here :-)
from microbit import *
import radio
import utime
radio.config(group=23)
radio.on()

while True:
    radio.send(str(temperature())+'A')
    utime.sleep(30)
