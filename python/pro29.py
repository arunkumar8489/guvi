def nu(n):
    m=0
    k=0
    l=[]
    while m<100 and m<n:
        c=0
        for x in str(n-m):
            c+=int(x)
        if c+(n-m)==n:
            k+=1
            l.append(n-m)
        m+=1
    print(k)  
    for m in l:
            print(m)
n=int(input())
nu(n)

