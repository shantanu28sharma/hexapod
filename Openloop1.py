from evdev import InputDevice, categorize, ecodes
import time
import math
from adafruit_servokit import ServoKit

def moveforward():
    # Move/Walk Forward
    #leg 4 lift->forward -> Drop
    time.sleep(1)
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.2)
    kit.servo[7].angle = 90

    #leg 2 lift->forward -> Drop
    time.sleep(1)
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.2)
    kit.servo[3].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    #2&4 to mean, 1&3 to RM
    time.sleep(1)
    #kit.servo[1].angle = 30
    kit.servo[0].angle = 30
    #kit.servo[3].angle = 150
    kit.servo[2].angle = 90
    #kit.servo[5].angle = 150
    kit.servo[4].angle = 30
    #kit.servo[7].angle = 30
    kit.servo[6].angle = 90
    time.sleep(0.4)

    #leg 3 lift->forward -> Drop
    time.sleep(1)
    kit.servo[5].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.2)
    kit.servo[5].angle = 90
        #wmax=3.7 rad/s

    #leg 1 lift->forward -> Drop
    kit.servo[1].angle = 30
    kit.servo[0].angle = 150
    time.sleep(0.2)
    kit.servo[1].angle = 90
        #wmax=3.7 rad/s

    # All legs move forward While in contact with ground, i.e. body moves forward
    time.sleep(1)
    #kit.servo[1].angle = 30
    kit.servo[0].angle = 90
    #kit.servo[3].angle = 150
    kit.servo[2].angle = 150
    #kit.servo[5].angle = 150
    kit.servo[4].angle = 90
    #kit.servo[7].angle = 30
    kit.servo[6].angle = 150
    time.sleep(0.4)
    pass

#defining servo controller board PCA9685 i.e. 16 channel servokit = ServoKit(channels=16)
kit = ServoKit(channels=16)
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
#Setting pulse width range for all servos and setting them to its initial mean position
kit.servo[0].set_pulse_width_range(700, 2500)
kit.servo[0].angle =90
kit.servo[1].set_pulse_width_range(650, 2350)
kit.servo[1].angle =90
kit.servo[2].set_pulse_width_range(700, 2300)
kit.servo[2].angle =90
kit.servo[3].set_pulse_width_range(750, 2350)
kit.servo[3].angle =90
kit.servo[4].set_pulse_width_range(880, 2050)
kit.servo[4].angle =90
kit.servo[5].set_pulse_width_range(800, 2350)
kit.servo[5].angle =90
kit.servo[6].set_pulse_width_range(800, 2250)
kit.servo[6].angle =90
kit.servo[7].set_pulse_width_range(750, 2450)
kit.servo[7].angle =90
kit.servo[8].set_pulse_width_range(700, 2400)
kit.servo[8].angle =90
kit.servo[9].set_pulse_width_range(750, 2300)
kit.servo[9].angle =90
kit.servo[10].set_pulse_width_range(650, 2250)
kit.servo[10].angle =90
time.sleep(1)

# creates object gamepad
gamepad = InputDevice('/dev/input/event1')

# prints out device info at start
print(gamepad)

# define codes of the remote controllers
# Ground Movement
frwdBtn = 544
bkwdBtn = 545
lftBtn = 546
rgtBtn = 547

lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == frwdBtn:
                print("Forward")
                moveforward()

            elif event.code == bkwdBtn:
                print("Backward")
                movebackward()

            elif event.code == lftBtn:
                print("Left")
                moveleft()
            
            elif event.code == rgtBtn:
                print("Right")
                moveright()


            elif event.code == lBtn:
                print("LEFT")
            elif event.code == rBtn:
                print("RIGHT")
            elif event.code == selBtn:
                print("Select")
            elif event.code == staBtn:
                print("Start")
        elif event.value == 0:
          print("Relache | Release")

    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             if absevent.event.value == 0:
                print("Left")
             elif absevent.event.value == 255:
                print("Right")
             elif absevent.event.value == 127:
                print("Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == 0:
                print("Up")
             elif absevent.event.value == 255:
                print("Down")
             elif absevent.event.value == 127:
                print("Center")