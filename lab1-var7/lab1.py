import math  # Импортируем модуль для работы с математическими функциями.
import sympy as s  # Импортируем модуль для символьных вычислений.
import matplotlib.pyplot as plot  # Импортируем модуль для построения графиков.
import numpy as np  # Импортируем модуль для работы с массивами.
from matplotlib.animation import FuncAnimation  # Импортируем класс для создания анимации.

# Функция для вращения точки на заданный угол.
def rotation2D(x, y, angle):
    Rot_x = x * np.cos(angle) - y * np.sin(angle)  # Вычисляем новую координату x после поворота.
    Rot_y = x * np.sin(angle) + y * np.cos(angle)  # Вычисляем новую координату y после поворота.
    return Rot_x, Rot_y  # Возвращаем повёрнутые координаты.

# Функция для создания стрелки, представляющей вектор.
def Vect_arrow(VecX, VecY, X, Y):
    a = 0.3  # Длина "хвоста" стрелки.
    b = 0.2  # Ширина "хвоста" стрелки.
    arrow_x = np.array([-a, 0, -a])  # Координаты контура стрелки по x.
    arrow_y = np.array([b, 0, -b])  # Координаты контура стрелки по y.

    phi = math.atan2(VecY, VecX)  # Угол наклона вектора.

    RotX, RotY = rotation2D(arrow_x, arrow_y, phi)  # Вращаем стрелку по углу.

    arrow_x = RotX + X + VecX  # Смещаем стрелку по x.
    arrow_y = RotY + Y + VecY  # Смещаем стрелку по y.

    return arrow_x, arrow_y  # Возвращаем координаты стрелки.

# Функция для обновления данных на каждом кадре анимации.
def anim(i):
    Pnt.set_data(X[i], Y[i])  # Обновляем положение точки.

    RVector.set_data([0, X[i]], [0, Y[i]])  # Обновляем радиус-вектор.
    RArrow.set_data(Vect_arrow(X[i], Y[i], 0, 0))  # Обновляем стрелку радиус-вектора.

    VVector.set_data([X[i], X[i] + X_velocity[i]], [Y[i], Y[i] + Y_velocity[i]])  # Обновляем вектор скорости.
    VArrow.set_data(Vect_arrow(X_velocity[i], Y_velocity[i], X[i], Y[i]))  # Обновляем стрелку скорости.

    AVector.set_data([X[i], X[i] + X_acceleration[i]], [Y[i], Y[i] + Y_acceleration[i]])  # Обновляем вектор ускорения.
    AArrow.set_data(Vect_arrow(X_acceleration[i], Y_acceleration[i], X[i], Y[i]))  # Обновляем стрелку ускорения.

    RCVector.set_data([X[i], X[i] + X_rcurvature[i]], [Y[i], Y[i] + Y_rcurvature[i]])  # Обновляем вектор радиуса кривизны.
    RCArrow.set_data(Vect_arrow(X_rcurvature[i], Y_rcurvature[i], X[i], Y[i]))  # Обновляем стрелку радиуса кривизны.

    return

# Определяем параметр времени t как символ.
t = s.Symbol('t')

# Задаём радиус и угол в полярной системе координат.
r = 2 + s.cos(6 * t)  # Радиус.
phi = t + 1.2 * s.cos(6 * t)  # Угол.

# Переводим полярные координаты в декартовы.
x = r * s.cos(phi)  # Координата x.
y = r * s.sin(phi)  # Координата y.

# Вычисляем производные для скорости.
x_velocity = s.diff(x)  # Производная x, скорость по x.
y_velocity = s.diff(y)  # Производная y, скорость по y.

# Вычисляем производные для ускорения.
x_acceleration = s.diff(x_velocity)  # Производная скорости по x, ускорение по x.
y_acceleration = s.diff(y_velocity)  # Производная скорости по y, ускорение по y.

# Вычисляем величины скорости и ускорения.
Velocity = s.sqrt(x_velocity ** 2 + y_velocity ** 2)  # Величина скорости.
Acceleration = s.sqrt(x_acceleration ** 2 + y_acceleration ** 2)  # Величина ускорения.

# Вычисляем тангенциальное и нормальное ускорение.
Acceleration_t = s.diff(Velocity)  # Тангенциальное ускорение.
Acceleration_n = s.sqrt(Acceleration ** 2 - Acceleration_t ** 2)  # Нормальное ускорение.

# Вычисляем радиус кривизны.
RСurvature = (Velocity ** 2) / Acceleration_n

step = 2000  # Количество шагов.

T = np.linspace(0, 10, step)  # Создаём временной интервал.

# Создаём массивы для координат, скорости, ускорения и радиуса кривизны.
X = np.zeros_like(T)
Y = np.zeros_like(T)

X_velocity = np.zeros_like(T)
Y_velocity = np.zeros_like(T)

X_acceleration = np.zeros_like(T)
Y_acceleration = np.zeros_like(T)

X_rcurvature = np.zeros_like(T)
Y_rcurvature = np.zeros_like(T)

# Заполняем массивы значениями, подставляя время в символьные выражения.
for i in np.arange(len(T)):
    X[i] = s.Subs(x, t, T[i])  # Вычисляем координату x.
    Y[i] = s.Subs(y, t, T[i])  # Вычисляем координату y.

    X_velocity[i] = s.Subs(x_velocity, t, T[i])  # Скорость по x.
    Y_velocity[i] = s.Subs(y_velocity, t, T[i])  # Скорость по y.

    X_acceleration[i] = s.Subs(x_acceleration, t, T[i])  # Ускорение по x.
    Y_acceleration[i] = s.Subs(y_acceleration, t, T[i])  # Ускорение по y.

    Veloctity_angle = math.atan2(Y_velocity[i], X_velocity[i])  # Угол скорости.
    Acceleration_angle = math.atan2(Y_acceleration[i], X_acceleration[i])  # Угол ускорения.
    RСurvature_angle = Veloctity_angle - math.pi / 2 if Veloctity_angle - Acceleration_angle > 0 else Veloctity_angle + math.pi / 2  # Угол радиуса кривизны.

    X_rcurvature[i] = RСurvature.subs(t, T[i]) * math.cos(RСurvature_angle)  # Радиус кривизны по x.
    Y_rcurvature[i] = RСurvature.subs(t, T[i]) * math.sin(RСurvature_angle)  # Радиус кривизны по y.

fgr = plot.figure()  # Создаём окно для графика.

grf = fgr.add_subplot(1, 1, 1)  # Создаём координатную плоскость.
grf.axis('equal')  # Устанавливаем равный масштаб осей.
grf.set(xlim=[-10, 10], ylim=[-10, 10])  # Устанавливаем границы графика.
grf.plot(X, Y)  # Рисуем траекторию.

Pnt = grf.plot(X[0], Y[0], marker='o')[0]  # Рисуем начальную точку.

# Добавляем радиус-вектор, скорость, ускорение и радиус кривизны с их стрелками.
X_RArrow, Y_RArrow = Vect_arrow(X[0], Y[0], 0, 0)
RArrow = grf.plot(X_RArrow, Y_RArrow, 'black')[0]
RVector = grf.plot([0, X[0]], [0, Y[0]], 'black')[0]

X_VArrow, Y_VArrow = Vect_arrow(X_velocity[0], Y_velocity[0], X[0], Y[0])
VArrow = grf.plot(X_VArrow, Y_VArrow, 'r')[0]
VVector = grf.plot([X[0], X[0] + X_velocity[0]], [Y[0], Y[0] + Y_velocity[0]], 'r')[0]

X_AArrow, Y_AArrow = Vect_arrow(X_acceleration[0], Y_acceleration[0], X[0], Y[0])
AArrow = grf.plot(X_AArrow, Y_AArrow, 'g')[0]
AVector = grf.plot([X[0], X[0] + X_acceleration[0]], [Y[0], Y[0] + Y_acceleration[0]], 'g')[0]

X_RCArrow, Y_RCArrow = Vect_arrow(X_rcurvature[0], Y_rcurvature[0], X[0], Y[0])
RCArrow = grf.plot(X_RCArrow, Y_RCArrow, 'y')[0]
RCVector = grf.plot([X[0], X[0] + X_rcurvature[0]], [Y[0], Y[0] + Y_rcurvature[0]], 'y')[0]

an = FuncAnimation(fgr, anim, frames=step, interval=20)  # Создаём анимацию.

plot.show()  # Показываем график.