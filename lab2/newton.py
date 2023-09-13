def newton_validate(f, f_der_zeros, f_der_der_zeros, a, b):
    for zero in f_der_zeros:
        if zero >= a and zero <= b:
            return False
    for zero in f_der_der_zeros:
        if zero >= a and zero <= b:
            return False
    
    return True

def newton_x0(f, f_der_der, a, b):
    if(f(a) * f_der_der(a) > 0):
        return a
    else:
        return b
    
def newton(f, f_der, x, eps):
    f_x = f(x)
    f_der_x = f_der(x)
    x1 = x - f_x / f_der_x
    if abs(x1 - x) <= eps or abs(f_x / f_der_x) <= eps or abs(f(x1)) <= eps:
        print(f'x = {x1:.3f}, f(x) = {f(x1):.3f}')
        return 1
    
    return newton(f, f_der, x1, eps) + 1