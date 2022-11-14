
# По данному натуральному n ≤ 9 выведите лесенку
# из i ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.

def lab4_task10():
    top_number = int(input("i: "))
    for temp_top_number in range(1, top_number + 1):
        print(*range(1, temp_top_number + 1))

lab4_task10()