#нахождение суммы делителей числа
def find_del(a):
    summa = 0
    for i in range(1, a):
        if a % i == 0:
            summa += i
    return summa

n = int(input('n: '))
sp2 = []
sum_del = {}

#cловарь сумм делителей
for i in range(1, n + 1):
    sum_del[i] = find_del(i)

#находим дружественные пары
for i in range(1, n + 1):
    j = sum_del[i]
    if j <= n and j != i and sum_del.get(j) == i:
        sp2.append((i, j))
print(sp2)

