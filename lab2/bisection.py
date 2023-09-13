def bisection(f, a, b, eps):
    x = (b + a) / 2
    f_x = f(x)
    
    if abs(b - a) < eps or abs(f_x) < eps:
        print(f'x = {x:.3f}, f(x) = {f_x:.3f}')
        return 1
    
    if(f_x * f(a) < 0):
        return bisection(f, a, x, eps) + 1
    else:
        return bisection(f, x, b, eps) + 1
