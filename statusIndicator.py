#!/usr/bin/python

import sys
import RPi.GPIO as GPIO # Import GPIO library - access to the pi pins
import time # Import time library. Allows us to use sleep

# Device states'
READY_TO_CONNECT = "READY_TO_CONNECT"
DEVICE_CONNECTED = "DEVICE_CONNECTED"
DEVICE_DISCONNECTED = "DEVICE_DISCONNECTED"
TRANSFER_IN_PROGRESS = "TRANSFER_IN_PROGRESS"
TRANSFER_COMPLETE = "TRANSFER_COMPLETE"

# Output pins
SPEAKER_PIN = 22
LED_PIN = 0

# Set up 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SPEAKER_PIN, GPIO.OUT) # set 15 to be output for speaker

# DEBUG PRINTS FOR ERORR CHECKS
print 'Number of arguments passed: ', len(sys.argv)
print 'Argument List: ', str(sys.argv)
print 'Arguement passed - should be a status indicator: ', sys.argv[1]

def dockReady():
	print 'Dock is powered on and waiting for connection with device'
	startLED();
	return

def deviceConnected():
	print 'device connected...'
	playSound();
	return

def deviceDisconnected():
	print 'device has been disconnected...'
	playSound();
	startLED();
	return

def transferringData():
	print 'data is being transferred from the device'
	blinkLED();
	return

def transferringComplete():
	print 'Transfer of data is complete'
	stopLED();
	return

def blinkLED():
	numTimes = 100
	blinkSpeed = 0.5
	for i in range(0,numTimes):
		print "Iteration " + str(i+1)
		GPIO.output(LED_PIN,True)
		time.sleep(blinkSpeed)
		GPIO.output(LED_PIN,False)
		time.sleep(blinkSpeed)
	GPIO.cleanup()
	return

def startLED():
	GPIO.output(LED_PIN,True)
	return

def stopLED():
	GPIO.output(LED_PIN,False)
	return

def playSound():
	GPIO.output(SPEAKER_PIN, True)
	sleep(1)
	GPIO.output(SPEAKER_PIN, False)
	GPIO.cleanup()
	return

if (str(sys.argv[1]) == READY_TO_CONNECT) : dockReady();:
elif (str(sys.argv[1]) == DEVICE_CONNECTED) : deviceConnected();
elif (str(sys.argv[1]) == TRANSFER_IN_PROGRESS) : transferringData();
elif (str(sys.argv[1]) == TRANSFER_COMPLETE) : transferringComplete();
elif (str(sys.argv[1]) == DEVICE_DISCONNECTED) : deviceDisconnected();
