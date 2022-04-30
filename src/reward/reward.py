import math
from typing import Tuple
import numpy as np

"""
Repeat action, sum reward, and max over last observations.
"""

R0 = 0.3
R02 = R0**2
start_point = np.array([0, 0])

A = 2
B = 1

A2 = A*A
B2 = B*B

iA2 = 1/A2
iB2 = 1/B2

# todo
#   jetson проверить время обработки массива
# todo
#   объединить - в одно увязать (модульно), как это всё использовать
# todo
#   таблица логарифмов

cos_memo = {}
sin_memo = {}

def init_memos():
    for i in range(0, 361):
        cos_memo[i] = math.cos(math.radians(i))
        sin_memo[i] = math.sin(math.radians(i))

# phi in range [0, 719) - 0.5 degree per step
def point_reward(phi, r) -> Tuple[float, bool]:
    if 360 < phi < 720:
        return 0, False

    x = r * f_cos(phi)
    y = r * f_sin(phi)

    dst = (x**2)*iA2 + (y**2)*iB2

    if 0 < dst <= 1:
        dst_sq = f_sqrt(dst)

        if R0 < dst_sq:
            return 100 * f_log(1 - R0 / dst_sq), True

    return 0, False

def f_cos(phi) -> float:
    return cos_memo[phi/2]

def f_sin(phi) -> float:
    return sin_memo[phi/2]

def f_log(v) -> float:
    return np.log(v)

def f_sqrt(dst) -> float:
    return np.sqrt(dst)
