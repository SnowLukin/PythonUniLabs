
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

lab6_task11()