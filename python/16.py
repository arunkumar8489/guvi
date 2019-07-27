n,m=list(map(int,input().split()))
for i in range(n,m):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:        
            print(i)
