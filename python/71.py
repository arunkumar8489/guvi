def re(s):
    return s[::-1]
def p(s):
    rev=re(s)
    if (s==rev):
        return True
    return False
s=input()
a=p(s)
if a==1:
    print('yes')
else:
    print('no')
