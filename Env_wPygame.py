import pygame
import numpy as np

WIN_Size = (600,600)

class Blob:
    def __init__(self, Size):
        self.x = np.random.randint(0, Size)
        self.y = np.random.randint(0, Size)

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def action(self, choice):
        if choice == 0:
            self.move(-1,0)

        elif choice == 1:
            self.move(1,0)

        elif choice == 2:
            self.move(0,-1)

        elif choice == 3:
            self.move(0,1)


    def move(self, x=False,y=False):
        pass
