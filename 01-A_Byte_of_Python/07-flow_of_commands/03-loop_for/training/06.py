"""
Пользователь вводит число N. Найдите сумму чисел: 1 + 1/2 + 1/3 + ... + 1/N
"""

N = int(input('Введите число: '))
result = 0

for i in range(1, N + 1):
    result = result + (1 / i)
print('{0:.4}'.format(result))