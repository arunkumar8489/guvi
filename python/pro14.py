x,y=map(int,input().split())
n=list(map(int,input().split()))
m=[]
for x in range(y):
       j=list(map(int,input().split()))
       m.append(j)
for i in m:
    v=0
    for k in range(i[0]-1,i[1]):
        v=v^n[k]
    print(v)    
