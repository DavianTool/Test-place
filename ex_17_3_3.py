number = int(input('Введите число: '))
res = number % 2
if res == 0 and number > 0:
    print('число положительное, четное')
elif res == 0 and number < 0:
    print('число отрицательное, четное')
elif res != 0 and number > 0:
    print('число положительное, нечетное')
elif res != 0 and number < 0:
    print('число отрицательное, нечетное')
else:
    print('число равно нулю')