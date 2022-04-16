import numpy as np

"""
Repeat action, sum reward, and max over last observations.
"""

r0 = np.array([0, 0])

def reward_return(ax, rx, by, ry, total_reward):
    if np.min(rx, ry) > r0:
        reward = 100 * np.log(1 - r0 / np.sqrt(ax * rx ** 2 + by * ry ** 2))
    else:
        reward = -5000

    total_reward += reward

    return total_reward
