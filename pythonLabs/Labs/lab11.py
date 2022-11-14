
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