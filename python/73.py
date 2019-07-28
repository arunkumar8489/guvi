n=int(input())
m,l=map(int,input().split())
b=0
for i in range(m+1,l):
    if i==n:
        print('yes')
        b=1
        break
if b==0:
    print('no')
