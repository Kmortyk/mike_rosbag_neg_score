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

iA2 = 1/A2
iB2 = 1/B2

# phi in range [0, 719) - 0.5 degree per step
def point_reward(phi, r) -> Tuple[float, bool]:
    x = r * math.cos(phi/2)
    y = r * math.sin(phi/2)

    dst = (x**2)*iA2 + (y**2)*iB2

    if min(x, y) != 0 and dst <= 1:
        return -(100 * np.log(1 / np.sqrt(dst))), True

    return 0, False

##### old

def reward_return(ax, rx, by, ry, total_reward):
    if np.min(rx, ry) > R0:
        reward = 100 * np.log(1 - R0 / np.sqrt(ax * rx ** 2 + by * ry ** 2))
    else:
        reward = -5000

    total_reward += reward

    return total_reward
