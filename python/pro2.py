from itertools import combinations
nu ,vm = input().split()
vm = int(vm)
nila = []
hj = combinations(nu,len(nu)-vm)
for d in hj:
    nila.append("".join(d))
print(min(nila))
