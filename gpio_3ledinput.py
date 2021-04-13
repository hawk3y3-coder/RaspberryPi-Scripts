import RPi.GPIO as GPIO
from time import sleep

#GPIO.setmode(GPIO.BOARD)  # Reference pins by numerical position
GPIO.setmode(GPIO.BCM)   # Reference pins by BCM label value

ledPins = [17,27,22]
buttonPin = 6

for pin in ledPins:
    GPIO.setup(pin, GPIO.OUT)  #set pin as output

GPIO.setup(buttonPin, GPIO.IN)

currentLed = 0
i = 0

while i <= 25:
#while True:
    pin = ledPins[currentLed]
    GPIO.output(pin, True)
    buttonPress = not GPIO.input(buttonPin)
    #print buttonPress
    print GPIO.input(buttonPin)
    if buttonPress == True:        # If button is pressed, turn off current
        GPIO.output(pin, False)     # led and turn on the next one
        if currentLed == 2:
            currentLed = 0
            i += 1
        else:
            currentLed += 1
            i += 1
        #print "i = ", i
        sleep(0.2)
    
GPIO.cleanup()   # Clear the state of all pins

