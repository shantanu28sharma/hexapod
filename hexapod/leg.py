import math
import numpy as np

class Leg:
    def __init__(self, number, kit, index, label, init_angle, length, origin):
        self.l_up = length[0]
        self.l_lo = length[1]
        self.origin = origin
        self.label = label
        self.angle_x = number*45*(math.pi)/180
        self.angle_up = init_angle[0]
        self.angle_lo = init_angle[1]
        self.pin1 = number*2
        self.pin2 = number*2+1
        self.kit = kit
        self.index = index
        self.disable = False

    def _disable(self):
        self.inc_below_angle(-50)
        self.disable = True
    
    def _enable(self):
        self.inc_below_angle(50)
        self.disable = False
    
    def inc_up_angle(self, inc):
        if self.disable:
            return
        self.angle_up += inc
        self.angle_up = max(self.angle_up, 0)
        self.angle_up = min(self.angle_up, 180)
        self.kit.servo[self.pin1].angle = self.angle_up
    
    def inc_below_angle(self, inc):
        if self.disable:
            return
        self.angle_lo += inc
        self.angle_lo = max(self.angle_lo, 0)
        self.angle_lo = min(self.angle_lo, 180)
        self.kit.servo[self.pin2].angle = self.angle_lo
    
    def abs_cordinates(self, cog):
        the = self.angle_x
        rot_mat = np.array([[math.cos(the), -math.sin(the), 0], [math.sin(the), math.cos(the), 0], [0, 0, 1]])
        tra_mat = np.array([[self.origin[0]+cog[0]], [self.origin[1]+cog[1]], [self.origin[2]+cog[2]]])
        up_cord = self.get_up_cord(self.l_up, self.angle_up)
        up_cord = np.add(np.matmul(rot_mat, up_cord), tra_mat)
        low_cord = np.add(np.matmul(rot_mat, self.get_bel_cord()), tra_mat)
        origin_cord = tra_mat
        res_x = [origin_cord[0][0], up_cord[0][0], low_cord[0][0]]
        res_y = [origin_cord[1][0], up_cord[1][0], low_cord[1][0]]
        res_z = [origin_cord[2][0], up_cord[2][0], low_cord[2][0]]
        return [res_x, res_y, res_z, self.label]

    def get_up_cord(self, l, angle, z=0):
        return np.array([[l*math.cos(angle*math.pi/180)], [l*math.sin(angle*math.pi/180)], [z]])

    def get_bel_cord(self):
        return self.get_up_cord(self.l_up + self.l_lo*math.cos(self.angle_lo*math.pi/180), self.angle_up, -self.l_lo*math.sin(self.angle_lo*math.pi/180))

    def calc_inv(self, height):
        self.angle_lo = math.asin(height/self.l_lo)    