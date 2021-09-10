import pygame
pygame.init()

from Env_wPygame import *
from Q_Learning import *

colors = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}

Size = (600,600)

Win = pygame.display.set_mode(Size)
pygame.display.set_caption("Environnement")

def test():
    run = True
    while run:
        Win.fill((10,120,24))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

def main(Size, colors):
    run = True
    while run:
        Win.fill((10,120,24))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False

        QLearning()



main(Size, colors)
#test()
