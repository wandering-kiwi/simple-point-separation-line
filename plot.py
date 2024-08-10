from model import *
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# red and blue dots
ax.scatter(red_x, red_y, c='red')
ax.scatter(blue_x, blue_y, c='blue')

# green line
X = np.arange(0, 8)
lines = tweak(M, C, learning_rate=0.5, delta=0.001, iters=600, cost_func=better_cost)

# for j in range(len(lines)):
#     i=lines[j]
#     m=i[0]
#     c=i[1]
#     if j > 0:
#         ax.plot(X, m * X + c, "g-", linewidth=1)

ax.plot(X, lines[0][0] * X + lines[0][1], "y-", linewidth=1)
ax.plot(X, lines[-1][0] * X + lines[-1][1], "g-", linewidth=1)

ax.legend()
ax.grid()
plt.show()