def nu(n):
      a=m2-m1
      b=m3-m4
      c=n3-n2
      d=n4=n1
      if(a==b==c==d):
        print("yes")
      else:
        print("no")
n1,m1=list(map(int,input().split()))
n2,m2=list(map(int,input().split()))  
n3,m3=list(map(int,input().split()))  
n4,m4=list(map(int,input().split()))
nu(n1)
