import math

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
import reward

np.random.seed(1905)

font = {'family': 'normal',
        'size' : 6}

matplotlib.rc('font', **font)

# data = np.random.randint(1000, size=(500, 2)) / 100

# gen points in polar system - pairs (phi, dst)

r0 = np.array([1/2, 1/2])
xs1, ys1 = [], []
xs2, ys2 = [], []

plt.figure()

for layer in np.arange(0, 100, 10):
    for phi in range(0, 720, 10):
        r = 0.3*layer

        x = r0[0] + r*math.cos(phi)
        y = r0[1] + r*math.sin(phi)

        dx = x - r0[0]
        dy = y - r0[1]

        if (dx*dx)/reward.A2 + (dy*dy)/reward.B2 <= 1:
            xs2.append(x)
            ys2.append(y)
        else:
            xs1.append(x)
            ys1.append(y)

        plt.text(x, y, f"{reward.point_reward(phi, r)}")

ax = plt.gca()
ax.set_aspect('equal')

ax.plot(xs1, ys1, marker='o', color='r', ls='')
ax.plot(xs2, ys2, marker='o', color='b', ls='')
ax.plot(r0[0], r0[1], marker='o', color='g', ls='')
ax.add_patch(Ellipse(tuple(r0), width=reward.A*2, height=reward.B*2, edgecolor='m', fc='None', lw=2, zorder=5))

plt.show()
