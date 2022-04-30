import numpy as np
import reward

from timeit import timeit

np.random.seed(1905)

r0 = np.array([1/2, 1/2])
xs1, ys1 = [], []
xs2, ys2 = [], []

reward.init_memos()

def func_reward(layers):
    for layer in np.arange(0, layers, 1):
        for phi in range(0, 720, 30):
            r = 0.3*layer
            reward.point_reward(phi, r)

if __name__ == '__main__':
    t = timeit(lambda: func_reward(1), number=100000)
    print(t)
