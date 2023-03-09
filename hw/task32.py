# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(numbers_list: list, min_number: int, max_number: int) -> list:
    indexes_list = []
    for i in range(len(numbers_list)):
        if min_number <= numbers_list[i] <= max_number:
            indexes_list.append(i)
    return indexes_list


# numbers_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# print(numbers_list)

numbers_list = [int(i) for i in input('enter array divider space: ').split()]
min_number = int(input("Enter min: "))
max_number = int(input("Enter max: "))

print(find_indexes(numbers_list, min_number, max_number))
