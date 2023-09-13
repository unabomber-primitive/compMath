import rectangle_methods as rm
import simpson_method as sm
import trapezoid_rule as tr
import functions

functions.print_functions()

method = input("""
    Выберите используемый метод (число):
    • Метод прямоугольников - 1
    • Метод трапеций - 2
    • Метод Симпсона - 3
    """)
fn = int(input("Номер функции: "))
a = int(input("Левая граница: "))
b = int(input("Правая граница: "))
eps = float(input("Точность: "))

if(method == "1"):
    left = rm.solve_left(a,b,functions.get_function(fn),eps)
    mid = rm.solve_mid(a,b,functions.get_function(fn),eps)
    right = rm.solve_right(a,b,functions.get_function(fn),eps)
    print(f"""
    • Метод левых прямоугольников (интеграл, число разбиений): {left[0]}, n = {left[1]}
    • Метод средних прямоугольников (интеграл, число разбиений): {mid[0]}, n = {mid[1]}
    • Метод правых прямоугольников (интеграл, число разбиений): {right[0]}, n = {right[1]}
      """)
elif(method == "2"):
    res = tr.calculate_integral(a,b,functions.get_function(fn),eps)

    if res[0]:
        print(f"Значение интеграла: {res[1][0]}, n = {res[1][1]}")
    else:
        print(f"{res[1]}")
elif(method == "3"):
    try:
        res = sm.calculate_integral(a,b,functions.get_function(fn),eps)
        print(f"Значение интеграла: {res[0]}, n = {res[1]}")
    except Exception as e:
        print(e)
else:
    print("Ошибка ввода: вводить необходимо целое число от 1 до 3")
