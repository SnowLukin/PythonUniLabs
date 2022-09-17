import math

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

def lab1_task6():
    row_distance = int(input('a: '))
    column_distance = int(input('b: '))
    free_length = int(input('l: '))
    nodes_amount = int(input('n: '))
    result = 2 * free_length + (2 * nodes_amount - 1) * row_distance + 2 * (nodes_amount - 1) * column_distance
    print(f'Result: {result}')



# Минимум из двух чисел. Даны два целых числа. Выведите
# значение наименьшего из них.

def lab2_task1():
    a = int(input("a: "))
    b = int(input("b: "))
    if a > b:
        print(a)
    else:
        print(b)


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

    print(f'Row: {max_element_row + 1}, Column: {max_element_column + 1}')


# Даны два списка чисел. Посчитайте, сколько чисел
# содержится одновременно как в первом списке, так и во втором.

def lab10_task2():
    print(len(set(set(input().split()) & set(input().split()))))


# Политическая жизнь одной страны очень оживленная. В стране действует K политических
# партий, каждая из которых регулярно объявляет национальную забастовку.
# Дни, когда хотя бы одна из партий объявляет забастовку, при условии,
# что это не суббота или воскресенье (когда и так никто не работает), наносят большой ущерб экономике страны.
# i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i.
# То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д.
# Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.
# В календаре страны N дней, пронумерованных, начиная с единицы.
# Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.
# В первой строке даны числа N и K. Далее идет K строк, описывающие
# графики проведения забастовок. i-я строка содержит числа a_i и b_i.
# Вам нужно определить число забастовок, произошедших в этой стране в течении года.

def lab10_task12():
    days = int(input('N: '))
    polit_parties = int(input('K: '))
    # without Saturday and Sunday
    work_days = set([day for day in range(days) if day % 7 < 5])
    no_actions = set(work_days)
    for party in range(polit_parties):
        print(f'Party: {party + 1}')
        a = int(input('a: '))
        b = int(input('b: '))
        # b + 1 to count the first day of action
        max_actions_amount = (days - a) // b + 1
        no_actions -= {a + b * i for i in range(max_actions_amount)}
    print(len(work_days) - len(no_actions))

# Родословная: предки и потомки. Даны два элемента в дереве.
# Определите, является ли один из них потомком другого.
# Во входных данных записано дерево в том же формате, что и в
# предыдущей задаче Далее идет число запросов . В каждой из следующих
# строк, содержатся имена двух элементов дерева.
# Для каждого такого запроса выведите одно из трех чисел: 1, если первый
# элемент является предком второго, 2, если второй является предком первого
# или 0, если ни один из них не является предком другого.
# 9
# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# 3
# Anna Nicholaus_I
# Peter_II Peter_I
# Alexei Paul_I


def is_ancestor(human, possible_ancestor, tree):
    if human == possible_ancestor:
        return True
    while human in tree:
        human = tree[human]
        if human == possible_ancestor:
            return True
    return False


def lab11_task12():
    tree = {}
    n = int(input('N: '))
    for i in range(n - 1):
        child, parent = input().split()
        tree[child] = parent
    print(tree)
    for i in range(int(input('K: '))):
        first, second = input().split()
        if is_ancestor(second, first, tree):
            print(1)
        elif is_ancestor(first, second, tree):
            print(2)
        else:
            print(0)


# Самое длинное слово в файле. В данном задании вы должны
# написать программу, которая будет находить самое длинное слово в файле. В
# качестве результата программа должна выводить на экран длину самого
# длинного слова и все слова такой длины. Для простоты принимайте за
# значимые буквы любые непробельные символы, включая цифры и знаки
# препинания.
# Example:
# ['один', 'два', 'самое_длинное_слово1', 'не_самое', 'почтиСамое_длинное', 'самое_длинное_слово2']
# Максимальная длина слова: 20
# Слова: ['самое_длинное_слово1', 'самое_длинное_слово2']

def lab12_task5():
    words = open("Lab12SampleText.txt", "r").read().split()
    print(words)
    max_length_words = []
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            max_length_words = [word]
        elif len(word) == max_length:
            max_length_words.append(word)
    print(f'Максимальная длина слова: {max_length}')
    print(f'Слова: {max_length_words}')


# Дана последовательность, которая состоит из пар натуральных чисел.
# Необходимо выбрать из каждой пары ровно одно число
# так, чтобы сумма всех выбранных чисел имела такой же остаток от деления на
# 7, как наименьшая возможная, и при этом была максимальной возможной.
# Гарантируется, что искомую сумму получить можно. Программа должна
# напечатать одно число – максимальную возможную сумму, соответствующую
# условиям задачи.
# Входные данные: Даны два входных файла: файл A (6a.txt) и файл B
# (6b.txt), каждый из которых содержит в первой строке количество чисел
# (1 ≤ ≤ 100000). Каждая из следующих строк содержит два натуральных
# числа, не превышающих 10000

def individual_task_1(file_number):
    file_name = "Individual_Task_1_0.txt" if file_number == 0 \
        else "Individual_Task_1_a.txt" if file_number == 1 \
        else "Individual_Task_1_b.txt"
    text = open(file_name, "r")
    lines = text.readlines()
    pair_amount = int(lines[0])
    pair_difference = []
    min_sum = max_sum = 0
    for pair_index in range(1, pair_amount + 1):
        first_element, second_element = map(int, lines[pair_index].split())
        pair_difference.append(abs(first_element - second_element))
        min_sum += min(first_element, second_element)
        max_sum += max(first_element, second_element)
    print(f'Минимальная сумма: {min_sum}')
    print(f'Максимальная сумма: {max_sum}')
    # Если остаток макс суммы не равен остатку мин суммы то
    if max_sum % 7 - min_sum % 7:
        print(max_sum % 7, min_sum % 7)
        # Находим разницу остатков
        residual = abs(max_sum % 7 - min_sum % 7)
        print(f'Разница остатков: {residual}')
        # Если остаток от деления на 7 минимальной суммы будет больше, чем от максимальной
        # То чтобы прировнять остатки в будущем вычтем из 7 разность остатков.
        residual = 7 - residual if max_sum % 7 < min_sum % 7 else residual
        # Фильтруем массив
        # Оставляем только элементы, остаток от деления на 7 которых будет равен разнице остатков
        pair_difference = [element for element in pair_difference if element % 7 == residual]
        # Чтобы получить максимальное возможное число нужно вычесть минимальный элемент из pair_difference
        # То есть по факту здесь мы заменяем бОльшее число, которое мы взяли из пары ранее, на меньшее
        # Причем заменяем именно так, чтобы по итогу разность остатков была равна 0
        max_sum -= min(pair_difference)
        print(max_sum % 7, min_sum % 7)
    # Финальная проверка
    print(f'Финальная проверка. Разность остатков: {(max_sum % 7) - (min_sum % 7)}')
    print(f'Ответ: {max_sum}')


# lab1_task6()
# lab2_task1()
# lab3_task9()
# lab4_task10()
# lab5_task6()
# lab6_task11()
# lab7_task5()
# power(2, 4) # lab8
# lab9_task1()
# lab10_task2()
# lab10_task12()
# lab11_task12()
# lab12_task5()
# individual_task_1(0) # тестовый вариант (Пример задания). Ответ: 36
# individual_task_1(1) # первый файл. Ответ: 109307
# individual_task_1(2) # второй файл. Ответ: 410884352