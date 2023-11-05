# Получение числа Фибоначи

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
n = int(input('Число в последовательности: '))
for i in range(n):
    c = a + b
    a = b
    b = c
print(b)
