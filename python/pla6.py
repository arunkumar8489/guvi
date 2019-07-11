n,k=map(str,input().split())
if(len(n)!=len(k)):
    print("no")
else :
    s1=[n.count(i) for i in n]
    s2=[k.count(i) for i in k]
if(s1==s2):
    print("yes")
else:
    print("no")
