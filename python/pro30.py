def nu(n):
    a=0
    for i in range(0,len(n)):
        s=n[0:i]+n[i+1::]
        if(int(s)%8==0):
            a=1
            break
    if(a==1):
        print("yes")
    else:
        print("no")
n=input()
nu(n)
