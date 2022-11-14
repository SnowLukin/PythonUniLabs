
# Улитка ползет по вертикальному шесту высотой h метров,
# поднимаясь за день на a a метров, а за ночь спускаясь на b метров.
# На какой день улитка доползет до вершины шеста?
# Программа получает на вход натуральные числа h, a, b.
# Программа должна вывести одно натуральное число. Гарантируется, что a>b.

def lab3_task9():
    column_height = int(input("Column height: "))
    up = int(input("Up: "))
    down = int(input("Down: "))

    # a_n = a1 + d(n-1), where d = a2 - a1
    # a_n / d = a1 / d + n - 1
    # n = a_n / d - a1 / d + 1

    first_day_max_distance = up
    second_day_max_distance = 2 * up - down
    delta = second_day_max_distance - first_day_max_distance

    result = column_height / delta - first_day_max_distance / delta + 1
    print(result)

lab3_task9()