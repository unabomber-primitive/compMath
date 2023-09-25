import numpy as np
from matplotlib import pyplot as plt

def f1(x, y):
    return y + (1 + x) * np.power(y, 2)

def c1(x, y):
    return -np.exp(x) / y - x*np.exp(x)

def s1(x, C):
    return -np.exp(x) / (x * np.exp(x) + C)

def f2(x, y):
    return y + 2 * x

def c2(x, y):
    return (y + 2 * x + 2) / (np.exp(x))

def s2(x, C):
    return C * np.exp(x) - 2 * x - 2

def diff(y_h, y_h2, p):
    return abs(y_h - y_h2) / (2 ** p - 1)

def runge_rule(f, h0, p, eps):
    r0 = f(h0)
    r1 = f(h0 / 2)
    deep = 0
    while diff(r0, r1, p) > eps and deep < 5:
        deep += 1
        h0 /= 2
        r0 = r1
        r1 = f(h0)
    return r0, h0

def apply_with_eps(x0, y0, h0, xn, f, stage, p, eps):
    xs = [x0]
    ys = [y0]
    hs = [h0]

    cnt = 0
    while xn - xs[-1] > 0.01 and cnt < 100:
        y, h = runge_rule(lambda h: stage(xs[-1], ys[-1], h, f), hs[-1], p, eps)
        
        ys.append(y)
        xs.append(xs[-1] + h)
        hs.append(h)
    
    return xs, ys, hs
            
def eiler_stage(x, y, h, f):
    return y + h * f(x, y)

def eiler(x0, y0, h0, xn, f, eps):
    return apply_with_eps(x0, y0, h0, xn, f, eiler_stage, 1, eps)

def mod_eiler_stage(x, y, h, f):
    return y + (h/2) * (f(x, y) + f(x+h, eiler_stage(x, y, h, f)))

def mod_eiler(x0, y0, h0, xn, f, eps):
    return apply_with_eps(x0, y0, h0, xn, f, mod_eiler_stage, 2, eps)

def runge_stage(x, y, h, f):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def runge(x0, y0, h0, xn, f, eps):
    return apply_with_eps(x0, y0, h0, xn, f, runge_stage, 4, eps)

def apply_multistaged(x0, y0, h, xn, f, stage, k):
    xs = [x0]
    ys = [y0]
    fs = [f(x0, y0)]

    for _ in range(1, k):
        ys.append(runge_stage(xs[-1], ys[-1], h, f))
        xs.append(xs[-1] + h)
        fs.append(f(xs[-1], ys[-1]))
    
    while xn >= xs[-1]:
        ys.append(stage(xs, ys, fs, h))
        xs.append(xs[-1] + h)
        fs.append(f(xs[-1], ys[-1]))
    
    return xs, ys, [h] * len(xs) 

def apply_multistage_with_eps(x0, y0, h, xn, f, stage, k, p, eps):
    y, h = runge_rule(lambda h: apply_multistaged(x0, y0, h, xn, f, stage, k)[1][-1], h, p, eps)
    return apply_multistaged(x0, y0, h, xn, f, stage, k)

def adams_stage(xs, ys, fs, h):
    d1_f = fs[-1] - fs[-2]
    d2_f = fs[-1] - 2 * fs[-2] + fs[-3]
    d3_f = fs[-1] - 3 * fs[-2] + 3 * fs[-3] - fs[-3]
    return ys[-1] + h * fs[-1] + (h ** 2) * d1_f / 2 + 5 * (h ** 3) * d2_f / 12 + 3 * (h ** 4) * d3_f / 8

def adams(x0, y0, h, xn, f, eps):
    return apply_multistage_with_eps(x0, y0, h, xn, f, adams_stage, 4, 4, eps)

if __name__ == "__main__":
    fs = [f1, f2]
    solution = [s1, s2]
    c = [c1, c2]

    print("(1) dy = y + (1 + x) * y^2")
    print("(2) dy = 2x + y")

    f_type = int(input("Введите номер уравнения: ")) - 1
    x0, y0 = map(float, input("Введите (x0,y0) через пробел: ").split(' '))
    xn = float(input("Введите границу диффернцирования x_n: "))
    h0 = float(input("Введите шаг h: "))
    eps = float(input("Введите точность eps: "))

    f = fs[f_type]

    methods = [eiler, mod_eiler, runge, adams]
    name = ['эйлера', 'модифицированный эйлер', 'рунге-кутта', 'адамса']

    for m in range(len(methods)):
        print(f"Метод {name[m]}:")
        x, y, h = methods[m](x0, y0, h0, xn, f, eps)

        print("i\tx\th\ty\ty_real")
        for i in range(len(x)):
            print(f"{i}\t{x[i]:.3f}\t{h[i]:.3f}\t{y[i]:.3f}\t{solution[f_type](x[i], c[f_type](x0, y0)):.3f}")
        plt.plot(x, y, label=f'Метод {name[m]}')
    plt.plot(np.linspace(x[0], x[-1], 1000), solution[f_type](np.linspace(x[0], x[-1], 1000), c[f_type](x0, y0)), label='Точное решение')
    plt.legend()
    plt.show()