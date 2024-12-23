import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
import math

matplotlib.use("TkAgg")


t = np.linspace(1, 20, 1001)

x = np.cos(t)
phi = np.sin(2 * t)
alpha = math.pi / 6
X_0 = 4
a = 2.5
b = 3
l = 3

# s = 4 * np.cos(3 * t)

# X_A = -x * np.cos(alpha) + 4 / 5 * a
# Y_A = x * np.sin(alpha) - 1.6 / 2 * b

# X_A = X_0 + a / 2 + x
# Y_A = 4 * b / 2 + np.sin(phi)
X_A = a / 2 * x
Y_A = X_A
X_B = X_A - l * np.sin(phi)
Y_B = Y_A - l * np.cos(phi)
X_Box = np.array([-1.5, -3, 0, 1.5, -1.5])
Y_Box = np.array([-1.5, -0.5, 2.5, 1.5, -1.5])

X_Straight = [-10, 0, 10]
Y_Straight = [-10, 0, 10]

fig = plt.figure(figsize = [9, 5])
ax = fig.add_subplot(1, 2, 1)
ax.axis('equal')
ax.set(xlim = [-5, 5], ylim = [-5, 5])

ax.plot(X_Straight, Y_Straight)
Drawed_Box = ax.plot(X_A[0] + X_Box,Y_A[0] + Y_Box)[0]
Line_AB = ax.plot([X_A[0], X_B[0],], [Y_A[0], Y_B[0]])[0]
Point_A = ax.plot(X_A[0], Y_A[0], marker = 'o')[0]
Point_B = ax.plot(X_B[0], Y_B[0], marker = 'o', markersize = 10)[0]

ax2 = fig.add_subplot(4, 2, 2)
ax2.plot(t, X_A)
# plt.title('xA of the Point A')
plt.xlabel('t values')
plt.ylabel('x values')

ax3 = fig.add_subplot(4, 2, 4)
ax3.plot(t,Y_A)
# plt.title('yA of the Point A')
plt.xlabel('t values')
plt.ylabel('y values')

ax4 = fig.add_subplot(4, 2, 6)
ax4.plot(t, X_B)
# plt.title('xB of the Point B')
plt.xlabel('t values')
plt.ylabel('x values')

ax5 = fig.add_subplot(4, 2, 8)
ax5.plot(t,Y_B )
# plt.title('yB of the Point B')
plt.xlabel('t values')
plt.ylabel('y values')

plt.subplots_adjust(wspace=0.3, hspace=0.7)


def Kino(i):
    Point_A.set_data(X_A[i], Y_A[i])
    Point_B.set_data(X_B[i], Y_B[i])
    Line_AB.set_data([X_A[i], X_B[i],], [Y_A[i], Y_B[i]])
    Drawed_Box.set_data(X_A[i] + X_Box, Y_A[i] + Y_Box)
    return [Point_A, Point_B, Line_AB, Drawed_Box] 

anima = FuncAnimation(fig, Kino,frames = 1001, interval = 10)
plt.show()