from math import sqrt
er = []
i = input()
while i != "stop":
    i = int(i)
    if i > 0:
        er.append(i)
    i = input()

er.sort(reverse=True)
print(er)
maxx = 0
p = 0
while True:
    a = er[maxx]
    b = er[maxx + 1]
    c = er[maxx + 2]
    if a < b+c and c < a+b and b < a+c:
        p = (a+b+c)/2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        print(a, b, c, s)
        break
    else:
        maxx += 1



