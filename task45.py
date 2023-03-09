# Найти все пары дружественных чисел до 10 000. Пара дружественных чисел - это два различных натуральных числа, для которых сумма всех делителей первого числа равна второму числу и наоборот, сумма всех делителей второго числа равна первому числу. Например, 220 и 284 (делители для 220 это 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, сумма делителей равна 284. Делители для 284 это 1, 2, 4, 71 и 142, сумма которых равна 220).
# Программа получает на вход одно натуральное число k, не
# превосходящее 10 в степени 5 . Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.

import cProfile  # профилирование

# выдает массив всех делителей числа
# def deviders_list(n):
#     res_list = [1]
#     for i in range(2, n // 2 +1):
#         if n % i == 0:
#             res_list.append(i)
#     return res_list


def sum_deviders(n):
    sum_dev = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_dev += i
    return sum_dev


def find_friendly_numbers(k):
    friendly_list = []
    friendly_numbers = set()
    for i in range(2, k+1):
        if i in friendly_numbers:
            continue
        friendly = sum_deviders(i)
        # print(i, friendly)
        if friendly != i and sum_deviders(friendly) == i:
            friendly_list.append((i, friendly))
            friendly_numbers.add(friendly)
    return friendly_list


k = int(input("Enter k: "))


def main():
    print(find_friendly_numbers(k))


if __name__ == '__main__':
    cProfile.run('main()')
