n,m=input().split()
l=len(n) if len(n)<len(m) else len(m)
d=abs(len(n)-len(m))
count=d
for i in range(l):
  if(len(m)==1 and m[i] in n):
    break
  if(n[i]!=m[i]):
    count+=1
print(count)
