import pygame
pygame.init()

from Env_wPygame import Blob
from Q_Learning import *

colors = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}

Size = (600,600)

Win = pygame.display.set_mode(Size)
#pygame.display.set_caption("Environnement")

def update_win():
    pygame.display.update()

def main(Win, Size, colors):
    run = True
    Width_chunk, Height_chunk = binning(Size, 20)
    Q_Table = create_Q_Table(Width_chunk, Height_chunk)
    launched = False
    #QLearning(Win, Q_Table, Episodes, Size, colors, Width_chunk, Height_chunk, launched)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()

        if not launched:
            QLearning(Win, Q_Table, Episodes, Size, colors, Width_chunk, Height_chunk, launched)

        launched = True





main(Win, Size, colors)
#test()
