import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for color,number in kwargs.items():
            for x in range(number):
                self.contents.append(color)

    def draw(self,numbers):
        balls=[]
        copycontents=[]
        if numbers>=len(self.contents):
            copycontents=self.contents[:]
            self.contents.clear()
            return copycontents
        for x  in range(numbers):
            x=random.choice(self.contents)
            balls.append(x)
            self.contents.remove(x)
        return balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succes=0
    for x in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        ok =1
        result=copy_hat.draw(num_balls_drawn)
        for color in expected_balls:
            count=0
            for ball in result:
                if ball==color:
                    count+=1
            if count<expected_balls[color]:
                ok=0
        if ok==1:
            succes+=1
    return succes/num_experiments

