import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
import math
from scipy.integrate import odeint

matplotlib.use("TkAgg")

t = np.linspace(1, 20, 1001)

def odesys(y, t, m1, m2, l, g, alpha):
    dy = np.zeros(4)
    dy[0] = y[2]
    dy[1] = y[3]

    a11 = m1 + m2
    a12 = -m2 * l * np.cos(y[1] - alpha)
    a21 = -np.cos(y[1] - alpha)
    a22 = l

    b1 = (m1 + m2) * g * np.sin(alpha) - m2 * l * (y[3])**2 * np.sin(y[1] - alpha)
    b2 = -g * np.sin(y[1])

    dy[2] = (b1 * a22 - a12 * b2) / (a11 * a22 - a21 * a12)
    dy[3] = (b2 * a11 - b1 * a21) / (a11 * a22 - a21 * a12)

    return dy

m1 = 1
m2 = 500
l = 5
g = 9.81
alpha = math.pi / 4

x0 = 0
phi0 = 0
dx0 = 0
dphi0 = 12
y0 = [x0, phi0, dx0, dphi0]

Y = odeint(odesys, y0, t, (m1, m2, l, g, alpha))

# print(Y.shape)

x = Y[:, 0]
phi = Y[:, 1]
dx = Y[:, 2]
dphi = Y[:, 3]
X_0 = 4
a = 2.5
b = 3

X_A = -a / 40 * x
Y_A = X_A
Y_B = Y_A - l * np.sin(math.pi / 1.2 - phi)
X_B = X_A + l * np.cos(math.pi / 1.2 - phi)
# X_B = X_A + l * np.cos(phi) 
# Y_B = Y_A - l * np.sin(phi)
X_Box = np.array([-0.75, -1.3, 0.2, 0.75, -0.75])
Y_Box = np.array([-0.75, -0.25, 1.25, 0.75, -0.75])

X_Straight = [-10, 0, 10]
Y_Straight = [-10, 0, 10]

fig = plt.figure(figsize = [9, 5])
ax = fig.add_subplot(1, 1, 1)
ax.axis('equal')
ax.set(xlim = [-5, 5], ylim = [-5, 5])

ax.plot(X_Straight, Y_Straight)
Drawed_Box = ax.plot(X_A[0] + X_Box,Y_A[0] + Y_Box)[0]
Line_AB = ax.plot([X_A[0], X_B[0],], [Y_A[0], Y_B[0]])[0]
Point_A = ax.plot(X_A[0], Y_A[0], marker = 'o')[0]
Point_B = ax.plot(X_B[0], Y_B[0], marker = 'o', markersize = 5)[0]

fig2 = plt.figure(figsize = [9, 5])
ax2 = fig2.add_subplot(2, 2, 1)
ax2.plot(t, -x)
plt.title('x(t)')

ax3 = fig2.add_subplot(2, 2, 2)
ax3.plot(t, phi)
plt.title('phi(t)')

ax4 = fig2.add_subplot(2, 2, 3)
ax4.plot(t, dx)
plt.title('dx(t)')

ax5 = fig2.add_subplot(2, 2, 4)
ax5.plot(t, dphi)
plt.title('dphi(t)')

plt.subplots_adjust(wspace=0.3, hspace=0.7)

def Kino(i):
    Point_A.set_data(X_A[i], Y_A[i])
    Point_B.set_data(X_B[i], Y_B[i])
    Line_AB.set_data([X_A[i], X_B[i],], [Y_A[i], Y_B[i]])
    Drawed_Box.set_data(X_A[i] + X_Box, Y_A[i] + Y_Box)
    return [Point_A, Point_B, Line_AB, Drawed_Box] 

anima = FuncAnimation(fig, Kino,frames = 1000, interval = 50)
plt.show()