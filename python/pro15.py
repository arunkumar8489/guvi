n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(n):
    l.sort(reverse=True)
print(*l,sep="\n")
