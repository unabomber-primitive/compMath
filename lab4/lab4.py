import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def linear(x, y, loud=False):
    # returns coefs (a, b) in y = ax + b approximation
    SX = np.sum(x)
    SXX = np.sum(np.power(x, 2))
    SY = np.sum(y)
    SXY = np.dot(x, y)
    
    if loud:
        print(f'SX = {SX:.3f}')
        print(f'SXX = {SXX:.3f}')
        print(f'SY = {SY:.3f}')
        print(f'SXY = {SXY:.3f}')
    
    n = np.size(x)
    delta = SXX * n - SX * SX
    delta_1 = SXY * n - SX * SY
    delta_2 = SXX * SY - SX * SXY
    
    if loud:
        print(f'delta = {delta:.3f}')
        print(f'delta_1 = {delta_1:.3f}')
        print(f'delta_2 = {delta_2:.3f}')
    
    a, b = delta_1/delta, delta_2/delta

    return a, b

def gen_linear(a, b):
    return lambda x: a*x+b

def triangle(n: int, matrix: np.ndarray):
    swaps = 0
    for i in range(n):
        if matrix[i][i] == 0:
            k = i + 1
            while k < n and matrix[k][i] == 0:
                k += 1
            if k < n:
                matrix[i], matrix[k] = matrix[k], matrix[i]
                swaps += 1
            else:
                return -1
        for j in range(i + 1, n):
            if matrix[j][i] != 0:
                matrix[j] -= matrix[i] * (matrix[j][i] / matrix[i][i])    
    return swaps

def solve(n: int, matrix: np.ndarray):
    swaps = triangle(n, matrix)
    if swaps == -1:
        return None
    solution = np.linspace(0, 0, n)
    for i in range(n-1, -1, -1):
        solution[i] = matrix[i][n] - sum([matrix[i][j] * solution[j] for j in range(n-1, i, -1)])
        solution[i] /= matrix[i][i]
    return solution

def polinom(x, y, n, loud=False):
    matrix = np.ndarray((n+1, n+2))
    for i in range(n+1):
        for k in range(n+1):
            matrix[i][k] = np.sum(np.power(x, i + k))
        matrix[i][n+1] = np.dot(y, np.power(x, i))
    if loud:
        print("Matrix: ")
        for i in range(n+1):
            for k in range(n+1):
                print(f'{matrix[i][k]:.3f}\t', end='')
            print(f'| {matrix[i][n+1]:.3f}')
    return solve(n+1, matrix)

def gen_polinom(coefs):
    return lambda x: sum([coefs[i] * np.power(x, i) for i in range(len(coefs))])

def power(x, y):
    if np.min(x) <= 0: 
        return None
    if np.min(y) <= 0:
        return None
    a, b = linear(np.log(x), np.log(y))
    return np.exp(a), b

def gen_power(a, b):
    return lambda x: a * np.power(x, b)

def exponent(x, y):
    if np.min(y) <= 0:
        return None
    a, b = linear(x, np.log(y))
    return np.exp(b), a

def gen_exponent(a, b):
    return lambda x: a * np.exp(b * x)

def logarithm(x, y):
    if np.min(x) <= 0: 
        return None
    return linear(np.log(x), y)

def gen_logarithm(a, b):
    return lambda x: a * np.log(x) + b

def corr(x, y):
    avg_x = np.average(x)
    avg_y = np.average(y)
    x = x - avg_x
    y = y - avg_y
    return np.dot(x, y) / np.sqrt(np.dot(x, x) * np.dot(y, y))

def delta(x, y, f):
    diff = y - f(x)
    return np.sqrt(np.dot(diff, diff) / np.size(x))

def clear_axes(arr):
    arr.sort()
    delta = (arr[-1] - arr[0]) * 0.05
    to_del = []
    
    for i in range(len(arr) - 1):
        # print(i + 1, i, arr[i + 1], arr[i], sep='\t')
        if abs(arr[i + 1] - arr[i]) < delta:
            to_del.append(i)
    
    arr = np.delete(arr, to_del)
    return arr

def draw(x, y, f):
    min_x = np.min(x)
    l = min_x * 0.9 if min_x > 0 else min_x * 1.1
    max_x = np.max(x)
    r = max_x * 1.1 if max_x > 0 else max_x * 0.9

    plt.plot(x, y, '.k')
    plt.plot(np.linspace(l, r, 100), f(np.linspace(l, r, 100)))
    
    xticks = clear_axes(list(x))
    yticks = clear_axes(list(y) + list(f(x)))
    plt.xticks(xticks, map(lambda x: round(x * 100) / 100, xticks))
    plt.yticks(yticks, map(lambda x: round(x * 100) / 100, yticks), fontsize=8)

if __name__ == "__main__":
    sns.set_theme()

    dataset = pd.read_csv('log2.txt')
    x, y = dataset['x'], dataset['y']

    method_name = ['ax+b', 'ax^2+bx+c', 'ax^3+bx^2+cx+d',
                   'ax^b', 'a * exp(bx)', 'a*ln(x) + b']
    # method_name = ['ax+b', 'ax^2+bx+c']
    method_coefs = [linear, lambda x,y: polinom(x,y,2),
                    lambda x,y: polinom(x,y,3), power,
                    exponent, logarithm]
    # method_coefs = [linear, lambda x,y: polinom(x, y, 2)]

    method_func_gen = [gen_linear, lambda a, b, c: gen_polinom((a, b, c)),
                       lambda a, b, c, d: gen_polinom((a,b,c,d)), 
                       gen_power, gen_exponent, gen_logarithm]
    # method_func_gen = [gen_linear, lambda a, b, c: gen_polinom((a, b, c))]

    min_method = 0
    min_diff = float('inf')
    for method in range(len(method_name)):
        print(f"name: {method_name[method]}")

        coefs = method_coefs[method](x, y)
        if coefs is None:
            print("Impossible")
            continue

        f = method_func_gen[method](*coefs)
        diff = delta(x,y,f)
        if diff < min_diff:
            min_method = method
            min_diff = diff
        if method == 0:
            print(f"corr: {corr(x,y):.3f}")
        print(f"coefs: ",end='')
        print(*reversed(list(map(lambda x: round(x*1000)/1000, coefs))))
        print(f"delta: {diff:.3f}")
        print(f"x,\ty,\tphi(x),\tdelta")
        for i in range(len(x)):
            print(f"{x[i]:.3f},\t{y[i]:.3f},\t{f(x[i]):.3f},\t{f(x[i])-y[i]:.3f}")
        # draw(x, y, method_func_gen[method](*method_coefs[method](x, y)))
    print("Min method: ", method_name[min_method])
    draw(x,y,method_func_gen[min_method](*method_coefs[min_method](x,y)))
    plt.show()