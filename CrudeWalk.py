import time
import math
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
#Setting pulse width range for all servos and setting them to its initial mean position
kit = ServoKit(channels=16)
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
#while 1==1:
    
kit.servo[1].angle = 30
kit.servo[0].angle = 150
time.sleep(0.2)
kit.servo[1].angle = 90
    #wmax=3.7 rad/s

time.sleep(1)
kit.servo[3].angle = 150
kit.servo[2].angle = 30
time.sleep(0.2)
kit.servo[3].angle = 90

time.sleep(1)
kit.servo[5].angle = 150
kit.servo[4].angle = 150
time.sleep(0.2)
kit.servo[5].angle = 90
    #wmax=3.7 rad/s

time.sleep(1)
kit.servo[7].angle = 30
kit.servo[6].angle = 30
time.sleep(0.2)
kit.servo[7].angle = 90
#all legs went forward____________________________
#Now reverse time
time.sleep(1)
kit.servo[1].angle = 30
kit.servo[0].angle = 30
time.sleep(0.4)
kit.servo[1].angle = 90
    #wmax=3.7 rad/s

time.sleep(1)
kit.servo[3].angle = 150
kit.servo[2].angle = 150
time.sleep(0.4)
kit.servo[3].angle = 90

time.sleep(1)
kit.servo[5].angle = 150
kit.servo[4].angle = 30
time.sleep(0.4)
kit.servo[5].angle = 90
    #wmax=3.7 rad/s

time.sleep(1)
kit.servo[7].angle = 30
kit.servo[6].angle = 150
time.sleep(0.4)
kit.servo[7].angle = 90


