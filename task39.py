# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
#Вывод: 3 3 2 12
#(каждое число вводится с новой строки)

n = int(input("enter count of array N: "))
list_n = [int(input("enter item: ")) for _ in range(n)]

m = int(input("enter count of array M: "))
list_m = [int(input("enter item: ")) for _ in range(m)]

for i in list_n:
    if i not in list_m:
        print(i, end=' ')

# list_n = [3, 1, 3, 4, 2, 4, 12]
# list_m = [4, 15, 43, 1, 15, 1]

set_diff = set(list_n) - set(list_m)
# print(set_diff)

list_diff_n = []
for i in list_n:
    if i in set_diff:
        list_diff_n.append(i)
print("set()", list_diff_n)