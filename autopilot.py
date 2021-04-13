import RPi.GPIO as gpio
from time import sleep,time
#from Tkinter import *
from distance import distance_front, distance_rear
import random


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(13, gpio.OUT)    # Yellow wire
    gpio.setup(15, gpio.OUT)    # Green wire
    gpio.setup(16, gpio.OUT)    # Red wire
    gpio.setup(18, gpio.OUT)    # Brown wire

def forward(tf):            # tf = time frame for action
    init()
    gpio.output(16, True)   # Turn wheels straight forward
    gpio.output(18, True)   #

    gpio.output(13, True)   # Roll wheels forward
    gpio.output(15, False)  #

    sleep(tf)
    gpio.cleanup()


def reverse(tf):            # tf = time frame for action
    init()
    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)
    gpio.cleanup()

def right(tf):              # tf = time frame for action
    init()
    gpio.output(16, True)   # Turn wheels to the right
    gpio.output(18, False)  #

    gpio.output(13, True)   # Roll wheels forward
    gpio.output(15, False)  #

    sleep(tf)
    gpio.cleanup()

def left(tf):               # tf = time frame for action
    init()
    gpio.output(16, False)  # Turn wheels to the left
    gpio.output(18, True)   #

    gpio.output(13, True)   # Roll wheels forward
    gpio.output(15, False)  #

    sleep(tf)
    gpio.cleanup()

def revright(tf):           # tf = time frame for action
    init()
    gpio.output(16, True)   # Turn wheels to the right
    gpio.output(18, False)  #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)

    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #
    gpio.cleanup()

def revleft(tf):            # tf = time frame for action
    init()
    gpio.output(16, False)  # Turn wheels to the left
    gpio.output(18, True)   #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)

    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #
    gpio.cleanup()


#action = random.randrange(1, 6+1)
#print action
#print int(time()) % 6


tf = 0.03
action_list = [ forward, reverse, left, right, revleft, revright ]

#action = int(time()) % 6
#print action
#action_list[action](tf)

try:
    while True:
        
        action = int(time()) % 6        # pick a random action

        if action in (0,2,3):           # forward moving actions
            curDis = distance_front()
            i = 0
            while curDis > 30 and i < 30:   # repeat action until time or distance limit
                action_list[action](tf)
                curDis = distance_front()
                i = i + 1

            if curDis < 30:     # move backward if distance less than 30 cm
                reverse(.5)

        if action in (1,4,5):           # backwards moving actions
            curDis_rear = distance_rear()
            i = 0
            while curDis_rear > 30 and i < 30: # repeat action until time or distance limit
                action_list[action](tf)
                curDis_rear = distance_rear()
                i = i + 1

            if curDis_rear < 30:    # move forward if distance less than 30 cm
                forward(.5)
            


except KeyboardInterrupt:
    gpio.cleanup()



