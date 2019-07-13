a=int(input())
s=[]
d=0
for i in range (0,a+1):
    d=abs((2**i)-a)
    s.append(d)
print(min(s))
