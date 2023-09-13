import numpy as np

def simple_it_params(f_der, f_der_der_zeros, a, b):
    candidates = [f_der(a), f_der(b)]
    for zero in f_der_der_zeros:
        if zero >= a and zero <= b:
            candidates.append(f_der(zero))

    lamb = -1 / np.max(candidates)
    q = 1 + np.min(candidates) * lamb
    return lamb, q

def phi(f, lamb, x):
    return x + lamb * f(x)

def simple_it(f, lamb, x, eps):
    x1 = phi(f, lamb, x)
    if abs(x1 - x) <= eps:
        print(f'x = {x1:.3f}, f(x) = {f(x1):.3f}')
        return 1
    
    return simple_it(f, lamb, x1, eps) + 1