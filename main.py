import math
import numpy as np
import math
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Leg:
    def __init__(self, rel_angle, init_angle, origin, length, label):
        self.l_up = length[0]
        self.l_lo = length[1]
        self.origin = origin
        self.angle_x = rel_angle*(math.pi)/180
        self.angle_up = init_angle[0]
        self.angle_lo = init_angle[1]
        self.label = label

    def abs_cordinates(self, cog):
        the = self.angle_x
        rot_mat = np.array([[math.cos(the), -math.sin(the), 0],[math.sin(the), math.cos(the), 0],[0, 0, 1]])
        tra_mat = np.array([[self.origin[0]+cog[0]],[self.origin[1]+cog[1]],[self.origin[2]+cog[2]]])
        up_cord = self.get_up_cord(self.l_up, self.angle_up)
        up_cord = np.add(np.matmul(rot_mat, up_cord), tra_mat)
        low_cord = np.add(np.matmul(rot_mat, self.get_bel_cord()), tra_mat)
        origin_cord = tra_mat
        res_x = [origin_cord[0][0], up_cord[0][0], low_cord[0][0]]
        res_y = [origin_cord[1][0], up_cord[1][0], low_cord[1][0]]
        res_z = [origin_cord[2][0], up_cord[2][0], low_cord[2][0]]
        return (res_x, res_y, res_z, self.label)

    def get_up_cord(self, l, angle, z=0):
        return np.array([[l*math.cos(angle*math.pi/180)],[l*math.sin(angle*math.pi/180)],[z]])

    def get_bel_cord(self):
        return self.get_up_cord(self.l_up + self.l_lo*math.cos(self.angle_lo*math.pi/180), self.angle_up, -self.l_lo*math.sin(self.angle_lo*math.pi/180))

    def inc_up_angle(self, inc):
        # print
        self.angle_up+=inc

    def inc_below_angle(self, inc):
        self.angle_lo+=inc

class HexaPod:
    def __init__(self, cog, m, f, s, angles):
        self.cog = cog
        self.m = m
        self.f = f
        self.s = s
        self.f1 = Leg(45, (0, 70), (f, s, 0), (15, 15), "f1")
        self.f2 = Leg(135, (0, 70), (-f, s, 0), (15, 15), "f2")
        self.m1 = Leg(0, (0, 70), (m, 0, 0), (15, 15), "m1")
        self.m2 = Leg(180, (0, 70), (-m, 0, 0), (15, 15), "m2")
        self.b1 = Leg(315, (0, 70), (f, -s, 0), (15, 15), "b1")
        self.b2 = Leg(225, (0, 70), (-f, -s, 0), (15, 15), "b2")

    def get_polygon(self):
        x_cor = [self.m+self.cog[0], self.f+self.cog[0], -self.f+self.cog[0], -self.m+self.cog[0], -self.f+self.cog[0], self.f+self.cog[0], self.m+self.cog[0]]
        y_cor = [self.cog[1], self.s+self.cog[1], self.s+self.cog[1], self.cog[1], -self.s+self.cog[1], -self.s+self.cog[1], self.cog[1]]
        z_cor = [0, 0, 0, 0, 0, 0, 0]
        return (x_cor, y_cor, z_cor, "polygon")
    
    def get_cords(self):
        x_cor = []
        y_cor = []
        z_cor = []
        label = []
        pol_cor = self.get_polygon()
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.f1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.f2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.m1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.m2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.b1.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        pol_cor = self.b2.abs_cordinates(self.cog)
        x_cor.append(pol_cor[0])
        y_cor.append(pol_cor[1])
        z_cor.append(pol_cor[2])
        label.append(pol_cor[3])
        return (x_cor, y_cor, z_cor, label) 

    def simulate_tripod(self, inc, time):
        frames = []
        self.f1.inc_up_angle(inc/2)
        self.m2.inc_up_angle(inc/2)
        self.b1.inc_up_angle(inc/2)
        self.m1.inc_up_angle(inc/2)
        self.b2.inc_up_angle(inc/2)
        self.f2.inc_up_angle(inc/2)
        frames.append(self.get_cords())
        for i in range(time):
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(-inc/2)
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_below_angle(-inc)
            self.m2.inc_below_angle(-inc)
            self.b2.inc_below_angle(-inc)
            frames.append(self.get_cords())
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/2)
            self.b1.inc_up_angle(-inc/2)
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_below_angle(inc)
            self.m2.inc_below_angle(inc)
            self.b2.inc_below_angle(inc)
            frames.append(self.get_cords())
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f2.inc_up_angle(inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/2)
            self.f1.inc_up_angle(inc/2)
            self.m1.inc_below_angle(-inc)
            self.b1.inc_below_angle(-inc)
            self.f1.inc_below_angle(-inc)
            frames.append(self.get_cords())
            self.f2.inc_up_angle(inc/2)
            self.m1.inc_up_angle(inc/2)
            self.b2.inc_up_angle(inc/2)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/2)
            self.f1.inc_up_angle(inc/2)
            self.m1.inc_below_angle(inc)
            self.b1.inc_below_angle(inc)
            self.f1.inc_below_angle(inc)
            frames.append(self.get_cords())
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
        return frames 


class Plotter:
    @staticmethod
    def plot(points, clear = False):
        mpl.rcParams['legend.fontsize'] = 8
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
        # z = np.linspace(-2, 2, 100)
        # r = z**2 + 1
        # x = r * np.sin(theta)
        # y = r * np.cos(theta)
        # m = 10
        # f = 5
        # s = 15
        # p1 = [m, f, -f, -m, -f, f, m]
        # p2 = [0, s, s, 0, -s, -s, 0]
        # p3 = [0, 0, 0, 0, 0, 0, 0]
        # ax.plot(p1, p2, p3, label='parametric curve')
        # p1 = [0, 10]
        # p2 = [0, 10]
        # p3 = [0, 0]
        # ax.plot(p1, p2, p3, label='parametric curve')
        # ax.legend()

        # line_1  = plt.plot([1, 2, 3])
        # line_2  = plt.plot([2, 4, 6])
        # line = line_2.pop(0)
        # line.remove()
        # https://www.kite.com/python/answers/how-to-remove-a-line-from-a-plot-in-python
        for i in range(len(points[0])):
            px = points[0][i]
            py = points[1][i]
            pz = points[2][i]
            ax.plot(px, py, pz, label = points[3][i])
        ax.legend()
        plt.show()
        if clear:
            plt.close()

    def plot_frames(frames):
        mpl.rcParams['legend.fontsize'] = 8
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.legend()
        ax.set_xlim(-100, 100)
        ax.set_ylim(-20, 200)
        ax.set_zlim(-20, 5)
        ax.set_aspect('auto')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        handles = []
        colors = {0: 'b', 1: 'g', 2: 'r', 3: 'm', 4: 'c', 5: 'm', 6: 'r'}
        def get_frame(i):
            points = frames[i]
            if len(handles)>0:
                for j in handles:
                    j.remove()
            handles.clear()
            for i in range(len(points[0])):
                px = points[0][i]
                py = points[1][i]
                pz = points[2][i]
                temp, = ax.plot(px, py, pz, label = points[3][i], color=colors[i])
                handles.append(temp)
        a = anim.FuncAnimation(fig, get_frame, frames=80, repeat=True)
        plt.show()




if __name__ == "__main__":
    hex = HexaPod((0, 0, 0), 10, 5, 15, ())
    res = hex.get_cords()
    # print(res[3])
    stamps = hex.simulate_tripod(20, 20)
    # print(stamps)
    Plotter.plot_frames(stamps)
    # Plotter.plot(res)
    