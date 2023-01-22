count = 0
f = open('5650.txt')
# перебираем строки
for s in f:
    lst = list(map(int, s.split()))
    st = set(lst)
    summ = 0
    repeat = False
    if len(lst) != len(st):
        repeat = True
    for j in st:
        symbCount = 0
        for i in lst:
            if i == j:
                symbCount += 1
                if symbCount > 1:
                    summ += i
    if repeat and summ % 3:
        count += 1
print(count)
