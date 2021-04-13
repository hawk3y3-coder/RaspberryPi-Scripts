import RPi.GPIO as gpio
from time import sleep, time


def distance_front(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(38, gpio.OUT)    # Orange wire
    gpio.setup(40, gpio.IN)     # Yellow wire

    gpio.output(38, False)  # Clear the state

    sig = 0
    nosig = 0

    while gpio.input(40) == 0:
        nosig = time()

    while gpio.input(40) == 1:
        sig = time()

    tl = sig - nosig  # time that has passed

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    return distance

def distance_rear(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(35, gpio.OUT)    # Green wire
    gpio.setup(37, gpio.IN)     # Gray wire

    gpio.output(35, False)  # Clear the state

    sig = 0
    nosig = 0

    while gpio.input(37) == 0:
        nosig = time()

    while gpio.input(37) == 1:
        sig = time()

    tl = sig - nosig  # time that has passed

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('improper choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    return distance

#try:
#    while True:
        #print( distance() )
        #print( distance_rear() )

#except:
#    gpio.cleanup()
