import math
import copy
from itertools import combinations
import sqlite3
# import tkinter as tk

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

# Даны два списка чисел. Найдите все
# числа, которые входят как в первый, так и во второй список и выведите их в
# порядке возрастания.

def lab10_task3():
    print(sorted(set(input().split()).intersection(set(input().split()))))


# Дан текст: в первой строке записано
# число строк, далее идут сами строки. Определите, сколько различных слов
# содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов или символами
# конца строки.

# Количество строк: 2
# one two three;
# four. Five, six


def lab10_task6():
    amount_of_lines = int(input('Количество строк: '))
    text = []
    for _ in range(amount_of_lines):
        line = input().split()
        text += line
    print(len(text))

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

# В единственной строке записан
# текст. Для каждого слова из данного текста подсчитайте, сколько раз оно
# встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов или символами
# конца строки.
# Входные данные
# one two one tho three
# Правильный ответ
# 0 0 1 0 0


def lab11_task1():
    dict = {}
    text = input('Text: ').split()
    for word in text:
        dict[word] = dict.get(word, 0) + 1
        print(dict[word] - 1, end=' ')


# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову. Все слова в словаре
# различны.
# Для слова из словаря, записанного в последней строке, определите его
# синоним.
# Входные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# Правильный ответ
# Bye

def lab11_task2():
    amount_of_pairs = int(input('Количество пар: '))
    dict = {}
    for pair_index in range(amount_of_pairs):
        first, second = input().split()
        dict[first] = second
        dict[second] = first
    print(dict[input()])

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


# Отображаем начало файла. В операционных системах на базе
# Unix обычно присутствует утилита с названием head. Она выводит первые
# десять строк содержимого файла, имя которого передается в качестве
# аргумента командной строки. Напишите программу на Python, имитирующую
# поведение этой утилиты. Если файла, указанного пользователем, не
# существует, или не задан аргумент командной строки, необходимо вывести
# соответствующее сообщение об ошибке.

def lab12_task1():
    file_name = input("Введите имя файла: ")
    file_opened = False
    while not file_opened:
        try:
            with open(file_name, 'r') as f:
                lines = [next(f) for x in range(10)]
            for line in lines:
                print(line, end='')
            file_opened = True
        except FileNotFoundError:
            print("Файл не найден. Попробуйте еще.")
            file_name = input("Введите имя файла: ")


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

# lab12_task5()


# Создание пароля посредством генерирования случайных символов может обернуться сложностью в
# запоминании полученной относительно надежной
# последовательности. Некоторые системы создания паролей рекомендуют
# сцеплять вместе два слова на английском языке, тем самым упрощая
# запоминание заветного ряда символов – правда, в ущерб его надежности.
# Напишите программу, которая будет открывать файл со списком слов,
# случайным образом выбирать два из них и сцеплять вместе для получения
# итогового пароля. При создании пароля исходите из следующего требования:
# он должен состоять минимум из восьми символов и максимум из десяти, а
# каждое из используемых слов должно быть длиной хотя бы в три буквы. Кроме
# того, сделайте заглавными первые буквы обоих слов, чтобы легко можно было
# понять, где заканчивается одно и начинается другое. По завершении процесса
# полученный пароль должен быть отображен на экране.

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

def get_min_combinations(pair_difference, residual):
    # Находим все элементы которые при делении на 7 дают в остатке значение равное residual
    sub_pair_difference = [element for element in pair_difference if element % 7 == residual]
    # Находим такое число которое подходит под условие но не является суммой
    # (те возможно не является минимальным решением)
    sub = min(sub_pair_difference)
    min_sum = 0
    flag = True
    # На этом этапе отфильтруем массив так чтобы уменьшить время поиска нужного решения
    print(f'Before: {len(pair_difference)}')
    pair_difference = [element for element in pair_difference if element <= sub]
    print(f'After: {len(pair_difference)}')
    for n in range(1, len(pair_difference) + 1):
        sub_combinations = [list(ele) for ele in list(combinations(pair_difference, n))]
        for combination in sub_combinations:
            summary = sum(combination)
            if summary % 7 == residual:
                if flag:
                    min_sum = summary
                    flag = False
                else:
                    if summary < min_sum:
                        min_sum = summary
    print(min_sum)
    return min_sum


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
        # Находим минимальную возможную сумму элементов или же один элемент, который при делении на 7
        # в остатке будет давать результат равный 'residual'
        min_combination = get_min_combinations(pair_difference, residual)
        # Чтобы получить максимальное возможное число нужно вычесть минимальный элемент из pair_difference
        # То есть по факту здесь мы заменяем бОльшее число, которое мы взяли из пары ранее, на меньшее
        # Причем заменяем именно так, чтобы по итогу разность остатков была равна 0
        max_sum -= min_combination
        print(max_sum % 7, min_sum % 7)
    # Финальная проверка
    print(f'Финальная проверка. Разность остатков: {(max_sum % 7) - (min_sum % 7)}')
    print(f'Ответ: {max_sum}')


def lab13_task1():
    class Cat:
        def __init__(self, name, color, weight):
            self.name = name
            self.color = color
            self.weight = weight

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

    kitten = Cat("Алеша", "белый", 50)
    kitten.meow()

# lab13_task1()

def lab13_task2():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")
    animal = Animal("Данила")
    print(animal.get_name())
    animal.set_name("Максим")
    animal.eat()
    animal.make_noise()

# lab13_task2()

def lab13_task3():
    class StringVar:
        def __init__(self, text):
            self.string = str(text)

        def set(self, text):
            self.string = text

        def get(self):
            return self.string
    string = StringVar("один")
    print(string.get())
    string.set("два")
    print(string.get())

# lab13_task3()

def lab13_task4():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Point(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            return Point(self.x * other.x, self.y * other.y)

        def __truediv__(self, other):
            return Point(self.x / other.x, self.y / other.y)

        def __floordiv__(self, other):
            return Point(self.x // other.x, self.y // other.y)

        def __mod__(self, other):
            return Point(self.x % other.x, self.y % other.y)

        def __pow__(self, other):
            return Point(self.x ** other.x, self.y ** other.y)

        def __lt__(self, other):
            return self.x < other.x and self.y < other.y

        def __le__(self, other):
            return self.x <= other.x and self.y <= other.y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __ne__(self, other):
            return self.x != other.x and self.y != other.y

        def __gt__(self, other):
            return self.x > other.x and self.y > other.y

        def __ge__(self, other):
            return self.x >= other.x and self.y >= other.y

    point1 = Point(1, 2)
    point2 = Point(3, 4)
    print(point1 + point2)
    print(point1 - point2)
    print(point1 * point2)
    print(point1 / point2)
    print(point1 // point2)
    print(point1 % point2)
    print(point1 ** point2)
    print(point1 < point2)
    print(point1 <= point2)
    print(point1 == point2)
    print(point1 != point2)
    print(point1 > point2)
    print(point1 >= point2)

# lab13_task4()

def lab13_task5():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом {weight} кг, цветом {color}")

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

        def make_noise(self):
            print(f"{self.name} говорит: Мяу")
    kitten = Cat("Алеша", "белый", 50)
    kitten.meow()
    kitten.make_noise()

# lab13_task5()

def lab13_task6():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом {weight} кг, цветом {color}")

        def bark(self):
            print(f"Cобака {self.name}, весом {self.weight} кг, цветом {self.color}, гавкнула")

        def make_noise(self):
            print(f"{self.name} говорит: Гав")

    dog = Dog("Алеша", "белый", 50)
    dog.bark()
    dog.make_noise()

# lab13_task6()

def lab13_task7():
    class Animal:
        def __init__(self, name):
            self.name = name
            print(f"Родилось животное {name}")

        def eat(self):
            print("Намнём")

        def set_name(self, name):
            self.name = name

        def get_name(self):
            return self.name

        def make_noise(self):
            print(f"{self.name} говорит: Гррр")

    class Cat(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился кот по имени: {name}, весом {weight} кг, цветом {color}")

        def meow(self):
            print(f"Кот по имени {self.name}, весом {self.weight} кг и цветом {self.color}, мяукнул")

        def make_noise(self):
            print(f"{self.name} говорит: Мяу")

    class Dog(Animal):
        def __init__(self, name, color, weight):
            super().__init__(name)
            self.color = color
            self.weight = weight
            print(f"Родился собака по имени: {name}, весом {weight} кг, цветом {color}")

        def bark(self):
            print(f"Cобака {self.name}, весом {self.weight} кг, цветом {self.color}, гавкнула")

        def make_noise(self):
            print(f"{self.name} говорит: Гав")

    cat = Cat("жч", "белый", 7)
    cat.set_name("Железный человек")
    cat.meow()
    cat.make_noise()
    dog = Dog("хлк", "черный", 10)
    dog.set_name("Халк")
    dog.bark()
    dog.make_noise()
    dog2 = Dog("анн", "красный", 5)
    dog2.set_name("Анна")
    dog2.bark()
    dog2.make_noise()
    animal = Animal("Александр")
    animal.set_name("Саня")
    animal.make_noise()


def individual_task_2():
    def print_matrix(matrix):
        print('\n'.join('\t'.join(map(str, row)) for row in matrix))
        print()

    class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix

        def print_matrix(self):
            print('\n'.join('\t'.join(map(str, row)) for row in self.matrix))
            print()

        def change_size(self, i, j):
            current_columns = len(self.matrix[0])
            current_rows = len(self.matrix)

            if i == 0 or j == 0:
                self.matrix = []
                return
            # Changing rows
            if current_rows < i:
                for _ in range(0, i - current_rows):
                    self.add_row()
            elif current_rows > i:
                for _ in range(0, current_rows - i):
                    self.del_row(len(self.matrix) - 1)
            # Changing columns
            if current_columns < j:
                for _ in range(0, j - current_columns):
                    self.add_column()
            elif current_columns > j:
                for _ in range(0, current_columns - j):
                    self.del_column(len(self.matrix[0]) - 1)
        def add_column(self):
            self.matrix = [row + [0] for row in self.matrix]

        def add_row(self):
            self.matrix.append([0 for _ in range(len(self.matrix[0]))])

        def del_column(self, i):
            self.matrix = [row[: i] + row[i + 1:] for row in self.matrix]

        def del_row(self, i):
            self.matrix = self.matrix[:i] + self.matrix[i + 1:]

        def sub_matrix(self, start_row, end_row, start_column, end_column):
            return [[self.matrix[i][j] for j in range(start_column, end_column + 1)] for i in range(start_row, end_row + 1)]
    entity = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Initial matrix")
    entity.print_matrix()
    print("Changed size")
    entity.change_size(2, 2)
    entity.print_matrix()
    # entity.add_column()
    # entity.add_row()
    # entity.print_matrix()
    # print("Sub matrix")
    # sub_matrix = entity.sub_matrix(1, 2, 1, 2)
    # print_matrix(sub_matrix)
    #
    # print("Delete column")
    # entity.del_column(0)
    # entity.print_matrix()
    #
    # print("Delete row")
    # entity.del_row(1)
    # entity.print_matrix()
individual_task_2()

def sqlite_sample_table_command(name):
    sqlite_command = f'''CREATE TABLE {name} (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        surname TEXT NOT NULL,
                                        salary REAL NOT NULL);'''
    return sqlite_command

def create_data_base_with_five_tables():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        names = ['first_table', 'second_table', 'third_table', 'fourth_table', 'fifth_table']
        sqlite_create_tables = [sqlite_sample_table_command(name) for name in names]
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        for table in sqlite_create_tables:
            cursor.execute(table)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def insert_data_to_table(table_name):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        data = [
            (1, 'One', 'OneOne', 1000),
            (2, 'Two', 'TwoTwo', 2000),
            (3, 'Three', 'ThreeThree', 3000),
            (4, 'Four', 'FourFour', 4000),
            (5, 'Five', 'FiveFive', 5000),
            (6, 'Six', 'SixSix', 6000),
            (7, 'Seven', 'SevenSeven', 7000),
            (8, 'Eight', 'EightEight', 8000),
            (9, 'Nine', 'NineNine', 9000),
            (10, 'Ten', 'TenTen', 10000)
        ]
        cursor.executemany(f'INSERT INTO {table_name} VALUES(?,?,?,?);', data)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def actions_with_data_base(table_name):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_command_1 = f"""SELECT count(*) from {table_name}"""
        cursor.execute(sqlite_select_command_1)
        total_rows = cursor.fetchone()
        print("Кол-во строк: ", total_rows)

        sql_update_command_1 = f"""Update {table_name} set salary = 999999 where id = 4"""
        sql_update_command_2 = f"""Update {table_name} set name = 'ChangedName' where id = 4"""
        sql_update_command_3 = f"""Update {table_name} set surname = 'ChangedSurname' where id = 4"""
        sql_update_command_4 = f"""Update {table_name} set salary = 10 where salary = 10000"""
        sql_update_command_5 = f"""Update {table_name} set name = 'Changed_Name_Ten' where salary = 10000"""
        sql_update_command_6 = f"""Update {table_name} set surname = 'Changed_Surname_Ten' where salary = 10000"""
        sql_update_command_7 = f"""Update {table_name} set id = 100 where id = 9"""
        cursor.execute(sql_update_command_1)
        cursor.execute(sql_update_command_2)
        cursor.execute(sql_update_command_3)
        cursor.execute(sql_update_command_4)
        cursor.execute(sql_update_command_5)
        cursor.execute(sql_update_command_6)
        cursor.execute(sql_update_command_7)

        sql_delete_command_1 = f"""DELETE from {table_name} where id = 1"""
        sql_delete_command_2 = f"""DELETE from {table_name} where id = 2"""
        sql_delete_command_3 = f"""DELETE from {table_name} where id = 3"""
        sql_delete_command_4 = f"""DELETE from {table_name} where id = 5"""
        cursor.execute(sql_delete_command_1)
        cursor.execute(sql_delete_command_2)
        cursor.execute(sql_delete_command_3)
        cursor.execute(sql_delete_command_4)

        sqlite_select_command_2 = f"""SELECT count(*) from {table_name}"""
        cursor.execute(sqlite_select_command_2)
        total_rows = cursor.fetchone()
        print("Кол-во строк: ", total_rows)

        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if (sqlite_connection):
            print("Всего строк, измененных после подключения к базе данных: ", sqlite_connection.total_changes)
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def lab15():
    # create_data_base_with_five_tables()  # Creating 5 tables
    tables = ['first_table', 'second_table', 'third_table', 'fourth_table', 'fifth_table']
    # for table in tables:
    #     insert_data_to_table(table)  # Adding data to existing tables
    actions_with_data_base(tables[1])

# lab15()


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
# individual_task_1(1) # первый файл. Ответ: 115110
# individual_task_1(2) # второй файл. Ответ: 410884352
# lab13_task1()
# lab13_task2()
# lab13_task3()
# lab13_task4()
# lab13_task5()
# lab13_task6()
# lab13_task7()
# individual_task_2()