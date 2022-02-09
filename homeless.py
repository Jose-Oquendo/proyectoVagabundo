import random

class Homeless:

    def __init__(self, name, x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def distance_origin(self):
        return(self.x**2 + self.y**2)

class StandarHomeless(Homeless):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(1,0),(-1,0),(0,1),(0,-1)])

class ModerateHomeless(Homeless):
    def __init__(self, name):
        super().__init__(name)

    def ModerateWalk(self):
        dx, dy = random.choice([(2,0),(-2,0),(0,2),(0,-2)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]

class LeftHomeless(Homeless):
    def __init__(self, name):
        super().__init__(name)

    def leftWalk(self):
        dx, dy = random.choice([(0,1),(-1,0),(0,1),(0,-5)])
        self.x += dx
        self.y += dy
        return [self.x, self.y]

