from Ball import *
import math

class simulation:
    def __init__(self):
        self.val = 100.12442
        self.pause = False
        self.counter = 200
    def input(self):
        while True:
            ball.velocity = input("Enter the horizontal velocity in m/s: ")
            ball.height = input("Enter the height of the table in meters: ")
            try:
                ball.velocity = float(ball.velocity)
                ball.height = float(ball.height)
                if ball.height > 50:
                    print("Enter a height 50 or lower")
                    continue
                if ball.velocity > 30:
                    print("Enter a velocity 30 or lower")
                    continue
                break
            except:
                continue

    def equation(self, x):
        ball.divisor = ((ball.height)/((ball.h_distance*ball.h_distance)))/10

        self.val = -(ball.divisor)*((x-(10*ball.h_distance)-200)*(x+(10*ball.h_distance)-200))
       
            
            
sim = simulation()
