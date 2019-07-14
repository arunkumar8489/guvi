n= int(input())
l = list(map(str,input().split()))
m=[]
for i in range(n):
    if int(l[i])==i:
        m.append(l[i])
if(len(m)==0):
    print(-1)
else:
    print(" ".join(m))
