import math
from typing import Tuple
import numpy as np

"""
Repeat action, sum reward, and max over last observations.
"""

R0 = 0.9
R02 = R0**2
start_point = np.array([0, 0])

A = 2 # радиус описанной вокруг робота окружности (todo нужны точные геометрические размеры робота)
B = 1 # вытянутая окружность робота вдоль продолтноц оси (todo подобрать расстояние)

# todo
#  a. Связаться с Эльдаром, нарисовать точные размеры робота
#  b. Интегральный штраф 12 раз в секунду - усреднять штрафы за некоторый промежуток времени,
#  все окружающие точки нужно брать сумму по кругу - для нескольких проходов, усреднять отрицательные награды
#  c. Найти переднюю полусферу (-90 до +90)
#  d. Найти нулевую полуось, нарисовать систему координат x и y, нулевой угол, как считается угол (со сдвигом и др).
#  e. Попробовать привести углы к виду (-,+), отрицательный угол
#  f. Эллипс граница безопасности - какие-то расстояние, граница опасности - находить точку пересечения
# todo
#  1. Сравнить по скорости tf.math.log и log_memo.
#  2. Использовать DLA для вычислений.
#  3. Определить точное направление оси X и Y Ox должно идти вдоль продольной оси робота.

# todo rx*(-vx)*t

A2 = A*A
B2 = B*B

iA2 = 1/A2
iB2 = 1/B2

# todo
#  (вы можете считать от 0 до 260, с учетом 0,5 град от 0 до 720 против часовой,
#  но в формулу нужно будет подставлять углы в пределах от 0 до Pi и от 0 до -Pi. Все, как в обычном тригонометрическом круге,
#  только у тебя радиус-вектор описывает в данном случае не круг, а эллипс.

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

# робот с гусеницами
# R0 - радиус крайней опасности - R0 - малая ось эллипса *размер по диагонали)
# малая полуось - R0

# phi in range [0, 719) - 0.5 degree per step
def point_reward(phi, r) -> Tuple[float, bool]:
    # todo
    # if 360 < phi < 720:
    #    return 0, False

    x = r * f_cos(phi)
    y = r * f_sin(phi)

    dst = (x**2)*iA2 + (y**2)*iB2

    if 0 < dst <= 1:
        dst_sq = f_sqrt(dst)

        if R0 < dst_sq:
            return 10000 * f_log(1 - R0 / dst_sq), True

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
