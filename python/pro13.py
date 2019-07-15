x,y=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for x in range(y):
       j,k=map(int,input().split())
       g=min(n[j-1:k])
       m.append(g)
for j in m:
       print(j)
