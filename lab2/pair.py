import numpy as np
from functions import *
import matplotlib.pyplot as plt



def pair_validate(phi_1_der_x, phi_1_der_y, phi_2_der_x, phi_2_der_y, x0, y0):
    x_min, x_max = x0 - abs(x0 * 0.2) - 0.1, x0+abs(x0 * 0.2) + 0.1
    y_min, y_max = y0 - abs(y0 * 0.2) - 0.1, y0+abs(y0 * 0.2) + 0.1

    if abs(phi_1_der_x(x_max, y_max)) + abs(phi_1_der_y(x_max, y_max)) >= 1:
        return False
    if abs(phi_2_der_x(x_max, y_max)) + abs(phi_2_der_y(x_max, y_max)) >= 1:
        return False
    if abs(phi_1_der_x(x_min, y_min)) + abs(phi_1_der_y(x_min, y_min)) >= 1:
        return False
    if abs(phi_2_der_x(x_min, y_min)) + abs(phi_2_der_y(x_min, y_min)) >= 1:
        return False
    
    return True

def pair_simple_it(f1, f2, phi_1, phi_2, x, y, eps):
    x1 = phi_1(x, y)
    y1 = phi_2(x, y)

    if abs(x1 - x) <= eps or abs(y1 - y) < eps:
        print(f'(x, y) = ({x1:.3f},{y1:.3f}), f1(x, y) = {f1(x1, y1):.3f}, f2(x, y) = {f2(x1, y1):.3f}') 
        return 1
    return pair_simple_it(f1, f2, phi_1, phi_2, x1, y1, eps) + 1

def pair():
    print('List of systems:')
    print('(0) 0.1a**2 + a + 0.2b**2 - 0.3 = 0 and 0.2a**2 + b + 0.1ab - 0.7 = 0')
    print('(1) a**2 + 2a + 0.5b**2 + 0.4 = 0 and 0.1a**2 + b + b**2 = 0')

    f_idx = int(input('Choose system num:'))

    x0, y0 = map(float, input('Input (x0, y0):').split(' '))

    xs = np.linspace(x0 - abs(x0 * 0.3) - 0.1, x0+abs(x0 * 0.3) + 0.1, 1000)
    ys = np.linspace(y0 - abs(y0 * 0.3) - 0.1, y0+abs(y0 * 0.3) + 0.1, 1000)
    X,Y = np.meshgrid(xs, ys)
    F0, F1 = None, None
    if f_idx == 0:
        F0 = 0.1*X**2 + X + 0.2*Y**2 - 0.3
        F1 = 0.2*X**2 + Y + 0.1 * X*Y - 0.7    
    else:
        F0 = X**2 + 2*X + 0.5 * Y**2 +0.4
        F1 = 0.1 * X**2 + Y + Y**2

    valid = True
    if f_idx == 0:
        valid = pair_validate(phi1_1_der_x, phi1_1_der_y, phi1_2_der_x, phi1_2_der_y, x0, y0)
    else:
        valid = pair_validate(phi2_1_der_x, phi2_1_der_y, phi2_2_der_x, phi2_2_der_y, x0, y0)
    if not valid:
        print("Couldn't be applyed in this zone")
        return
    
    eps = float(input('Input epsilon: '))
    
    res = 0
    if f_idx == 0:
        res = pair_simple_it(f1_1, f1_2, phi1_1, phi1_2, x0, y0, eps)
    else:
        res = pair_simple_it(f2_1, f2_2, phi2_1, phi2_2, x0, y0, eps)
    print('Iterations count: ', res)

    plt.figure()
    plt.contour(X, Y, F0, [0], colors='r')
    plt.contour(X, Y, F1, [0], colors='b')
    plt.show()