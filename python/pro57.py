n,m=map(str,input().split())
c=0
for i in range(0,len(n)):
    for j in range(0,len(m)):
        if n[i]==m[j]:
            c+=1
if c>=2:
    print("yes")
else:
    print("no")
