# Обувная фабрика собирается начать выпуск элитной модели ботинок.
# Дырочки для шнуровки будут расположены в два ряда, расстояние между рядами равно a,
# а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N.
# Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, наверх,
# по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было
# завязать элитным бантиком, длина свободного конца шнурка должна быть l.
# Какова должна быть длина шнурка для этих ботинок?
#
# Программа получает на вход четыре натуральных числа a, b, l и N — именно в таком порядке
# — и должна вывести одно число — искомую длину шнурка.
import math


def lab1_task6():
    row_distance = int(input())
    column_distance = int(input())
    free_length = int(input())
    nodes_amount = int(input())
    result = 2 * free_length + (2 * nodes_amount - 1) * row_distance + 2 * (nodes_amount - 1) * column_distance
    print(f'Result: {result}')


# Минимум из двух чисел. Даны два целых числа. Выведите
# значение наименьшего из них.

def lab2_task1():
    a = int(input("a: "))
    b = int(input("b: "))
    print(min(a, b))


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


# По данному натуральному n ≤ 9 выведите лесенку
# из i ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

def lab4_task10():
    top_number = int(input("i: "))
    for temp_top_number in range(1, top_number + 1):
        print(*range(1, temp_top_number + 1))


# Дана строка. Найдите в этой строке второе
# вхождение буквы f, и выведите индекс этого вхождения. Если буква f в данной
# строке встречается только один раз, выведите число -1, а если не встречается
# ни разу, выведите число -2

def lab5_task6():
    word = input('word: ')
    if word.count('f') < 1:
        print(-2)
    elif word.count('f') == 1:
        print(-1)
    else:
        print(word.find('f', word.find('f') + 1))


# Количество элементов, которые больше предыдущего.
# Последовательность состоит из натуральных чисел и завершается числом 0
# Определите, сколько элементов этой последовательности больше предыдущего элемента.

def lab6_task11():
    element = int(input('-> '))
    elements_greater_than_prev = 0
    while element != 0:
        next_element = int(input('-> '))
        if next_element > element:
            elements_greater_than_prev += 1
        element = next_element
    print(elements_greater_than_prev)


# Дан список чисел. Определите,
# сколько в этом списке элементов, которые больше двух своих соседей, и
# выведите количество таких элементов. Крайние элементы списка никогда не
# учитываются, поскольку у них недостаточно соседей.

def lab7_task5():
    print('Input your list')
    given_list = [int(number) for number in input().split()]
    elements_greater_than_neighbors = 0
    for index in range(1, len(given_list) - 1):
        if given_list[index - 1] < given_list[index] > given_list[index + 1]:
            elements_greater_than_neighbors += 1
    print(elements_greater_than_neighbors)


# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
# а используя рекуррентное соотношение an=a⋅an-1.
# Решение оформите в виде функции power(a, n).

def power(a, n):
    if n != 0:
        return a * power(a, n - 1)
    else:
        return 1


# Найдите индексы первого вхождения максимального элемента.
# Выведите два числа: номер строки и номер столбца,
# в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот,
# у которого меньше номер строки, а если номера строк равны то тот,
# у которого меньше номер столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.


def lab9_task1():
    rows = int(input("Number of rows: "))
    columns = int(input("Number of columns: "))
    matrix = [[int(input()) for x in range(columns)] for y in range(rows)]
    print(f'Matrix: {matrix}')
    max_element = matrix[0][0]
    max_element_row, max_element_column = 0, 0
    for row_index in range(rows):
        for column_index in range(columns):
            if matrix[row_index][column_index] > max_element:
                max_element = matrix[row_index][column_index]
                max_element_row, max_element_column = row_index, column_index

    print(f'Row: {max_element_row}, Column: {max_element_column}')


