from data import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.scatter(red_x, red_y, c='red')
ax.scatter(blue_x, blue_y, c='blue')

ax.legend()
ax.grid()
plt.show()