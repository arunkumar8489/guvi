n=int(input())
l=[]
for i in range(1,11):
    i=i*7
    l.append(i)
if n in l:
    print('yes')
else:
    print('no')
