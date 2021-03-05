from evdev import InputDevice, categorize, ecodes
import time
import math
from adafruit_servokit import ServoKit

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

#---------------------------------------------------------------
#        Defining Move Functions
#---------------------------------------------------------------

def moveforward():
    # Move/Walk Forward
    #leg 4 lift->forward -> Drop
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90

    #leg 2 lift->forward -> Drop
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
#        print(math.degrees(th1))
#        print(math.degrees(th2))
#        print("--ts fin--")
        kit.servo[0].angle = 90-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 30+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 90-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 30+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
#    print("first half finished \n")
    time.sleep(0.4)
    #leg 3 lift->forward -> Drop
    kit.servo[5].angle = 150
    time.sleep(0.1)
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
        #wmax=3.7 rad/s

    #leg 1 lift->forward -> Drop
    kit.servo[1].angle = 30
    time.sleep(0.1)
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
        #wmax=3.7 rad/s

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
#        print(math.degrees(th1))
#        print(math.degrees(th2))
#        print("--ts fin--")
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        #print('Servo 0: ' + str(150-math.degrees(th1)) )
        kit.servo[2].angle = 90+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        #print('Servo 4: ' + str(150-math.degrees(th1)) )
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 90+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass

    pass

def movebackward():
    # Move/Walk Backward
    #leg 4 lift->forward -> Drop
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90

    #leg 2 lift->forward -> Drop
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=-60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
#        print(math.degrees(th1))
#        print(math.degrees(th2))
#        print("--ts fin--")
        kit.servo[0].angle = 90-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 30+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 90-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 30+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
#    print("first half finished \n")
    time.sleep(0.4)
    #leg 3 lift->forward -> Drop
    kit.servo[5].angle = 150
    time.sleep(0.1)
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
        #wmax=3.7 rad/s

    #leg 1 lift->forward -> Drop
    kit.servo[1].angle = 30
    time.sleep(0.1)
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
        #wmax=3.7 rad/s

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
#        print(math.degrees(th1))
#        print(math.degrees(th2))
#        print("--ts fin--")
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        #print('Servo 0: ' + str(150-math.degrees(th1)) )
        kit.servo[2].angle = 90+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        #print('Servo 4: ' + str(150-math.degrees(th1)) )
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 90+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    pass

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
                print("ReStart")
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

        elif event.value == 0:
          print("Release")

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