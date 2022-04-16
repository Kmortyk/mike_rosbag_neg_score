import math
from typing import Tuple

import numpy as np

"""
Repeat action, sum reward, and max over last observations.
"""

R0 = np.array([0, 0])
A = 2
B = 1

A2 = A*A
B2 = B*B

def point_reward(phi, r) -> Tuple[float, bool]:
    x = R0[0] + r * math.cos(phi)
    y = R0[1] + r * math.sin(phi)

    dx = x - R0[0]
    dy = y - R0[1]

    if (dx * dx) / A2 + (dy * dy) / B2 <= 1:
        return -1000, True

    return 0, False

def reward_return(ax, rx, by, ry, total_reward):
    if np.min(rx, ry) > R0:
        reward = 100 * np.log(1 - R0 / np.sqrt(ax * rx ** 2 + by * ry ** 2))
    else:
        reward = -5000

    total_reward += reward

    return total_reward
