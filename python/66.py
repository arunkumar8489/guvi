def nu(n):
    for i in range(2,n):
        if(n%i==0):
            print('no')
            break
    else:
            print('yes')

n=int(input())
nu(n)
