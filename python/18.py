n,m=map(int,input().split())
for n in range(n,m):
    o= len(str(n))
    s = 0
    t = n
    while t > 0:
       d = t % 10
       s+= d**o
       t//=10

    if n == s:
       print(n,end=' ')
   
   
   
   
