from itertools import cycle, islice
n1=input()
m=n1.split(" ")
l=[]
for a in m:
    l.append(int(a))
N=l[0]
W=l[1]
o1=input()
p1=o1.split(" ")
q1=[]
for b in p1:
    q1.append(int(b))
o2=input()
p2=o2.split(" ")
q2=[]
for c in p2:
    q2.append(int(c))
q3=[]
for c in range(0,N):
    q3.append(q1[c]*q2[c])
k=0
s1=0

q4=[]

q5=[]

q5=list(islice(cycle(q1),N+1))
q6=list(islice(cycle(q2),N+1))

for y in range(0,N+1):
    sum = 0
    for k in range(y,N+1):
        sum+=q5[k]
        #print(k, sum)
        if sum>W:

            for z in range(y,k):
                s1+=q6[z]
            break

    #print(s1)
    q4.append(s1)
    s1=0
print(max(q4))
