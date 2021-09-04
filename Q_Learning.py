import pygame
import matplotlib.pyplot as plt

Size = 20

Episodes = 30000
Move_Penalty = 1
Enemy_Penalty = 300
Food_Reward = 30
Eps = 0.95
Eps_Decay = 0.9998
Eps_Decay_Reduc = 0.0001

Lr = 0.1
Gamma = 0.95

Q_table = []
