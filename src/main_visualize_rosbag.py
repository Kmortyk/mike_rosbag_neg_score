import math
import time
from datetime import datetime
import genpy.rostime as rostime
import matplotlib
from matplotlib import pyplot as plt
import rosbag
from matplotlib.patches import Ellipse, Circle

from src import reward
from src.config import config
from src.reward import point_reward, start_point

matplotlib.rc('font', size=6)

bag = rosbag.Bag(config.ROS_BAG_PATH, 'r')

topics = [
    '/diffbot/scan',
]

xs1, ys1 = [], []
xs2, ys2 = [], []

reward.init_memos()

for _, msg, t in bag.read_messages(topics=topics, end_time=rostime.Time(nsecs=1643481665097880257)):
    for phi in range(0, 719, 1):
        r = msg.ranges[phi]

        x = r * math.cos(math.radians(phi / 2))
        y = r * math.sin(math.radians(phi / 2))

        rew, ok = point_reward(phi, r)
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
