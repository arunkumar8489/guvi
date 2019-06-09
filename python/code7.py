nn=int(input())
if nn<0:
    print()
else:
    su=0
    while(nn>0):
        su+=nn
        nn-=1
    print(su)
