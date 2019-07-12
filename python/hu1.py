n=int(input())
m=input()
o=m.split(" ")
p=[]
q=[]
t=0
for i in o:
    p.append(int(i))
for j in range(0,len(p)):
    for k in range(j+1,len(p)):
        if p[j]==p[k] and not(p[j] in q):
            q.append(p[j])
q.sort()
for t in q:
    print(l,end=" ")
if t==0:
    print('unique')
