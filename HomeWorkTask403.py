# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

lst = [int(i) for i in input('Введите числа через пробел: ').split()]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(f"Список из неповторяющихся элементов: {new_lst}")