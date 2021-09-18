from Q_Learning import create_Q_Table, binning
import sys
import pygame

Width_chunk, Height_chunk = binning((600,600),40)


#Q_Table = create_Q_Table(Width_chunk, Height_chunk)
#print(Q_Table)
Size = (600,600)

Win = pygame.display.set_mode(Size)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    Win.fill((40, 120, 40))
    pygame.display.update()
