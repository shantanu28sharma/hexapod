from evdev import InputDevice, categorize, ecodes
import time
import math
from adafruit_servokit import ServoKit

lastcomm=int(0)
#defining servo controller board PCA9685 i.e. 16 channel servokit = ServoKit(channels=16)
kit = ServoKit(channels=16)
def ReStart():
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
    lastcomm=0
    pass

#---------------------------------------------------------------
#        Defining Move Functions
#---------------------------------------------------------------

def moveforward():
    # Move/Walk Forward
    #leg 4 lift->forward -> Drop
    kit.servo[5].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90

    #leg 2 lift->forward -> Drop
    kit.servo[1].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90

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
    time.sleep(0.4)
    
    #leg 3 lift->forward -> Drop
    kit.servo[7].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90

    #leg 1 lift->forward -> Drop
    kit.servo[3].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
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
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 90+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 90+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    lastcomm=1
    pass

def moveforward2():
    # Move/Walk Forward
    #leg 4 lift->forward -> Drop
    kit.servo[9].angle = 100
    kit.servo[10].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[9].angle = 90
#    kit.servo[5].angle = 90
    kit.servo[10].angle = 90

    #leg 2 lift->forward -> Drop
#    kit.servo[1].angle = 110
    kit.servo[10].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90
#    kit.servo[1].angle = 90
    kit.servo[10].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=0 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
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
    time.sleep(0.4)
    
    #leg 3 lift->forward -> Drop
#    kit.servo[7].angle = 110
    kit.servo[9].angle = 100
    kit.servo[10].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
#    kit.servo[7].angle = 90
    kit.servo[10].angle = 90
    kit.servo[9].angle = 90

    #leg 1 lift->forward -> Drop
#    kit.servo[3].angle = 70
    kit.servo[10].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
#    kit.servo[3].angle = 90
    kit.servo[10].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=0 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 90+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 90+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    lastcomm=1
    pass

def movebackward():
    # Move/Walk Backward
    #leg 2 lift->Backward -> Drop
    kit.servo[1].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 150
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
        
    #leg 4 lift->Backward -> Drop
    kit.servo[5].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 150
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90
    
    
    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=0 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
        kit.servo[0].angle = 90+math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 150-math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 90+math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 150-math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    #leg 3 lift->backward -> Drop
    kit.servo[7].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 30
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90

    #leg 1 lift->backward -> Drop
    kit.servo[3].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 30
    time.sleep(0.4)
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=0 # distance from X that has to be maintained suring straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
        kit.servo[0].angle = 30+math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 90-math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 30+math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 90-math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    lastcomm=2
    pass

def moveleft():
    pass

def moveright():
    
    pass 

def turnleft():
    #leg 2 lift->forward -> Drop
    kit.servo[1].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
    
    #leg 4 lift->forward -> Drop
    kit.servo[5].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90

    #leg 1 lift->backward -> Drop
    kit.servo[3].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 30
    time.sleep(0.4)
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90

    #leg 3 lift->backward -> Drop
    kit.servo[7].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 30
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90
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
        kit.servo[0].angle = 30+math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 30+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 30+math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 30+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    lastcomm=3
    pass

def turnright():
    #leg 1 lift->forward -> Drop
    kit.servo[3].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90

    #leg 3 lift->forward -> Drop
    kit.servo[7].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90
    
    #leg 2 lift->Backward -> Drop
    kit.servo[1].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 150
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90  
        
    #leg 4 lift->Backward -> Drop
    kit.servo[5].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 150
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90
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
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 150-math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 150-math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    lastcomm=4
    pass   

#---------------------------------------------------------------
#        Defining Moves while climbing Functions
#---------------------------------------------------------------

def climbUpward():
    # Climb Upward
    # I will have to save the breadth of the trunk or I can give minimum Angle so that it will exert maximum torque
    
    #leg 1 lift->forward -> Drop
    kit.servo[3].angle = 70
    kit.servo[1].angle = 30
    kit.servo[0].angle = 150
    time.sleep(0.4)
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90

    #leg 2 lift->forward -> Drop
    kit.servo[1].angle = 110
    kit.servo[3].angle = 150
    kit.servo[2].angle = 30
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
    
    #leg 3 lift->forward -> Drop
    kit.servo[7].angle = 110
    kit.servo[5].angle = 150
    kit.servo[4].angle = 150
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90

    #leg 4 lift->forward -> Drop
    kit.servo[5].angle = 70
    kit.servo[7].angle = 30
    kit.servo[6].angle = 30
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained during straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
        kit.servo[0].angle = 150-math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 30+math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 150-math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 30+math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    pass

def climbDownward():
    # Climb Upward
    # I will have to save the breadth of the trunk or I can give minimum Angle so that it will exert maximum torque
    
    #leg 3 lift->Downward -> Drop
    kit.servo[7].angle = 70
    kit.servo[5].angle = 150
    time.sleep(0.1)
    kit.servo[4].angle = 30
    time.sleep(0.4)
    kit.servo[5].angle = 90
    kit.servo[7].angle = 90

    #leg 4 lift->Downward -> Drop
    kit.servo[5].angle = 110
    kit.servo[7].angle = 30
    kit.servo[6].angle = 150
    time.sleep(0.4)
    kit.servo[7].angle = 90
    kit.servo[5].angle = 90

    #leg 1 lift->Downward -> Drop
    kit.servo[3].angle = 110
    kit.servo[1].angle = 30
    time.sleep(0.1)
    kit.servo[0].angle = 30
    time.sleep(0.4)
    kit.servo[1].angle = 90
    kit.servo[3].angle = 90

    #leg 2 lift->Downward -> Drop
    kit.servo[1].angle = 70
    kit.servo[3].angle = 150
    kit.servo[2].angle = 150
    time.sleep(0.4)
    kit.servo[3].angle = 90
    kit.servo[1].angle = 90
      

    # All legs move forward While in contact with ground,  i.e. body moves forward
    # Constant speed ground stroke
    w= 2  #2rad/s=2*180/pi
    th1_c= 0 #initial Th_1
    th1_cmd=60 #Commanded Backward Stroke angle in degrees
    X_dis=23 # distance from X that has to be maintained during straight backstroke
    l1=46 #mm
    l2=137.44 #mm
    dt=0.01 #s -time step for fine actuation
    while th1_c <math.radians(th1_cmd) :
        th1=th1_c + w*dt
        th2=math.asin((X_dis/l2)+((l1/l2)*math.cos(th1)))
        #bodymove stroke
        kit.servo[0].angle = 30+math.degrees(th1)
        kit.servo[1].angle=90-math.degrees(th2)
        kit.servo[2].angle = 150-math.degrees(th1)
        kit.servo[3].angle=90+math.degrees(th2)
        kit.servo[4].angle = 30+math.degrees(th1)
        kit.servo[5].angle=90+math.degrees(th2)
        kit.servo[6].angle = 150-math.degrees(th1)
        kit.servo[7].angle=90-math.degrees(th2)
        th1_c=th1
        time.sleep(0.01)
        pass
    pass

def rotateLeft():
    pass

def rotateRight():
    pass

def main():
    ReStart()
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
    selBtn = 314
    startBtn = 315
    
    oBtn=305
    squareBtn=308
    triangleBtn=307
    xBtn=304

    L1btn=310
    R1btn=311

    #affiche les codes interceptes |  display codes
    for event in gamepad.read_loop():
        #Boutons | buttons 
        if event.type == ecodes.EV_KEY:
            #print(event)
            if event.value == 1:
                if event.code == frwdBtn:
                    print("Forward")
                    moveforward2()

                elif event.code == bkwdBtn:
                    print("Backward")
                    movebackward()

                elif event.code == lftBtn:
                    print("move left")
                    turnleft()
                
                elif event.code == rgtBtn:
                    print("move right")
                    turnright()
                
                elif event.code == triangleBtn:
                    print("Climb Upward")
                    climbUpward()
                
                elif event.code == xBtn:
                    print("Climb Downward")
                    climbDownward()
                
                elif event.code == L1btn:
                    if kit.servo[1].angle>=0 and kit.servo[1].angle<=180 and kit.servo[3].angle>=0 and kit.servo[3].angle<=180:
                        kit.servo[1].angle=kit.servo[1].angle+10
                        kit.servo[3].angle=kit.servo[3].angle-10
                        pass
                elif event.code == R1btn:
                    if kit.servo[7].angle>=0 and kit.servo[7].angle<=180 and kit.servo[5].angle>=0 and kit.servo[5].angle<=180:
                        kit.servo[5].angle=kit.servo[5].angle-10
                        kit.servo[7].angle=kit.servo[7].angle+10
                        pass

                elif event.code == selBtn:
                    print("Select")
                elif event.code == startBtn:
                    print("ReStart")
                    ReStart()
            elif event.value == 0:
              print("Release")
        #Gamepad analogique | Analog gamepad
        elif event.type == ecodes.EV_ABS:
            absevent = categorize(event)
            #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
            if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":#L2
                 print("L1btn: Release the Front Grip")
                 kit.servo[1].angle =30
                 kit.servo[3].angle =150
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ": #R2
                 print("R1btn: Release the Rear Grip")
                 kit.servo[5].angle =150
                 kit.servo[7].angle =30

            # Incremental Spine Movement
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                 if absevent.event.value<127:
                    tempangle=kit.servo[8].angle+5
                    if tempangle>=0 and tempangle<=180:
                        kit.servo[8].angle=tempangle
                 elif absevent.event.value>127:
                    tempangle=kit.servo[8].angle-5
                    if tempangle>=0 and tempangle<=180:
                        kit.servo[8].angle=tempangle
                 elif absevent.event.value == 127:
                    print("Hold position")
                    pass
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                 if absevent.event.value <127:
                    tempangle=kit.servo[9].angle-5
                    if tempangle>=0 and tempangle<=180:
                        kit.servo[9].angle=tempangle
                 elif absevent.event.value >127:
                     tempangle=kit.servo[9].angle+5
                     if tempangle>=0 and tempangle<=180:
                         kit.servo[9].angle=tempangle
                 elif absevent.event.value == 127:
                    print("Hold position")            
                    pass
            elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RX":
                 if absevent.event.value<127:
                    tempangle=kit.servo[10].angle-5
                    if tempangle>=0 and tempangle<=180:
                        kit.servo[10].angle=tempangle
                 elif absevent.event.value>127:
                    tempangle=kit.servo[10].angle+5
                    if tempangle>=0 and tempangle<=180:
                        kit.servo[10].angle=tempangle
                 elif absevent.event.value == 127:
                    print("Hold position")
                    pass
    pass

if __name__ == '__main__':
    main()
#Implementation code