import matplotlib.pyplot as plt
import seaborn as sns
from functions import *
from simple_iteration import *
from newton import *
from bisection import *

def roots_amount(f, f_der_zeros, a, b):
    for zero in f_der_zeros:
        if zero > a and zero < b:
            return roots_amount(f, f_der_zeros, a, zero) + roots_amount(f, f_der_zeros, zero, b)

    if(f(a) * f(b) < 0):
        return 1
    return 0 

def single():
    fs = [f0, f1, f2]
    f_ders = [f0_der, f1_der, f2_der]
    f_der_zeros = [[-np.pi / 2 - 2*np.pi, -np.pi / 2, -np.pi/2 + 2*np.pi], [-0.577, 0.577], [0.333, 3]]
    f_der_ders = [f0_der_der, f1_der_der, f2_der_der]   
    f_der_der_zeros = [[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], [0], [10/6]]

    print('Functions list:')
    print('(0) y = x - cos(x)')
    print('(1) y = x**3 - x + 4')
    print('(2) y = x**3 - 5x**2 + 3x + 1')
    f_idx = int(input('Choose one: '))
    
    if f_idx < 0 or f_idx > 2:
        print('Invalid number. Bye.')
        return

    a, b = map(float, input('Choose borders(separate by whitespace): ').split(' '))
    
    roots_num = roots_amount(fs[f_idx], f_der_zeros[f_idx], a, b)
    
    if roots_num == 0:
        print('There is no roots. Bye.')
        return
    
    if roots_num > 1:
        print('There is more than one root. Bye.')
        return
    
    x0_flag = int(input('Do you want to choose x0(0 or 1): '))
    x0 = None
    if(x0_flag):
        x0 = float(input('Choose x0: '))
        if x0 < a or x0 > b:
            print('Invalid x0, choose from [a, b]. Bye.')
            return
        
    eps = float(input('Choose epsilon: '))
    if(eps <= 0):
        print('Invalid epsilon. Choose epsilon > 0. Bye.')
    
    print('Method list: ')
    print('(0) Bisection')
    print('(1) Newton')
    print('(2) Simple Iteration')

    method_idx = int(input('Choose method: '))
    if method_idx < 0 or method_idx > 2:
        print('Invalid method idx. Bye.')
        return
    
    if method_idx == 0:
        res = bisection(fs[f_idx], a, b, eps)
        print('Iteration count:', res)
    
    if method_idx == 1:
        if not newton_validate(fs[f_idx], f_der_zeros[f_idx], f_der_der_zeros[f_idx], a, b):
            print("Newtown's method can't be applyed to this range")
            return

        if x0 == None:
            x0 = newton_x0(fs[f_idx], f_der_ders[f_idx], a, b)
        
        res = newton(fs[f_idx], f_ders[f_idx], x0, eps)
        print('Iteration count:', res)
    
    if method_idx == 2:
        lamb, q = simple_it_params(f_ders[f_idx], f_der_der_zeros[f_idx], a, b)
        if q >= 1:
            print("Simple iterations method can't be applyed to this range")
            return
        
        if x0 == None:
            x0 = (a + b) / 2

        res = simple_it(fs[f_idx], lamb, x0, eps)
        print('Iteration count:', res)

    xs = np.linspace(a - abs(0.1*a), b + abs(0.1*b), 1000)
    sns.set_theme()
    plt.plot(xs, fs[f_idx](xs), '.k', markersize=0.5)
    plt.show()
