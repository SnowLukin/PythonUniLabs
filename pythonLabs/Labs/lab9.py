
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

lab9_task1()