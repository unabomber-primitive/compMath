def check(a,b,f):
    if (a <= 0 and 0 <= b or b <= 0 and 0 <= a):
        try:
            f(0)
        except:
            return False
    return True

def solve_mid(a, b, f, step):
    n = 4
    h = (b - a) / n
    int_prev = 0
    integral = 0
    counter = 0
    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"
    while(((integral-int_prev)/3 >= step) or counter == 0):
        counter = 1
        int_prev = integral
        try:
            integral_sum = sum(f(a + h/2 + i * h) for i in range(n))
        except:
            pass

        integral = h * integral_sum
        n*=2
        h = (b - a) / n


    return [integral, n]

def solve_left(a, b, f, step):
    n = 4
    h = (b - a) / n
    int_prev = 0
    integral = 0
    counter = 0
    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"
    while(((integral-int_prev) >= step) or counter == 0):
        counter = 1
        int_prev = integral
        try:
            integral_sum = sum(f(a + i * h) for i in range(n))
        except:
            pass

        integral = h * integral_sum
        n*=2
        h = (b - a) / n

    return [integral, n]

def solve_right(a, b, f, step):
    n = 4
    h = (b - a) / n
    int_prev = 0
    integral = 0
    counter = 0
    if (not check(a,b,f)): return "Integrated function has discontinuity or does not defined in current interval"
    while(((integral-int_prev) >= step) or counter == 0):
        counter = 1
        int_prev = integral
        try:
            integral_sum = sum(f(a + (i + 1) * h) for i in range(n))
        except:
            pass

        integral = h * integral_sum
        n*=2
        h = (b - a) / n

    return [integral, n]
