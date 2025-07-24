number = int(input('Введите число для проверки четности: '))

res = number % 2
if res == 0:
    print('число четное')
else:
    print('число нечетное')