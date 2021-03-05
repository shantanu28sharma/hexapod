import time
import math
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

kit.servo[0].set_pulse_width_range(650, 2500)
kit.servo[0].angle =90
#i=kit.servo[0].angle
#print(i)
kit.servo[1].set_pulse_width_range(600, 2250)
kit.servo[1].angle =90
#j=kit.servo[1].angle
#print(j)
kit.servo[2].set_pulse_width_range(700, 2300)
kit.servo[2].angle =90
kit.servo[3].set_pulse_width_range(750, 2350)
kit.servo[3].angle =90
kit.servo[4].set_pulse_width_range(880, 2050)
kit.servo[4].angle =90
#k=kit.servo[4].angle
#print(k)
kit.servo[5].set_pulse_width_range(800, 2350)
kit.servo[5].angle =90
kit.servo[6].set_pulse_width_range(800, 2250)
kit.servo[6].angle =90
kit.servo[7].set_pulse_width_range(750, 2450)
kit.servo[7].angle =90
kit.servo[8].set_pulse_width_range(700, 2400)
kit.servo[8].angle =90
#l=kit.servo[8].angle
#print(l)
kit.servo[9].set_pulse_width_range(750, 2300)
kit.servo[9].angle =90
kit.servo[10].set_pulse_width_range(650, 2250)
kit.servo[10].angle =90