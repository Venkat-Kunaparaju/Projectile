import math 

class ball:
    def __init__(self):
        self.velocity = 100
        self.height =  100 
        self.time = 100
        self.h_distance = 100
        self.divisor =  100
    def calculations(self):
        self.time = math.sqrt((2*self.height)/10)
        self.h_distance = self.time*self.velocity

ball = ball()

