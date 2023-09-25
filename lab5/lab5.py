import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from math import factorial

def input_x_y():
    n = int(input("Количество точек: "))
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(float, input().split(' '))
        xs.append(x)
        ys.append(y)
    return np.array(sorted(xs)), np.array(sorted(ys))

def file_x_y():
    filename = input("Введите название файла: ")
    f = open(filename)
    xs = []
    ys = []
    for line in f:
        x, y = map(float, line.split(' '))
        xs.append(x)
        ys.append(y)
    zipped = sorted(zip(xs, ys), key=lambda x: x[0])
    return [i[0] for i in zipped], [i[1] for i in zipped]

def f1(x):
    return np.sin(x)

def f2(x):
    return np.log(np.sin(np.cos(x)) + 1)

def f3(x):
    return np.exp(np.power(x, -1))

def fun_x_y():
    print("(1) sin(x) ")
    print("(2) ln(sin(cos(x)) + 1)")
    print("(3) exp(x^-1)")
    
    fs = [f1, f2, f3]

    f_type = int(input('Выберите функцию: '))
    a, b = map(float, input('Введите интервал: ').split(' '))
    dots = int(input('Введите количество точек: '))
    
    x = np.linspace(a, b, dots)
    y = fs[f_type-1](x)
    return x, y, fs[f_type-1]

def lagrange(x, y, x0):
    res = 0
    for i in range(len(x)):
        sum = y[i]
        for k in range(len(x)):
            if i == k:
                continue
            sum *= ((x0 - x[k]) / (x[i] - x[k]))
        res += sum
    return res

def check_eq_diff(x):
    if len(x) == 1:
        return False
    diff = x[1] - x[0]
    for i in range(len(x) - 1):
        if abs(diff - (x[i + 1] - x[i])) >= 0.01:
            return False
    return True 

def diff(y):
    res = [y]
    for i in range(1, len(y)):
        res.append([])
        for k in range(len(res[i-1]) - 1):
            res[i].append(res[i-1][k+1] - res[i-1][k])
    return res

def to_gauss_idx(i, n):
    mid = n // 2 - 1 + (n % 2)
    if i <= mid:
        return -(mid - i)
    return i - mid

def from_gauss_idx(i, n):
    return n // 2 - 1 + (n % 2) + i

def right_gauss(table, n, t):
    res = 0
    for i in range(len(y)):
        m = table[i][from_gauss_idx(-(i // 2), len(x))]
        for k in range(1, i+1):
            m *= (t - ((-1) ** (k % 2)) * (k // 2))
        m /= factorial(i)
        res += m
    return res

def left_gauss(table, n, t):
    res = 0
    for i in range(len(y)):
        m = table[i][from_gauss_idx(-((i + 1) // 2), len(x))]
        for k in range(1, i+1):
            m *= (t + ((-1) ** (k % 2)) * (k // 2))
        m /= factorial(i)
        res += m
    return res

def check_gauss(x, y):
    return (check_eq_diff(x) and len(x) % 2 == 1)

def gauss(x, y, x0):
    table = diff(y)

    h = x[1] - x[0] 
    t = (x0 - x[from_gauss_idx(0, len(x))]) / h

    if abs(x0 - x[from_gauss_idx(0, len(x))]) < 0.01:
        return y[from_gauss_idx(0, len(x))]
    
    if x0 > x[from_gauss_idx(0, len(x))]:
        return right_gauss(table, len(x), t)
    return left_gauss(table, len(x), t)

def check_stirling(x, y):
    return (check_eq_diff(x) and len(x) % 2 == 1)

def stirling(x, y, x0):
    table = diff(y)

    h = x[1] - x[0]
    t = (x0 - x[len(x) // 2]) / h

    res = left_gauss(table, len(x), t)
    res += right_gauss(table, len(x), t)
    res /= 2

    return res

def check_bessel(x, y):
    return (check_eq_diff(x) and len(x) % 2 == 0)

def bessel(x, y, x0):
    table = diff(y)

    h = x[1] - x[0]
    t = (x0 - x[from_gauss_idx(0, len(x))]) / h

    res = 0
    for i in range(0, len(x)):
        if i % 2 == 0:
            m = 1
            if i != 0:
                m = t
            
            for k in range(1, i // 2):
                m *= (t - k) * (t + k)
            
            m *= (t - i // 2)
            
            m /= factorial(i)
            m *= (table[i][from_gauss_idx(0 - (i // 2), len(x))] + table[i][from_gauss_idx(1 - (i // 2), len(x))]) / 2
            res += m
        else:
            m = (t - 0.5)
            if i != 1:
                m *= t
            for k in range(1, i // 2):
                m *= (t - k) * (t + k)
            
            m *= (t - i // 2)

            m /= factorial(i)
            m *= (table[i][from_gauss_idx(0 - (i // 2), len(x))])
            res += m
    return res

def print_table(x, table):
    print('\tx\ty\tdy\t', end='')
    for i in range(2, len(x)):
        print(f'dy_{i}\t', end='')
    print()
    for i in range(len(x)):
        print(f'{to_gauss_idx(i, len(x))}\t{x[i]:.3f}\t', end='')
        for k in range(len(x) - i):
            print(f'{table[k][i]:.3f}\t', end='')
        print()

if __name__ == '__main__':
    # sns.set_theme()

    print("(1) Клавиатура")
    print("(2) Файл")
    print("(3) Функция")
    
    input_type = int(input('Выберите способ ввода данных: '))
    
    x = np.array([])
    y = np.array([])

    if input_type == 1:
        x,y = input_x_y()
    elif input_type == 2:
        x,y = file_x_y()
    elif input_type == 3:
        x,y,f = fun_x_y()
    else:
        exit()

    if len(x) < 2:
        print("Точек должно быть >= 2")
        exit()

    method = [lagrange, gauss, stirling, bessel]
    check = [lambda x,y: True, check_gauss, check_stirling, check_bessel]
    name = ['лагранжа', 'гаусса', 'стирлинга', 'бесселя']

    x0 = float(input("Введите точку: "))

    print_table(x,diff(y))
    
    xs = np.linspace(x[0], x[-1], 100)

    for m in range(len(method)):
        loc_x = x
        loc_y = y
        if not check[m](loc_x, loc_y):
            print(f"Невозможно применить метод {name[m]}")
            continue

        val = method[m](loc_x, loc_y, x0)
        print(f"Значение в точке методом {name[m]} {x0:.3f} = {val:.3f}")
        
        if input_type == 3:
            print(f"Разница с функцией {abs(f(x0) - val):.3f}")
        
        ys = [method[m](loc_x, loc_y, x0) for x0 in xs]

        plt.plot(xs, ys, label=f'метод {name[m]}')

    if input_type == 3:
        plt.plot(xs, f(xs), label='функция')
    plt.plot(x, y, 'k.')
    plt.legend()
    plt.show()
    