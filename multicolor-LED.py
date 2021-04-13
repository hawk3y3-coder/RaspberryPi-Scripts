import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)  # Reference pins by numerical position
#GPIO.setmode(GPIO.BCM)   # Reference pins by BCM label value

ledPins = [11,13,15]

for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)  #set pin as output

i = 1


try:
    while True:
        GPIO.output(11, GPIO.HIGH)   # Turn the pin on
        sleep(.6)
        GPIO.output(11, False)  # Turn the pin off
        #sleep(.6)
        GPIO.output(13, True)
        sleep(.6)
        GPIO.output(13, False)
        #sleep(.6)
        GPIO.output(15, True)
        sleep(.6)
        GPIO.output(15, False)
        sleep(.4)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        sleep(.6)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        sleep(.6)
        GPIO.output(15, True)   # Turn the pin on
        sleep(.6)
        GPIO.output(15, False)  # Turn the pin off
        #sleep(.6)
        GPIO.output(13, True)
        sleep(.6)
        GPIO.output(13, False)
        #sleep(.6)
        GPIO.output(11, True)
        sleep(.6)
        GPIO.output(11, False)
        sleep(.4)
        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        sleep(.6)
        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        sleep(.6)
        
        i = i+1

except KeyboardInterrupt:
    print "Cleaning up...\n"    
    GPIO.cleanup()   # Clear the state of all pins
    print "All clean :)"
