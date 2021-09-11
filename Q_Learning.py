import pygame
import matplotlib.pyplot as plt

import numpy as np

Episodes = 30000
Move_Penalty = 1
Enemy_Penalty = 300
Food_Reward = 30
Eps = 0.95
Eps_Decay = 0.9998
Eps_Decay_Reduc = 0.0001

Lr = 0.1
Gamma = 0.95


def create_Q_Table(Size):

    Q_table = {}
    for x1 in range(0, Size[0]):
        for y1 in range(0, Size[1]):
            for x2 in range(0, Size[0]):
                for y2 in range(0, Size[1]):
                    Q_table[((x1, y1), (x2, y2))] = [np.random.uniform(-5,0) for i in range(4)]

    return Q_table

def plot(moving_avg):
    plt.plot([i for i in range(len(moving_avg))], moving_avg)
    plt.ylabel(f"reward {100}")
    plt.xlabel("episode")
    plt.show()

def QLearning(Win, Episodes, Size, colors):

    Eps_rewards = []
    show = False
    run = True

    Q_table = create_Q_Table(Size)

    for episode in range(Episodes):
        print(f"ep : {episode}")
        Player = Blob(colors["blue"], Size[0], Size[0]//15, 15)
        Enemy = Blob(colors["red"], Size[0], Size[0]//15, 15)
        Food = Blob(colors["green"], Size[0], Size[0]//15, 15)
        Ep_rewards = 0

        if episode % 2 == 0:
            print(f"ep : {episode}" )
            print(f"ep mean : {np.mean(Eps_rewards[-20:])}")
            show = True

        else:
            show = False


        for i in range(200):
            reward = 0
            obs = (Player - Food, Player - Enemy)

            if np.random.random() > Eps:
                action = np.argmax(Q_table[obs])

            else:
                action = np.random.randint(0,4)

            """
            Player.action(action)
            Enemy.draw(Win)
            Food.draw(Win)
            Player.draw(Win)
            pygame.display.update()
            """


            if Player.collide(Enemy.Rect):
                reward = -Enemy_Penalty

            elif Player.collide(Food.Rect):
                reward = Food_Reward

            else:
                reward = -Move_Penalty

            new_obs = (Player - Food, Player - Enemy)
            max_future_q = np.max(Q_table[new_obs])
            current_q = Q_table[obs][action]

            if reward == Food_Reward:
                new_q = Food_Reward

            elif reward == -Enemy_Penalty:
                new_q = -Enemy_Penalty

            else:
                new_q = (1 - Lr) * current_q + Lr * (reward + Discount * max_future_q)

            Q_table[obs][action] = new_q

            if show:
                pass






            Ep_rewards += reward
            if reward == Food_Reward or reward == -Enemy_Penalty:
                break

        Eps_rewards.append(Ep_rewards)
        Eps *= Eps_Decay

    moving_avg = np.convolve(Eps_rewards, np.ones((100,)) / 100, mode="valid")
    plot(moving_avg)
