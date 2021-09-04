import pygame
import numpy as np

class Blob:
    def __init__(self, Size):
        self.x = np.random.randint(0, Size)
        self.y = np.random.randint(0, Size)

    
