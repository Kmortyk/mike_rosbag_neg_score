import math
from typing import Tuple
import numpy as np

"""
Repeat action, sum reward, and max over last observations.
"""

R0 = 0.18
R02 = R0**2
start_point = np.array([0, 0])

A = 1.9*R0 # радиус описанной вокруг робота окружности
B = 1.2*R0 # вытянутая окружность робота вдоль продолтноц оси

# todo
#  b. Интегральный штраф 12 раз в секунду - усреднять штрафы за некоторый промежуток времени,
#  все окружающие точки нужно брать сумму по кругу - для нескольких проходов, усреднять отрицательные награды
#  e. Попробовать привести углы к виду (-,+), отрицательный угол
# todo
#  1. Сравнить по скорости tf.math.log и log_memo.
#  2. Использовать DLA для вычислений.
#  3. прогнать через тестовые данные
# todo порог награды - 40% - средний штраф
# todo скорость rx*(-vx)*t
# todo данные среды - распознавание + lidar

# s - текущее состояние - обстановка - (облако точек + с камеры распознанный объект)
# action - управляющий сигнал
# s1 - новое состояние - состояние через время t
# r - награда - штраф + положительная компонента

# todo синхронизировать lidar с камеров
#   - сколько данных в секунду нужно lidar
#   - с такой же частотой брать кадры (можно брать меньше кадров - каждый 3)
# todo собрать буффер lidar_719_vector, action, inference_flag, total_score

A2 = A*A
B2 = B*B

iA2 = 1/A2
iB2 = 1/B2

CUT_BACK = False

cos_memo  = {}
sin_memo  = {}
log_memo  = {}
sqrt_memo = {}

def init_memos():
    for v in np.arange(0.00, 1.01, 0.01):
        r = round_float(v)

        if v > 0:
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
    if CUT_BACK and ((0 < phi < 180) or (540 < phi < 720)):
       return 0, False

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
