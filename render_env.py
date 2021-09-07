import pygame
pygame.init()

from Env_wpygame import *
from Q_Learning import *


def main():
    Size = (600,600)

    color = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}
    Eps_rewards = []
    show = False

    for episode in range(Episodes):
        Player = Blob(color["blue"], Size[0], Size[0]//15, 15)
        Enemy = Blob(color["red"], Size[0], Size[0]//15, 15)
        Food = Blob(color["green"], Size[0], Size[0]//15, 15)
        Ep_rewards = 0

        if episode % 20 == 0:
            print(f"ep : {episode})
            print(f"ep mean : {np.mean(Eps_rewards[-20:])}")
            show =True

        else:
            show = False


        for i in range(200):
            reward = 0
            obs = (Player - Food, Player - Enemy)

            if np.random.random() > Eps:
                action = np.argmax(Q_table[obs])

            else:
                action = np.random.randint(0,4)

            Player.action(action)


            if Player.collide(Enemy.Rect):
                reward = -Enemy_Penalty

            elif Player.collide(Food.Rect):
                reward = Food_Reward

            else:
                reward = -Move_Penalty

            new_obs = (Player - Food, Player - Enemy)
            
