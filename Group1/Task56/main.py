import numpy as np
from numpy import sin, cos, tan, pi
from scipy.integrate import quad
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

start_ = eval(input("Enter start: "))
end_ = eval(input("Enter end: "))
fx = input("Enter f(x): ")
gx = input("Enter g(x): ")


def f(x):
    return eval(fx)


def g(x):
    return eval(gx)


def abs_fx_gx(x):
    return abs(f(x) - g(x))


def area(start: float, end: float):
    temp = quad(abs_fx_gx, start, end)
    return temp[0]


def rand_dots_create(start, end, top, bottom):
    dots = []
    for i in range(10000):
        dots.append([random.uniform(start, end), random.uniform(bottom, top)])

    return dots


def check_dots(dots):
    good_dots_x = []
    good_dots_y = []
    bad_dots_x = []
    bad_dots_y = []

    for i in range(len(dots)):
        if (f(dots[i][0]) > dots[i][1] > g(dots[i][0])) or (f(dots[i][0]) < dots[i][1] < g(dots[i][0])):
            good_dots_x.append(dots[i][0])
            good_dots_y.append(dots[i][1])
        else:
            bad_dots_x.append(dots[i][0])
            bad_dots_y.append(dots[i][1])

    return good_dots_x, good_dots_y, bad_dots_x, bad_dots_y


def max_min_points_finder(f_values, g_values):
    max_func_point = max(f_values) if max(f_values) > max(g_values) else max(g_values)
    min_func_point = min(f_values) if min(f_values) < min(g_values) else min(g_values)
    return max_func_point, min_func_point


def program(start, end):
    values_x = np.linspace(start, end, 1000)

    f_values = []
    g_values = []
    for elem in values_x:
        f_values.append(f(elem))
        g_values.append(g(elem))

    max_height, min_height = max_min_points_finder(f_values, g_values)

    dots = rand_dots_create(start, end, max_height, min_height)
    good_dots_x, good_dots_y, bad_dots_x, bad_dots_y = check_dots(dots)

    print("Precise area: " + str(area(start, end)))
    print("Approximate area: " + str(len(good_dots_x)/len(dots)*(end-start)*(max_height-min_height)))

    plt.scatter(good_dots_x, good_dots_y, color='yellow')
    plt.scatter(bad_dots_x, bad_dots_y)

    plt.plot(values_x, f_values, color='blue', label='f(x)')
    plt.plot(values_x, g_values, color='red', label='g(x)')
    plt.legend()
    plt.show()


program(start_, end_)


