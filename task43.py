# Задача №43. Общее обсуждение
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

numbers_list = [int(i) for i in input("Enter list of numbers devided by space: ").split()]
numbers_len = len(numbers_list)

counter = 0
for i in range(numbers_len - 1):
    for j in range(i+1, numbers_len):
        if numbers_list[i] == numbers_list[j]:
            counter += 1

print(counter)

counter = 0
for i in range(numbers_len):
    counter += numbers_list[i+1:].count(numbers_list[i])

print(counter)
