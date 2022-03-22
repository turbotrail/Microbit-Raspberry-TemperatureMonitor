# Microbit-Raspberry-TemperatureMonitor
Simple project to monitor temperature using Raspberry pi and BBC microbits and store and visualize data using Mongo cloud free tier


===============================================================================

Hardware used:

1. Raspberry Pi running raspbian image (Desktop with remote enabled)
2 . Three BBC microbit (1 master connected to raspberry pi using microusb) and (2 slaves in different rooms transmitting temp data battery powered)
note: Microbit should have micropython configured . You can use Mu editor for programming and writing code to microbit

--------------------------------------------------------------------------------

Software :

transmitter.py - running on the slave microbit with appended Meta data to represent the different rooms

masterReceiver.py - running on the master microbit connected to Raspberry pi using microUSB for serial communication

mongoPush.py - running on the Raspberry pi listening to the serial output from the master microbit and parsing the data - then caching it in a local CSV with respect to the Meta identifiers and also pushing data to Mongo cloud database (Using mongo cloud db setup Free tier)

=================================================================================

Please raise issues for any queries!

Happy Problem solving!
