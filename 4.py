t = (1, 2, 3)
try:
    t[0] = 1488
except:
    print("Кортежам недоступно назначение")

t2 = t + (4,5)
print(t2)

c2 = t2.count(3)
i4 = t2.index(4)
print(c2,i4)