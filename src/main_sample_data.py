from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

np.random.seed(1905)

data = np.random.randint(1000, size=(500, 2)) / 100
r0 = np.array([1/2, 1/2])

print(data)

plt.figure()
ax = plt.gca()

plt.plot(*zip(*data), marker='o', color='r', ls='')
plt.plot(r0[0], r0[1], marker='o', color='g', ls='')

ellipse = Ellipse(tuple(r0), width=0.7, height=0.5, edgecolor='b', fc='None', lw=2)
ax.add_patch(ellipse)

plt.show()
