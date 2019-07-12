n=int(input())
l=[]
v=0
for i in range(0,n):
    m=int(input())
    l.append(m)
for j in range(0,len(l)):
    for b in range(0,j):
        if l[j]==l[b]:
            print(l[j],end=' ')
            v+=1
    l.sort()
if v==0:
    print('unique')
