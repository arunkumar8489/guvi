n=int(input())
m=pow(2,n)
l=[]
for x in range(0,m):
    a=bin(x)
    a=a[2:]
    b=str(a)
    
    if len(b)==n:
        l.append(b)
    else:
        while len(b)!=n:
            b='0'+b
        l.append(b)
        
for y in range(0,n+1):
    for z in l:
        if z.count('1')==y:
            print(z)
