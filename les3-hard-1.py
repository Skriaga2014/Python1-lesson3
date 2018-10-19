def drob (txt):
    a = []
    if txt.count(" ") > 0:
        a.append(txt.split(" ")[0])
        if txt.split(" ")[1].count("/") > 0:
            a.append(txt.split(" ")[1].split("/")[0])
            a.append(txt.split(" ")[1].split("/")[1])
        else:
            a.append(txt.split(" ")[1])
    elif txt.count("/") > 0:
        a.append("0")
        a.append(txt.split("/")[0])
        a.append(txt.split("/")[1])
    else:
        a.append(txt)
    for i in range(len(a)): a[i] = int(a[i])

    if len(a) == 1:

        a.append(a[0])
        a.append(1)
        a.remove(a[0])

    else:
        if a[0] < 0:
            a[0] = -a[0]
            a[1] = -(a[0] * a[2] + a[1])
            a.remove(a[0])
        else:
            a[1] = a[0]*a[2]+a[1]
            a.remove(a[0])
    return a

#inp = input ("Введите выражение с дробями в формате \"n x/y +/- n x/y\": ")
inp = ""

if inp.count(" + ") > 0:
    list = inp.split(" + ")
    znak = "+"
if inp.count(" - ") > 0:
    list = inp.split(" - ")
    znak = "-"

print (list)


print(drob("2"))
print(drob("-2"))
print(drob("-1/2"))
print(drob("-1 1/2"))

def summ (a,b):
    c = [a[0]*b[1]+b[0]*a[1], a[1]*b[1]]
    print (c)
    n = max(c[0],c[1])
    while n > 0:
        if c[0] % n == 0 and c[1] % n == 0:
            c[0] = c[0] / n
            c[1] = c[1] / n
        n -= 1
    if c[0]>c[1]:
        n = str(int(c[0]//c[1]))+" "+str(int(c[0]%c[1]))+"/"+str(int(c[1]))
    else:
        n = str(c[0])+"/"+str(c[1])
    ar = "первое слогаемое:",a,"\nвторое слогаемое:",b,"\nнеправильная дробь:",str(c[0])+"/"+str(c[1]),"\nправильная дробь:",n
    return ar

import random
for i in range(100):

    print(summ(drob(str(random.randint(0,10))+" "+str(random.randint(0,10))+"/"+str(random.randint(0,10))), drob("-1 12/4")))