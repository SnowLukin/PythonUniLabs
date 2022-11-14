
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

lab7_task5()