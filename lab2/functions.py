import numpy as np

def f0(x):
    return x - np.cos(x)

def f0_der(x):
    return 1 + np.sin(x)

def f0_der_der(x):
    return np.cos(x)

def f1(x):
    return np.power(x, 3) - x + 4

def f1_der(x):
    return 3*np.power(x, 2) - 1

def f1_der_der(x):
    return 6*x

def f2(x):
    return np.power(x, 3) - 5 * np.power(x, 2) + 3 * x + 1

def f2_der(x):
    return 3*np.power(x, 2) - 10 * x + 3

def f2_der_der(x):
    return 6*x - 10

def phi1_1(x, y):
    return -0.1*np.power(x, 2) - 0.2*np.power(y, 2) + 0.3

def phi1_2(x, y):
    return -0.2*np.power(x, 2) + 0.7 - 0.1 * x * y

def phi1_1_der_x(x, y):
    return -0.2*x

def phi1_1_der_y(x, y):
    return -0.4*y

def phi1_2_der_x(x, y):
    return -0.4*x - 0.1*y

def phi1_2_der_y(x, y):
    return -0.1 * x

def phi2_1(x, y):
    return -np.power(x, 2) - 0.5 * np.power(y, 2) - 0.4

def phi2_2(x, y):
    return -0.1*np.power(x, 2) - np.power(y, 2)

def phi2_1_der_x(x, y):
    return -2*x

def phi2_1_der_y(x, y):
    return -1 * y

def phi2_2_der_x(x, y):
    return -0.2*x

def phi2_2_der_y(x, y):
    return -2 * y

def f1_1(x, y):
    return 0.1*x**2 + x + 0.2*y **2 - 0.3

def f1_2(x, y):
    return 0.2*x**2 + y + 0.1 * x * y - 0.7

def f2_1(x, y):
    return x**2 + 2*x + 0.5*y**2 + 0.4

def f2_2(x, y):
    return 0.1*x**2 + y + y**2