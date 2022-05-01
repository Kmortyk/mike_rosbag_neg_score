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
#  1. jetson проверить время обработки массива
#  2. объединить - в одно увязать (модульно), как это всё использовать

cos_memo  = {}
sin_memo  = {}
log_memo  = {}
sqrt_memo = {}

def init_memos():
    for v in np.arange(0.01, 1.01, 0.01):
        r = round_float(v)

        log_memo[r] = np.log(r)
        sqrt_memo[r] = np.sqrt(r)

    for v in np.arange(0.00, 360.05, 0.05):
        a = round_float(v)

        cos_memo[a] = math.cos(math.radians(a))
        sin_memo[a] = math.sin(math.radians(a))

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
    return log_memo[round_float(v)]

def f_sqrt(dst) -> float:
    return sqrt_memo[round_float(dst)]

def round_float(v: float) -> float:
    return round(v, 2)
