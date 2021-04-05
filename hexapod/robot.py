from leg import Leg

class Robot:
    def __init__(self, cog, m, f, s):
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
        self.functional = [True]*6

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
        return [x_cor, y_cor, z_cor, label] 

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
    
    def simulate_ripple(self, inc, time):
        frames = []
        self.f1.inc_up_angle(inc/2)
        self.f2.inc_up_angle(-inc/4)
        self.m1.inc_up_angle(-inc/4)
        self.m2.inc_up_angle(-inc/2)
        self.b1.inc_up_angle(-inc/4)
        self.b2.inc_up_angle(-inc/4)
        frames.append(self.get_cords())
        for i in range(time):
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(inc/4)
            self.f1.inc_below_angle(-inc)
            self.m2.inc_below_angle(-inc)
            frames.append(self.get_cords())
            self.f1.inc_up_angle(-inc/2)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(inc/2)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(inc/4)
            self.f1.inc_below_angle(inc)
            self.m2.inc_below_angle(inc)
            frames.append(self.get_cords())
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(-inc/2)
            self.m1.inc_below_angle(-inc)
            self.b2.inc_below_angle(-inc)
            frames.append(self.get_cords())
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(inc/4)
            self.m1.inc_up_angle(-inc/2)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(inc/4)
            self.b2.inc_up_angle(-inc/2)
            self.m1.inc_below_angle(inc)
            self.b2.inc_below_angle(inc)
            frames.append(self.get_cords())
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(inc/4)
            self.f2.inc_below_angle(-inc)
            self.b1.inc_below_angle(-inc)
            frames.append(self.get_cords())
            self.f1.inc_up_angle(inc/4)
            self.f2.inc_up_angle(-inc/2)
            self.m1.inc_up_angle(inc/4)
            self.m2.inc_up_angle(-inc/4)
            self.b1.inc_up_angle(-inc/2)
            self.b2.inc_up_angle(inc/4)
            self.f2.inc_below_angle(inc)
            self.b1.inc_below_angle(inc)
            frames.append(self.get_cords())
            self.cog = (self.cog[0], self.cog[1]+5, self.cog[2])
        return frames

    def fault(self, arr):
        for leg in arr:
            self.functional[leg.index] = False
            leg._disable()
        self.reconfigure()

    def recover(self, arr):
        for leg in arr:
            self.functional[leg.index] = True
            leg._enable()
        self.reconfigure()
    
    def get_number_legs(self):
        num = 0
        for leg in self.functional:
            if leg:
                num = num+1
        return num

    def reconfigure(self):
        num = self.get_number_legs()
        if num == 6:
            self.simulate_ripple()
            # do nothing
        else if num == 5:
            # disable one odd leg walk with four legs
        else if num == 4:
            # reconfigure according to the position of functional legs
        else if num == 3:
            # disable one odd leg, crawl witb two legs
        else if num == 2:
            # reconfigure according to the position of legs and then crawl
        else:
            # crawl
        return
            
    def walk(self):
        return
    
    def crawl(Self):
        return