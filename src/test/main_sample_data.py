import math

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle

from src.reward import reward
from src.testdata.circles_data import CirclesData
from src.testdata.one_wall_data import BoxData

np.random.seed(1905)

matplotlib.rc('font', size=6)

xs1, ys1 = [], []
xs2, ys2 = [], []

plt.figure()

reward.init_memos()

points_data = [
    # BoxData(size=0.3, offset_x=1, offset_y=1),
    # BoxData(size=0.3, offset_x=-1, offset_y=1),
    # BoxData(size=0.3, offset_x=1, offset_y=-1),
    # BoxData(size=0.3, offset_x=-1, offset_y=-1),
    CirclesData()
]

for pd in points_data:
    for scan in pd.laser_scan_data():
        for phi in range(0, 720, 1):
            r = scan[phi]

            x = r*math.cos(math.radians(phi/2))
            y = r*math.sin(math.radians(phi/2))

            rew, ok = reward.point_reward(phi, r)
            if ok:
                xs2.append(x)
                ys2.append(y)
            else:
                xs1.append(x)
                ys1.append(y)

            plt.text(x, y, f"{rew:.2f}")

ax = plt.gca()
ax.set_aspect('equal')

ax.plot(xs1, ys1, marker='o', color='r', ls='')
ax.plot(xs2, ys2, marker='o', color='y', ls='')
ax.plot(0, 0, marker='o', color='g', ls='')
ax.add_patch(Circle(tuple((0, 0)), reward.R0, edgecolor='m', fc='None', lw=2, zorder=5))
ax.add_patch(Ellipse(tuple((0, 0)), width=reward.A*2, height=reward.B*2, edgecolor='m', fc='None', lw=2, zorder=5))

plt.show()
