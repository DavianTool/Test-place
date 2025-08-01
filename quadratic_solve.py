def D(a, b, c):
    return b ** 2 - 4 * a * c

def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return 'Вещественных корней нет'
    elif D(a, b, c) == 0:
        return -b / (2 * a)
    else:
        return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)

L = list(map(int, input().split()))

print(quadratic_solve(*L))
