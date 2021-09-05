import pygame
from Env_wpygame import *
from Q_Learning import *


def main():
    Size = (600,600)
    color = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}
    Player = Blob(color["blue"], Size[0], Size[0]//15, 15)
    Enemy = Blob(color["red"], Size[0], Size[0]//15, 15)
    Food = Blob(color["green"], Size[0], Size[0]//15, 15)
