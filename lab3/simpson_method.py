
def calculate_integral(a, b, f, epsilon):
    n = 2
    w = (b - a) / n
    int_prev = 0
    integral = 0
    counter = 0
    while((abs(integral-int_prev)/15 >= epsilon) or counter == 0):
        counter = 1
        int_prev = integral
        integral = 0
        for i in range(n):
            x1 = a + i * w
            x2 = a + (i + 1) * w

            try:
                integral += (x2 - x1) / 6.0 * (f(x1) + 4.0 * f(0.5 * (x1 + x2)) + f(x2))
            except:
                if i == 0:
                    raise ValueError("Integrated function has discontinuity or does not defined in current interval")
                pass
        n*=2
        w = (b - a) / n


    return [integral, n*2]
