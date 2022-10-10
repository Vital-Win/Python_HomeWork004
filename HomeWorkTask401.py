# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

import math

def calculation(num):
    result = 0
    while num % 1 > 0:
        num *= 10
        result += 1
    return result

accuracy = float(input('Введите необходимую точность: '))        
round_pi = round(math.pi, calculation(accuracy))
print(round_pi)
