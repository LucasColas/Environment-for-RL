import pygame
import numpy as np

import matplotlib.pyplot as plt

pygame.init()

WIN_Size = (600,600)

pygame.display.set_caption("Environnement")
Win = pygame.display.set_mode(WIN_Size)


class Blob:
    def __init__(self, Color, Size, Step, Length):
        self.Size_x = Size[0]
        self.Size_y = Size[1]
        self.Step = Step
        self.Length = Length
        self.x = np.random.randint(0, self.Size_x)
        self.y = np.random.randint(0, self.Size_y)
        self.Rect = pygame.Rect(self.x, self.y , self.Length, self.Length)


    #def __str__(self):
        #return f"{self.x}, {self.y}"

    #def __sub__(self, other):
        #return (self.x - other.x, self.y - other.y)

    def collide(self, other):
        if self.Rect.colliderect(other):
            return True

    def info(self, other):
        return (self.x - other.x, self.y - other.y)

    def action(self, choice):
        if choice == 0:
            self.move(-self.Step,0)

        elif choice == 1:
            self.move(self.Step,0)

        elif choice == 2:
            self.move(0,-self.Step)

        elif choice == 3:
            self.move(0,self.Step)


    def move(self, x=False,y=False):
        if not x:
            self.x += np.random.randint(-1,2)

        else:
            self.x += x

        if not y:
            self.y += np.random.randint(-1,2)

        else:
            self.y += y

        self.checkBorders()

        self.Rect.x = self.x
        self.Rect.y = self.y


    def checkBorders(self):
        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

        if self.x > self.Size_x:
            self.x = self.Size_x - self.Length

        if self.y > self.Size_y:
            self.y = self.Size_y - self.Length


    def draw(self, Win):
        pygame.draw.rect(Win, self.color, self.Rect)
