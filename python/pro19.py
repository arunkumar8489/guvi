n=int(input())
m=[]
l=[]
for i in range(0,n):
    m.append(input().split())
for j in m:
    for k in j:
        l.append(int(k))
for p in sorted(l):
    print(p,end=' ')
