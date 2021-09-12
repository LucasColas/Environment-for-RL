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

#TODO : binning

def binning(Size, numsamples):
    Width_chunk = np.linspace(0, Size[0], numsamples)
    Height_chunk = np.linspace(0, Size[1], numsamples)

    return Width_chunk, Height_chunk


def get_discrete_state(sate, binning):
    x_dis = np.digitize(state[0], binning[0])
    y_dis = np.digitize(state[1], binning[1])

    return x_dis, y_dis



def create_Q_Table(Width_chunk, Height_chunk):
    print("Creating Q_Table")
    Q_table = {}
    
    for x1 in range(0, len(Width_chunk)):
        for y1 in range(0, len(Height_chunk)):

            for x2 in range(0, len(Width_chunk)):
                for y2 in range(0, len(Height_chunk)):
                    Q_table[((x1, y1), (x2, y2))] = [np.random.uniform(-5,0) for i in range(4)]

    print("Q_Table created")
    return Q_table

def plot(moving_avg):
    plt.plot([i for i in range(len(moving_avg))], moving_avg)
    plt.ylabel(f"reward {100}")
    plt.xlabel("episode")
    plt.show()

def QLearning(Episodes, Size, Width_chunk, Height_chunk):
    print("Initializing QLearning")
    Eps_rewards = []
    show = False
    run = True

    Q_table = create_Q_Table(Width_chunk, Height_chunk)
    print("launching QLearning")
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
