def calculate_integral(a, b, fun, epsilon):
    n = 4
    h = (b - a) / n
    int_prev = 0
    integral = 0
    counter = 0

    try:
        integral = 0.5 * (fun(a) + fun(b)) * h
    except:
        return [False,"Отрезок не подходит под ОДЗ"]
    
    while(((integral-int_prev)/3 >= epsilon) or counter == 0):
        counter = 1
        int_prev = integral
        integral = 0
        for i in range(1, n):
            x = a + i * h
            try:
                integral += fun(x)
            except:
                pass
        integral*=h
        n*=2
        h = (b - a) / n

    return [True, [integral, n]]
