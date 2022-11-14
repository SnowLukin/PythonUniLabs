import copy
from itertools import combinations

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

# individual_task_1(0) # тестовый вариант (Пример задания). Ответ: 36
# individual_task_1(1) # первый файл. Ответ: 115110
# individual_task_1(2) # второй файл. Ответ: 410884352