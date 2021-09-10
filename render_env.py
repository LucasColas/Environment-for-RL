import pygame
pygame.init()

from Env_wPygame import *
from Q_Learning import *

colors = {"blue": (20, 81, 232), "red": (238, 34, 24), "green":( 0, 252, 8)}


def main(Size, colors):

    Win = pygame.display.set_mode(Size)

    Eps_rewards = []
    show = False

    for episode in range(Episodes):
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

            Player.action(action)


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
                Win.fill((0,0,0))
                Enemy.draw(Win)
                Food.draw(Win)
                Player.draw(Win)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()


            Ep_rewards += reward
            if reward == Food_Reward or reward == -Enemy_Penalty:
                break

        Eps_rewards.append(Ep_rewards)
        Eps *= Eps_Decay

    moving_avg = np.convolve(Eps_rewards, np.ones((100,)) / 100, mode="valid")
    plot(moving_avg)

def plot(moving_avg):
    plt.plot([i for i in range(len(moving_avg))], moving_avg)
    plt.ylabel(f"reward {100}")
    plt.xlabel("episode")
    plt.show()



main(Size, colors)
