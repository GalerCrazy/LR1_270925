from copy import deepcopy

n = [7,2.5]
n.append(4)
n.insert(1,10)
n.extend([1,1,1])
n.remove(7)
a = n[-1]
n.pop()
n.sort()
n.reverse()
print(n.count("2"))
n.index(1)
n1 = n.copy()
n2 = deepcopy(n)
n.clear()
print(n,n1,n2)