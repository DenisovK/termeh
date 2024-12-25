import matplotlib 
import numpy as np  
import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation  
import sympy as sp  # Импортируем библиотеку для символьной математики.
import math  

matplotlib.use("TkAgg")  # Указываем использование интерфейса Tk для отображения графиков.

# Создаём временной интервал.
t = np.linspace(1, 20, 1001)  # Массив значений времени от 1 до 20 с 1001 точкой.

# Задаём функции для движения точки.
x = np.cos(t)  # Значения по оси x
phi = np.sin(2 * t)  # Угловая координата
alpha = math.pi / 6  # Угол наклона
X_0 = 4  # Начальное значение координаты X.
a = 2.5  # Параметр для масштаба по оси X.
b = 3  # Параметр для масштаба по оси Y.
l = 3  # Длина соединяющего звена.

# Вычисляем координаты точки A.
X_A = a / 2 * x  
Y_A = X_A  

# Вычисляем координаты точки B.
X_B = X_A - l * np.sin(phi)  # Координата X точки B с учётом углового смещения.
Y_B = Y_A - l * np.cos(phi)  # Координата Y точки B с учётом углового смещения.

# Координаты для отрисовки коробки вокруг точки.
X_Box = np.array([-1.5, -3, 0, 1.5, -1.5])  # Контур коробки по оси X.
Y_Box = np.array([-1.5, -0.5, 2.5, 1.5, -1.5])  # Контур коробки по оси Y.

# Координаты прямой линии для справки.
X_Straight = [-10, 0, 10]  # Координаты линии по оси X.
Y_Straight = [-10, 0, 10]  # Координаты линии по оси Y.

# Создаём окно для графиков.
fig = plt.figure(figsize=[9, 5])  

# Добавляем основную координатную плоскость.
ax = fig.add_subplot(1, 2, 1)  # Создаём первую из двух колонок для графика.
ax.axis('equal')  # Устанавливаем равный масштаб по осям.
ax.set(xlim=[-5, 5], ylim=[-5, 5])  # Устанавливаем диапазон по осям.

# Рисуем начальные элементы на графике.
ax.plot(X_Straight, Y_Straight)  # Рисуем справочную прямую.
Drawed_Box = ax.plot(X_A[0] + X_Box, Y_A[0] + Y_Box)[0]  # Рисуем коробку вокруг точки A.
Line_AB = ax.plot([X_A[0], X_B[0]], [Y_A[0], Y_B[0]])[0]  # Соединительная линия между точками A и B.
Point_A = ax.plot(X_A[0], Y_A[0], marker='o')[0]  # Отображаем начальное положение точки A.
Point_B = ax.plot(X_B[0], Y_B[0], marker='o', markersize=10)[0]  # Отображаем начальное положение точки B.

# Добавляем графики координат X_A, Y_A, X_B, Y_B.
ax2 = fig.add_subplot(4, 2, 2)  # График X_A.
ax2.plot(t, X_A)  # Отображаем зависимость X_A от времени.
plt.xlabel('t values')  # Подпись оси X.
plt.ylabel('x values')  # Подпись оси Y.

ax3 = fig.add_subplot(4, 2, 4)  # График Y_A.
ax3.plot(t, Y_A)  # Отображаем зависимость Y_A от времени.
plt.xlabel('t values')  # Подпись оси X.
plt.ylabel('y values')  # Подпись оси Y.

ax4 = fig.add_subplot(4, 2, 6)  # График X_B.
ax4.plot(t, X_B)  # Отображаем зависимость X_B от времени.
plt.xlabel('t values')  # Подпись оси X.
plt.ylabel('x values')  # Подпись оси Y.

ax5 = fig.add_subplot(4, 2, 8)  # График Y_B.
ax5.plot(t, Y_B)  # Отображаем зависимость Y_B от времени.
plt.xlabel('t values')  # Подпись оси X.
plt.ylabel('y values')  # Подпись оси Y.

# Настраиваем расстояние между графиками.
plt.subplots_adjust(wspace=0.3, hspace=0.7)  

# Функция для обновления анимации.
def Kino(i):
    Point_A.set_data(X_A[i], Y_A[i])  # Обновляем положение точки A.
    Point_B.set_data(X_B[i], Y_B[i])  # Обновляем положение точки B.
    Line_AB.set_data([X_A[i], X_B[i]], [Y_A[i], Y_B[i]])  # Обновляем соединительную линию.
    Drawed_Box.set_data(X_A[i] + X_Box, Y_A[i] + Y_Box)  # Обновляем положение коробки.
    return [Point_A, Point_B, Line_AB, Drawed_Box]  # Возвращаем обновлённые объекты.

# Создаём анимацию.
anima = FuncAnimation(fig, Kino, frames=1001, interval=10)  

plt.show()  # Отображаем графики и анимацию.
