import pyray
from raylib import colors

class Points:
    "Зёрна"
    def __init__(self):
        self.array = list()

    def add(self, x, y, type):
        self.array.append(Point(x, y, type))
    
    def remove(self, n):
        self.array.pop(n)

    def draw(self):
        for i in range(len(self.array)):
            self.array[i].draw()

    def getAll(self):
        return self.array

class Point:
    "Зерно"
    def __init__(self, x=0, y=0, type="small"):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == "small":
            pyray.draw_circle(self.x, self.y, 5, colors.WHITE)
        if self.type == "big":
            pyray.draw_circle(self.x, self.y, 10, colors.WHITE)