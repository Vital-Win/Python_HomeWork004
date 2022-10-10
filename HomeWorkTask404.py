# Задана натуральная степень k. 
# Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num_n =  int(input('Введите число: '))
if num_n == 0:
    num_n = 1
str_line = ''
count = num_n
for i in range(num_n):
    new_n = random.randrange(0, 101)
    while count > 1:
        new_n = random.randrange(0, 101)
        str = (f'{new_n}*x^{count} + ')
        str_line += str
        count -= 1
    if i == num_n - 1:
        str = (f'{new_n}*x ')
        str_line += str
    if i == num_n - 1 or i == num_n:
        str = (f'+ {new_n} = 0')
        str_line += str
print(f'{str_line}')
with open('file_Task404.txt', 'w') as data:
    data.write(str_line)
