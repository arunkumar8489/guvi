def nu(n):
      while(n%10==0):
          n=n//10
      n=str(n)
      m=n[::-1]
      if n==m:
            print("yes")
      else:
            print("no")
n=int(input())
nu(n)
