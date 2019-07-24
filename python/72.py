n=input()
v=['a','e','i','o','u']
b=0
for i in range(len(n)):
    if n[i] in v:
        print('yes')
        b=1
        break
    
if b==0:
    print('no')
