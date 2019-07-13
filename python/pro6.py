nu=int(input())
l=list(map(int,input().split()))
m=0
for x in range(nu):
    for y in range(x,nu):  
        for z in range(y,nu):
            if l[x]<l[y]<l[z]:
                m+=1
print(m)
