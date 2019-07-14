n=int(input())
l=list(map(int,input().split()))
m=0

for i in range(0,n):

    for j in range(0,i):
        if l[j]<l[i]:
            m=m+l[j]

print(m)
