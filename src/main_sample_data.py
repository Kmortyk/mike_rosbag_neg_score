import math

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle
import reward

np.random.seed(1905)

matplotlib.rc('font', size=6)

r0 = np.array([1/2, 1/2])
xs1, ys1 = [], []
xs2, ys2 = [], []

plt.figure()

reward.init_memos()

for layer in np.arange(0, 10, 3):
    for phi in range(0, 720, 30):
        r = 0.3*layer

        x = r0[0] + r*math.cos(math.radians(phi/2))
        y = r0[1] + r*math.sin(math.radians(phi/2))

        dx = x - r0[0]
        dy = y - r0[1]

        rew, ok = reward.point_reward(phi, r)
        if ok:
            xs2.append(x)
            ys2.append(y)
        else:
            xs1.append(x)
            ys1.append(y)

        # plt.text(x, y, f"{rew:.2f},{phi:.0f}")
        plt.text(x, y, f"{rew:.2f}")

ax = plt.gca()
ax.set_aspect('equal')

ax.plot(xs1, ys1, marker='o', color='r', ls='')
ax.plot(xs2, ys2, marker='o', color='y', ls='')
ax.plot(r0[0], r0[1], marker='o', color='g', ls='')
ax.add_patch(Circle(tuple(r0), reward.R0, edgecolor='m', fc='None', lw=2, zorder=5))
ax.add_patch(Ellipse(tuple(r0), width=reward.A*2, height=reward.B*2, edgecolor='m', fc='None', lw=2, zorder=5))

plt.show()
