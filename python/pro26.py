def se(n,m):
    q=[]
    for x in range(0,n):
        k=1
        for y in range(x+1,n):
            if m[x]<m[y]:
                k+=1
                m[x]=m[y]
        q.append(k)
    print(max(q))
n=int(input())
m=list(map(int,input().split()))
se(n,m)
