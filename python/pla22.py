n,n=input().split()
n=int(n)
m=int(m)
d=0
for i in range(2,m+1):
    if(n%i==0 and m%i==0):
         d=i
print(d)
