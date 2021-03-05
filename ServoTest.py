import time
import math
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
ti=time.time()
print(ti)
kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[2].angle = 90
kit.servo[3].angle = 90
kit.servo[4].angle = 90
kit.servo[5].angle = 90
kit.servo[6].angle = 90
kit.servo[7].angle = 90


time.sleep(1)
while 1==1:
    t=time.time()
    crt_time=t-ti
    theta=90 + (30*math.sin(4*t))
    theta_dash=90 - (30*math.sin(4*t))
    #wmax=3.7 rad/s
    kit.servo[0].angle =theta
    kit.servo[1].angle =theta
    kit.servo[2].angle =theta_dash
    kit.servo[3].angle =theta_dash
    kit.servo[4].angle =theta
    kit.servo[5].angle =theta
    kit.servo[6].angle =theta_dash
    kit.servo[7].angle =theta_dash
    print(theta)
    time.sleep(0.1)
    pass
