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

lab1_task6()