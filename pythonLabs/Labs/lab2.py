# Минимум из двух чисел. Даны два целых числа. Выведите
# значение наименьшего из них.

def lab2_task1():
    a = int(input("a: "))
    b = int(input("b: "))
    if a > b:
        print(a)
    else:
        print(b)

lab2_task1()