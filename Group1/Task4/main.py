import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, sqrt, abs
from scipy.integrate import quad
from scipy.misc import derivative

print("y(x)")
f_y = input()

print("g(x)")
g_x = input()

print("x(x)")
f_x = input()


def fy_(x):
    return derivative(fy, x, dx=0.0001)


def fy(x):
    return eval(f_y)


def fx(x):
    return eval(f_x)


def fx_(x):
    return derivative(fx, x, dx=0.0001)


def g(x):
    return eval(g_x)


def pre_length(x):
    return np.sqrt(fx_(x)**2 + fy_(x)**2)


def length(x):
    res = quad(pre_length, 0, x)
    return res[0]


def numerator(x):
    return g(length(x))


def drib(x):
    return numerator(x)/pre_length(x)


numbers = np.linspace(-100, 100, 1000)

x_elems = []
y_elems = []
first = []
second = []

for elem in numbers:
    temp = drib(elem)

    temp_x = fx(elem) + temp*fy_(elem)
    temp_y = fy(elem) + temp*(-fx_(elem))
    first.append(temp_x)
    second.append(temp_y)
    x_elems.append(fx(elem))
    y_elems.append(fy(elem))

plt.plot(x_elems, y_elems, color="red")
plt.plot(first, second, color="blue")
plt.gca().set_aspect('equal')
plt.show()
