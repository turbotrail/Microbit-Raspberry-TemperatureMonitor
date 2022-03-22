from microbit import *
import radio

radio.config(group=23)
radio.on()
outdoorTemp = "-"

while True:
    message = radio.receive()
    if message:
        outdoorTemp = message
        print("(" + str(outdoorTemp) + ")")