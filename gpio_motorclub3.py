import RPi.GPIO as gpio
from time import sleep
from Tkinter import *
from distance import distance, distance_rear


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
    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)
    gpio.cleanup()

def right(tf):              # tf = time frame for action

    gpio.output(16, True)   # Turn wheels to the right
    gpio.output(18, False)  #

    gpio.output(13, True)   # Roll wheels forward
    gpio.output(15, False)  #

    sleep(tf)
    gpio.cleanup()

def left(tf):               # tf = time frame for action
 
    gpio.output(16, False)  # Turn wheels to the left
    gpio.output(18, True)   #

    gpio.output(13, True)   # Roll wheels forward
    gpio.output(15, False)  #

    sleep(tf)
    gpio.cleanup()

def revright(tf):           # tf = time frame for action

    gpio.output(16, True)   # Turn wheels to the right
    gpio.output(18, False)  #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)

    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #
    gpio.cleanup()

def revleft(tf):            # tf = time frame for action

    gpio.output(16, False)  # Turn wheels to the left
    gpio.output(18, True)   #

    gpio.output(13, False)  # Roll wheels backward
    gpio.output(15, True)   #

    sleep(tf)

    gpio.output(16, True)   # Turn wheels straight
    gpio.output(18, True)   #
    gpio.cleanup()

def key_input(event):
    init()
    print 'Key: ', event.char
    key_press = event.char
    sleep_time = 0.03

    if key_press.lower() == 'e':
        forward(sleep_time)
    elif key_press.lower() == 'x':
        reverse(sleep_time)
    elif key_press.lower() == 's':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)
    elif key_press.lower() == 'z':
        revleft(sleep_time)
    elif key_press.lower() == 'c':
        revright(sleep_time)
    else:
        gpio.cleanup()

    currentDist = distance()
    currentDist_rear = distance_rear()
    
    #print('currentDist is ', currentDist)
    #print('currentDist rear is ', currentDist_rear)

    if currentDist < 30:
        init()
        reverse(.5)

    if currentDist_rear < 30:
        init()
        forward(.5)

command = Tk()
command.bind('<KeyPress>', key_input)

tf = 1
bt = Button(text="Press my button", command=lambda: forward(tf))
bt.pack()
command.mainloop()

