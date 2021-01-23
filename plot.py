import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z**2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
m = 10
f = 5
s = 15
p1 = [m, f, -f, -m, -f, f, m]
p2 = [0, s, s, 0, -s, -s, 0]
p3 = [0, 0, 0, 0, 0, 0, 0]
ax.plot(p1, p2, p3, label='parametric curve')
p1 = [0, 10]
p2 = [0, 10]
p3 = [0, 0]
ax.plot(p1, p2, p3, label='parametric curve')
ax.legend()

# line_1  = plt.plot([1, 2, 3])
# line_2  = plt.plot([2, 4, 6])
# line = line_2.pop(0)
# line.remove()
# https://www.kite.com/python/answers/how-to-remove-a-line-from-a-plot-in-python


plt.show()
