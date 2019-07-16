def su(n,m):
    k=1
    for x in range(0,n-1):
        if m[x]<m[x+1]:
            k+=1
        else:
            l.append(k)
            k=1
    l.append(k)
    print(max(l))
            
n=int(input())
m=list(map(int,input().split()))
l=[]
su(n,m)
