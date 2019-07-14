n=int(input())
m=input()
o=m.split(" ")
p=[]
for i in o:
    p.append(int(i))
    
p.sort(reverse=True)
a=int("".join(map(str,p)))
print(a)
