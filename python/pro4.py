n,m=map(str,input().split())
t=0
if len(n)>len(m):
	n,m=m,n
v=0
while v<len(n):
	  t+=(ord(m[v])-ord(n[v]))
	  v+=1
for v in range(v,len(m)):
	  t+=ord(m[v])-ord('a')+1
print(t)
