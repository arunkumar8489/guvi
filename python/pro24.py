import itertools
for x in map(''.join,itertools.product('01',repeat=int(input()))):
             print(x)
