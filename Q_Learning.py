import pygame
import matplotlib.pyplot as plt

WIN_Size = (600, 600)

Episodes = 30000
Move_Penalty = 1
Enemy_Penalty = 300
Food_Reward = 30
Eps = 0.95
Eps_Decay = 0.9998
Eps_Decay_Reduc = 0.0001

Lr = 0.1
Gamma = 0.95

Q_table = {}

for x1 in range(0, WIN_Size[0]):
    for y1 in range(0, WIN_Size[1]):
        for x2 in range(0, WIN_Size[0]):
            for y2 in range(0, WIN_Size[1]):
                Q_table[((x1, y1), (x2, y2))] = [np.random.uniform(-5,0) for i in range(4)]
