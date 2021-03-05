import time
import math
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

kit.servo[0].angle =90
kit.servo[1].angle =90
kit.servo[2].angle =90
kit.servo[3].angle =90
kit.servo[4].angle =90
kit.servo[5].angle =90
kit.servo[6].angle =90
kit.servo[7].angle =90
kit.servo[8].angle =90
kit.servo[9].angle =90
kit.servo[10].angle =90
kit.servo[11].angle =150