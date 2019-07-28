def nu(n):
    a="abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in n.lower():
            return False
        return True
n=str(input().split())
if(nu(n)==True):
    print('yes')
else:
    print('no')
