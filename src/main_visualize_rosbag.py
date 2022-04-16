import math
import time
from datetime import datetime
import genpy.rostime as rostime
import matplotlib
from matplotlib import pyplot as plt
import rosbag
from matplotlib.patches import Ellipse

from src import reward
from src.config import config
from src.reward import point_reward, R0

matplotlib.rc('font', size=6)

bag = rosbag.Bag(config.ROS_BAG_PATH, 'r')

topics = [
    '/diffbot/scan',
]

xs1, ys1 = [], []
xs2, ys2 = [], []

for _, msg, t in bag.read_messages(topics=topics, end_time=rostime.Time(nsecs=1643481665097880257)):
    for phi in range(0, 719, 1):
        r = msg.ranges[phi]
        x = r * math.cos(phi)
        y = r * math.sin(phi)

        rew, include = point_reward(phi, r)
        if include:
            xs1.append(x)
            ys1.append(y)
        else:
            xs2.append(x)
            ys2.append(y)

        plt.text(x, y, f"{rew}")


ax = plt.gca()
ax.set_aspect('equal')

ax.plot(xs1, ys1, marker='o', color='b', ls='')
ax.plot(xs2, ys2, marker='o', color='r', ls='')
ax.add_patch(Ellipse(tuple(reward.R0), width=reward.A*2, height=reward.B*2, edgecolor='m', fc='None', lw=2, zorder=5))

plt.show()
